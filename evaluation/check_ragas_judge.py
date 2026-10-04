"""Synthetic evaluator sanity checks, separate from the application benchmark."""
import asyncio
import datetime as dt
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ['RAGAS_DO_NOT_TRACK'] = 'true'
from evaluation.ollama_judge import OllamaJudge
from evaluation.ragas_runner import request, save
from ragas.metrics.collections import Faithfulness


async def main():
    out = ROOT / 'evaluation/ragas_runs' / ('synthetic-controls-' + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    out.mkdir(parents=True, exist_ok=False)
    judge = OllamaJudge('http://127.0.0.1:11434', 'qwen3.5:9b', out / 'judge_calls.jsonl')
    metric = Faithfulness(llm=judge)
    context = 'In this fictional test policy, the remitter bank checks account enablement. The payee PSP does not perform that check.'
    controls = [dict(id='supported', response='The remitter bank checks account enablement.', expected=1.0),
                dict(id='wrong_participant', response='The payee PSP checks account enablement.', expected=0.0)]
    report = dict(kind='synthetic_judge_sanity_check_not_application_evaluation',
                  caveat='Artificial controls with explicit contradictions; not independent expert calibration.',
                  installed_models=request('http://127.0.0.1:11434/api/tags'), rows=[])
    try:
        for control in controls:
            judge.current = dict(control_id=control['id'], metric='faithfulness')
            result = await metric.ascore(user_input='Who checks account enablement in this fictional policy?',
                                        response=control['response'], retrieved_contexts=[context])
            row = dict(control, actual=float(result.value), matched=float(result.value) == control['expected'])
            report['rows'].append(row)
            save(out / 'controls.json', report)
            print(row, flush=True)
    finally:
        await judge.close()
    print(out, flush=True)
    return int(not all(row['matched'] for row in report['rows']))


if __name__ == '__main__':
    raise SystemExit(asyncio.run(main()))
