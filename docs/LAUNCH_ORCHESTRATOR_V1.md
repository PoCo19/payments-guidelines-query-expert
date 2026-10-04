# Feature Launch Orchestrator V1 — implementation and operations

Version **1.0.0**, 3 October 2026. The existing Circular Intelligence research app remains **v0.5.1**. These are separate local entry points sharing the imported circular evidence collection.

## Start

Double-click `run-launch.cmd` in the project folder, keep its window open and visit **http://127.0.0.1:8766**. The `.cmd` launcher avoids the PowerShell execution-policy issue encountered with `.ps1` files.

From PowerShell in the project folder:

```powershell
.\run.cmd launch
```

Open Ollama for local AI drafting. The app reads `ollama_url`, `generation_model`, `context_length` and `model_timeout_seconds` from the existing `config.json`. The current configuration uses `qwen3.5:9b`, 16,384 context tokens and a 300-second model timeout. Launch workflows request up to 4,096 output tokens, independently of the research app's answer setting. No model downloads or embedding rebuilds are needed for this V1.

The launch UI offers an explicit template mode when Ollama is unavailable. Fact extraction requires Ollama; manual fact entry works without it. The simulated pilot starts with six manually prepared, cited teaching facts awaiting approval.

The original circular research application still starts with `run.cmd` and uses port **8765**. Its navigation now links to the launch application. Each server must be started separately.

## File map

| Path | Responsibility |
|---|---|
| `launch_app.py` | Loopback HTTP server, routes, model health and lazy evidence-search adapter. |
| `launch_orchestrator/core.py` | Transactional workflow, provenance validation, revisions, reviews, dependencies, job persistence and export. |
| `launch_orchestrator/generation.py` | Team-specific prompts, JSON schemas, source-span selection, Ollama calls, template mode and single queue worker. |
| `launch_orchestrator/demo.py` | Clearly labelled synthetic pilot with facts, partner/control registers and a Risk → BD readiness dependency. |
| `web/launch/` | Browser screens, forms, background refresh and responsive styling. |
| `data/launches/launches.sqlite3` | Default persistent launch database; separate from the research corpus. |
| `tests/test_launch.py` | Workflow, model-contract and HTTP regression tests. |
| `evaluation/live_launch.py` | Opt-in real Ollama validation against a separate synthetic database. |
| `evaluation/browser_launch.cjs` | Full browser workflow against a separate server/database on port 8767. |
| `output/launch-validation/` | Validation reports, screenshots and isolated test databases. These are not the user's launch records. |

## Data model

SQLite stores each launch as a versioned JSON aggregate in `launches`. That aggregate contains the brief, immutable source snapshots, facts, approval, current/archived team deliverables, partners, controls, tasks and launch decision. `events` holds audit entries. `jobs` stores the queue, input snapshots, fingerprints and completion state. Indexed lookups cover launch history and queue state.

Writes use transactions and optimistic revision checking. Every mutation submits the revision the user reviewed; an outdated tab receives a conflict instead of silently overwriting newer work. Connections close after each transaction. WAL mode lets readers continue during short writes. Long model calls happen outside database transactions.

Source snapshots have stable local IDs and SHA-256 content hashes. Circular imports also retain document ID, chunk ID, page, issue date when known, and source URL. Imported text remains an excerpt, not proof of complete circular coverage. New sources do not automatically establish supersession or effective applicability.

## Generation flow

1. The request verifies role responsibility, current revision and the approved feature baseline. Fact extraction instead requires shared source text.
2. The server captures the relevant inputs and a SHA-256 fingerprint. Duplicate active jobs for the same launch/workflow are rejected. The global pending queue is capped at 32 jobs.
3. A single worker claims the next job. BD gets partner records; Risk gets controls. Other teams do not receive those registers. Shared sources and facts reach all teams; team-scoped sources reach their team only.
4. Source paragraphs are divided into exact passages of at most 1,200 characters. Each passage gets an allowed ID. The model selects IDs; Python reconstructs the original quotations. This generation-time passage selection is separate from the existing RAG's page/clause chunking.
5. Ollama returns structured JSON constrained by schemas and permitted fact/passage IDs. Outputs distinguish `source_summary`, `proposal` and `open_question`. A source summary needs at least one fact reference.
6. Python validates structure, lengths, references and exact quotations. Inputs over the 26,000-character workflow ceiling are rejected rather than silently truncated. A model response ending at its token limit is also rejected. The character ceiling is a practical local budget, not an exact tokenizer guarantee.
7. Before saving, the worker compares current inputs and deliverable state with the captured snapshot. Changed inputs/reviews produce `superseded`; prior content remains intact. Valid current results create a draft revision and archive the prior deliverable.
8. Human reviewers edit or approve the draft. Unknowns must be resolved or explicitly dispositioned with a recorded change note. Approval is blocked by unresolved question items/lists and narrow universal-availability/absolute-safety phrase checks.

Fact extraction is additive and deduplicates identical source/quotation/label combinations. It does not replace a reviewed fact silently. Similar facts with different labels may still need manual consolidation. Extracted facts always require fresh product-owner approval.

There is no hidden model fallback or automatic retry loop. Failed jobs expose the error; retry explicitly after correcting the cause. A restart marks previously running jobs `interrupted`; queued jobs resume. Running jobs are not forcibly cancelled from the UI. Stopping the server may leave a local Ollama request finishing in the background; it cannot apply a result after the application process exits.

## Reviews, tasks and change propagation

| Change | Review effect | Completion effect |
|---|---|---|
| Feature brief or new shared source | Clear baseline approval; stale all team drafts. | Reopen completed team tasks and dependent tasks. |
| Fact changed/removed | Clear baseline approval; stale drafts that received it. | Reopen corresponding completed work and dependencies. |
| New fact | Clear baseline approval; stale all team drafts. | Reopen affected completed work. |
| Team-specific source | Stale that team's draft. | Reopen team completion and downstream task dependencies. |
| Partner register | Stale BD draft. | Reopen BD completion and dependents. |
| Control register | Stale Risk draft. | Reopen Risk completion and dependents, including the demo's BD task. |
| Edited/regenerated deliverable | Create draft revision and preserve the previous one. | Reopen its completion evidence and dependent tasks. |
| Reopened prerequisite task | Does not change another team's content. | Reopen downstream completed tasks transitively. |

All facts offered to a team are tracked as dependencies, even if the model cites only some. This conservative policy avoids missed invalidation at the cost of extra review. Task dependencies represent sequencing, not document content dependencies; they are validated for missing IDs and cycles.

Task completion requires an owner, evidence, approved current facts, an approved team deliverable and completed prerequisites. The default four tasks are required gates. The product owner may record a launch decision only when the configured gates pass. Input changes mark an existing decision `requires_review`; they do not erase it. Neither a decision nor an export performs an external launch action.

## Evidence integration and optimisation

The launch evidence picker lazily creates an existing `Engine` with the lexical backend on first search. It applies the UPI product filter and returns up to six passages. It does not open Chroma, rebuild vectors or rewrite the vector registry. Import uses the server's actual chunk contents rather than trusting an edited browser excerpt. The original RAG remains available for richer hybrid search, reranking, summaries and comparisons.

The UI uses no new frontend framework or build chain. One local model serves the specialist roles sequentially. Idle screens poll every three seconds; unsaved forms are preserved when newer revisions arrive. Corpus loading is deferred until needed. No new runtime package is required by the launch server beyond the existing project environment.

## Access and limits

The server binds to `127.0.0.1`, validates Host/Origin, caps JSON request bodies at 128 KiB and uses a restrictive content security policy. Content is escaped in the UI. Model input is evidence, not permission to execute tools. The model has no external action tools.

**The role selector is not authentication.** All launch data is visible to a user who can access this local workspace. Team prompt separation does not make this suitable for confidential multi-user deployment. Reviewer names and completion evidence are self-reported. Audit history is useful application history, not a tamper-proof compliance ledger.

Run one application process per launch database. This is a local prototype with JSON aggregate updates; it is not designed for high-volume multi-user traffic. It has no automatic public-site synchronisation, enterprise permissions, backup scheduler, complete semantic contradiction detector or production fraud-rule engine.

## Backup, recovery and troubleshooting

Stop the launch server before copying the entire `data/launches/` folder to a backup location. Do not copy only the `.sqlite3` file while it is running; WAL data may still be separate. Restore the folder with the server stopped. Keep the existing circular dataset and configuration when moving the project to another computer.

| Symptom | Action |
|---|---|
| Ollama unavailable / model call failed | Start Ollama and check `ollama list` for the configured model; reload the page, then retry. Template mode remains explicit. |
| Input budget exceeded | Create a narrower launch and select only relevant passages. Do not assume a bigger context fixes source relevance. |
| Output token limit reached | Narrow the feature scope or evidence and retry. The incomplete result is not saved. |
| Launch changed / stale revision | Keep your unsaved text separately if needed, then refresh and reapply it to the current revision. |
| Deliverable is stale | Review the changed inputs, reapprove facts if needed and regenerate the affected team draft. |
| Approval blocked by questions | Record a reasoned disposition; update the draft and remove only resolved questions. |
| Task cannot complete | Check current approvals, owner, evidence and prerequisite status. Complete Risk before BD in the simulated pilot. |
| Port already in use | Use the existing server or stop it before starting another. Advanced: `python launch_app.py --port 8768`; update the browser URL. |
| Browser tool/runtime not installed | Normal browser usage still works. Automated browser tests additionally need the documented Playwright runtime and installed Edge. |

For repeatable demonstrations, create a new simulated pilot rather than overwriting previous launch history. See [the demo guide](LAUNCH_DEMO_GUIDE.md) and [validation record](LAUNCH_VALIDATION_V1.md).
