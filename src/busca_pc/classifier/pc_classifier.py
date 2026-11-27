from __future__ import annotations
from typing import Dict, Any, List
from busca_pc.models import ComputerListing, HardwareAudit, SentimentAudit, FinalClassification

class PCClassifierAgent:
    """
    Especialista em Classificação de PC.
    Cruza o laudo técnico de hardware com o laudo de sentimento da internet e o preço de mercado,
    calculando o Índice de Custo-Benefício (ICB), nota composta, faixa (Tier S a F) e veredito final.
    """

    NAME = "PCClassifierAgent"
    ROLE = "Especialista em Classificação e Custo-Benefício"

    def classify(
        self,
        listing: ComputerListing,
        hw_audit: HardwareAudit,
        sent_audit: SentimentAudit,
        benchmarks: Dict[str, Any]
    ) -> FinalClassification:
        """Emite o laudo final consolidado e a nota precisa para o computador."""

        # 1. Nota Composta de Qualidade do Produto (0 - 100)
        # Hardware: 55% de peso; Sentimento/Confiabilidade de Comunidade: 45% de peso
        composite_quality = (hw_audit.hardware_score * 0.55) + (sent_audit.sentiment_score * 0.45)

        # 2. Definição do Preço de Referência de Mercado em Recife
        fair_price = self._determine_benchmark_price(listing, benchmarks)

        # 3. Análise de Preço e Desconto Relativo
        price_delta_pct = ((fair_price - listing.price) / fair_price) * 100.0

        # 4. Cálculo do Índice de Custo-Benefício (ICB)
        # Fator de valor = Razão entre valor justo de mercado e preço anunciado
        price_ratio = fair_price / max(listing.price, 1.0)
        # Amortecimento exponencial suave para evitar distorções extremas
        price_multiplier = min(1.35, max(0.5, price_ratio ** 0.65))

        raw_cbi = composite_quality * price_multiplier

        # Penalidade drástica para produtos com alto risco crônico ou obsolescência (ex: Intel butterfly/flexgate)
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto":
            raw_cbi = min(raw_cbi * 0.4, 38.0)

        # Ajuste de condição: produtos novos têm prêmio de garantia de 1 ano, mas pagam ágio
        if listing.condition == "novo":
            # Novo tem garantia total, reduzindo risco a zero no 1º ano
            raw_cbi = min(raw_cbi * 1.05, 95.0)

        cbi_score = round(max(0.0, min(100.0, raw_cbi)), 1)

        # 5. Atribuição de Tier e Veredito
        tier, verdict = self._determine_tier_and_verdict(cbi_score, sent_audit, hw_audit, price_delta_pct)

        # 6. Elaboração da Justificativa Técnica & Recomendações
        justification = self._generate_justification(
            listing, hw_audit, sent_audit, cbi_score, tier, verdict, fair_price, price_delta_pct
        )

        precautions = self._generate_precautions(listing, sent_audit)

        return FinalClassification(
            listing=listing,
            hardware_audit=hw_audit,
            sentiment_audit=sent_audit,
            composite_score=round(composite_quality, 1),
            cost_benefit_index=cbi_score,
            tier=tier,
            verdict=verdict,
            fair_market_price_recife=fair_price,
            price_delta_pct=round(price_delta_pct, 1),
            justification=justification,
            key_precautions=precautions,
        )

    def _determine_benchmark_price(self, listing: ComputerListing, benchmarks: Dict[str, Any]) -> float:
        proc = listing.processor.upper()
        if "M1" in proc:
            if listing.condition == "novo":
                return 6000.0
            return 4200.0
        elif "M2" in proc:
            if listing.condition == "novo":
                return 7600.0
            return 6200.0
        elif "INTEL" in proc:
            return 2200.0
        return 4000.0

    def _determine_tier_and_verdict(
        self,
        cbi: float,
        sent_audit: SentimentAudit,
        hw_audit: HardwareAudit,
        price_delta_pct: float
    ) -> tuple[str, str]:
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto":
            return "F", "Evitar Absolutamente"

        if cbi >= 88.0:
            return "S", "Altamente Recomendado"
        elif cbi >= 76.0:
            return "A", "Bom Negócio"
        elif cbi >= 62.0:
            return "B", "Neutro"
        elif cbi >= 45.0:
            return "C", "Desaconselhado"
        else:
            return "F", "Evitar Absolutamente"

    def _generate_justification(
        self,
        listing: ComputerListing,
        hw: HardwareAudit,
        sent: SentimentAudit,
        cbi: float,
        tier: str,
        verdict: str,
        fair_price: float,
        delta: float
    ) -> str:
        if tier == "F":
            return (
                f"REPROVADO PELO ESPECIALISTA: Embora o preço de R$ {listing.price:,.2f} aparente ser convidativo, "
                f"o equipamento sofre com problemas crônicos graves ({', '.join(sent.chronic_flaws_identified)}) e "
                f"arquitetura defasada. Qualquer reparo de teclado ou tela em Recife custará entre R$ 1.800 e R$ 3.000, "
                f"inviabilizando totalmente o custo-benefício."
            )

        preco_str = (
            f"{abs(delta):.1f}% abaixo do valor de referência de Recife (R$ {fair_price:,.2f})"
            if delta >= 0 else
            f"{abs(delta):.1f}% acima da média de usados locais"
        )

        return (
            f"Classificação [{tier}] - Veredito: {verdict}. "
            f"Equilíbrio notável com Nota de Hardware {hw.hardware_score}/100 e Sentimento {sent.sentiment_score}/100. "
            f"Preço de R$ {listing.price:,.2f} está {preco_str}. "
            f"{hw.summary}"
        )

    def _generate_precautions(self, listing: ComputerListing, sent: SentimentAudit) -> List[str]:
        precautions = []
        if listing.condition in ["usado", "seminovo"]:
            precautions.append("Marcar encontro exclusivamente em local seguro e público em Recife (ex: Shopping Recife ou Shopping Riomar).")
            precautions.append("Exigir que o vendedor desvincule o iCloud e o 'Buscar Meu Mac' na sua frente antes do pagamento via Pix.")
            precautions.append("Testar todas as portas USB-C/Thunderbolt conectando um pen-drive ou carregador.")
            precautions.append("Executar o diagnóstico da Apple (ligar segurando a tecla 'D' ou botão Power) para testar memória e placa.")
            if listing.battery_health_pct and listing.battery_health_pct < 85:
                precautions.append(f"Atenção à bateria ({listing.battery_health_pct}%): provisionar ~R$ 600 para futura substituição.")
        else:
            precautions.append("Conferir se a Nota Fiscal está no seu nome/CPF e com o número de série correspondente.")
            precautions.append("Ativar a cobertura oficial de garantia de 1 ano no site checkcoverage.apple.com assim que abrir.")
        return precautions
