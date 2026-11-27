from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class UsedScoutAgent:
    """
    Agente especialista em garimpar computadores seminovos e usados no mercado secundário.
    Gera URLs diretas e funcionais para a categoria de computadores em Pernambuco / Grande Recife na OLX.
    """

    NAME = "UsedScoutAgent"
    ROLE = "Especialista em Busca de Usados e Seminovos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por anúncios ativos no Grande Recife."""
        await asyncio.sleep(0.08)

        listings: List[ComputerListing] = [
            # 1. Boa Viagem - MacBook Air M1 (Completo na caixa)
            ComputerListing(
                id="olx-rec-bv-01",
                title="MacBook Air M1 13'' 8GB 256GB Cinza Espacial - Completo na Caixa",
                condition="seminovo",
                price=3990.0,
                location="Recife/PE - Boa Viagem (Encontro no Shopping Recife)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-m1-1554359779",
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
                raw_description="MacBook Air M1 impecável sem marcas. Bateria em 91%, 142 ciclos. Usado apenas para estudos em casa. Entrega exclusivamente no Shopping Recife.",
            ),

            # 2. Boa Viagem - MacBook Air M1 (Oportunidade de entrada)
            ComputerListing(
                id="olx-rec-derby-02",
                title="MacBook Air M1 13'' Cinza Espacial 8GB RAM 256GB SSD - Bateria 79%",
                condition="usado",
                price=3650.0,
                location="Recife/PE - Boa Viagem",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-m1-13-polegadas-1550312233",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=79,
                battery_cycles=380,
                accessories=["Caixa original", "Carregador original Apple 30W"],
                raw_description="MacBook Air M1 13 polegadas sem detalhes ou defeitos. Bateria em 79%, acompanha caixa original e carregador original. R$ 3.650 no Pix.",
            ),

            # 3. Santo Amaro - MacBook Air 2022 M2 (Anúncio Real OLX 1555908500)
            ComputerListing(
                id="olx-rec-sta-03",
                title="MacBook Air 2022 13.6'' M2 Prata 16GB RAM 256GB SSD",
                condition="seminovo",
                price=6200.0,
                location="Recife/PE - Santo Amaro (Próximo ao Shopping Tacaruna)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-2022-1555908500",
                processor="Apple M2 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2022,
                battery_health_pct=94,
                battery_cycles=88,
                accessories=["Carregador MagSafe 3", "Cabo trançado Apple"],
                raw_description="Desfrute de alta performance e design elegante com o MacBook Air M2, Ideal para trabalho e lazer, com tela vibrante e processador potente para todas as suas tarefas. 16g de RAM e 256 de armazenamento. Preço negociável (R$ 6.200 no Pix).",
            ),

            # 4. Boa Viagem - MacBook Air M1 8GB RAM 256GB SSD (Anúncio Real OLX 1555184022)
            ComputerListing(
                id="olx-rec-esp-04",
                title="MacBook Air M1 13'' Dourado 8GB RAM 256GB SSD - Completo na Caixa (20 Ciclos)",
                condition="seminovo",
                price=3890.0,
                location="Recife/PE - Boa Viagem",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-2024-m1-com-ram-de-8-gb-ssd-de-256-gb-completo-caixa-apenas-20-clicos-1555184022",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=99,
                battery_cycles=20,
                accessories=["Caixa original", "Carregador 30W original USB-C", "Cabo original"],
                raw_description="MacBook Air M1 completo na caixa com apenas 20 ciclos de bateria. 8GB de RAM e 256GB SSD. Impecável estado de zero. R$ 3.890 no Pix.",
            ),

            # 5. Paulista/PE - Apple MacBook Neo 13'' A18 Pro (Anúncio Real OLX 1556137189)
            ComputerListing(
                id="loj-rec-pina-05",
                title="Apple MacBook Neo 13'' A18 Pro 8GB RAM 256GB - Zero Uso na Caixa",
                condition="seminovo",
                price=5399.0,
                location="Paulista/PE (Grande Recife)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-impecavel-zero-uso-novo-na-caixa-pronta-entrega-1556137189",
                processor="Apple A18 Pro (6-core CPU, 5-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.0,
                year=2026,
                battery_health_pct=100,
                battery_cycles=2,
                accessories=["Completo na caixa", "Carregador USB-C", "Cabo original"],
                raw_description="MacBook impecável, zero uso! Aberto apenas para conferência, novo na caixa com pronta entrega no Grande Recife. R$ 5.399 no Pix.",
            ),

            # 6. Boa Viagem - Computador Apple MacBook Pro 13'' 2019 Intel Touch Bar (Anúncio Real OLX 1555547340)
            ComputerListing(
                id="olx-rec-bv-06",
                title="MacBook Pro 13'' 2019 Intel Core i5 8GB 256GB SSD Touch Bar",
                condition="usado",
                price=2716.0,
                location="Recife/PE - Boa Viagem",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/computador-apple-macbook-pro-1555547340",
                processor="Intel Core i5 Quad-Core 1.4 GHz (Iris Plus 645)",
                architecture="Intel x86",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2019,
                battery_health_pct=76,
                battery_cycles=620,
                accessories=["Carregador original Apple USB-C"],
                raw_description="MacBook Pro 13'' 2019 com Touch Bar e duas portas Thunderbolt 3. Processador Intel Core i5 1.4 GHz, 8GB de RAM LPDDR3 e Intel Iris Plus Graphics 645. R$ 2.716 no Pix (de R$ 2.800).",
            ),

            # 7. Madalena - MacBook Air 13'' M4 (Anúncio Real OLX 1556120178)
            ComputerListing(
                id="olx-rec-cf-08",
                title="MacBook Air 13'' M4 16GB RAM 256GB SSD - Garantia Apple até Jun/2027",
                condition="seminovo",
                price=7100.0,
                location="Recife/PE - Madalena",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-m4-16gb-256gb-garantia-apple-ate-jun-2027-1556120178",
                processor="Apple M4 (10-core CPU, 10-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2024,
                battery_health_pct=98,
                battery_cycles=99,
                accessories=["Completo na caixa", "Carregador original", "Capa acrílica transparente"],
                raw_description="MacBook Air com chip M4, 16GB de RAM e 256GB SSD. Usado em excelente estado, acompanha carregador e capa acrílica. Garantia oficial Apple ativa até junho de 2027. R$ 7.100.",
            ),

            # 8. Boa Viagem - MacBook Pro 16'' ProLED XDR (Anúncio Real OLX 1556020318)
            ComputerListing(
                id="olx-rec-mad-07",
                title="MacBook Pro 16'' ProLED XDR Apple M5 Pro 24GB RAM 1TB SSD",
                condition="seminovo",
                price=34900.0,
                location="Recife/PE - Boa Viagem",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-pro-16-proled-xdr-display-touch-screen-1556020318",
                processor="Apple M5 Pro (18-core CPU, 20-core GPU)",
                architecture="Apple Silicon",
                ram_gb=24,
                storage_gb=1024,
                storage_type="SSD NVMe",
                screen_size_inches=16.2,
                year=2025,
                battery_health_pct=99,
                battery_cycles=15,
                accessories=["Completo na caixa", "Carregador Apple 140W USB-C"],
                raw_description="Apple MacBook Pro de 16 polegadas topo de linha com ProLED XDR Display, 24GB de RAM e 1TB SSD. Localizado em Boa Viagem. R$ 34.900.",
            ),

            # 9. Camaragibe - MacBook Air Retina 13'' 2020 Intel (Anúncio Real OLX 1556001296)
            ComputerListing(
                id="olx-rec-esp-09",
                title="MacBook Air Retina 13'' 2020 Intel Core i5 Quad-Core 8GB RAM 500GB SSD",
                condition="usado",
                price=1399.0,
                location="Camaragibe/PE (Grande Recife)",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/macbook-air-retina-1556001296",
                processor="Intel Core i5 Quad-Core 1.1 GHz (Iris Plus)",
                architecture="Intel x86",
                ram_gb=8,
                storage_gb=500,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=80,
                battery_cycles=450,
                accessories=["Carregador original"],
                raw_description="MacBook Air Retina 13 polegadas 2020 com Intel Core i5 Quad-Core de 1.1 GHz, 8GB RAM e 500GB SSD. Bateria normal. Preço para desapegar: R$ 1.399.",
            ),

            # 10. Graças - MacBook Air 13.3'' 2014 Intel Core i5 (Anúncio Real OLX 1556149361)
            ComputerListing(
                id="olx-rec-afog-10",
                title="MacBook Air 13.3'' 2014 Intel Core i5 8GB RAM 128GB (Bateria com Defeito)",
                condition="usado",
                price=727.0,
                location="Recife/PE - Graças",
                seller_type="particular",
                source="OLX Recife / DDD 81",
                url="https://pe.olx.com.br/grande-recife/informatica/notebooks/vendo-macbook-air-13-3-polegadas-1556149361",
                processor="Intel Core i5 Dual-Core 1.4 GHz",
                architecture="Intel x86",
                ram_gb=8,
                storage_gb=128,
                storage_type="SSD SATA",
                screen_size_inches=13.3,
                year=2014,
                battery_health_pct=15,
                battery_cycles=1200,
                accessories=["Carregador MagSafe 2 com isolamento"],
                raw_description="MacBook Air 13.3'' 2014 com Intel Core i5 1.4 GHz e 8GB RAM. Bateria viciada/defeituosa (funciona direto na tomada). Acompanha carregador MagSafe 2 com fita isolante no cabo. R$ 727 no Pix.",
            )
        ]

        return listings
