# Consolidated contextual retrieval comparison

AI-assisted development regression, not held-out testing or answer accuracy. Both arms retain the existing graph, vectors, reranker configuration and context budget. Only lexical metadata enrichment differs. Original request routes are preserved.

| Family / execution stratum | Cases | Expected anchors | Baseline found | Enriched found | Anchors gained / lost |
|---|---:|---:|---:|---:|---:|
| all | 138 | 223 | 208 | 208 | 2 / 2 |
| graph | 40 | 78 | 78 | 78 | 0 / 0 |
| original_upi | 50 | 55 | 55 | 55 | 0 / 0 |
| paraphrases | 28 | 56 | 46 | 46 | 2 / 2 |
| payments | 20 | 34 | 29 | 29 | 0 / 0 |
| reranked_both | 114 | 198 | 185 | 185 | 2 / 2 |
| bypass_both | 24 | 25 | 23 | 23 | 0 / 0 |
| reranking_changed | 0 | 0 | 0 | 0 | 0 / 0 |

Family rows partition the full set. Execution strata are a separate partition; do not add both sets of rows together. Bypass cases cannot demonstrate a reranking benefit. Graph controls include filtering and missing-reference routing, not general answer correctness.

See `stratified_summary.json` for negative empty-evidence counts, raw top-six diagnostic retrieval, graph controls, missing-source disclosures and local median times. Negative empty-evidence counts are not generated-answer abstention scores. Single-run latency includes warm-up and cache effects; it is not a proven performance difference.

Case-level gains/losses and routes: `paired_cases.csv`. Full evidence, traces and fingerprints: `capture.json`.
