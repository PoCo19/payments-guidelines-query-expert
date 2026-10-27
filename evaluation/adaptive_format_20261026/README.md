# Adaptive formatting checks

Presentation verification only; no independent answer-quality claim.

Closeout on 27 October: `format-final-tests.txt` records 15 passing formatting tests after the last Automatic-style fix; `javascript-tests-final.txt` records all four frontend suites passing again. The full 463-test Python result predates that small fix; the affected formatting suite was rerun afterward. The application was restarted with the final code, and its browser page loaded without console errors. The isolated preview servers were no longer running. No further model-quality run or publication was performed.

- `python-tests.txt`: final 463 tests passed. `python-tests-sandbox-blocked.txt` retains the initial attempt whose localhost HTTP tests were blocked by sandbox socket permissions.
- `javascript-tests.txt`: four suites passed, including cited table rendering, Markdown escaping and preserving human edits.
- `live_check.py`: reproducible development runner using the existing config and corpus. `live-*.json` records seven model attempts across the initial, repeat, schema and simple-comparison runs. Raw generation layouts are included from the repeat onward.
- `*-layout-replay.json`: deterministic presentation replay of previously saved statements/layouts. These are not new model responses. The simple comparison produces `repaired_layout`; other malformed layouts safely fall back.
- `preview.cjs`, `fixture-export.md`, `mixed-format-fixture.png`: clearly labelled synthetic mixed-format presentation fixture. It is not source evidence or model evaluation.
- `browser-replay-item.json`, `workflow-table-citation.png`: isolated Query Desk replay using the saved simple-comparison response plus layout repair. The visible incomplete-answer warning remains; the S8 table citation opened its supporting evidence.
- `workflow-export.md`: HTTP export from the isolated saved item; table structure, cell citations and unapproved Draft status were retained.
- `unchanged-core.json`: application orchestration, retrieval, graph, support-checking and configuration hashes match the earlier snapshot. The workflow module changed only to present the generated layout during export.

All seven live answers were marked incomplete. Several layouts referenced nonexistent statements; earlier schema attempts also placed table fields on prose or used headings subsequently excluded. These failures prompted a discriminated block schema, neutral table headers and narrow repair of phantom prose/list references. Every real draft statement must still occur once; table cells cannot be shifted or invented.

The final browser replay is intentionally isolated in `data/qa26/format-workflows.sqlite3`. No real workflow record was replaced or approved. Query Desk and Change Briefs share the same saved-result renderer and export path. Rich editing of generated table structure is outside this increment; edited prose is kept exactly as saved.
