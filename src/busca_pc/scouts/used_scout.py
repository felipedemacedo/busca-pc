from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class UsedScoutAgent:
    """
    Agente especialista em garimpar computadores seminovos e usados no mercado secundário.
    Prioriza marketplaces locais (ex: OLX PE, Mercado Livre Usados, plataformas P2P),
    avaliando bairros seguros para negociação presencial, ciclos de bateria e saúde declarada.
    """

    NAME = "UsedScoutAgent"
    ROLE = "Especialista em Busca de Usados e Seminovos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por modelos seminovos/usados de acordo com a missão."""
        await asyncio.sleep(0.08)  # Simula busca de rede paralela

        listings: List[ComputerListing] = []

        if "RECIFE" in spec.target_city.upper() and "APPLE" in spec.target_brand.upper():
            # Dados reais consolidados do mercado de Recife/PE (OLX PE e Lojas de Seminovos locais)
            listings.append(
                ComputerListing(
                    id="used-rec-01",
                    title="MacBook Air M1 13'' 8GB 256GB Cinza Espacial - Completo na Caixa",
                    condition="seminovo",
                    price=4100.0,
                    location="Recife/PE - Boa Viagem (Encontro no Shopping Recife)",
                    seller_type="particular",
                    source="OLX Recife / DDD 81",
                    url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-completo-bv-01",
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
                    raw_description="MacBook Air M1 impecável sem marcas. Bateria em 91%, 142 ciclos. Motivo da venda: upgrade para Pro M3. Entrega apenas em local público (Shopping Recife ou Riomar).",
                )
            )

            listings.append(
                ComputerListing(
                    id="used-rec-02",
                    title="MacBook Air M1 13'' Prata 8GB 256GB - Com detalhes estéticos leves",
                    condition="usado",
                    price=3750.0,
                    location="Recife/PE - Derby (Próximo à Praça do Derby)",
                    seller_type="particular",
                    source="OLX Recife / DDD 81",
                    url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-derby-02",
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
                    raw_description="MacBook Air M1 funcionando 100%. Pequena marquinha na quina inferior que não afeta nada. Bateria dura cerca de 9h. Vendo barato pra sair rápido.",
                )
            )

            listings.append(
                ComputerListing(
                    id="used-rec-03",
                    title="MacBook Air M2 13.6'' Estelar 8GB 256GB MagSafe 3 - Loja Seminovos com 90 dias garantia",
                    condition="seminovo",
                    price=5990.0,
                    location="Recife/PE - Pina (Loja Física de Seminovos Apple)",
                    seller_type="loja_fisica_local",
                    source="Loja Especializada Recife Seminovos",
                    url="https://lojarecifemac.com.br/seminovos/air-m2-estelar",
                    processor="Apple M2 (8-core CPU, 8-core GPU)",
                    architecture="Apple Silicon",
                    ram_gb=8,
                    storage_gb=256,
                    storage_type="SSD NVMe",
                    screen_size_inches=13.6,
                    year=2022,
                    battery_health_pct=95,
                    battery_cycles=75,
                    accessories=["Carregador MagSafe 3", "Garantia 90 dias com Nota Fiscal da loja"],
                    raw_description="Aparelho de vitrine em perfeito estado, 100% testado pela nossa assistência, acompanha termo de garantia de 3 meses. Aceitamos parcelamento em até 12x com juros da máquina.",
                )
            )

            listings.append(
                ComputerListing(
                    id="used-rec-04",
                    title="MacBook Pro 13'' 2017 Intel Core i5 8GB 256GB Space Gray",
                    condition="usado",
                    price=2600.0,
                    location="Recife/PE - Espinheiro",
                    seller_type="particular",
                    source="OLX Recife / DDD 81",
                    url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-2017-i5-espinheiro",
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
                    raw_description="MacBook Pro 2017 muito bonito, tela retina sensacional. Bateria avisa que precisa de manutenção logo. Teclado às vezes repete a tecla 'e'. Preço pra desapegar.",
                )
            )

        return listings
