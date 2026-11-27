from __future__ import annotations
import json
from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    JSON,
    Boolean,
)
from sqlalchemy.orm import relationship
from busca_pc.db.database import Base

class ListingModel(Base):
    __tablename__ = "listings"

    id = Column(String(64), primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    brand = Column(String(64), default="Apple", index=True)
    condition = Column(String(32), nullable=False, index=True)  # novo, seminovo, usado
    price = Column(Float, nullable=False, index=True)
    currency = Column(String(8), default="BRL")
    location = Column(String(255), nullable=False)
    seller_type = Column(String(64), nullable=False)
    source = Column(String(128), nullable=False)
    url = Column(Text, nullable=True)
    processor = Column(String(128), nullable=False, index=True)
    architecture = Column(String(64), nullable=False, index=True)
    ram_gb = Column(Integer, nullable=False, index=True)
    storage_gb = Column(Integer, nullable=False)
    storage_type = Column(String(64), default="SSD NVMe")
    screen_size_inches = Column(Float, default=13.3)
    year = Column(Integer, nullable=True)
    battery_health_pct = Column(Integer, nullable=True)
    battery_cycles = Column(Integer, nullable=True)
    accessories = Column(JSON, default=list)
    raw_description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamentos
    hardware_audit = relationship("HardwareAuditModel", back_populates="listing", uselist=False, cascade="all, delete-orphan")
    sentiment_audit = relationship("SentimentAuditModel", back_populates="listing", uselist=False, cascade="all, delete-orphan")
    classification = relationship("ClassificationModel", back_populates="listing", uselist=False, cascade="all, delete-orphan")

class HardwareAuditModel(Base):
    __tablename__ = "hardware_audits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    listing_id = Column(String(64), ForeignKey("listings.id", ondelete="CASCADE"), unique=True, nullable=False)
    hardware_score = Column(Float, nullable=False)
    tier_category = Column(String(64), nullable=False)
    processor_eval = Column(Text, nullable=False)
    ram_eval = Column(Text, nullable=False)
    storage_eval = Column(Text, nullable=False)
    thermal_and_efficiency_eval = Column(Text, nullable=False)
    estimated_lifespan_years = Column(Integer, default=3)
    pros = Column(JSON, default=list)
    cons = Column(JSON, default=list)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    listing = relationship("ListingModel", back_populates="hardware_audit")

class SentimentAuditModel(Base):
    __tablename__ = "sentiment_audits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    listing_id = Column(String(64), ForeignKey("listings.id", ondelete="CASCADE"), unique=True, nullable=False)
    sentiment_score = Column(Float, nullable=False)
    community_consensus = Column(Text, nullable=False)
    chronic_flaws_identified = Column(JSON, default=list)
    reliability_verdict = Column(String(128), nullable=False)
    pros = Column(JSON, default=list)
    cons = Column(JSON, default=list)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    listing = relationship("ListingModel", back_populates="sentiment_audit")

class ClassificationModel(Base):
    __tablename__ = "classifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    listing_id = Column(String(64), ForeignKey("listings.id", ondelete="CASCADE"), unique=True, nullable=False)
    composite_score = Column(Float, nullable=False, index=True)
    cost_benefit_index = Column(Float, nullable=False, index=True)
    tier = Column(String(8), nullable=False, index=True)  # S, A, B, C, F
    verdict = Column(String(64), nullable=False, index=True)
    fair_market_price_recife = Column(Float, nullable=False)
    price_delta_pct = Column(Float, nullable=False)
    justification = Column(Text, nullable=False)
    key_precautions = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

    listing = relationship("ListingModel", back_populates="classification")

class LearningModel(Base):
    __tablename__ = "learnings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(32), nullable=False)
    category = Column(String(128), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    lesson_learned = Column(Text, nullable=False)
    market_rules = Column(JSON, default=list)
    tags = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

class MissionRunModel(Base):
    __tablename__ = "mission_runs"

    id = Column(String(64), primary_key=True)
    title = Column(String(255), nullable=False)
    target_city = Column(String(64), default="Recife")
    target_state = Column(String(16), default="PE")
    status = Column(String(32), default="COMPLETED")
    elapsed_seconds = Column(Float, default=0.0)
    total_listings = Column(Integer, default=0)
    champion_id = Column(String(64), nullable=True)
    executed_at = Column(DateTime, default=datetime.utcnow)
