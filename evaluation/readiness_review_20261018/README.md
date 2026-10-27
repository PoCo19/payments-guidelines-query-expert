# Readiness evidence — 18 October 2026

Start with [the implementation and limitations](../../docs/READINESS_IMPROVEMENTS_20261018.md). Captures are development evidence, not approved compliance answers or independent accuracy scores.

The later [corpus graph and answer-fix iteration](../../docs/GRAPH_EXPANSION_20261018.md) has its own captures and final 390-test log, `graph-stage-tests-final-v3.txt`. `reference_graph_build_checks.json` verifies graph v4 anchors, identical reference edges versus evaluated v3, and reuse of all unchanged page scans. The earlier logs remain historical; do not combine their test counts or label every file as final-version verification.

## Files in this folder

- `python-tests.txt`: earlier 372-test run. Superseded for final code by `python-tests-final.txt` (375 tests).
- `repeatability-before.json`: 28 BM25 candidate requests in three hash-seeded processes. No ranking change was needed on this evidence; hybrid final-context repeatability is not measured here.
- `source_review_summary.json`: active corpus and graph fingerprints, counts and limitations.
- `source_review_queue.csv`: 2,132 pages prioritised for checking against originals. Signals are not confirmed defects; reviewer fields are deliberately empty.
- `metadata_review_queue.csv`: 1,455 documents lacking issue dates. Do not substitute a listing/update date for an issue or effective date.
- `unavailable_documents.json`: 359 unavailable records, not newly checked download failures.
- `closure_checks.json`: verifies runtime-code/config hashes against the final five-scenario capture, Python compilation and documentation links after reverting the unsuccessful prompt experiment. Browser release verification is explicitly deferred.

## Reviewer procedure

Open the recorded source page and compare its original against the extracted text, including currency signs, units, table headings, exceptions and participant scope. Record the source location, exact discrepancy and review decision. Only confirmed corrections should enter the existing candidate-release intake/validation process. Preserve before/after hashes and rebuild affected vectors; do not edit the active index from the queue. Unavailable or uncertain cases remain unresolved.

## Reproduction

Use the active repaired corpus and installed models recorded in the capture. From the repository root:

```powershell
.\.venv\Scripts\python.exe -X utf8 evaluation/readiness_cycle.py --mode evidence
.\.venv\Scripts\python.exe -X utf8 evaluation/readiness_cycle.py --mode generate --ids X-LIMIT-03,G-IPO-02,G-LIMIT-04,RAG-033,G-DD-01
.\.venv\Scripts\python.exe -X utf8 evaluation/readiness_paraphrases.py
.\.venv\Scripts\python.exe -X utf8 evaluation/checker_challenge.py
```

Run local-model experiments sequentially. The cycle checks its corpus/config fingerprints against the frozen baseline and writes timestamped captures under `evaluation/readiness_runs/`. Retain failures and fallback records. The checker challenge includes an observed false acceptance as well as deliberately constructed valid/invalid claims. None of these commands constitutes the deferred browser/clean-install release gate.
