from __future__ import annotations
from typing import List, Optional, Dict, Any
from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from busca_pc.db.database import engine, Base, AsyncSessionLocal
from busca_pc.db.schema import (
    ListingModel,
    HardwareAuditModel,
    SentimentAuditModel,
    ClassificationModel,
    LearningModel,
    MissionRunModel,
)
from busca_pc.models import (
    ComputerListing,
    HardwareAudit,
    SentimentAudit,
    FinalClassification,
    LearningRecord,
)

async def init_db() -> None:
    """Cria as tabelas no PostgreSQL se ainda não existirem."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def save_mission_results(
    session: AsyncSession,
    classifications: List[FinalClassification],
    learnings: List[LearningRecord],
    mission_id: str,
    elapsed_seconds: float,
    champion_id: Optional[str] = None,
) -> None:
    """Salva todas as máquinas auditadas e aprendizados no banco relacional PostgreSQL."""
    for c in classifications:
        l = c.listing
        # Upsert Listing
        existing_listing = await session.get(ListingModel, l.id)
        if existing_listing:
            listing_row = existing_listing
            listing_row.title = l.title
            listing_row.brand = getattr(l, "brand", "Apple") or "Apple"
            listing_row.condition = l.condition
            listing_row.price = l.price
            listing_row.location = l.location
            listing_row.seller_type = l.seller_type
            listing_row.source = l.source
            listing_row.url = l.url
            listing_row.processor = l.processor
            listing_row.architecture = l.architecture
            listing_row.ram_gb = l.ram_gb
            listing_row.storage_gb = l.storage_gb
            listing_row.screen_size_inches = l.screen_size_inches
            listing_row.year = l.year
            listing_row.battery_health_pct = l.battery_health_pct
            listing_row.battery_cycles = l.battery_cycles
            listing_row.accessories = l.accessories
            listing_row.raw_description = l.raw_description
        else:
            listing_row = ListingModel(
                id=l.id,
                title=l.title,
                brand=getattr(l, "brand", "Apple") or "Apple",
                condition=l.condition,
                price=l.price,
                currency=l.currency,
                location=l.location,
                seller_type=l.seller_type,
                source=l.source,
                url=l.url,
                processor=l.processor,
                architecture=l.architecture,
                ram_gb=l.ram_gb,
                storage_gb=l.storage_gb,
                storage_type=l.storage_type,
                screen_size_inches=l.screen_size_inches,
                year=l.year,
                battery_health_pct=l.battery_health_pct,
                battery_cycles=l.battery_cycles,
                accessories=l.accessories,
                raw_description=l.raw_description,
            )
            session.add(listing_row)

        await session.flush()

        # Hardware Audit
        stmt = select(HardwareAuditModel).where(HardwareAuditModel.listing_id == l.id)
        res = await session.execute(stmt)
        existing_hw = res.scalar_one_or_none()
        hw = c.hardware_audit
        if existing_hw:
            existing_hw.hardware_score = hw.hardware_score
            existing_hw.tier_category = hw.tier_category
            existing_hw.processor_eval = hw.processor_eval
            existing_hw.ram_eval = hw.ram_eval
            existing_hw.storage_eval = hw.storage_eval
            existing_hw.thermal_and_efficiency_eval = hw.thermal_and_efficiency_eval
            existing_hw.estimated_lifespan_years = hw.estimated_lifespan_years
            existing_hw.pros = hw.pros
            existing_hw.cons = hw.cons
            existing_hw.summary = hw.summary
        else:
            session.add(
                HardwareAuditModel(
                    listing_id=l.id,
                    hardware_score=hw.hardware_score,
                    tier_category=hw.tier_category,
                    processor_eval=hw.processor_eval,
                    ram_eval=hw.ram_eval,
                    storage_eval=hw.storage_eval,
                    thermal_and_efficiency_eval=hw.thermal_and_efficiency_eval,
                    estimated_lifespan_years=hw.estimated_lifespan_years,
                    pros=hw.pros,
                    cons=hw.cons,
                    summary=hw.summary,
                )
            )

        # Sentiment Audit
        stmt = select(SentimentAuditModel).where(SentimentAuditModel.listing_id == l.id)
        res = await session.execute(stmt)
        existing_sent = res.scalar_one_or_none()
        sent = c.sentiment_audit
        if existing_sent:
            existing_sent.sentiment_score = sent.sentiment_score
            existing_sent.community_consensus = sent.community_consensus
            existing_sent.chronic_flaws_identified = sent.chronic_flaws_identified
            existing_sent.reliability_verdict = sent.reliability_verdict
            existing_sent.pros = sent.pros
            existing_sent.cons = sent.cons
            existing_sent.summary = sent.summary
        else:
            session.add(
                SentimentAuditModel(
                    listing_id=l.id,
                    sentiment_score=sent.sentiment_score,
                    community_consensus=sent.community_consensus,
                    chronic_flaws_identified=sent.chronic_flaws_identified,
                    reliability_verdict=sent.reliability_verdict,
                    pros=sent.pros,
                    cons=sent.cons,
                    summary=sent.summary,
                )
            )

        # Classification
        stmt = select(ClassificationModel).where(ClassificationModel.listing_id == l.id)
        res = await session.execute(stmt)
        existing_class = res.scalar_one_or_none()
        if existing_class:
            existing_class.composite_score = c.composite_score
            existing_class.cost_benefit_index = c.cost_benefit_index
            existing_class.tier = c.tier
            existing_class.verdict = c.verdict
            existing_class.fair_market_price_recife = c.fair_market_price_recife
            existing_class.price_delta_pct = c.price_delta_pct
            existing_class.justification = c.justification
            existing_class.key_precautions = c.key_precautions
        else:
            session.add(
                ClassificationModel(
                    listing_id=l.id,
                    composite_score=c.composite_score,
                    cost_benefit_index=c.cost_benefit_index,
                    tier=c.tier,
                    verdict=c.verdict,
                    fair_market_price_recife=c.fair_market_price_recife,
                    price_delta_pct=c.price_delta_pct,
                    justification=c.justification,
                    key_precautions=c.key_precautions,
                )
            )

    # Persist Learnings
    for lr in learnings:
        session.add(
            LearningModel(
                date=lr.date,
                category=lr.category,
                title=lr.title,
                lesson_learned=lr.lesson_learned,
                market_rules=lr.market_rules,
                tags=lr.tags,
            )
        )

    # Persist Mission Run
    session.add(
        MissionRunModel(
            id=mission_id,
            title="Varredura de Todas as Possibilidades - Recife/PE",
            target_city="Recife",
            target_state="PE",
            status="COMPLETED",
            elapsed_seconds=elapsed_seconds,
            total_listings=len(classifications),
            champion_id=champion_id,
        )
    )

    await session.commit()

async def get_all_classified(
    session: AsyncSession,
    tier: Optional[str] = None,
    condition: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    architecture: Optional[str] = None,
    search: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Recupera computadores classificados com joins completos para o website/API."""
    query = (
        select(ListingModel)
        .options(
            selectinload(ListingModel.hardware_audit),
            selectinload(ListingModel.sentiment_audit),
            selectinload(ListingModel.classification),
        )
    )

    if condition and condition != "todos":
        query = query.where(ListingModel.condition == condition.lower())
    if architecture and architecture != "todos":
        query = query.where(ListingModel.architecture == architecture)
    if min_price is not None:
        query = query.where(ListingModel.price >= min_price)
    if max_price is not None:
        query = query.where(ListingModel.price <= max_price)
    if search:
        search_pattern = f"%{search}%"
        query = query.where(
            (ListingModel.title.ilike(search_pattern))
            | (ListingModel.processor.ilike(search_pattern))
            | (ListingModel.location.ilike(search_pattern))
        )

    result = await session.execute(query)
    listings = result.scalars().all()

    items = []
    for l in listings:
        if not l.classification:
            continue
        if tier and tier != "todos" and l.classification.tier != tier.upper():
            continue

        items.append({
            "id": l.id,
            "title": l.title,
            "brand": getattr(l, "brand", "Apple") or "Apple",
            "condition": l.condition,
            "price": l.price,
            "currency": l.currency,
            "location": l.location,
            "seller_type": l.seller_type,
            "source": l.source,
            "url": l.url,
            "processor": l.processor,
            "architecture": l.architecture,
            "ram_gb": l.ram_gb,
            "storage_gb": l.storage_gb,
            "storage_type": l.storage_type,
            "screen_size_inches": l.screen_size_inches,
            "year": l.year,
            "battery_health_pct": l.battery_health_pct,
            "battery_cycles": l.battery_cycles,
            "accessories": l.accessories or [],
            "raw_description": l.raw_description,
            "hardware_audit": {
                "score": l.hardware_audit.hardware_score if l.hardware_audit else 0,
                "tier_category": l.hardware_audit.tier_category if l.hardware_audit else "",
                "processor_eval": l.hardware_audit.processor_eval if l.hardware_audit else "",
                "ram_eval": l.hardware_audit.ram_eval if l.hardware_audit else "",
                "storage_eval": l.hardware_audit.storage_eval if l.hardware_audit else "",
                "thermal_eval": l.hardware_audit.thermal_and_efficiency_eval if l.hardware_audit else "",
                "lifespan_years": l.hardware_audit.estimated_lifespan_years if l.hardware_audit else 0,
                "pros": l.hardware_audit.pros if l.hardware_audit else [],
                "cons": l.hardware_audit.cons if l.hardware_audit else [],
                "summary": l.hardware_audit.summary if l.hardware_audit else "",
            } if l.hardware_audit else None,
            "sentiment_audit": {
                "score": l.sentiment_audit.sentiment_score if l.sentiment_audit else 0,
                "consensus": l.sentiment_audit.community_consensus if l.sentiment_audit else "",
                "chronic_flaws": l.sentiment_audit.chronic_flaws_identified if l.sentiment_audit else [],
                "reliability_verdict": l.sentiment_audit.reliability_verdict if l.sentiment_audit else "",
                "pros": l.sentiment_audit.pros if l.sentiment_audit else [],
                "cons": l.sentiment_audit.cons if l.sentiment_audit else [],
                "summary": l.sentiment_audit.summary if l.sentiment_audit else "",
            } if l.sentiment_audit else None,
            "classification": {
                "composite_score": l.classification.composite_score,
                "cost_benefit_index": l.classification.cost_benefit_index,
                "tier": l.classification.tier,
                "verdict": l.classification.verdict,
                "fair_market_price": l.classification.fair_market_price_recife,
                "price_delta_pct": l.classification.price_delta_pct,
                "justification": l.classification.justification,
                "precautions": l.classification.key_precautions or [],
            } if l.classification else None,
        })

    # Ordena por ICB decrescente
    items.sort(key=lambda x: (x["classification"]["cost_benefit_index"] if x["classification"] else 0), reverse=True)
    return items

async def get_learnings(session: AsyncSession) -> List[Dict[str, Any]]:
    query = select(LearningModel).order_by(desc(LearningModel.id))
    result = await session.execute(query)
    learnings = result.scalars().all()
    return [
        {
            "id": lr.id,
            "date": lr.date,
            "category": lr.category,
            "title": lr.title,
            "lesson_learned": lr.lesson_learned,
            "market_rules": lr.market_rules or [],
            "tags": lr.tags or [],
        }
        for lr in learnings
    ]
