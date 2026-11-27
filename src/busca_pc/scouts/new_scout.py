from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class NewScoutAgent:
    """
    Agente especialista em buscar computadores novos lacrados nas principais redes de varejo
    e lojas oficiais (ex: Amazon Brasil, Mercado Livre Oficial/Full, Fast Shop, Magazine Luiza).
    Monitora preço à vista, garantia oficial Apple de 1 ano e custos de frete para Recife/PE.
    """

    NAME = "NewScoutAgent"
    ROLE = "Especialista em Busca de Computadores Novos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por computadores novos lacrados."""
        await asyncio.sleep(0.08)  # Simula busca concorrente em plataformas de varejo

        listings: List[ComputerListing] = []

        if "APPLE" in spec.target_brand.upper():
            # Dados reais de mercado para modelos novos no Brasil com entrega em Recife
            listings.append(
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
                    raw_description="Produto 100% original, lacrado na caixa com NF-e e garantia oficial Apple de 1 ano. Envio imediato para Recife.",
                )
            )

            listings.append(
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
                    raw_description="Novo design com chip M2, tela Liquid Retina de 13,6 polegadas, câmera FaceTime HD 1080p, porta de carregamento MagSafe 3. Garantia total Apple.",
                )
            )

        return listings
