# Local RAGAS evaluation

Provisional automated evaluation. AI-assisted references await independent review. Scores are not overall answer accuracy. Same-model judging can share generation errors.

Judge: `qwen3.5:9b`. Same model name as generator: **True**. Human review: **pending**.

| Metric | Mean among successful scores | Scored | Errors | Skipped | Pending | Total cases |
|---|---:|---:|---:|---:|---:|---:|
| faithfulness | 1.000 | 2 | 0 | 2 | 0 | 4 |
| factual_correctness | 0.000 | 2 | 0 | 2 | 0 | 4 |
| context_recall | 1.000 | 2 | 0 | 2 | 0 | 4 |
| context_precision | 1.000 | 2 | 0 | 2 | 0 | 4 |
| citation_support | 1.000 | 2 | 0 | 2 | 0 | 4 |

Captured: 4/4 successful application responses.
Negative cases with app abstention: 2/2.
Positive cases with app abstention: 0/2.

Scores use displayed claims and supplied evidence. Reference-based scores use draft references; summary/comparison references are too incomplete and are skipped. Negative and empty-answer cases are reported separately. Failed scores are not converted to zero or hidden from denominators.

Citation ID validity is a structural check. Optional citation_support applies faithfulness separately to each claim and only its cited sources; it remains a model judgement. No overall accuracy score is calculated.

Files: `capture.json` preserves full application responses; this scoring directory contains `scores.json`, `judge_calls.jsonl` and this summary. `human_review.csv` is beside the capture.
