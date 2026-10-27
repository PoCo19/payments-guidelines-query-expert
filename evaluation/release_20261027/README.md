# Additional tests and GitHub handoff — 27 October 2026

These are development checks. They do not certify the answers or replace independent source/graph and acceptance review.

`smoke.py` runs five cases with the active local configuration. `smoke-config.json` records model names, corpus fingerprint and a configuration hash. Each response is retained separately, including warnings and check availability.

| Case | Observed result | Interpretation |
|---|---|---|
| Gibberish | Abstained, zero claims | Expected negative handling |
| Unrelated cooking question | Abstained, zero claims | Expected negative handling |
| Invented UPI OC999999 | Abstained, zero claims | Expected unavailable-reference handling |
| Brief UPI Lite explanation | Seven claims; completeness check unavailable | **Quality failure:** unqualified historical limits, absent later amendment in context, and poor brevity |
| OC185B cumulative versus single IPO mandate | Four claims retaining the distinction and OC127 provision; completeness check unavailable | Useful observed answer; not independently accepted or completeness-verified |

The UPI Lite answer cites OC169 dated 31 August 2023 for the transaction and balance figures. The indexed OC169A dated 27 February 2025 contains later UPI Lite limits and distinguishes Lite X. This finding requires a generic current-versus-historical evidence follow-up, not a hardcoded answer or a weakened warning. The original PDFs were not independently re-reviewed in this publication check.

Additional unit tests cover every withholding combination for a four-cell table, and preservation of each claim across all explicit styles for one through nine claims. Tests preserve citations and human edits; they do not measure factual correctness.

Cleanup keeps QA data and private workflow records local. Historical experiment records remain available; rebuildable whole-corpus graph candidates are excluded, with their code, casebooks and measured results retained. The maintained graph and corrected source release are shipped together in the new workbench handoff.

## Clean checkout verification

Source restoration reconstructed the corpus and registry fingerprints, validated 20 existing mixed-source case anchors, and checked the maintained graph against the new package. No embeddings were built during this check.

The first clean-checkout test run found a historical migration test depending on ignored personal configuration. It accidentally compared later OCR repairs against the original migration text. The test now explicitly selects the checked-in original multi-product fixture; no source corrections or assertions were removed. The other error was an absent reranker weight file, which is deliberately installed by setup rather than committed. The repeat uses the same hash-verified reranker assets as setup and the existing pinned Python environment. This is a clean source checkout test, not a claim of a fresh dependency installation or complete index rebuild.

Final clean-checkout result: **465 Python tests and all four JavaScript suites passed**. Installed Ollama digests and reranker hashes matched the package. See `clean-checkout-tests-final.txt`, `clean-checkout-javascript.txt`, `clean-checkout-models.txt` and `clean-checkout-restore.txt`. The earlier failed attempt remains saved for traceability. `publication-audit.json` reports no matches for its bounded credential/local-file checks; this is not an exhaustive security audit.
