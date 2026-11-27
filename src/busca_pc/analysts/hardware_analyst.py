from __future__ import annotations
import asyncio
from typing import Dict, Any
from busca_pc.models import ComputerListing, HardwareAudit

class HardwareAnalystAgent:
    """
    Agente especialista em auditoria técnica e classificação precisa de hardware.
    Mede poder computacional, arquitetura de silício (ARM Apple Silicon vs x86),
    largura de banda de memória, barramentos, eficiência térmica, longevidade e gargalos.
    """

    NAME = "HardwareAnalystAgent"
    ROLE = "Especialista em Auditoria e Classificação de Hardware"

    async def analyze(self, listing: ComputerListing) -> HardwareAudit:
        """Executa auditoria técnica profunda de especificações de hardware."""
        await asyncio.sleep(0.02)

        pros = []
        cons = []
        score = 50.0
        lifespan = 3

        proc = listing.processor.upper()

        # 1. Arquitetura e Processador
        if "M4 PRO" in proc or "M4 MAX" in proc:
            score += 42.0
            lifespan = 7
            proc_eval = f"SoC topo de linha ({listing.processor}) de última geração com litografia 3nm de 2ª geração, largura de banda absurda e Thunderbolt 5."
            pros.append(f"Chip {listing.processor} estado da arte com até 7 anos de longevidade máxima")
        elif "M3 MAX" in proc or "M2 MAX" in proc:
            score += 40.0
            lifespan = 6
            proc_eval = f"Monstro de computação ({listing.processor}) com dezenas de núcleos de GPU, motores neurais duplos e alta capacidade de renderização/LLMs."
            pros.append(f"Workstation extrema com chip {listing.processor}")
        elif "M3 PRO" in proc or "M2 PRO" in proc or "M1 PRO" in proc:
            score += 36.0
            lifespan = 6
            proc_eval = f"Processador profissional ({listing.processor}) com barramento de memória alargado (150-200 GB/s) e múltiplos encoders de mídia."
            pros.append(f"Silício profissional {listing.processor} com barramento ultraveloz e aceleração de mídia")
        elif "M3" in proc:
            score += 33.0
            lifespan = 5
            proc_eval = f"Chip {listing.processor} com Ray Tracing por hardware, Dynamic Caching e suporte a monitores múltiplos."
            pros.append("Chip M3 com aceleração gráfica moderna e suporte a telas externas")
        elif "M2" in proc:
            score += 30.0
            lifespan = 5
            proc_eval = f"Chip {listing.processor} com núcleos de alto desempenho e aceleração ProRes."
            pros.append(f"Excelente poder de CPU/GPU com chip {listing.processor}")
        elif "M1" in proc:
            score += 26.0
            lifespan = 4
            proc_eval = f"Chip Apple Silicon M1 pioneiro. Mantém performance formidável, autonomia de até 18h e superação nítida sobre x86."
            pros.append("Apple Silicon M1: autonomia estelar, operação fria e agilidade monothread")
        elif "INTEL" in proc or "CORE I" in proc:
            score -= 18.0
            lifespan = 1
            proc_eval = f"Processador legado Intel x86 ({listing.processor}). Arquitetura defasada no ecossistema Apple, alto consumo térmico e término de suporte oficial."
            cons.append("Processador Intel ultrapassado no ecossistema Mac: quente, ruidoso e sem longevidade de software")
        else:
            proc_eval = f"Processador: {listing.processor}"

        # 2. Memória RAM
        if listing.ram_gb >= 32:
            score += 18.0
            ram_eval = f"{listing.ram_gb}GB de memória unificada massiva. Capacidade para rodar modelos de IA locais (LLMs), múltiplos containers e timelines 8K sem qualquer swap."
            pros.append(f"{listing.ram_gb}GB RAM: capacidade para fluxos extremos e IA local")
        elif listing.ram_gb >= 16:
            score += 14.0
            ram_eval = f"{listing.ram_gb}GB de memória unificada. Amplo espaço para compilação pesada, Docker, multitarefa e longevidade sem desgaste de swap."
            pros.append(f"{listing.ram_gb}GB RAM: padrão ideal para longevidade e multitarefa pesada")
        elif listing.ram_gb == 8:
            score += 4.0
            ram_eval = "8GB de memória unificada. Excelente para uso geral, navegação intensa, estudos e escritório; sob cargas muito pesadas, recorre ao swap do SSD."
            pros.append("8GB unificados bem otimizados pelo macOS para tarefas cotidianas")
            cons.append("8GB é o limite básico atual; sem possibilidade de upgrade físico")
        else:
            score -= 22.0
            ram_eval = f"{listing.ram_gb}GB de RAM: insuficiente para padrões contemporâneos."
            cons.append(f"Apenas {listing.ram_gb}GB de memória RAM")

        # 3. Armazenamento SSD
        if listing.storage_gb >= 1024:
            score += 12.0
            storage_eval = f"{listing.storage_gb}GB (1TB) SSD NVMe de alta velocidade, espaço profissional com sobra."
            pros.append(f"{listing.storage_gb}GB SSD espaçoso de 1TB")
        elif listing.storage_gb >= 512:
            score += 8.0
            storage_eval = f"{listing.storage_gb}GB SSD NVMe veloz, espaço seguro para sistema e bibliotecas locais."
            pros.append(f"{listing.storage_gb}GB SSD balanceado")
        elif listing.storage_gb == 256:
            score += 3.0
            storage_eval = "256GB SSD ultrarrápido. Atende perfeitamente sistema e projetos em nuvem, mas requer cautela ou drive externo para mídias pesadas."
            cons.append("256GB requer disciplina com armazenamento ou SSD externo")
        else:
            score -= 12.0
            storage_eval = f"{listing.storage_gb}GB muito restrito para instalações e atualizações do SO."
            cons.append("Armazenamento extremamente limitado")

        # 4. Tela e Conectividade
        if listing.screen_size_inches and listing.screen_size_inches >= 14.0:
            score += 6.0
            pros.append("Tela Liquid Retina XDR Mini-LED com taxa de 120Hz ProMotion e portas HDMI/SD")
        elif listing.screen_size_inches and listing.screen_size_inches == 13.6:
            score += 3.0
            pros.append("Tela Liquid Retina com bordas finas e 500 nits de brilho")

        # 5. Eficiência Térmica e Autonomia
        if listing.architecture == "Apple Silicon":
            score += 8.0
            thermal_eval = "Arquitetura Apple Silicon de altíssima eficiência energética, mantendo 14 a 22 horas de bateria real e operação fria."
            pros.append("Autonomia de bateria estelar (14h a 22h) e operação silenciosa")
        else:
            score -= 12.0
            thermal_eval = "Arquitetura x86 com alta dissipação térmica, ventoinhas constantes e autonomia reduzida (2 a 4 horas)."
            cons.append("Esquenta consideravelmente e ventoinhas disparam sob carga leve")

        # 6. Saúde da Bateria
        if listing.battery_health_pct is not None:
            if listing.battery_health_pct < 80:
                score -= 10.0
                cons.append(f"Saúde da bateria em {listing.battery_health_pct}% (necessitará de manutenção em breve)")
            elif listing.battery_health_pct >= 90:
                score += 3.0
                pros.append(f"Saúde da bateria excelente: {listing.battery_health_pct}%")

        final_hw_score = max(5.0, min(100.0, round(score, 1)))

        if final_hw_score >= 88:
            tier = "Excelente"
        elif final_hw_score >= 75:
            tier = "Muito Bom"
        elif final_hw_score >= 60:
            tier = "Bom"
        elif final_hw_score >= 40:
            tier = "Medíocre"
        else:
            tier = "Obsoleto"

        summary = (
            f"Hardware classificado como '{tier}' (Nota: {final_hw_score}/100). "
            f"Equipado com {listing.processor}, {listing.ram_gb}GB RAM e {listing.storage_gb}GB SSD. "
            f"Expectativa de longevidade estimada em {lifespan} anos."
        )

        return HardwareAudit(
            hardware_score=final_hw_score,
            tier_category=tier,
            processor_eval=proc_eval,
            ram_eval=ram_eval,
            storage_eval=storage_eval,
            thermal_and_efficiency_eval=thermal_eval,
            estimated_lifespan_years=lifespan,
            pros=pros,
            cons=cons,
            summary=summary,
        )
