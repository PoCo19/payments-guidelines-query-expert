# Engineering closeout — 24 October 2026

The two supervised prototypes now have a reproducible engineering candidate. This closes the implementation and operational-verification work described below. It does **not** close answer-quality acceptance or authorize unattended payments decisions.

## What changed

- Local-model HTTP calls now have a total connection deadline, including stalled headers and trickling response bodies. The timer closes the socket; late completions are rejected. OS suspension can still delay timer execution. Existing model sizes and budgets are unchanged.
- Monetary support checks compare amounts with their units. An unrelated address digit such as “10th floor” cannot support a claim of ₹10 lakh when the monetary evidence says ₹5 lakh. This catches a class of numerical errors; it does not establish eligibility, applicability or completeness. Unitless tables still require the existing scope and semantic checks.
- Bounded repair of a malformed internal document label uses only its attached evidence and excludes the original question from that repair prompt. This reduces contamination from a disputed amount in the question. Repaired claims still pass support checks.
- Added reproducible workflow-latency, recovery, portable-packaging and candidate-verification tools. These preserve failures and distinguish engineering verification from independent acceptance.

No active source text, model configuration, corpus format or live embeddings were changed during this closeout. The synthetic intake test ran in an isolated copy.

## Verification and evidence

| Check | Result | Evidence |
|---|---|---|
| Fresh Python 3.12 environment | Pinned runtime and optional acquisition dependencies installed; dependency check passed | `clean-install.txt`, `clean-acquisition-install.txt` |
| Python regression | 445 tests passed, no skips | `clean-tests.txt` |
| JavaScript regression | All four suites passed: answer formatting, research coverage, intake and workbench rendering | `javascript-tests.txt` |
| Full fresh Chroma rebuild | 14,480 chunks rebuilt from 14,480 matching cache entries; no existing Chroma index copied | `fresh-index-rebuild.txt` |
| Incremental intake | One synthetic new chunk computed; 14,480 unchanged embeddings reused; activation and rollback passed | `recovery.json` |
| Recovery | Model outage retained source evidence; stale graph degraded visibly; interrupted generation retained its saved draft; negative routing passed | `recovery.json` |
| Browser workflows | Query and impact draft generation, source reading, versioned edits, review submission and evidence export checked in the isolated application | `browser-verification.md` |
| Maintained graph | 144 cases: on 223/234, off 211/234; 12 gained anchors and zero losses within this run | `graph-comparison.json` |
| Colleague candidate | Portable paths, source and graph snapshot, dependency locks, available originals, embedding cache and per-file hashes | `ENGINEERING_START.md`, archive checksum and package manifest |

Evidence files are under [evaluation/engineering_20261024](../evaluation/engineering_20261024/). The index rebuild reuses verified cached vectors; it does not claim to have recomputed all embeddings. Recovery and intake changes were confined to `data/qa24/app`, and its original configuration was restored.

The graph-on anchor results match the earlier 144-case run exactly. The graph-off baseline lost one previously found anchor on G-MODE-04 (212 became 211); the changed baseline is preserved in `graph-repeat-diff.json`, not attributed to a new quality improvement. No causal claim about that variation is established. Routing statuses were unchanged across arms. These are AI-assisted development references, not independently scored answers. Browser generation overlapped part of this retrieval run, so its durations are not used for latency claims.

## Performance result and its limits

The serial development workload contained five questions and five document pairs, each repeated twice after first execution of each workflow. Continuous GPU readings and all raw responses are in `workflow-latency.json`.

| Workflow | Warm observations | Observed warm p95 | Proposed target | Main-model failures |
|---|---:|---:|---:|---:|
| Query Desk | 10 | 26.844 seconds | 45 seconds | 0 |
| Change-Impact Brief | 10 | 41.046 seconds | 90 seconds | 0 |

Both timing targets were met in this small run. With ten samples, nearest-rank p95 is the maximum; this is provisional engineering evidence, not a production SLA. First executions took 25.297 and 27.094 seconds respectively and are excluded from the warm figures. They are not automatically labelled fully cold starts.

**All 20 warm responses were marked incomplete.** Two brief completeness reviews were unavailable because the model returned an invalid conflict finding, not because of a timeout. No warning was suppressed to improve these figures. These results establish workflow completion and timing, not materially complete answer quality.

## What is still open

1. A payments reviewer must assess the 11 missed expected passages, all 55 maintained graph anchors and 13 relationships, and the provisional 50-case acceptance pack against originals. The new `retrieval-review-queue.json` includes the missing passages and retrieval-stage evidence; all 11 quotations exist in the current Markdown, but their essentiality is not independently established.
2. Eligibility omissions, attribution and completeness remain quality work. The IPO browser replay retained OC127 and OC71 history, but still withheld another statement. A successful repair on that question is not a general completeness pass.
3. Run reviewed paired graph answers and score the reviewed 50-case benchmark. These runs remain gated on independent expected outcomes. Keep failures as regression cases; do not repeatedly call the same failed cases held-out.
4. Freeze a pilot-approved release only after those gates pass, and repeat affected release checks if code or sources change. The package produced here is an **engineering candidate**, not a pilot-approved release.

The maintained graph remains supported with bounded coverage. Automatic whole-corpus expansion remains not selected. Unlinked eligible documents remain searchable. No GitHub publication or business action was performed.
