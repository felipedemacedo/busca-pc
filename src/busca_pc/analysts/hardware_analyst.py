from __future__ import annotations
import asyncio
from typing import Dict, Any
from busca_pc.models import ComputerListing, HardwareAudit

class HardwareAnalystAgent:
    """
    Agente especialista em auditoria técnica e classificação precisa de hardware.
    Mede poder computacional, arquitetura de silício (ARM vs x86), eficiência térmica,
    longevidade e gargalos de RAM/SSD.
    """

    NAME = "HardwareAnalystAgent"
    ROLE = "Especialista em Auditoria e Classificação de Hardware"

    async def analyze(self, listing: ComputerListing) -> HardwareAudit:
        """Executa auditoria técnica profunda de especificações de hardware."""
        await asyncio.sleep(0.05)  # Simula latência de processamento/consulta técnica assíncrona

        pros = []
        cons = []
        score = 50.0
        lifespan = 2

        # 1. Arquitetura e Processador
        proc = listing.processor.upper()
        if "M3" in proc or "M4" in proc:
            score += 35.0
            lifespan = 6
            proc_eval = f"Processador de ponta ({listing.processor}) com litografia de 3nm, Ray Tracing por hardware e máxima eficiência por Watt."
            pros.append(f"Chip {listing.processor} ultrarrápido com altíssima longevidade")
        elif "M2" in proc:
            score += 30.0
            lifespan = 5
            proc_eval = f"Chip {listing.processor} com núcleos de alto desempenho, aceleração ProRes e excelente eficiência energética."
            pros.append(f"Excelente poder de CPU/GPU com chip {listing.processor}")
        elif "M1" in proc:
            score += 26.0
            lifespan = 4
            proc_eval = f"Chip Apple Silicon M1 pioneiro. Mantém performance formidável no dia a dia, autonomia de até 18h e superação nítida sobre x86."
            pros.append("Apple Silicon M1: revolução em autonomia, frio ao toque e velocidade monothread")
        elif "INTEL" in proc or "CORE I" in proc:
            score -= 15.0
            lifespan = 1
            proc_eval = f"Processador legado Intel x86 ({listing.processor}). Arquitetura defasada no ecossistema Apple, alto consumo térmico e término iminente de suporte de SO."
            cons.append("Processador Intel ultrapassado no ecossistema Mac: quente, ruidoso e sem futuro suporte")
        else:
            proc_eval = f"Processador: {listing.processor}"

        # 2. Memória RAM
        if listing.ram_gb >= 16:
            score += 15.0
            ram_eval = f"{listing.ram_gb}GB de memória. Amplo espaço para compilação, edição pesada, Docker e multitarefa sem pressão de swap no SSD."
            pros.append(f"{listing.ram_gb}GB RAM: capacidade profissional sem degradação por swap")
        elif listing.ram_gb == 8:
            score += 5.0
            ram_eval = "8GB de memória unificada. Excelente para uso geral, navegação intensa, estudos e escritório; sob cargas muito pesadas, recorre ao swap do SSD."
            pros.append("8GB unificados bem otimizados pelo macOS para tarefas cotidianas")
            cons.append("8GB é o limite inferior atual; sem possibilidade de upgrade físico")
        else:
            score -= 20.0
            ram_eval = f"{listing.ram_gb}GB de RAM: insuficiente para os padrões modernos de software."
            cons.append(f"Apenas {listing.ram_gb}GB de memória RAM")

        # 3. Armazenamento SSD
        if listing.storage_gb >= 512:
            score += 10.0
            storage_eval = f"{listing.storage_gb}GB SSD NVMe veloz, espaço seguro para sistema e bibliotecas locais."
            pros.append(f"{listing.storage_gb}GB SSD espaçoso")
        elif listing.storage_gb == 256:
            score += 4.0
            storage_eval = "256GB SSD ultrarrápido. Atende perfeitamente sistema e projetos em nuvem, mas requer cautela ou drive externo para mídias pesadas."
            cons.append("256GB requer disciplina com armazenamento ou SSD externo")
        else:
            score -= 10.0
            storage_eval = f"{listing.storage_gb}GB muito restrito para instalações e atualizações do SO."
            cons.append("Armazenamento extremamente limitado")

        # 4. Eficiência Térmica e Autonomia
        if listing.architecture == "Apple Silicon":
            score += 10.0
            thermal_eval = "Design fanless (silencioso e sem poeira interna) ou com ventoinha ultrassilenciosa, com autonomia de 14 a 18 horas de bateria real."
            pros.append("Autonomia de bateria estelar (14h-18h) e operação fria")
        else:
            score -= 10.0
            thermal_eval = "Arquitetura x86 com alta dissipação de calor, ventoinhas ativas constantes e bateria com autonomia degradada (3 a 5 horas)."
            cons.append("Esquenta consideravelmente e ventoinhas disparam sob carga leve")

        # 5. Penalidades por ano e bateria
        if listing.battery_health_pct is not None:
            if listing.battery_health_pct < 80:
                score -= 10.0
                cons.append(f"Saúde da bateria em {listing.battery_health_pct}% (necessitará de manutenção em breve)")
            elif listing.battery_health_pct >= 90:
                score += 5.0
                pros.append(f"Saúde da bateria excelente: {listing.battery_health_pct}%")

        # Normalização de Score (0 a 100)
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
