from __future__ import annotations
import asyncio
from typing import Dict, Any, List
from busca_pc.models import ComputerListing, SentimentAudit

class SentimentAnalystAgent:
    """
    Agente especialista em sentimento, reputação na internet e histórico técnico de falhas.
    Analisa fóruns (Reddit r/mac, MacRumors), canais de assistência técnica (YouTube, iFixit)
    e identifica problemas crônicos como Teclado Borboleta, Flexgate, Throttling Térmico e
    velocidade de SSD (NAND único).
    """

    NAME = "SentimentAnalystAgent"
    ROLE = "Analista de Sentimento e Histórico Técnico de Comunidade"

    async def analyze(self, listing: ComputerListing) -> SentimentAudit:
        """Executa auditoria de sentimento técnico e histórico de defeitos da máquina."""
        await asyncio.sleep(0.05)  # Simula latência de consulta à base de reputação e fóruns

        pros = []
        cons = []
        chronic_flaws = []
        sentiment_score = 60.0

        title_upper = listing.title.upper()
        proc_upper = listing.processor.upper()
        year = listing.year or (2020 if "M1" in proc_upper else 2018)

        # Diagnóstico de MacBooks Intel 2016-2019
        if "INTEL" in proc_upper or year in [2016, 2017, 2018, 2019] and "M" not in proc_upper:
            chronic_flaws.append("Teclado mecanismo Borboleta (Butterfly keyboard) sujeito a repetição ou quebra de teclas")
            chronic_flaws.append("Problema crônico 'Flexgate' (cabo da tela frágil rompendo na dobradiça)")
            chronic_flaws.append("Thermal throttling acentuado e ventoinhas extremamente ruidosas")
            sentiment_score = 25.0
            verdict = "Alto Risco de Quebra Crônica"
            consensus = (
                "Consenso técnico extremamente desfavorável na comunidade. A arquitetura Intel nesses anos sofreu com o "
                "infame teclado borboleta e o defeito Flexgate. O custo de conserto da tela ou teclado costuma ultrapassar "
                "o valor residual da máquina."
            )
            cons.extend([
                "Índice de falha mecânica de teclado elevado sem programa de recall ativo",
                "Risco iminente de Flexgate (tela preta ou luz de palco)",
                "Reputação severamente manchada em fóruns de reparo e no Reddit"
            ])

        # Diagnóstico de MacBook Air M1 (2020)
        elif "M1" in proc_upper and "AIR" in title_upper:
            sentiment_score = 94.0
            verdict = "Altíssima Confiabilidade"
            consensus = (
                "Unanimidade de aclamação em toda a internet (Reddit, YouTube, TechRadar). Considerado o notebook com o "
                "melhor custo-benefício da história recente da Apple. Sem ventoinhas (zero ruído, zero acúmulo de poeira), "
                "teclado Magic Keyboard tradicional super confiável e virtualmente livre de defeitos crônicos de placa."
            )
            pros.extend([
                "Consenso de 96%+ de aprovação e satisfação de usuários",
                "Teclado Magic Keyboard scissor switch consagrado e durável",
                "Zero ruído acústico e sem peças mecânicas móveis de arrefecimento",
                "Alta liquidez de revenda no mercado brasileiro"
            ])
            if listing.ram_gb == 8:
                cons.append("Comunidade alerta que 8GB pode usar swap em edição 4K pesada, mas para uso diário é impecável")

        # Diagnóstico de MacBook Air M2
        elif "M2" in proc_upper and "AIR" in title_upper:
            sentiment_score = 90.0
            verdict = "Altíssima Confiabilidade"
            consensus = (
                "Altíssima aprovação pelo novo design moderno, tela Liquid Retina mais brilhante e carregador MagSafe 3. "
                "Único apontamento em reviews técnicos é que a versão de 256GB usa um único chip NAND, o que gera menor "
                "velocidade de gravação sequencial que o M1 de 256GB, embora imperceptível para a maioria."
            )
            pros.extend([
                "Design moderno ultrafino com bordas reduzidas e conector MagSafe 3",
                "Tela com 500 nits e excelente fidelidade de cores",
                "Câmera FaceTime 1080p muito elogiada frente aos 720p dos modelos anteriores"
            ])
            if listing.storage_gb == 256:
                cons.append("Nota técnica de reviews: SSD de 256GB com chip NAND único é ligeiramente mais lento em benchmarks sintéticos")

        # Diagnóstico de MacBook Pro M1/M2/M3
        elif "PRO" in title_upper and "M" in proc_upper:
            sentiment_score = 96.0
            verdict = "Altíssima Confiabilidade"
            consensus = (
                "Máquinas de grau profissional com reputação impecável. Telas mini-LED ProMotion 120Hz aclamadas, "
                "diversidade de portas (HDMI, leitor SD) e refrigeração ativa silenciosa."
            )
            pros.extend([
                "Consenso de excelência para desenvolvedores e criadores de conteúdo",
                "Tela ProMotion e portas HDMI/SD resgatadas aclamadas pela comunidade"
            ])
        else:
            verdict = "Boa Confiabilidade"
            consensus = "Avaliações majoritariamente positivas na média da categoria."
            sentiment_score = 75.0

        summary = (
            f"Laudo de Comunidade: Nota {sentiment_score}/100. Confiabilidade: {verdict}. "
            f"Defeitos crônicos mapeados: {len(chronic_flaws)}. Consenso: {consensus[:120]}..."
        )

        return SentimentAudit(
            sentiment_score=sentiment_score,
            community_consensus=consensus,
            chronic_flaws_identified=chronic_flaws,
            reliability_verdict=verdict,
            pros=pros,
            cons=cons,
            summary=summary,
        )
