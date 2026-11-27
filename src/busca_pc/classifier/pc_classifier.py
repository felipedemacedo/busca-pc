from __future__ import annotations
from typing import Dict, Any, List
from busca_pc.models import ComputerListing, HardwareAudit, SentimentAudit, FinalClassification

class PCClassifierAgent:
    """
    Especialista em Classificação de PC.
    Avalia TODO o espectro de máquinas (de modelos de baixo custo a workstations de ponta),
    sem limites artificiais de orçamento. Calcula a nota composta de produto, o valor justo
    de mercado específico da configuração, o Índice de Custo-Benefício (ICB), o Tier (S a F)
    e o veredito final.
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

        # 2. Definição do Preço de Referência Específico de Mercado em Recife
        fair_price = self._determine_benchmark_price(listing)

        # 3. Análise de Preço e Desconto Relativo
        price_delta_pct = ((fair_price - listing.price) / fair_price) * 100.0

        # 4. Cálculo do Índice de Custo-Benefício (ICB)
        price_ratio = fair_price / max(listing.price, 1.0)
        price_multiplier = min(1.35, max(0.5, price_ratio ** 0.65))

        raw_cbi = composite_quality * price_multiplier

        # Penalidade drástica para produtos com alto risco crônico ou obsolescência (ex: Intel butterfly/flexgate)
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto":
            raw_cbi = min(raw_cbi * 0.35, 30.0)

        # Ajuste de condição: produtos novos têm prêmio de garantia de 1 ano
        if listing.condition == "novo":
            raw_cbi = min(raw_cbi * 1.05, 96.0)

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

    def _determine_benchmark_price(self, listing: ComputerListing) -> float:
        """Determina o preço de referência justo com base na configuração real da máquina."""
        proc = listing.processor.upper()
        cond = listing.condition
        ram = listing.ram_gb
        storage = listing.storage_gb

        # Workstations e Máquinas Pro
        if "M4 PRO" in proc:
            return 23500.0 if cond == "novo" else 18500.0
        elif "M3 MAX" in proc:
            return 26000.0 if cond == "novo" else 21000.0
        elif "M3 PRO" in proc:
            return 17500.0 if cond == "novo" else 13500.0
        elif "M2 PRO" in proc:
            return 15000.0 if cond == "novo" else 12500.0
        elif "M1 PRO" in proc:
            return 12000.0 if cond == "novo" else 8800.0

        # Linha Air e modelos de consumo
        elif "M3" in proc:
            if ram >= 16:
                return 11200.0 if cond == "novo" else 8500.0
            return 9500.0 if cond == "novo" else 7200.0
        elif "M2" in proc:
            if ram >= 16:
                return 9200.0 if cond == "novo" else 7200.0
            return 7600.0 if cond == "novo" else 6200.0
        elif "M1" in proc:
            if ram >= 16:
                return 7200.0 if cond == "novo" else 5200.0
            return 6000.0 if cond == "novo" else 4200.0

        # Modelos Intel Antigos
        elif "INTEL" in proc:
            if (listing.year or 2017) >= 2017:
                return 2200.0
            return 1400.0

        return 4500.0

    def _determine_tier_and_verdict(
        self,
        cbi: float,
        sent_audit: SentimentAudit,
        hw_audit: HardwareAudit,
        price_delta_pct: float
    ) -> tuple[str, str]:
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto":
            return "F", "Evitar Absolutamente"

        if cbi >= 90.0:
            return "S", "Altamente Recomendado"
        elif cbi >= 78.0:
            return "A", "Bom Negócio"
        elif cbi >= 64.0:
            return "B", "Neutro"
        elif cbi >= 48.0:
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
                f"REPROVADO PELO ESPECIALISTA: Embora o preço de R$ {listing.price:,.2f} pareça barato, "
                f"o equipamento sofre com problemas crônicos graves ({', '.join(sent.chronic_flaws_identified)}) e "
                f"arquitetura defasada. Qualquer reparo de teclado ou tela em Recife custará entre R$ 1.800 e R$ 3.000, "
                f"tornando a máquina financeiramente inviável."
            )

        preco_str = (
            f"{abs(delta):.1f}% abaixo do valor justo de mercado em Recife (R$ {fair_price:,.2f})"
            if delta >= 0 else
            f"{abs(delta):.1f}% acima da média praticada"
        )

        return (
            f"Classificação [{tier}] - Veredito: {verdict}. "
            f"Nota de Hardware {hw.hardware_score}/100 e Sentimento {sent.sentiment_score}/100. "
            f"Preço de R$ {listing.price:,.2f} está {preco_str}. "
            f"{hw.summary}"
        )

    def _generate_precautions(self, listing: ComputerListing, sent: SentimentAudit) -> List[str]:
        precautions = []
        if listing.condition in ["usado", "seminovo"]:
            precautions.append("Marcar encontro exclusivamente em local monitorado em Recife (ex: Shopping Recife, Shopping Riomar ou Plaza Casa Forte).")
            precautions.append("Exigir a desvinculação completa do iCloud e do 'Buscar Meu Mac' na sua frente antes da transferência Pix.")
            precautions.append("Testar todas as portas Thunderbolt/USB-C, teclado e trackpad.")
            precautions.append("Executar o Diagnóstico Oficial Apple (ligar pressionando 'D' ou mantendo o botão Power pressionado).")
            if listing.battery_health_pct and listing.battery_health_pct < 85:
                precautions.append(f"Atenção à bateria ({listing.battery_health_pct}% de saúde): orçar futura substituição.")
        else:
            precautions.append("Conferir se a Nota Fiscal está emitida em seu CPF com número de série correspondente.")
            precautions.append("Ativar a cobertura de garantia oficial Apple de 1 ano no portal checkcoverage.apple.com.")
        return precautions
