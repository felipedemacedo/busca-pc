from __future__ import annotations
from typing import Dict, Any, List
from busca_pc.models import ComputerListing, HardwareAudit, SentimentAudit, FinalClassification

class PCClassifierAgent:
    """
    Especialista em Classificação de PC.
    Avalia notebooks Apple e Dell, calculando notas compostas, preços justos de mercado,
    Índice de Custo-Benefício (ICB), Tiers (S a F) e vereditos técnicos.
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
        composite_quality = (hw_audit.hardware_score * 0.52) + (sent_audit.sentiment_score * 0.48)

        # 2. Definição do Preço de Referência Específico de Mercado
        fair_price = self._determine_benchmark_price(listing)

        # 3. Análise de Preço e Desconto Relativo
        price_delta_pct = ((fair_price - listing.price) / fair_price) * 100.0

        # 4. Cálculo Rigoroso do Índice de Custo-Benefício (ICB)
        # 4.1 Fator de Preço Absoluto: Desincentiva compras de valor desproporcional (lei dos rendimentos decrescentes)
        # R$ 3.000 -> 1.08; R$ 5.000 -> 1.02; R$ 8.000 -> 0.92; R$ 12.000 -> 0.80; R$ 19.000 -> 0.58
        price_factor = max(0.55, 1.10 - (max(0.0, listing.price - 2500.0) / 32000.0))

        # 4.2 Fator Desconto de Mercado (em relação ao valor justo da configuração em Recife)
        discount_factor = 1.0 + ((price_delta_pct / 100.0) * 0.75)

        # 4.3 Ajuste de condição: produto novo lacrado com garantia de fabricante de 12 meses
        cond_multiplier = 1.04 if listing.condition == "novo" else 1.0

        raw_cbi = composite_quality * price_factor * discount_factor * cond_multiplier

        # Penalidade drástica para produtos com alto risco crônico ou obsolescência (ex: Intel butterfly/flexgate em Mac antigo)
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto" or sent_audit.sentiment_score <= 30.0:
            raw_cbi = min(raw_cbi * 0.20, 20.0)

        cbi_score = round(max(0.0, min(100.0, raw_cbi)), 1)

        # 5. Atribuição de Tier e Veredito Seletivos
        tier, verdict = self._determine_tier_and_verdict(cbi_score, sent_audit, hw_audit, price_delta_pct)

        # 6. Justificativa Técnica
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
        title = listing.title.upper()
        brand = listing.brand.upper()
        cond = listing.condition

        # === LINHA DELL ===
        if "DELL" in brand or "INSPIRON" in title or "G15" in title or "XPS" in title:
            if "XPS 16" in title or "RTX 4060" in title:
                return 21000.0 if cond == "novo" else 14500.0
            elif "XPS 13" in title or "CORE ULTRA" in proc:
                return 13000.0 if cond == "novo" else 8900.0
            elif "RTX 4050" in title or "RTX 4050" in proc:
                return 7500.0 if cond == "novo" else 5500.0
            elif "RTX 3050" in title or "RTX 3050" in proc or "G15" in title:
                return 5800.0 if cond == "novo" else 4200.0
            elif "I5" in proc or "16GB" in title:
                return 3900.0 if cond == "novo" else 2700.0
            elif "I3" in proc:
                return 2900.0 if cond == "novo" else 1900.0
            return 4000.0

        # === LINHA APPLE MACBOOK ===
        if "NEO" in title or "A18" in proc:
            if listing.storage_gb >= 512:
                return 7400.0 if cond == "novo" else 5500.0
            return 6400.0 if cond == "novo" else 4800.0
        elif "M5" in proc:
            return 38000.0 if cond == "novo" else 32000.0
        elif "M4 MAX" in proc:
            return 28000.0 if cond == "novo" else 23000.0
        elif "M4 PRO" in proc:
            return 23500.0 if cond == "novo" else 18500.0
        elif "M4" in proc:
            return 9500.0 if cond == "novo" else 7600.0
        elif "M3 MAX" in proc:
            return 26000.0 if cond == "novo" else 21000.0
        elif "M3 PRO" in proc:
            return 17500.0 if cond == "novo" else 13500.0
        elif "M2 PRO" in proc:
            return 15000.0 if cond == "novo" else 12500.0
        elif "M1 PRO" in proc:
            return 12000.0 if cond == "novo" else 8800.0
        elif "M3" in proc:
            return 11200.0 if cond == "novo" else 8500.0
        elif "M2" in proc:
            if listing.ram_gb >= 16:
                return 8900.0 if cond == "novo" else 7200.0
            return 7600.0 if cond == "novo" else 6200.0
        elif "M1" in proc:
            if listing.ram_gb >= 16:
                return 7200.0 if cond == "novo" else 5200.0
            return 6000.0 if cond == "novo" else 4200.0
        elif "INTEL" in proc:
            if (listing.year or 2017) >= 2020:
                return 2200.0 if cond == "novo" else 1500.0
            elif (listing.year or 2017) >= 2017:
                return 2000.0 if cond == "novo" else 1400.0
            return 1100.0 if cond == "novo" else 750.0

        return 4500.0

    def _determine_tier_and_verdict(
        self,
        cbi: float,
        sent_audit: SentimentAudit,
        hw_audit: HardwareAudit,
        price_delta_pct: float
    ) -> tuple[str, str]:
        if "Alto Risco" in sent_audit.reliability_verdict or hw_audit.tier_category == "Obsoleto" or sent_audit.sentiment_score <= 30.0:
            return "F", "Evitar Absolutamente"

        if cbi >= 88.0:
            return "S", "Altamente Recomendado"
        elif cbi >= 78.0:
            return "A", "Altamente Recomendado"
        elif cbi >= 66.0:
            return "B", "Bom Negócio"
        elif cbi >= 45.0:
            return "C", "Neutro"
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
                f"arquitetura defasada. Qualquer reparo em assistência especializada custará entre R$ 1.800 e R$ 3.000, "
                f"tornando a máquina financeiramente inviável."
            )

        preco_str = (
            f"{abs(delta):.1f}% abaixo do valor de referência de mercado (R$ {fair_price:,.2f})"
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
            if "APPLE" in listing.brand.upper():
                precautions.append("Exigir a desvinculação completa do iCloud e do 'Buscar Meu Mac' na sua frente antes da transferência Pix.")
                precautions.append("Executar o Diagnóstico Oficial Apple (ligar pressionando 'D' ou botão Power).")
            else:
                precautions.append("Executar teste de estresse de CPU/GPU (ex: CrystalDiskInfo para o SSD e FurMark para a placa dedicada).")
                precautions.append("Conferir etiqueta de Service Tag no chassi para checar garantia remanescente no site da Dell.")
            precautions.append("Testar todas as portas USB/Thunderbolt, teclado e carregador original.")
        else:
            if "DELL" in listing.brand.upper():
                precautions.append("Cadastrar a Service Tag no site da Dell para ativar a garantia com atendimento em domicílio (on-site).")
                precautions.append("Aproveitar condições de frete grátis e cupons adicionais da loja oficial Dell Brasil.")
            else:
                precautions.append("Conferir se a Nota Fiscal está emitida em seu CPF com número de série correspondente.")
                precautions.append("Ativar a cobertura de garantia oficial no portal da fabricante.")
        return precautions
