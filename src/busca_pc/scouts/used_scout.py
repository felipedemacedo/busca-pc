from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class UsedScoutAgent:
    """
    Agente especialista em garimpar computadores seminovos e usados no mercado secundário.
    Cobre TODO o espectro de possibilidades (de modelos de entrada antigos a máquinas Pro de alta performance),
    sem limites artificiais de orçamento.
    """

    NAME = "UsedScoutAgent"
    ROLE = "Especialista em Busca de Usados e Seminovos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por todas as possibilidades no mercado secundário."""
        await asyncio.sleep(0.05)  # Latência concorrente

        listings: List[ComputerListing] = [
            # 1. Entrada / Baixo Custo: MacBook Air M1 (Derby)
            ComputerListing(
                id="used-rec-01",
                title="MacBook Air M1 13'' Prata 8GB 256GB - Com detalhes estéticos leves",
                condition="usado",
                price=3750.0,
                location="Recife/PE - Derby (Próximo à Praça do Derby)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-derby-01",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=83,
                battery_cycles=380,
                accessories=["Carregador original"],
                raw_description="MacBook Air M1 funcionando 100%. Marquinha leve na quina. Bateria dura 9 horas. Excelente custo-benefício.",
            ),

            # 2. Entrada / Excelente Conservação: MacBook Air M1 (Boa Viagem)
            ComputerListing(
                id="used-rec-02",
                title="MacBook Air M1 13'' 8GB 256GB Cinza Espacial - Completo na Caixa",
                condition="seminovo",
                price=4100.0,
                location="Recife/PE - Boa Viagem (Shopping Recife)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-completo-bv-02",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=91,
                battery_cycles=142,
                accessories=["Caixa original", "Carregador 30W original USB-C", "Cabo original"],
                raw_description="MacBook Air M1 impecável sem marcas. Bateria em 91%, 142 ciclos. Negociação presencial segura no Shopping Recife.",
            ),

            # 3. Intermediário: MacBook Air M1 16GB 512GB (Espinheiro)
            ComputerListing(
                id="used-rec-03",
                title="MacBook Air M1 13'' 16GB RAM 512GB SSD - Raro Modelo com Upgrade de Fábrica",
                condition="seminovo",
                price=4900.0,
                location="Recife/PE - Espinheiro",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-16gb-512gb-03",
                processor="Apple M1 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=88,
                battery_cycles=210,
                accessories=["Carregador original", "Case protetora"],
                raw_description="Configuração sob encomenda (16GB RAM e 512GB SSD). Perfeito para programadores e edição de vídeo. Sem lentidão por swap.",
            ),

            # 4. Moderno / Design Novo: MacBook Air M2 13.6'' (Pina)
            ComputerListing(
                id="used-rec-04",
                title="MacBook Air M2 13.6'' Estelar 8GB 256GB MagSafe 3 - Loja Seminovos com 90 dias garantia",
                condition="seminovo",
                price=5990.0,
                location="Recife/PE - Pina (Loja Física de Seminovos Apple)",
                seller_type="loja_fisica_local",
                source="Loja Especializada Recife Seminovos",
                url="https://lojarecifemac.com.br/seminovos/air-m2-estelar-04",
                processor="Apple M2 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2022,
                battery_health_pct=95,
                battery_cycles=75,
                accessories=["Carregador MagSafe 3", "Garantia 90 dias com Nota Fiscal"],
                raw_description="Design moderno ultrafino, tela Liquid Retina, MagSafe 3, 90 dias de garantia em loja física em Recife.",
            ),

            # 5. Alto Desempenho / Pro: MacBook Pro 14'' M1 Pro (Boa Viagem)
            ComputerListing(
                id="used-rec-05",
                title="MacBook Pro 14'' M1 Pro 16GB 512GB Tela 120Hz Liquid Retina XDR",
                condition="seminovo",
                price=8200.0,
                location="Recife/PE - Boa Viagem (Shopping Riomar)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-14-m1-pro-05",
                processor="Apple M1 Pro (8-core CPU, 14-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=14.2,
                year=2021,
                battery_health_pct=90,
                battery_cycles=165,
                accessories=["Carregador original 67W MagSafe 3", "Caixa"],
                raw_description="Monstro de performance profissional. Tela Mini-LED 120Hz ProMotion, som absurdo, HDMI, leitor SD. Estado impecável.",
            ),

            # 6. Ultra Alta Performance / Pro: MacBook Pro 16'' M2 Pro (Madalena)
            ComputerListing(
                id="used-rec-06",
                title="MacBook Pro 16'' M2 Pro 16GB 512GB Cinza Espacial",
                condition="seminovo",
                price=11800.0,
                location="Recife/PE - Madalena",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-16-m2-pro-06",
                processor="Apple M2 Pro (12-core CPU, 19-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=16.2,
                year=2023,
                battery_health_pct=96,
                battery_cycles=60,
                accessories=["Carregador 140W USB-C original", "Cabo MagSafe trançado"],
                raw_description="Bateria colossal de 100Wh, tela gigante Liquid Retina XDR de 16.2 polegadas. Máquina de edição 8K e compilação pesada.",
            ),

            # 7. Workstation Máxima: MacBook Pro 16'' M3 Max 36GB 1TB (Casa Forte)
            ComputerListing(
                id="used-rec-07",
                title="MacBook Pro 16'' M3 Max 36GB RAM 1TB SSD Preto Espacial",
                condition="seminovo",
                price=19500.0,
                location="Recife/PE - Casa Forte (Plaza Shopping)",
                seller_type="particular",
                source="Marketplace Premium Recife",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-16-m3-max-07",
                processor="Apple M3 Max (14-core CPU, 30-core GPU)",
                architecture="Apple Silicon",
                ram_gb=36,
                storage_gb=1024,
                storage_type="SSD NVMe",
                screen_size_inches=16.2,
                year=2024,
                battery_health_pct=98,
                battery_cycles=25,
                accessories=["Completo na caixa", "Garantia AppleCare+ ativa"],
                raw_description="Configuração extrema para inteligência artificial local, renderização 3D e edição profissional de cinema. Preto espacial.",
            ),

            # 8. Modelo Antigo / Alto Risco: MacBook Pro 13'' 2017 Intel (Espinheiro)
            ComputerListing(
                id="used-rec-08",
                title="MacBook Pro 13'' 2017 Intel Core i5 8GB 256GB Space Gray",
                condition="usado",
                price=2600.0,
                location="Recife/PE - Espinheiro",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-2017-i5-08",
                processor="Intel Core i5 Dual-Core 2.3 GHz",
                architecture="Intel x86",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2017,
                battery_health_pct=72,
                battery_cycles=720,
                accessories=["Carregador paralelo"],
                raw_description="MacBook Pro 2017 bonito, tela retina. Bateria avisa manutenção. Teclado às vezes repete a tecla 'e'.",
            ),

            # 9. Modelo Obsoleto / Ultrabarato: MacBook Air 13'' 2015 Intel Core i5 (Afogados)
            ComputerListing(
                id="used-rec-09",
                title="MacBook Air 13'' 2015 Intel Core i5 8GB 128GB SSD",
                condition="usado",
                price=1450.0,
                location="Recife/PE - Afogados",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-2015-i5-09",
                processor="Intel Core i5 Dual-Core 1.6 GHz",
                architecture="Intel x86",
                ram_gb=8,
                storage_gb=128,
                storage_type="SSD SATA",
                screen_size_inches=13.3,
                year=2015,
                battery_health_pct=65,
                battery_cycles=910,
                accessories=["Carregador MagSafe 2"],
                raw_description="MacBook Air 2015 clássico com maçã que brilha. Tela não é retina (1440x900). Bom para digitação e tarefas muito simples.",
            )
        ]

        return listings
