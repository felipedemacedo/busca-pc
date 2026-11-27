from __future__ import annotations
import asyncio
from typing import Dict, Any
from busca_pc.models import ComputerListing, HardwareAudit

class HardwareAnalystAgent:
    """
    Agente especialista em auditoria técnica e classificação precisa de hardware.
    Avalia Apple Silicon (M1 a M4), processadores Intel modernos (Core 13ª Geração e Core Ultra),
    placas de vídeo dedicadas NVIDIA GeForce RTX, memória unificada vs DDR5 expansível,
    telas (120Hz/165Hz/OLED) e eficiência térmica.
    """

    NAME = "HardwareAnalystAgent"
    ROLE = "Especialista em Auditoria e Classificação de Hardware"

    async def analyze(self, listing: ComputerListing) -> HardwareAudit:
        """Executa auditoria técnica profunda de especificações de hardware."""
        await asyncio.sleep(0.02)

        pros = []
        cons = []
        score = 50.0
        lifespan = 4

        proc = listing.processor.upper()
        title = listing.title.upper()

        # 1. Arquitetura, Processador & Gráficos
        # Placas de Vídeo Dedicadas Gamer/Workstation
        if "RTX 4060" in proc or "RTX 4060" in title:
            score += 38.0
            lifespan = 6
            proc_eval = f"{listing.processor} com GPU dedicada NVIDIA RTX 4060 8GB (DLSS 3 e Ray Tracing). Altíssimo poder gráfico para games pesados e inteligência artificial."
            pros.append("NVIDIA GeForce RTX 4060 8GB dedicada: excelente para IA, 3D e jogos em 1440p")
        elif "RTX 4050" in proc or "RTX 4050" in title:
            score += 34.0
            lifespan = 5
            proc_eval = f"{listing.processor} com GPU dedicada NVIDIA RTX 4050 6GB. Ótima performance em jogos modernos e aceleração CUDA."
            pros.append("NVIDIA GeForce RTX 4050 6GB: suporte moderno a DLSS 3 e aceleração gráfica")
        elif "RTX 3050" in proc or "RTX 3050" in title:
            score += 28.0
            lifespan = 4
            proc_eval = f"{listing.processor} com GPU dedicada NVIDIA RTX 3050 6GB. Entrada gamer competente para 1080p."
            pros.append("NVIDIA GeForce RTX 3050 6GB dedicada: boa entrada gráfica com suporte a ray tracing")

        # Apple Silicon Chips
        elif "M4 PRO" in proc or "M4 MAX" in proc:
            score += 42.0
            lifespan = 7
            proc_eval = f"SoC topo de linha ({listing.processor}) de última geração com litografia 3nm de 2ª geração, largura de banda absurda e Thunderbolt 5."
            pros.append(f"Chip {listing.processor} estado da arte com até 7 anos de longevidade")
        elif "M3 MAX" in proc or "M2 MAX" in proc:
            score += 40.0
            lifespan = 6
            proc_eval = f"Monstro de computação ({listing.processor}) com dezenas de núcleos de GPU, motores neurais duplos e alta capacidade de renderização."
            pros.append(f"Workstation extrema com chip {listing.processor}")
        elif "M3 PRO" in proc or "M2 PRO" in proc or "M1 PRO" in proc:
            score += 36.0
            lifespan = 6
            proc_eval = f"Processador profissional ({listing.processor}) com barramento de memória alargado (150-200 GB/s) e múltiplos encoders de mídia."
            pros.append(f"Silício profissional {listing.processor} com barramento ultraveloz")
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
            proc_eval = f"Chip Apple Silicon M1 pioneiro. Mantém performance formidável, autonomia de até 18h e superação nítida sobre x86 antigo."
            pros.append("Apple Silicon M1: autonomia estelar, operação fria e agilidade monothread")

        # Processadores Modernos Intel (PC Dell)
        elif "CORE ULTRA 9" in proc or "CORE ULTRA 7" in proc:
            score += 36.0
            lifespan = 6
            proc_eval = f"Processador Intel Core Ultra de ponta ({listing.processor}) com NPU dedicada para IA local, arquitetura híbrida e eficiência aprimorada."
            pros.append(f"Intel Core Ultra com NPU integrada para tarefas inteligentes de IA")
        elif "I7-13" in proc or "I5-13" in proc:
            score += 29.0
            lifespan = 5
            proc_eval = f"Processador moderno Intel Core 13ª Geração ({listing.processor}). Alta contagem de núcleos (P-cores + E-cores) e ótimo desempenho multithread."
            pros.append(f"Intel Core 13ª Geração de alto rendimento para produtividade")
        elif "I3-12" in proc or "I3-13" in proc:
            score += 18.0
            lifespan = 3
            proc_eval = f"Processador de entrada Intel Core i3 ({listing.processor}). Adequado para tarefas cotidianas, estudos e escritório leve."
            pros.append("Intel Core de arquitetura recente competente para tarefas leves")

        # Processadores Antigos Intel em MacBooks
        elif "APPLE" in listing.brand.upper() and ("INTEL" in proc or "CORE I" in proc):
            score -= 18.0
            lifespan = 1
            proc_eval = f"Processador legado Intel x86 em Mac ({listing.processor}). Arquitetura defasada no ecossistema Apple, alto consumo térmico e término de suporte oficial."
            cons.append("Processador Intel ultrapassado no ecossistema Mac: quente, ruidoso e sem longevidade")
        else:
            proc_eval = f"Processador: {listing.processor}"

        # 2. Memória RAM
        if listing.ram_gb >= 32:
            score += 18.0
            ram_eval = f"{listing.ram_gb}GB de memória veloz. Capacidade profissional para múltiplos containers, edição pesada e IA."
            pros.append(f"{listing.ram_gb}GB RAM de capacidade profissional")
        elif listing.ram_gb >= 16:
            score += 14.0
            ram_eval = f"{listing.ram_gb}GB de memória. Amplo espaço para multitarefa, compilação pesada e longevidade sem gargalo."
            pros.append(f"{listing.ram_gb}GB RAM: padrão ideal para longevidade e multitarefa")
        elif listing.ram_gb == 8:
            score += 5.0
            ram_eval = "8GB de memória. Suficiente para escritório e uso geral; tarefas muito pesadas podem exigir upgrade ou swap."
            if "DELL" in listing.brand.upper():
                pros.append("8GB de RAM (expansível via slots SO-DIMM na linha Dell)")
            else:
                cons.append("8GB soldados sem possibilidade de upgrade físico")
        else:
            score -= 20.0
            ram_eval = f"{listing.ram_gb}GB de RAM: insuficiente para padrões contemporâneos."
            cons.append(f"Apenas {listing.ram_gb}GB de memória RAM")

        # 3. Armazenamento SSD
        if listing.storage_gb >= 1024:
            score += 12.0
            storage_eval = f"{listing.storage_gb}GB (1TB) SSD NVMe veloz, espaço profissional amplo."
            pros.append(f"{listing.storage_gb}GB SSD espaçoso de 1TB")
        elif listing.storage_gb >= 512:
            score += 8.0
            storage_eval = f"{listing.storage_gb}GB SSD NVMe de alta velocidade, espaço seguro para sistema e arquivos."
            pros.append(f"{listing.storage_gb}GB SSD NVMe veloz")
        elif listing.storage_gb == 256:
            score += 4.0
            storage_eval = "256GB SSD. Atende perfeitamente sistema e projetos em nuvem, mas requer atenção com mídias pesadas."
        else:
            score -= 12.0
            storage_eval = f"{listing.storage_gb}GB muito restrito."
            cons.append("Armazenamento restrito")

        # 4. Tela e Conectividade
        if "OLED" in title or "4K" in title:
            score += 10.0
            pros.append("Tela 4K OLED de altíssima fidelidade de cor e contraste infinito")
        elif "165HZ" in title:
            score += 8.0
            pros.append("Tela gamer rápida de 165Hz com 100% sRGB")
        elif "120HZ" in title or (listing.screen_size_inches and listing.screen_size_inches >= 14.0 and "APPLE" in listing.brand.upper()):
            score += 6.0
            pros.append("Tela fluida de 120Hz para máxima suavidade visual")

        # 5. Eficiência Térmica
        if listing.architecture == "Apple Silicon":
            score += 8.0
            thermal_eval = "Arquitetura Apple Silicon de altíssima eficiência energética, mantendo 14 a 22 horas de bateria real e operação silenciosa."
            pros.append("Autonomia de bateria estelar (14h a 22h)")
        elif "GAMER" in title or "G15" in title:
            thermal_eval = "Sistema térmico robusto com ventiladores duplos e câmara de exaustão inspirada na Alienware para sustentar carga contínua da GPU."
            pros.append("Arrefecimento com ventoinhas duplas para manter a GPU em alto desempenho")
        elif "DELL" in listing.brand.upper():
            thermal_eval = "Dissipação térmica balanceada para laptops finos com dobradiça elevatória para melhor fluxo de ar."
        else:
            thermal_eval = "Térmica convencional de notebook."

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
