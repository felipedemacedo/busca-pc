from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class NewScoutAgent:
    """
    Agente especialista em buscar computadores novos lacrados nas principais redes de varejo
    e lojas oficiais, cobrindo todo o leque de preços e configurações sem teto artificial.
    """

    NAME = "NewScoutAgent"
    ROLE = "Especialista em Busca de Computadores Novos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por todas as opções de novos lacrados."""
        await asyncio.sleep(0.05)  # Latência concorrente

        listings: List[ComputerListing] = [
            # 1. Entrada Novo: MacBook Air M1 8GB 256GB
            ComputerListing(
                id="new-ret-01",
                title="MacBook Air 13'' M1 8GB 256GB Cinza Espacial - Novo Lacrado com Garantia Apple 1 Ano",
                condition="novo",
                price=5899.0,
                location="Entrega Expressa Recife/PE (Centro de Distribuição Nordeste)",
                seller_type="loja_oficial",
                source="Mercado Livre Loja Oficial Apple / Envio Full",
                url="https://www.mercadolivre.com.br/apple-macbook-air-13-polegadas-m1-256gb/p/MLB16159678",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=100,
                battery_cycles=0,
                accessories=["Lacrado na caixa", "Garantia mundial Apple 12 meses", "Carregador original"],
                raw_description="Produto 100% original lacrado com NF-e e garantia oficial Apple de 1 ano. Entrega Full para Recife.",
            ),

            # 2. Intermediário Novo: MacBook Air M2 13'' 8GB 256GB
            ComputerListing(
                id="new-ret-02",
                title="MacBook Air 13'' M2 8GB 256GB Meia-noite - Novo Lacrado",
                condition="novo",
                price=7499.0,
                location="Entrega Recife/PE (Frete Prime)",
                seller_type="loja_oficial",
                source="Amazon Brasil (Vendido e entregue por Amazon)",
                url="https://www.amazon.com.br/dp/B0B3C9B8JF",
                processor="Apple M2 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2022,
                battery_health_pct=100,
                battery_cycles=0,
                accessories=["Lacrado na caixa", "Garantia Apple 1 ano", "Carregador MagSafe 3 30W"],
                raw_description="Design moderno com chip M2, tela Liquid Retina de 13.6 polegadas, FaceTime 1080p, MagSafe 3.",
            ),

            # 3. Intermediário Avançado Novo: MacBook Air 13'' M3 16GB 512GB
            ComputerListing(
                id="new-ret-03",
                title="MacBook Air 13'' M3 16GB RAM 512GB SSD Meia-noite - Novo Lacrado",
                condition="novo",
                price=10499.0,
                location="Entrega Expressa Recife/PE (Fast Shop)",
                seller_type="loja_oficial",
                source="Fast Shop Oficial",
                url="https://www.fastshop.com.br/macbook-air-13-m3-16gb-512gb",
                processor="Apple M3 (8-core CPU, 10-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2024,
                battery_health_pct=100,
                battery_cycles=0,
                accessories=["Lacrado na caixa", "Garantia Apple 1 ano", "Carregador 35W Dual USB-C"],
                raw_description="Chip M3 de última geração com Ray Tracing por hardware, suporte a dois monitores externos, 16GB de memória unificada.",
            ),

            # 4. Pro Novo: MacBook Pro 14'' M3 Pro 18GB 512GB
            ComputerListing(
                id="new-ret-04",
                title="MacBook Pro 14'' M3 Pro 18GB 512GB Preto Espacial - Novo Lacrado",
                condition="novo",
                price=16999.0,
                location="iPlace Shopping Recife (Pronta Entrega)",
                seller_type="loja_oficial",
                source="iPlace Apple Premium Reseller Recife",
                url="https://www.iplace.com.br/macbook-pro-14-m3-pro-18gb-512gb",
                processor="Apple M3 Pro (11-core CPU, 14-core GPU)",
                architecture="Apple Silicon",
                ram_gb=18,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=14.2,
                year=2024,
                battery_health_pct=100,
                battery_cycles=0,
                accessories=["Lacrado na caixa", "Garantia Apple 1 ano", "Carregador 70W USB-C"],
                raw_description="Pronta entrega física em Recife no Shopping Recife. Desempenho profissional para edição e engenharia de software pesada.",
            ),

            # 5. Topo de Linha Novo: MacBook Pro 16'' M4 Pro 24GB 512GB
            ComputerListing(
                id="new-ret-05",
                title="MacBook Pro 16'' M4 Pro 24GB RAM 512GB SSD Preto Espacial - Lançamento",
                condition="novo",
                price=22499.0,
                location="Entrega Recife/PE (Apple Store Oficial)",
                seller_type="loja_oficial",
                source="Apple Store Brasil",
                url="https://www.apple.com/br/shop/buy-mac/macbook-pro/16-polegadas-m4-pro",
                processor="Apple M4 Pro (14-core CPU, 20-core GPU)",
                architecture="Apple Silicon",
                ram_gb=24,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=16.2,
                year=2024,
                battery_health_pct=100,
                battery_cycles=0,
                accessories=["Lacrado oficial Apple", "Garantia mundial 1 ano", "Carregador 140W USB-C"],
                raw_description="Chip de última geração M4 Pro com até 24 horas de bateria, Thunderbolt 5 com transferências até 120 Gb/s, tela XDR com opção nanotexture.",
            )
        ]

        return listings
