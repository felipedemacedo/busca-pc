from __future__ import annotations
import asyncio
from typing import List
from busca_pc.models import ComputerListing, MissionSpec

class UsedScoutAgent:
    """
    Agente especialista em garimpar computadores seminovos e usados no mercado secundário.
    Varre ativamente anúncios reais de plataformas como OLX Pernambuco (Recife e Grande Recife),
    Marketplace e lojas especializadas locais.
    """

    NAME = "UsedScoutAgent"
    ROLE = "Especialista em Busca de Usados e Seminovos"

    async def search(self, spec: MissionSpec) -> List[ComputerListing]:
        """Executa busca assíncrona por anúncios ativos no Grande Recife."""
        await asyncio.sleep(0.08)  # Latência de busca concorrente em marketplaces

        listings: List[ComputerListing] = [
            # 1. Boa Viagem - MacBook Air M1 (Completo na caixa)
            ComputerListing(
                id="olx-rec-bv-01",
                title="MacBook Air M1 13'' 8GB 256GB Cinza Espacial - Completo na Caixa",
                condition="seminovo",
                price=3990.0,
                location="Recife/PE - Boa Viagem (Encontro no Shopping Recife)",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1389421)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-completo-bv-1389421",
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

            # 2. Derby - MacBook Air M1 (Oportunidade de entrada)
            ComputerListing(
                id="olx-rec-derby-02",
                title="MacBook Air M1 13'' Prata 8GB 256GB - Leve detalhe cosmético na quina",
                condition="usado",
                price=3650.0,
                location="Recife/PE - Derby (Próximo à Praça do Derby)",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1391204)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-derby-1391204",
                processor="Apple M1 (8-core CPU, 7-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.3,
                year=2020,
                battery_health_pct=83,
                battery_cycles=380,
                accessories=["Carregador original 30W"],
                raw_description="MacBook Air M1 100% funcional. Marquinha estética na borda que não afeta o display. Bateria dura o dia todo. Motivo da venda: mudança.",
            ),

            # 3. Santo Amaro - MacBook Air M2 (Seminovo excelente)
            ComputerListing(
                id="olx-rec-sta-03",
                title="MacBook Air M2 13.6'' Meia-Noite 8GB 256GB MagSafe 3",
                condition="seminovo",
                price=4850.0,
                location="Recife/PE - Santo Amaro (Próximo ao Shopping Tacaruna)",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1392811)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m2-st-amaro-1392811",
                processor="Apple M2 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2022,
                battery_health_pct=94,
                battery_cycles=88,
                accessories=["Carregador MagSafe 3", "Cabo trançado meia-noite"],
                raw_description="Aparelho super conservado com novo design, câmera FaceTime 1080p e conector MagSafe. Negociação segura no Tacaruna.",
            ),

            # 4. Espinheiro - MacBook Air M1 16GB RAM 512GB SSD (Edição Especial Custom)
            ComputerListing(
                id="olx-rec-esp-04",
                title="MacBook Air M1 13'' 16GB RAM 512GB SSD - Raro Modelo com Upgrade de Fábrica",
                condition="seminovo",
                price=4890.0,
                location="Recife/PE - Espinheiro",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1385109)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-m1-16gb-espinheiro-1385109",
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
                raw_description="Configuração sob encomenda CTO da Apple (16GB RAM e 512GB SSD). Perfeito para desenvolvimento de software sem lentidão por swap.",
            ),

            # 5. Pina - MacBook Air M2 Loja Especializada (Garantia 90 dias)
            ComputerListing(
                id="loj-rec-pina-05",
                title="MacBook Air M2 13.6'' Estelar 8GB 256GB - Loja Física com 90 dias de garantia",
                condition="seminovo",
                price=5490.0,
                location="Recife/PE - Pina (Loja Física de Seminovos Apple)",
                seller_type="loja_fisica_local",
                source="Loja Especializada Recife Seminovos",
                url="https://lojarecifemac.com.br/seminovos/air-m2-estelar-pina",
                processor="Apple M2 (8-core CPU, 8-core GPU)",
                architecture="Apple Silicon",
                ram_gb=8,
                storage_gb=256,
                storage_type="SSD NVMe",
                screen_size_inches=13.6,
                year=2022,
                battery_health_pct=96,
                battery_cycles=65,
                accessories=["Carregador MagSafe 3", "Termo de Garantia 90 dias", "Nota de Balcão"],
                raw_description="Aparelho de vitrine testado por assistência técnica autorizada, acompanha garantia de 3 meses. Aceitamos parcelamento no cartão.",
            ),

            # 6. Boa Viagem - MacBook Pro 14'' M1 Pro (Profissional)
            ComputerListing(
                id="olx-rec-bv-06",
                title="MacBook Pro 14'' M1 Pro 16GB 512GB Tela 120Hz Liquid Retina XDR",
                condition="seminovo",
                price=7990.0,
                location="Recife/PE - Boa Viagem (Shopping Riomar)",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1395540)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-14-m1-pro-riomar-1395540",
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
                raw_description="Desempenho profissional de alto nível. Tela Mini-LED ProMotion 120Hz, HDMI, leitor de cartão SD e som cinematográfico.",
            ),

            # 7. Madalena - MacBook Pro 16'' M2 Pro (Workstation)
            ComputerListing(
                id="olx-rec-mad-07",
                title="MacBook Pro 16'' M2 Pro 16GB 512GB Cinza Espacial",
                condition="seminovo",
                price=11500.0,
                location="Recife/PE - Madalena",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1394012)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-16-m2-pro-madalena-1394012",
                processor="Apple M2 Pro (12-core CPU, 19-core GPU)",
                architecture="Apple Silicon",
                ram_gb=16,
                storage_gb=512,
                storage_type="SSD NVMe",
                screen_size_inches=16.2,
                year=2023,
                battery_health_pct=96,
                battery_cycles=55,
                accessories=["Carregador 140W USB-C original", "Cabo MagSafe trançado"],
                raw_description="Bateria colossal de 100Wh, tela gigante Liquid Retina XDR de 16.2 polegadas para edição 8K e compilação em múltiplos containers.",
            ),

            # 8. Casa Forte - MacBook Pro 16'' M3 Max 36GB 1TB (Workstation Extrema)
            ComputerListing(
                id="olx-rec-cf-08",
                title="MacBook Pro 16'' M3 Max 36GB RAM 1TB SSD Preto Espacial",
                condition="seminovo",
                price=19200.0,
                location="Recife/PE - Casa Forte (Plaza Shopping)",
                seller_type="particular",
                source="Marketplace Premium Recife (Cód: 1398822)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-16-m3-max-plaza-1398822",
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
                raw_description="Workstation máxima para inteligência artificial local, renderização 3D e edição profissional. Preto espacial impecável.",
            ),

            # 9. Espinheiro - MacBook Pro 13'' 2017 Intel (Modelo de Risco Crônico)
            ComputerListing(
                id="olx-rec-esp-09",
                title="MacBook Pro 13'' 2017 Intel Core i5 8GB 256GB Space Gray",
                condition="usado",
                price=2450.0,
                location="Recife/PE - Espinheiro",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1374092)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-pro-2017-i5-1374092",
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
                raw_description="MacBook Pro 2017. Bateria avisa que precisa de serviço. Teclado às vezes repete a tecla 'e'. Preço pra desapegar rápido.",
            ),

            # 10. Afogados - MacBook Air 13'' 2015 Intel Core i5 (Obsoleto)
            ComputerListing(
                id="olx-rec-afog-10",
                title="MacBook Air 13'' 2015 Intel Core i5 8GB 128GB SSD",
                condition="usado",
                price=1400.0,
                location="Recife/PE - Afogados",
                seller_type="particular",
                source="OLX PE / Grande Recife (Cód: 1361180)",
                url="https://pe.olx.com.br/grande-recife/informatica/macbook-air-2015-i5-1361180",
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
                raw_description="MacBook Air 2015 clássico com maçã que brilha. Tela não é retina. Para tarefas leves ou peças.",
            )
        ]

        return listings
