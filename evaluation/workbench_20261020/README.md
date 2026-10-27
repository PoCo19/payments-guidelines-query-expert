# Supervised workbench verification, 20–22 October 2026

Status: prototype engineering verified; supervised-pilot acceptance and release verification pending.

Latest follow-up: `tests-readiness-fixes-final.txt` records 438 passing Python tests after timing, reviewer diagnostics and citation-label repair changes. [Diagnostic model attempts](../readiness_diagnostics/README.md) preserve successful runtime repeats, incomplete outputs, rejected prompt changes and one recovered frozen claim. [Action register](../../docs/ACTION_ITEMS_20261022.md) is current. The earlier records below retain their original test counts and findings.

`final-readiness-http-smoke.json` records the restarted server's IPO answer: completed in 19.406 seconds, two retained claims including the OC127 history, two withheld claims, and incomplete status. Current Python hashes match this capture as verified on 23 October. Final release and independent acceptance gates remain open.

- `tests-model-fingerprints.txt`: 430 Python tests passed. Covers existing RAG controls, new workflow lifecycles, concurrent edits, stale sources/models, intake graph validity, HTTP origin checks and review-pack gates.
- `javascript.txt`: four JavaScript suites plus syntax checks.
- `retrieval_misses.json` / `.md`: all eleven existing missing anchors classified (five candidate-pool misses; six ranking/context-selection misses). Their quotes are present; relevance remains provisional.
- `../maintained_graph_runs/20261020T175334016268Z/capture.json`: 144-case maintained graph ablation; 212/234 off, 223/234 on; eleven gains, no losses. Retrieval-only timing is not generation performance.
- `paired_answer_findings.json`: the later six-attempt answer comparison had three timeouts and incomplete successful answers. Neither independent answer correctness nor pilot latency passed.
- `impact-browser-work.json` / `impact-browser-export.md`: real generated biometric comparison, edited reviewer question, Needs review status, version history, source excerpts and model digests. No agent-authored human approval.
- `query-browser-work.json` / `query-browser-export.md`: incomplete response-code comparison preserved; the pre-digest snapshot now requires revalidation. Original generation, source inspection, submission and export were browser exercised on 20 October.
- `acceptance-gate.json`: the provisional 50-case pack is correctly blocked pending independent review. No acceptance answers were generated from it.
- `source-graph-snapshot/`: maintained manifest and matching source-release hashes; not a standalone release.

Browser checks are feature-development checks, not the deferred final clean-install/full-rebuild/recovery exercise. Synthetic tests verify approval/rejection transitions; an agent did not attest that real payments answers were independently reviewed. Source files, existing embeddings and model budgets were preserved. Nothing was pushed to GitHub.

Remaining: independently review originals and graph links; fix confirmed qualifications/attribution/history defects; run reviewed paired answers and the 50-case pilot; investigate generation reliability under controlled load; finally run release verification and freeze a new colleague package.
