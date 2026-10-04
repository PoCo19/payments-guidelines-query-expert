# Multi-product operations and rollback

Current release: **all-products-v1**, selected by `config.json`. Run all commands in the project folder. Ollama is needed for neural indexing, hybrid search and generated answers.

## Use the installed release

Start Ollama, then double-click `run.cmd`. Open http://127.0.0.1:8765. No import or embedding rebuild is needed on every launch. In PowerShell use `.\run.cmd`, avoiding the `run.ps1` execution-policy issue.

Useful checks:

```powershell
.\run.cmd test
.\run.cmd validate
.\run.cmd live-check
```

Validation checks the configured **candidate** in `config.products.json`; the running application reads **active** `config.json`. They currently point to the same release. Stop the app before any rebuild; restart afterward. An accepted source review is stored in the active dataset, then applied on rebuild:

```powershell
.\run.cmd embed
.\run.cmd
```

## What the files contain

| Path | Purpose |
|---|---|
| `config.json` | Active runtime settings and dataset path. |
| `config.products.json` | Candidate configuration used for build validation/activation. |
| `data/all-products-v1/index.json` | Canonical documents, source listings, memberships and availability. |
| `data/all-products-v1/all_circular_pages.jsonl` | Page text, blank-page records and extraction provenance. |
| `data/all-products-v1/sources/` | Local copies of all 1,619 Markdown sources and inventory JSONs. |
| `data/all-products-v1/source_manifest.json` | SHA-256 checksums for 1,631 Markdown/inventory source files. |
| `data/all-products-v1/review_annotations.json` | Current source-hash-bound review overlays. |
| `data/all-products-v1/feature_rules.json` | 18 heuristic product-scoped categories. |
| `data/all-products-v1/chroma/`, `registry/` | Generated vector and SQLite snapshots. |
| `data/all-products-v1/embedding_build.json` | Actual vector build counts, model digest and timing. |
| `data/embedding_cache.sqlite3` | Reusable vectors keyed by exact text/model identity. |
| `data/index.json`, `data/all_circular_pages.jsonl` | Preserved original corpus, not current input. |
| `versions/v0.4.0/` | Preserved code/config/UI/documentation for rollback. |
| `reports/v05_*.json`, `reports/v05_unit_tests.txt` | Validation evidence. |

`corpus.json` describes the import build. Its `staged_not_active` value is the status when built; **config.json is the authority for which dataset is active**. Do not infer the live server state from an immutable import manifest.

## Reproduce an import in a fresh release directory

Do not overwrite `all-products-v1`. The importer refuses an existing destination. Example:

```powershell
.venv\Scripts\python.exe -X utf8 tools/import_products.py --source 'C:\Users\Admin\Downloads\circulars' --destination data/all-products-v2
.venv\Scripts\python.exe -X utf8 app.py embed --config config.products.json
.\run.cmd test
.\run.cmd validate
.\run.cmd live-check
.venv\Scripts\python.exe -X utf8 tools/activate_corpus.py
```

The importer is designed for the inspected inventory schema and builds on the preserved v0.4 baseline. Before a future refreshed pack, review changed schemas, source conflicts and any **new v0.5 review annotations**: they are not automatically migrated into a fresh import. Tests include fixed v1 counts and fixtures; update those deliberately for a genuinely new dataset rather than treating changed counts as proven correctness. The illustrative v2 command is not an unattended update mechanism. A failed `.building` directory is retained for inspection; choose another release name rather than deleting evidence blindly.

After activation, restart the application and confirm the library count and neural index Ready status under Project notes. Directly editing a Markdown copy does not update the structured page input or existing vectors.

## Restore the previous dataset

Stop the running server first. Then:

```powershell
.venv\Scripts\python.exe -X utf8 tools/activate_corpus.py --rollback
.\run.cmd
```

This restores the preserved v0.4 configuration and corpus using compatible current code; it does not remove v0.5 data or reviews. The preserved index is checked before switching. To return to v0.5, run the activation command without `--rollback`, then restart. Source changes require fresh validation/live reports before activation.

For complete code rollback, the v0.4 snapshot is under `versions/v0.4.0/`; keep any newer work backed up before restoring files. No rollback command deletes a corpus.

## Review priorities

Resolve the two quarantined metadata/body conflicts against original PDFs; review the UPI 76B candidate; obtain missing originals; repair empty/thin extraction and ZIP annexures; verify issue dates; then build a product-balanced, independently reviewed evaluation set. Same-title/text similarity does not prove that two circulars are the same or one supersedes the other.
