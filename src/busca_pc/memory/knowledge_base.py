from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from busca_pc.models import LearningRecord

class KnowledgeBase:
    """Gerencia a memória persistente e o aprendizado contínuo do ecossistema de agentes."""

    def __init__(self, base_dir: Optional[Path] = None):
        if base_dir is None:
            self.base_dir = Path(__file__).resolve().parent.parent.parent / "knowledge_base"
        else:
            self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.learnings_file = self.base_dir / "aprendizados.json"
        self.benchmarks_file = self.base_dir / "benchmarks.json"
        self._ensure_files()

    def _ensure_files(self) -> None:
        if not self.learnings_file.exists():
            self._save_json(self.learnings_file, [])
        if not self.benchmarks_file.exists():
            default_benchmarks = {
                "recife_pe": {
                    "macbook_air_m1_8gb_256gb_usado": {
                        "min_price": 3800.0,
                        "avg_price": 4200.0,
                        "max_price": 4500.0,
                        "notes": "Acima de R$ 4.400 compensa negociar ou ver M2. Abaixo de R$ 3.800 verificar procedência."
                    },
                    "macbook_air_m2_8gb_256gb_usado": {
                        "min_price": 5500.0,
                        "avg_price": 6200.0,
                        "max_price": 6800.0
                    },
                    "macbook_pro_intel_2017_2019_usado": {
                        "max_acceptable_price": 2400.0,
                        "flag": "HIGH_RISK_OBSOLETE",
                        "notes": "Risco de flexgate e teclado borboleta, sem updates macOS recentes."
                    },
                    "macbook_air_m1_8gb_256gb_novo": {
                        "retail_avg": 6200.0,
                        "notes": "Raramente compensa comparado ao seminovo em Recife."
                    }
                }
            }
            self._save_json(self.benchmarks_file, default_benchmarks)

    def _load_json(self, path: Path) -> Any:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_json(self, path: Path, data: Any) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def record_learning(self, record: LearningRecord) -> None:
        """Adiciona um novo registro de aprendizado à base."""
        learnings = self._load_json(self.learnings_file)
        learnings.append(record.model_dump())
        self._save_json(self.learnings_file, learnings)

    def get_all_learnings(self) -> List[Dict[str, Any]]:
        return self._load_json(self.learnings_file)

    def get_benchmarks(self, region: str = "recife_pe") -> Dict[str, Any]:
        benchmarks = self._load_json(self.benchmarks_file)
        return benchmarks.get(region, {})

    def update_benchmark(self, region: str, key: str, data: Dict[str, Any]) -> None:
        benchmarks = self._load_json(self.benchmarks_file)
        if region not in benchmarks:
            benchmarks[region] = {}
        benchmarks[region][key] = data
        self._save_json(self.benchmarks_file, benchmarks)
