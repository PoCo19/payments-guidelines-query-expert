# Product-maturity verification — completed 28 October 2026

The folder retains its 27 October start label. Final verification ran on 28 October. This is development evidence, not independently reviewed payments acceptance.

## Final engineering results

- **474 Python tests passed**: `full-tests-verified.txt`.
- **Four JavaScript suites passed**: `javascript-tests.txt`.
- Browser journeys: real answer → save → evidence export; document-first comparison → baseline confirmation → generated summary → citation/source reader; saved-work list and cross-page library navigation. Narrow-width checks are in `design-qa.md`.
- No API provider, corpus correction, embedding rebuild, graph change or database migration was introduced.

Earlier logs are preserved: the request-budget failure was fixed by shortening comparison instructions; the subsequent wording assertion was aligned with the equivalent “not proof of supersession” safeguard. `maturity-tests.txt` includes 21 tests accidentally imported a second time; final discovery removes that duplication. Do not add interim test counts together.

## Retrieval comparison

The two complete comparison files are preserved byte-for-byte inside **`retrieval-records.zip`** at `retrieval-pairs.json` and `final-retrieval/retrieval-pairs.json`. Extract this archive to inspect the raw records. SHA-256 equivalence was checked before packaging; local uncompressed copies are ignored. This keeps the public change review readable without dropping failed or intermediate results.

`final-retrieval/retrieval-pairs.json` holds 144 paired questions with **234 expected source anchors**. Before: **223/234**. After: **223/234**. Zero lost anchors and zero exceptions. Eleven existing misses remain. Both arms use the maintained graph; this is not another Graph RAG ablation. The comparison isolates broad-overview amendment recovery and uses the same corpus, model settings and datasets. Arm order alternates. It measures retrieval, not answer correctness or independent acceptance.

`lite-before.json` and `lite-after.json` preserve the targeted diagnosis: OC169A's operative limit clause was omitted before, then included as `operative_change_context`. A paraphrase probe found a stop-word normalization defect; that was corrected and guarded by a regression test. Final scope tests cover strict document, product and cutoff boundaries.

## Final seven live probes

Full requests, claims, checks and sources are in `live-closeout/`; model digests, configuration hash and code hashes are in its metadata. `summary.json` reports statuses and citation-ID resolution. Timings are observations, not a controlled p95 benchmark; CPU software tests also ran during part of this session.

| Case | Observation | Interpretation |
|---|---|---|
| UPI Lite limits | ₹1,000 per transaction and ₹5,000 total; completeness check unavailable | Correct target figures against selected evidence; unavailable review is not a pass |
| Explain UPI Lite in simple words | Recovered amendment and corrected figures; marked incomplete | The old-figure failure is repaired in this probe, but offline/authentication scope is still oversimplified |
| Historical OC169 | Retained ₹500 as the historical provision | The fix did not rewrite the historical answer using later limits |
| OC185B IPO control | Distinguished ₹5 lakh per transaction from ₹10 lakh cumulative | Central answer retained; some history statements withheld and response remains incomplete |
| Gibberish | Abstained without claims | No fabricated answer; this probe still invoked the model |
| Invented reference | No evidence; abstained without model generation | Missing reference did not generate an invented rule |
| Change summary | Correct old/new limit contrast; four statements withheld | Incomplete; it still overstates novelty of replenishment/top-up, and the advisory checker misreads some table scope |

All displayed citation identifiers resolve in these seven probes. That is an identifier check, not a claim-support score. There is no defensible overall correctness percentage from this small, tuned set.

`change-first.json` preserves the earlier comparison failure: a referenced RBI date was called the NPCI issue date and an unsupported post-deadline restriction was inferred. `live-final/` is an intermediate instruction trial, before the final normalization and shortened prompt. Those records are not silently replaced by the final run. `ask-saved.json` and `browser-export.md` preserve the real saved-answer/export journey.

## What is closed and what is open

The six implementation items, interface journeys and bounded retrieval repair are implemented and verified at the engineering level. **Answer-quality acceptance remains open.** Better retrieval does not ensure the model uses it correctly. Current examples still show scope/novelty errors, incomplete answers and noisy advisory findings. The supported next work is reviewed synthesis/checker cases, not broader graph expansion or new models. Human evaluation was deferred by the user and is not claimed complete.

## Reproduce

After normal setup, run from the repository root with Ollama available:

```powershell
.\.venv\Scripts\python.exe -X utf8 -m unittest discover -s tests
node tests/test_answer_format.js
node tests/test_research_view.js
node tests/test_intake_view.js
node tests/test_work_view.js
.\.venv\Scripts\python.exe -X utf8 evaluation/product_maturity_check.py --output evaluation/my-retrieval-repeat --config config.workbench.json
.\.venv\Scripts\python.exe -X utf8 evaluation/product_maturity_live.py --output evaluation/my-live-repeat --config config.workbench.json
```

Both runners default to local `config.json`; the commands above explicitly use the restored workbench configuration on a teammate machine. Output directories must be fresh; existing results are protected from overwrite. Live probes store disposable workflow records under `data/qa-maturity-20261028`, separate from real saved work. Preserve configuration/source/model fingerprints when comparing repeats.
