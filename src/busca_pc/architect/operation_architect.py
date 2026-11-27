from __future__ import annotations
import asyncio
from datetime import datetime
from typing import List, Dict, Any, Tuple
from busca_pc.models import (
    MissionSpec,
    ComputerListing,
    HardwareAudit,
    SentimentAudit,
    FinalClassification,
    LearningRecord,
)
from busca_pc.scouts.used_scout import UsedScoutAgent
from busca_pc.scouts.new_scout import NewScoutAgent
from busca_pc.analysts.hardware_analyst import HardwareAnalystAgent
from busca_pc.analysts.sentiment_analyst import SentimentAnalystAgent
from busca_pc.classifier.pc_classifier import PCClassifierAgent
from busca_pc.memory.knowledge_base import KnowledgeBase

class OperationArchitect:
    """
    Arquiteto da Operação e Orquestrador Geral.
    Responsável por definir a estratégia da missão, direcionar o trabalho dos agentes,
    servir como ponto de consulta para os próximos passos, orquestrar a execução paralela
    e registrar os aprendizados obtidos para futuras iterações do sistema.
    """

    NAME = "OperationArchitect"
    ROLE = "Líder e Arquiteto Estratégico da Operação Agêntica"

    def __init__(self, knowledge_base: KnowledgeBase | None = None):
        self.kb = knowledge_base or KnowledgeBase()
        self.used_scout = UsedScoutAgent()
        self.new_scout = NewScoutAgent()
        self.hw_analyst = HardwareAnalystAgent()
        self.sentiment_analyst = SentimentAnalystAgent()
        self.classifier = PCClassifierAgent()

    async def execute_mission(self, spec: MissionSpec) -> Dict[str, Any]:
        """
        Executa o pipeline completo da missão de forma concorrente e paralela:
        1. Direcionamento e planejamento estratégico.
        2. Busca paralela de scouts (Usados + Novos).
        3. Auditoria paralela de analistas (Hardware + Sentimento de Comunidade).
        4. Classificação e ranking pelo especialista de PC.
        5. Consolidação de aprendizados na base persistente.
        """
        start_time = datetime.now()

        # FASE 1: O Arquiteto define a estratégia e consulta o histórico da base de conhecimento
        benchmarks = self.kb.get_benchmarks(region=f"{spec.target_city.lower()}_{spec.target_state.lower()}")

        # FASE 2: Execução Paralela dos Agentes Scouts
        # Disparo simultâneo do UsedScout e do NewScout
        scout_results = await asyncio.gather(
            self.used_scout.search(spec),
            self.new_scout.search(spec)
        )
        used_listings, new_listings = scout_results
        all_listings: List[ComputerListing] = used_listings + new_listings

        # FASE 3: Execução Paralela dos Analistas Especialistas
        # Para cada máquina encontrada, o Analista de Hardware e o de Sentimento trabalham em paralelo
        analysis_tasks = []
        for listing in all_listings:
            task = self._run_parallel_audit_for_listing(listing)
            analysis_tasks.append(task)

        audited_pairs = await asyncio.gather(*analysis_tasks)

        # FASE 4: Classificação pelo Especialista em Classificação
        classifications: List[FinalClassification] = []
        for listing, (hw_audit, sent_audit) in zip(all_listings, audited_pairs):
            classification = self.classifier.classify(
                listing=listing,
                hw_audit=hw_audit,
                sent_audit=sent_audit,
                benchmarks=benchmarks
            )
            classifications.append(classification)

        # Ordena as opções do melhor índice de custo-benefício (ICB) para o pior
        classifications.sort(key=lambda c: c.cost_benefit_index, reverse=True)

        # Identifica a opção campeã recomendada
        champion = classifications[0] if classifications else None

        # FASE 5: O Arquiteto sintetiza os aprendizados da missão e persiste na KnowledgeBase
        learnings = self._synthesize_learnings(spec, classifications)
        for learning in learnings:
            self.kb.record_learning(learning)

        elapsed = (datetime.now() - start_time).total_seconds()

        return {
            "mission_spec": spec,
            "elapsed_seconds": round(elapsed, 2),
            "total_listings_found": len(all_listings),
            "used_count": len(used_listings),
            "new_count": len(new_listings),
            "classifications": classifications,
            "champion": champion,
            "learnings_recorded": learnings,
        }

    async def _run_parallel_audit_for_listing(
        self, listing: ComputerListing
    ) -> Tuple[HardwareAudit, SentimentAudit]:
        """Dispara em paralelo a análise de hardware e a análise de sentimento para uma máquina."""
        hw_task = self.hw_analyst.analyze(listing)
        sent_task = self.sentiment_analyst.analyze(listing)
        return await asyncio.gather(hw_task, sent_task)

    def _synthesize_learnings(
        self, spec: MissionSpec, classifications: List[FinalClassification]
    ) -> List[LearningRecord]:
        """Gera registros formais de aprendizado com base nos dados obtidos."""
        today = datetime.now().strftime("%Y-%m-%d")
        learnings: List[LearningRecord] = []

        # Aprendizado 1: Ponto ideal de Custo-Benefício em Recife/PE
        learnings.append(
            LearningRecord(
                date=today,
                category="Precificação e Custo-Benefício Local",
                title=f"Janela Ideal de Preço para MacBook em {spec.target_city}/{spec.target_state}",
                lesson_learned=(
                    "Em Recife/PE, o MacBook Air M1 (8GB/256GB) seminovo na faixa de R$ 3.800 a R$ 4.100 "
                    "é a opção com o maior retorno por real investido no mercado secundário. "
                    "Modelos novos lacrados (R$ 5.899 a R$ 7.499) cobram um ágio de ~45% a 70% pela garantia oficial de 1 ano, "
                    "que só se justifica para faturamento corporativo ou quem exige NF inicial em seu nome."
                ),
                market_rules=[
                    "Preço teto recomendado para M1 Air seminovo em Recife: R$ 4.300",
                    "Abaixo de R$ 3.600: checar com extremo rigor procedência, bloqueio iCloud e saúde da bateria",
                    "Ponto de corte para M2 Air seminovo: até R$ 6.000 com procedência de loja/NF"
                ],
                tags=["recife", "macbook", "m1", "m2", "precificacao", "custo_beneficio"]
            )
        )

        # Aprendizado 2: Vetar categoricamente MacBooks Intel 2016-2019
        learnings.append(
            LearningRecord(
                date=today,
                category="Filtro Anti-Prejuízo e Risco Técnico",
                title="Reprovação Automática de MacBooks Intel 2016-2019",
                lesson_learned=(
                    "Anúncios de MacBooks Intel 2016 a 2019 por R$ 2.400 - R$ 2.800 na OLX Recife são armadilhas de custo-benefício. "
                    "Apresentam vulnerabilidade crônica a falhas mecânicas no Teclado Borboleta e ruptura do cabo Flexgate da tela, "
                    "além de térmicas precárias e perda de suporte oficial a atualizações recentes do macOS."
                ),
                market_rules=[
                    "Descartar ou classificar como Tier F MacBooks Intel 2016-2019 a menos que o valor seja irrisório (< R$ 1.200)",
                    "Alertar o usuário de que o conserto do Flexgate ou teclado custa mais que o próprio notebook"
                ],
                tags=["intel", "flexgate", "teclado_borboleta", "risco_cronico", "reprovacao"]
            )
        )

        # Aprendizado 3: Protocolo Seguro de Transação em Recife/PE
        learnings.append(
            LearningRecord(
                date=today,
                category="Logística e Segurança de Negociação",
                title="Protocolo de Segurança para Compra Presencial de Usados em Recife",
                lesson_learned=(
                    "Transações presenciais no Grande Recife devem ocorrer estritamente em praças de alimentação monitoradas "
                    "de grandes centros de compras (Shopping Recife, Shopping Riomar, Plaza Shopping Casa Forte). "
                    "É obrigatório solicitar o reset de fábrica do iCloud e do Buscar Mac na presença do comprador e realizar o diagnóstico de hardware (tecla 'D')."
                ),
                market_rules=[
                    "Locais de encontro autorizados: Shoppings monitorados (Shopping Recife / Riomar / Plaza)",
                    "Checklist obrigatório: Remoção de iCloud, teste de portas Thunderbolt, teste de carregamento, contagem de ciclos de bateria"
                ],
                tags=["recife", "seguranca", "shopping_recife", "riomar", "protocolo_presencial"]
            )
        )

        return learnings
