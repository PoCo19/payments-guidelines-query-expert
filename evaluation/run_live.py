"""Repeatable local-model smoke checks; outputs are not an accuracy benchmark."""
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import Engine, ROOT

engine = Engine()
report = {"created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "models": engine.config, "fingerprint": engine.fingerprint,
          "note": "Developer smoke checks, not a held-out accuracy benchmark. Review claims against their cited passages.",
          "retrieval": [], "answers": []}
target = ROOT / "evaluation" / "live_results.json"

def save():
    target.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

for method in ("bm25", "vector", "hybrid"):
    result = engine.evaluate(method)
    report["retrieval"].append(result)
    save()
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}), flush=True)

for query in (
    "According to OC 186A, what consent must the user give for UPI Tap & Pay on PoS?",
    "According to OC 201, who is the primary user and who is the secondary user in UPI Circle?",
    "What requirements are specified in OC 999?",
    "Explain quantum photosynthesis and chlorophyll.",
):
    print("Testing answer: " + query, flush=True)
    try:
        result = engine.answer({"query":query,"method":"hybrid","mode":"generate"})
        report["answers"].append({"query":query,**result})
        print(json.dumps({k:v for k,v in result.items() if k != "sources"},ensure_ascii=False),flush=True)
    except Exception as exc:
        report["answers"].append({"query":query,"error":str(exc)})
        print("ERROR: " + str(exc),flush=True)
    save()
