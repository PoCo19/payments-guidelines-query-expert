# V2 implementation and maintenance

Release: **UPI Feature Workspace 2.0.0**, 3 October 2026. Built on the V1 transaction/review engine and the existing Circular Intelligence corpus.

## Current files

| File | Responsibility |
|---|---|
| `launch_app.py` | Loopback server, V2 assets, upload preview, evidence adapter, CRUD/job routes. |
| `launch_orchestrator/core.py` | Revisions, approvals, rule records/assessments, next-step selection, deletion, atomic batch queue and change propagation. |
| `launch_orchestrator/generation.py` | Mode-aware specialist prompts, exact source-span selection, structured rule assessment and worker. |
| `launch_orchestrator/documents.py` | Bounded text preview for Markdown/text, DOCX and text-bearing PDF. |
| `launch_orchestrator/demo.py` | V1 legacy fixture plus the V2 existing-feature example. |
| `web/launch/index_v2.html`, `app_v2.js`, `style_v2.css` | Current interface, served at `/`, `/app.js` and `/style.css`. Earlier assets remain V1 reference files. |
| `tests/test_launch_v2.py` | Workspace modes, deletion, rule provenance/assessment, migration and upload checks. |
| `evaluation/browser_launch_v2.cjs` | Isolated full UI journey in installed Edge. |
| `evaluation/live_launch_v2.py` | Isolated real Ollama checks for all five workflows. |

## Data changes and compatibility

Launch aggregates now include `workspace_type` (`existing`, `change`, `new_launch`) and `risk_rules`. Reads supply defaults for V1 records: `new_launch` and an empty transaction-rule register. Existing facts, reviews, task titles, controls and archived drafts are preserved. Legacy control notes are context, not transaction rules; the system does not manufacture structured rules from them.

The default database remains `data/launches/launches.sqlite3`. Before implementation, the V1 code and an online SQLite backup were saved in `backups/launch-v1-20261003/`. Backups contain only the state at their recorded creation time, not subsequent edits. A rollback to V1 should use the matching code and database backup; do not assume an older UI fully understands V2 rule data.

## Transaction-rule contract

Each rule contains stable ID, name, feature scope, condition, action, owner, reported status, source ID/quotation and a verification note. Rules are limited to 20 per workspace to keep assessment focused. Conditions are text for analysis, never executable code.

Non-proposed rules require a quotation matching an allowed shared/Risk source. An active status cannot cite only a source classified as public; it also requires a configuration/deployment note. Source classification and status are user assertions, not independently certified provenance.

The Risk model response uses a schema keyed by every supplied rule ID. Python normalises it into assessments and verifies exact coverage with no unknown/duplicate IDs. An assessment records applicability, recommendation, rationale and proposed change. Saving a human-edited risk draft applies the same coverage checks. Rule changes invalidate Risk content and reopen relevant completed actions; ordinary task dependencies do not incorrectly invalidate other teams' unchanged documents.

## Orchestration and deletion

`POST /api/launches/{id}/prepare` queues all four team jobs in one SQLite transaction. It requires product-owner responsibility, current revision, an approved brief and no existing active workspace job. Partial batches are not committed. The existing single worker executes jobs sequentially.

Every job retains its input snapshot and fingerprint. The result is applied only to the matching current input/review state. Result application checks job existence/state first, so deleting a workspace while a call is running cannot recreate its data. Deletion checks the current revision and exact workspace-name confirmation, then removes launch, event and job rows atomically. It does not delete corpus files, exported packs or backups, and does not forcibly cancel Ollama's in-flight computation.

Next-step routing is computed from actual sources, brief approval, team draft state, task prerequisites and final review state. The UI links to real views and can open the relevant action editor. Modal/form errors retain values, receive focus and appear beside their owning controls. Unsaved forms are protected from polling and navigation.

## Upload boundaries

Uploads are JSON/base64 requests to `/api/extract-document`. The route accepts at most 7 MiB of request data and a 5 MiB decoded file; normal requests remain limited to 128 KiB. Uploaded binaries are not retained. A preview does not save a source until the user adds it.

UTF-8 text/Markdown is decoded directly. DOCX extraction reads bounded `word/document.xml`, rejects entity declarations and collects paragraph/table text. PDF extraction uses pinned `pypdf==6.10.0`, rejects encrypted PDFs and limits the document to 60 pages. There is no OCR. Layout, tables, reading order and embedded images still need source review. The first 24,000 extracted characters are returned with an explicit truncation flag; for very large PDFs extraction stops after sufficient preview text, so its character count is not a full-document total.

The combined model input budget remains 26,000 characters, with a 16,384-token context in the current configuration and up to 4,096 output tokens. This character budget is a practical bound, not an exact tokenizer guarantee. Oversized inputs/output truncation fail visibly rather than saving partial drafts.

## Safety and operating scope

The server remains loopback-only with Host/Origin checks, allowlisted static files and a content security policy. Uploaded/model text is escaped in the UI. The model has no external action tools. It cannot deploy risk rules or send communications.

This remains a local single-user course prototype. Role selection is not authentication; all local workspace content is accessible to the local user. Audit records and evidence are not tamper-proof attestations. There is no live transaction feed, production rule-engine connection, effective-rule determination or independent domain approval. Those require separate operational design and validation.

Use `setup.cmd` to recreate pinned dependencies, `run.cmd launch` to start the workspace and `run.cmd test` for all Python tests. The browser test also needs the bundled Playwright package and installed Edge; the live model test needs Ollama and the configured model. Reports go to `output/launch-v2/` with isolated test databases. See [validation](V2_VALIDATION.md) for measured results.
