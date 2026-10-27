# Engineering candidate evidence — 24 October 2026

Read [engineering closeout](../../docs/ENGINEERING_CLOSEOUT_20261024.md) for results and limitations, and [action register](../../docs/ACTION_ITEMS_20261022.md) for remaining quality/independent-review gates.

- `clean-install.txt`, `clean-acquisition-install.txt`, `clean-tests.txt`: fresh pinned Python environment and 445 passing tests without skips.
- `javascript-tests.txt`: four passing JavaScript suites.
- `fresh-index-rebuild.txt`: complete 14,480-chunk index built from content-addressed cached vectors.
- `recovery.json`, `recovery-run.txt`: model outage, stale graph, negative inputs, actual process interruption, isolated incremental intake, activation and rollback.
- `workflow-latency.json`: 22 actual attempts, raw responses, code/source/model fingerprints and GPU samples. All 20 warm outputs incomplete; timings are not answer-quality scores.
- `graph-comparison.json`: 144 questions, maintained graph on/off, 223/234 versus 211/234 expected passages, 12 gains and zero losses. `graph-repeat-diff.json` retains one graph-off baseline variation compared with the earlier run; graph-on matches it exactly.
- `retrieval-review-queue.json`: 11 remaining missing expected anchors with Markdown context and retrieval stage, awaiting original-source/essentiality review.
- `browser-verification.md`, `browser-*.md`, `browser-*.txt`, `browser-*.png`: actual workflow actions and exports; no independent approval recorded.
- `candidate-verification.json`: packaged file/model/index verification, produced after archive freeze.

Reproduce using [ENGINEERING_START.md](../../ENGINEERING_START.md). Runtime commands:

```powershell
.venv\Scripts\python.exe -X utf8 -m unittest discover -s tests
.venv\Scripts\python.exe -X utf8 evaluation\maintained_graph_eval.py
.venv\Scripts\python.exe -X utf8 evaluation\workflow_latency.py
```

The recovery runner tests configuration activation and rollback; run it **only in a new isolated candidate**, with no other app process accessing that candidate. Its synthetic intake release name is intentionally fixed; create another isolated copy for a repeated run. Local candidate records and installed model weights are excluded from the handoff. Raw JSON timestamps are UTC; this report uses the user's India date.

These are engineering/development checks, not the independently reviewed 50-case acceptance benchmark. Independent graph/source review and material answer completeness remain release dependencies.
