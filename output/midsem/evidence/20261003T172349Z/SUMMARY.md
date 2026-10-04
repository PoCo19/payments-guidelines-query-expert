# Preliminary retrieval comparison

AI-assisted 50-case UPI set awaiting independent review. Anchor recall is evidence coverage, not answer accuracy. Negative empty evidence is not generated abstention. One interleaved pass after warm-up; timings are preliminary, not a capacity benchmark.

| Variant | Expected anchors found | Negative cases with no evidence | Median ms | Errors |
|---|---:|---:|---:|---:|
| bm25 | 55/55 | 6/6 | 12.0 | 0 |
| vector | 55/55 | 5/6 | 83.0 | 0 |
| hybrid | 55/55 | 5/6 | 78.0 | 0 |
| hybrid_reranked | 55/55 | 5/6 | 160.5 | 0 |

Summary/comparison routes bypass reranking. Per-route results are in retrieval.json. Only hybrid versus hybrid_reranked isolates the reranking toggle.

Human answer correctness and source review remain pending.