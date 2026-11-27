from __future__ import annotations
from typing import Literal, Optional, List, Dict, Any
from pydantic import BaseModel, Field

class ComputerListing(BaseModel):
    """Representa um anúncio ou oferta de computador encontrado por um Scout."""
    id: str
    title: str
    condition: Literal["novo", "seminovo", "usado"]
    price: float
    currency: str = "BRL"
    location: str
    seller_type: Literal["loja_oficial", "loja_fisica_local", "particular"]
    source: str
    url: Optional[str] = None
    processor: str
    architecture: Literal["Apple Silicon", "Intel x86", "AMD x86", "Outro"]
    ram_gb: int
    storage_gb: int
    storage_type: Literal["SSD NVMe", "SSD SATA", "eMMC", "HD"] = "SSD NVMe"
    screen_size_inches: Optional[float] = 13.3
    year: Optional[int] = None
    battery_health_pct: Optional[int] = None
    battery_cycles: Optional[int] = None
    accessories: List[str] = Field(default_factory=list)
    raw_description: str = ""

class HardwareAudit(BaseModel):
    """Laudo técnico de hardware emitido pelo Analista de Hardware."""
    hardware_score: float = Field(..., ge=0, le=100, description="Nota de 0 a 100")
    tier_category: Literal["Excelente", "Muito Bom", "Bom", "Medíocre", "Obsoleto"]
    processor_eval: str
    ram_eval: str
    storage_eval: str
    thermal_and_efficiency_eval: str
    estimated_lifespan_years: int
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    summary: str

class SentimentAudit(BaseModel):
    """Laudo de sentimento e comunidade emitido pelo Analista de Sentimento."""
    sentiment_score: float = Field(..., ge=0, le=100, description="Nota de 0 a 100")
    community_consensus: str
    chronic_flaws_identified: List[str] = Field(default_factory=list)
    reliability_verdict: Literal["Altíssima Confiabilidade", "Boa Confiabilidade", "Atenção a Defeitos Conhecidos", "Alto Risco de Quebra Crônica"]
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    summary: str

class FinalClassification(BaseModel):
    """Classificação e veredito final emitido pelo Especialista em Classificação."""
    listing: ComputerListing
    hardware_audit: HardwareAudit
    sentiment_audit: SentimentAudit
    composite_score: float = Field(..., ge=0, le=100, description="Nota combinada ponderada")
    cost_benefit_index: float = Field(..., ge=0, le=100, description="Índice de Custo-Benefício relativo ao preço")
    tier: Literal["S", "A", "B", "C", "F"]
    verdict: Literal["Altamente Recomendado", "Bom Negócio", "Neutro", "Desaconselhado", "Evitar Absolutamente"]
    fair_market_price_recife: float
    price_delta_pct: float
    justification: str
    key_precautions: List[str] = Field(default_factory=list)

class MissionSpec(BaseModel):
    """Diretriz de missão formulada pelo Arquiteto da Operação."""
    mission_id: str
    title: str
    target_category: str
    target_city: str
    target_state: str
    max_budget: Optional[float] = None
    min_ram_gb: int = 8
    target_brand: str = "Apple"
    instructions: str

class LearningRecord(BaseModel):
    """Registro persistente de aprendizados para evolução contínua do sistema."""
    date: str
    category: str
    title: str
    lesson_learned: str
    market_rules: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
