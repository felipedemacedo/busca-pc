from __future__ import annotations
import os
import asyncio
from datetime import datetime
from typing import Optional, List, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Query, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

from busca_pc.db.database import get_db, AsyncSessionLocal
from busca_pc.db.repository import (
    init_db,
    get_all_classified,
    get_learnings,
    save_mission_results,
)
from busca_pc.models import MissionSpec
from busca_pc.architect.operation_architect import OperationArchitect

templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializa o banco de dados PostgreSQL
    try:
        await init_db()
        print("✓ Banco de dados PostgreSQL inicializado com sucesso!")
        # Roda um scan inicial se o banco estiver vazio
        async with AsyncSessionLocal() as session:
            existing = await get_all_classified(session)
            if not existing:
                print("⚡ Banco vazio: Executando primeira varredura agêntica para popular o catálogo...")
                architect = OperationArchitect()
                spec = MissionSpec(
                    mission_id="INIT-SCAN-RECIFE",
                    title="Varredura Inicial de Todas as Possibilidades em Recife/PE",
                    target_category="MacBook",
                    target_brand="Apple",
                    target_city="Recife",
                    target_state="PE",
                    instructions="Escanear todas as possibilidades sem teto de compra e classificar."
                )
                res = await architect.execute_mission(spec)
                await save_mission_results(
                    session=session,
                    classifications=res["classifications"],
                    learnings=res["learnings_recorded"],
                    mission_id=spec.mission_id,
                    elapsed_seconds=res["elapsed_seconds"],
                    champion_id=res["champion"].listing.id if res["champion"] else None,
                )
                print(f"✓ Catálogo populado com {len(res['classifications'])} computadores no PostgreSQL!")
    except Exception as e:
        print(f"⚠️ Aviso na inicialização do DB: {e}")
    yield

app = FastAPI(
    title="Busca-PC: Plataforma Agêntica de Classificação de Computadores",
    description="Sistema Multiagente Paralelo com Análise de Hardware, Sentimento de Comunidade e Classificação com Banco PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}

@app.get("/api/listings")
async def list_computers(
    tier: Optional[str] = Query(None, description="Filtro por Tier: S, A, B, C, F ou todos"),
    condition: Optional[str] = Query(None, description="novo, seminovo, usado ou todos"),
    architecture: Optional[str] = Query(None, description="Apple Silicon, Intel x86 ou todos"),
    min_price: Optional[float] = Query(None, description="Preço mínimo"),
    max_price: Optional[float] = Query(None, description="Preço máximo"),
    search: Optional[str] = Query(None, description="Termo de busca textual"),
    db: AsyncSession = Depends(get_db),
):
    items = await get_all_classified(
        session=db,
        tier=tier,
        condition=condition,
        architecture=architecture,
        min_price=min_price,
        max_price=max_price,
        search=search,
    )
    return {"total": len(items), "data": items}

@app.get("/api/stats")
async def get_stats(db: AsyncSession = Depends(get_db)):
    items = await get_all_classified(session=db)
    if not items:
        return {"total": 0, "tiers": {}, "conditions": {}, "avg_price": 0.0}

    tiers_count = {}
    conditions_count = {}
    total_price = 0.0

    for it in items:
        t = it["classification"]["tier"] if it["classification"] else "Outro"
        c = it["condition"]
        tiers_count[t] = tiers_count.get(t, 0) + 1
        conditions_count[c] = conditions_count.get(c, 0) + 1
        total_price += it["price"]

    champion = items[0] if items else None

    return {
        "total_analyzed": len(items),
        "tiers": tiers_count,
        "conditions": conditions_count,
        "avg_price": round(total_price / len(items), 2),
        "champion": {
            "id": champion["id"],
            "title": champion["title"],
            "price": champion["price"],
            "icb": champion["classification"]["cost_benefit_index"],
            "tier": champion["classification"]["tier"],
        } if champion and champion.get("classification") else None
    }

@app.get("/api/learnings")
async def list_learnings(db: AsyncSession = Depends(get_db)):
    learnings = await get_learnings(session=db)
    return {"total": len(learnings), "data": learnings}

@app.post("/api/missions/run")
async def trigger_mission_scan(db: AsyncSession = Depends(get_db)):
    """Dispara uma nova varredura agêntica paralela completa e persiste os resultados no PostgreSQL."""
    architect = OperationArchitect()
    spec = MissionSpec(
        mission_id=f"SCAN-{int(datetime.utcnow().timestamp())}",
        title="Varredura Completa de Todas as Possibilidades em Recife/PE",
        target_category="MacBook",
        target_brand="Apple",
        target_city="Recife",
        target_state="PE",
        instructions="Buscar sem teto de compra, auditar hardware e sentimento em paralelo, e gravar no PostgreSQL."
    )

    res = await architect.execute_mission(spec)
    champ_id = res["champion"].listing.id if res["champion"] else None

    await save_mission_results(
        session=db,
        classifications=res["classifications"],
        learnings=res["learnings_recorded"],
        mission_id=spec.mission_id,
        elapsed_seconds=res["elapsed_seconds"],
        champion_id=champ_id,
    )

    # Retorna o catálogo atualizado
    updated_items = await get_all_classified(session=db)
    return {
        "success": True,
        "elapsed_seconds": res["elapsed_seconds"],
        "total_found": len(res["classifications"]),
        "champion": res["champion"].listing.title if res["champion"] else None,
        "data": updated_items,
    }
