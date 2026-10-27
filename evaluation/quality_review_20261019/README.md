# Quality cycle records: 19–20 October 2026

Read [the narrative report](../../docs/QUALITY_CYCLE_20261019.md) first. This is a development quality cycle, not a release acceptance certificate.

- `closure_manifest.json`: final code fingerprints, unchanged config/corpus checks and completion boundaries.
- `before/`: pre-cycle root Python snapshots; `final_code/`: final root Python and evaluation/test scripts, preserving relative paths. These are reference snapshots, not a separate runnable installation.
- `production.patch`: the three changed production modules relative to the pre-cycle snapshots.
- `retrieval_summary.json`: paired 144-case result: 220/234 to 223/234 source anchors, three gains, no losses.
- `final_live_summary.json`: ten live cases, 19/19 anchors, six model timeouts. This run did not pass generation verification.
- `human_review_final.csv`: the first ten-case run with six timeouts. `human_review_rerun.csv` and `rerun_live_summary.json`: the final-code repeat after GPU memory became available, with no generation fallback but remaining answer/reviewer issues. Reviewer judgements are deliberately blank. `human_review.csv` is the earlier five-case run. Do not mix these captures.
- `regression-tests-closed.txt`: final 399-test pass. Earlier test logs retain their original counts.
- `repair-regression-before.txt`, `combined-repair-before.txt`: reproduced failures before targeted fixes.
- `frontend-tests.txt`: all three JavaScript suites passed; this does not replace a browser journey.
- `generation_experiment_decision.json`: why extra generation instructions were rejected.
- `gpu-load-20261020.txt`, `resident-models-20261020.json`: read-only runtime snapshots following live failures. Ollama logs preserve request timing/cancellation evidence. Concurrent game presence was observed; its causal contribution was not isolated.

Raw timestamped captures are linked in the narrative report. The first ten-case coverage attempt stopped after one baseline output. The completed repeat is summarised in `coverage_challenge_summary.json`: the experimental reviewer reduced false warnings but missed four of five provisionally labelled gaps, so it was not promoted. No source repair, embedding rebuild, model/config change, server restart or GitHub push was part of this cycle.
