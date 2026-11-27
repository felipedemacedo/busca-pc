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
        """Executa auditoria técnica profunda de especificações de hardware sem saturação artificial."""
        await asyncio.sleep(0.02)

        pros = []
        cons = []
        proc = listing.processor.upper()
        title = listing.title.upper()
        brand = listing.brand.upper()
        lifespan = 4

        # 1. CPU / Processamento Central (Máximo: 40 pontos)
        cpu_score = 20.0
        if "M5" in proc or "M4 MAX" in proc or "M3 MAX" in proc:
            cpu_score = 40.0
            lifespan = 7
            proc_eval = f"Monstro de processamento topo de linha ({listing.processor}) com dezenas de núcleos e motores de IA."
            pros.append(f"Workstation topo de linha com {listing.processor}")
        elif "M4 PRO" in proc:
            cpu_score = 38.0
            lifespan = 7
            proc_eval = f"Chip topo de linha de 2ª geração 3nm ({listing.processor}) com altíssima vazão monothread e multithread."
            pros.append(f"Processador estado da arte {listing.processor}")
        elif "CORE ULTRA 9" in proc:
            cpu_score = 36.0
            lifespan = 6
            proc_eval = f"Intel Core Ultra 9 ({listing.processor}) com 16 núcleos híbridos e NPU dedicada para IA local."
            pros.append("Intel Core Ultra 9 com NPU integrada de aceleração neural")
        elif "M3 PRO" in proc or "M2 PRO" in proc or "M1 PRO" in proc:
            cpu_score = 34.0
            lifespan = 6
            proc_eval = f"Processador profissional ({listing.processor}) com barramento ampliado e alta longevidade."
            pros.append(f"Silício profissional {listing.processor}")
        elif "M4" in proc:
            cpu_score = 33.0
            lifespan = 6
            proc_eval = f"Chip Apple M4 de última geração ({listing.processor}) com alta vazão de CPU e motores neurais."
            pros.append("Chip Apple M4 de última geração")
        elif "CORE ULTRA 7" in proc:
            cpu_score = 32.0
            lifespan = 6
            proc_eval = f"Processador Intel Core Ultra 7 ({listing.processor}) moderno com NPU integrada."
            pros.append("Intel Core Ultra 7 de alta eficiência com NPU para IA")
        elif "A18 PRO" in proc or "A18" in proc or "NEO" in title:
            cpu_score = 30.0
            lifespan = 5
            proc_eval = f"Chip Apple A18 Pro (3nm) ultrassilencioso fanless e eficiente com suporte ao Apple Intelligence."
            pros.append("Chip Apple A18 Pro (3nm): ultraeficiente, operação fria e suporte a IA")
        elif "M2" in proc:
            cpu_score = 29.0
            lifespan = 5
            proc_eval = f"Chip Apple M2 com aceleração ProRes e núcleos rápidos."
            pros.append(f"Chip {listing.processor} com boa aceleração de mídia")
        elif "I7-13" in proc:
            cpu_score = 28.0
            lifespan = 5
            proc_eval = f"Processador Intel Core i7 13ª Geração com 14 núcleos de alto desempenho."
            pros.append("Intel Core i7 13ª Ger potente para tarefas pesadas")
        elif "M1" in proc:
            cpu_score = 26.0
            lifespan = 4
            proc_eval = f"Chip Apple Silicon M1 pioneiro com excelente autonomia e fluidez diária."
            pros.append("Apple Silicon M1 pioneiro com alta eficiência energética")
        elif "I5-13" in proc:
            cpu_score = 25.0
            lifespan = 4
            proc_eval = f"Processador Intel Core i5 13ª Geração ({listing.processor}) balanceado para trabalho e produtividade."
            pros.append("Intel Core i5 13ª Ger competente para produtividade")
        elif "I3-12" in proc or "I3" in proc:
            cpu_score = 18.0
            lifespan = 3
            proc_eval = f"Processador de entrada Intel Core i3 ({listing.processor}) para estudos e tarefas leves."
            pros.append("Intel Core de entrada competente para escritório leve")
        elif "APPLE" in brand and ("INTEL" in proc or "CORE I" in proc):
            cpu_score = 10.0 if (listing.year or 2017) >= 2018 else 6.0
            lifespan = 1
            proc_eval = f"Processador legado Intel x86 em Mac ({listing.processor}). Arquitetura defasada e término de suporte oficial."
            cons.append("Processador Intel ultrapassado no ecossistema Mac: quente e descontinuado")
        else:
            proc_eval = f"Processador: {listing.processor}"

        # 2. GPU / Poder Gráfico (Máximo: 24 pontos)
        gpu_score = 8.0
        if "RTX 4060" in proc or "RTX 4060" in title:
            gpu_score = 24.0
            pros.append("NVIDIA GeForce RTX 4060 8GB dedicada: excelente para IA, 3D e jogos em 1440p")
        elif "M3 MAX" in proc or "M4 MAX" in proc:
            gpu_score = 24.0
            pros.append("GPU integrada colossal com dezenas de núcleos gráficos e Ray Tracing")
        elif "RTX 4050" in proc or "RTX 4050" in title:
            gpu_score = 20.0
            pros.append("NVIDIA GeForce RTX 4050 6GB: suporte a DLSS 3 e aceleração CUDA")
        elif "M2 PRO" in proc or "M1 PRO" in proc or "M3 PRO" in proc:
            gpu_score = 20.0
            pros.append("GPU profissional com largura de banda de memória ampliada")
        elif "RTX 3050" in proc or "RTX 3050" in title:
            gpu_score = 17.0
            pros.append("NVIDIA GeForce RTX 3050 6GB dedicada: boa entrada gamer")
        elif "A18" in proc or "M2" in proc:
            gpu_score = 16.0
            pros.append("Gráficos integrados Apple modernos com suporte a aceleração de hardware")
        elif "M1" in proc:
            gpu_score = 14.0
            pros.append("GPU integrada 7/8-core Apple Silicon ágil para uso geral")
        elif "CORE ULTRA" in proc:
            gpu_score = 14.0 # Intel Arc Graphics
            pros.append("Gráficos integrados Intel Arc de nova geração")
        elif "APPLE" in brand and ("INTEL" in proc or "CORE I" in proc):
            gpu_score = 4.0
            cons.append("Gráficos Intel integrados legados com baixo rendimento 3D")
        elif "I5" in proc or "I3" in proc:
            gpu_score = 8.0

        # 3. Memória RAM (Máximo: 20 pontos)
        ram_score = 8.0
        if listing.ram_gb >= 32:
            ram_score = 20.0
            ram_eval = f"{listing.ram_gb}GB de memória veloz. Capacidade profissional para múltiplos containers, edição pesada e IA."
            pros.append(f"{listing.ram_gb}GB RAM de capacidade profissional extrema")
        elif listing.ram_gb >= 16:
            ram_score = 16.0
            ram_eval = f"{listing.ram_gb}GB de memória. Amplo espaço para multitarefa e longevidade sem gargalo."
            pros.append(f"{listing.ram_gb}GB RAM: padrão ideal para multitarefa pesada")
        elif listing.ram_gb == 8:
            if listing.architecture == "Apple Silicon" or "13" in proc:
                ram_score = 10.0
                ram_eval = "8GB de memória unificada/DDR5. Suficiente para escritório e uso geral; tarefas muito pesadas recorrem a swap."
            else:
                ram_score = 6.0
                ram_eval = "8GB de memória LPDDR3/DDR4 legada. Limite básico com risco de lentidão."
            if "DELL" in brand:
                pros.append("8GB de RAM (expansível via slots SO-DIMM na linha Dell)")
            else:
                cons.append("8GB soldados sem possibilidade de upgrade físico")
        else:
            ram_score = 3.0
            ram_eval = f"{listing.ram_gb}GB de RAM: insuficiente para padrões contemporâneos."
            cons.append(f"Apenas {listing.ram_gb}GB de RAM")

        # 4. Armazenamento SSD (Máximo: 10 pontos)
        st_score = 5.0
        if listing.storage_gb >= 1024:
            st_score = 10.0
            storage_eval = f"{listing.storage_gb}GB (1TB) SSD NVMe veloz, espaço profissional amplo."
            pros.append(f"{listing.storage_gb}GB SSD espaçoso de 1TB")
        elif listing.storage_gb >= 512:
            st_score = 8.0
            storage_eval = f"{listing.storage_gb}GB SSD NVMe de alta velocidade, espaço seguro para sistema e arquivos."
            pros.append(f"{listing.storage_gb}GB SSD NVMe veloz")
        elif listing.storage_gb == 256:
            st_score = 5.0
            storage_eval = "256GB SSD. Atende perfeitamente sistema e projetos em nuvem, mas requer atenção com mídias pesadas."
        else:
            st_score = 2.0
            storage_eval = f"{listing.storage_gb}GB muito restrito."
            cons.append("Armazenamento restrito")

        # 5. Tela, Conectividade e Eficiência (Máximo: 6 pontos)
        screen_score = 2.0
        if "OLED" in title or "4K" in title:
            screen_score = 6.0
            pros.append("Tela 4K OLED de altíssima fidelidade de cor e contraste infinito")
        elif (listing.screen_size_inches and listing.screen_size_inches >= 14.0 and "APPLE" in brand) or "16.2" in str(listing.screen_size_inches):
            screen_score = 5.5
            pros.append("Tela Mini-LED Liquid Retina XDR de 120Hz com brilho de até 1600 nits")
        elif "165HZ" in title:
            screen_score = 4.5
            pros.append("Tela gamer rápida de 165Hz com 100% sRGB")
        elif "120HZ" in title or "LIQUID RETINA" in title:
            screen_score = 4.0
            pros.append("Tela fluida de 120Hz / Liquid Retina para suavidade visual")
        elif listing.screen_size_inches == 13.6:
            screen_score = 3.5

        # 6. Avaliação Térmica
        if listing.architecture == "Apple Silicon":
            thermal_eval = "Arquitetura Apple Silicon de altíssima eficiência energética, mantendo 14 a 22 horas de bateria real e operação silenciosa."
            pros.append("Autonomia de bateria estelar (14h a 22h)")
        elif "GAMER" in title or "G15" in title:
            thermal_eval = "Sistema térmico robusto com ventiladores duplos e câmara de exaustão inspirada na Alienware para sustentar carga contínua da GPU."
            pros.append("Arrefecimento com ventoinhas duplas para manter a GPU em alto desempenho")
        elif "DELL" in brand:
            thermal_eval = "Dissipação térmica balanceada para laptops finos com dobradiça elevatória para melhor fluxo de ar."
        else:
            thermal_eval = "Térmica convencional de notebook."

        # Pontuação consolidada sem saturação artificial (escala 0 a 100)
        final_hw_score = max(5.0, min(100.0, round(cpu_score + gpu_score + ram_score + st_score + screen_score, 1)))

        if final_hw_score >= 88:
            tier = "Excelente"
        elif final_hw_score >= 75:
            tier = "Muito Bom"
        elif final_hw_score >= 58:
            tier = "Bom"
        elif final_hw_score >= 38:
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
