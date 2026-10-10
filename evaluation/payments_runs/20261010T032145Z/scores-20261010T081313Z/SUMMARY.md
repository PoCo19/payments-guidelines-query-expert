# Local RAGAS evaluation

Provisional automated evaluation. AI-assisted references await independent review. Scores are not overall answer accuracy. Same-model judging can share generation errors.

Judge: `qwen3.5:9b`. Same model name as generator: **True**. Human review: **pending**.

| Metric | Mean among successful scores | Scored | Errors | Skipped | Pending | Total cases |
|---|---:|---:|---:|---:|---:|---:|
| faithfulness | 1.000 | 1 | 1 | 3 | 0 | 5 |
| context_recall | 0.833 | 3 | 0 | 2 | 0 | 5 |

Captured: 5/5 successful application responses.
Negative cases with app abstention: 1/1.
Positive cases with app abstention: 2/4.

Scores use displayed claims and supplied evidence. Reference-based scores use draft references; summary/comparison references are too incomplete and are skipped. Negative and empty-answer cases are reported separately. Failed scores are not converted to zero or hidden from denominators.

Short draft references can produce misleading factual_correctness scores: for example, "P2M only." omits the circular and feature named in the question. Inspect judge_calls.jsonl before interpreting disagreements. Do not report these draft-reference scores as validated answer accuracy.

Citation ID validity is a structural check. Optional citation_support applies faithfulness separately to each claim and only its cited sources; it remains a model judgement. No overall accuracy score is calculated.

Files: `capture.json` preserves full application responses; this scoring directory contains `scores.json`, `judge_calls.jsonl` and this summary. `human_review.csv` is beside the capture.
