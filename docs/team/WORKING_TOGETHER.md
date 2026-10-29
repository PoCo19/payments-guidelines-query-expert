# Working on the project as a team

Start with [TEAM_START_HERE.md](../../TEAM_START_HERE.md). This guide is for making changes, not for running a live payments service.

## Where things are

| Files or folder | Responsibility |
|---|---|
| `app.py` | Local HTTP application, engine setup, retrieval/generation orchestration |
| `ingestion.py`, `registry.py`, `quality.py` | Chunking, document metadata and source-review handling |
| `context.py`, `adaptive_context.py`, `research.py` | Route selection, candidate/evidence assembly and coverage checking |
| `vector_store.py`, `embedding_cache.py`, `reranker.py` | Vector storage, reusable embeddings and local reranking |
| `graph_context.py`, `pilot/upi_extended_graph_v3.json` | Maintained graph-assisted retrieval and its source-anchored manifest |
| `claim_check.py`, `scope_guard.py`, `claim_repair.py` | Statement support, scope checks and bounded repair |
| `answer_format.py`, `web/answer_format.js` | Validated answer layout and HTML/Markdown rendering |
| `web/` | Browser interface; plain HTML, CSS and JavaScript |
| `work_items.py`, `web/work.*` | Saved answer/change-summary records, history, review and export |
| `local_jobs.py`, `tools/document_pipeline.py` | Local jobs and staged document intake/activation |
| `tests/` | Software regression tests |
| `evaluation/` | Question sets, evaluation runners, saved results and limitations |
| `docs/`, `output/midsem/` | Explanations and the historical submission package |
| `handoff/workbench-20261027/`, `config.workbench.json` | Frozen corrected sources and portable configuration |
| `data/` | Local/restored sources, generated indexes and private work records; not all of it belongs in Git |

Some experimental modules remain in the repository. Their presence does not mean they are active. Check [current flow](PROJECT_FLOW.md) and the configuration before describing a feature as implemented in normal use.

## A small, safe change cycle

1. Agree on a specific problem and how to check the result. Avoid changing retrieval, prompts and UI simultaneously without a reason.
2. From a clean working tree, update `main` and create a branch:

```powershell
git switch main
git pull --ff-only
git switch -c codex/describe-your-change
```

3. Make the change. Add or update a focused regression test when behaviour changes.
4. Run relevant tests and inspect the application. A documentation-only edit usually needs link/command checking rather than a model evaluation.
5. Review `git diff` and `git status`. Add only the intended files. Check that no personal data, credentials, generated indexes or model files are included.
6. Commit, push the branch and open a pull request on GitHub. Explain what changed, why, what you checked and what remains uncertain.

```powershell
git status --short
git diff
git add path/to/the/file-you-changed
git commit -m "Describe the completed change"
git push -u origin codex/describe-your-change
```

Replace the sample branch and file path. Do not paste them unchanged. If Git reports existing local changes or divergent history, preserve the work and discuss it; do not use a force push or reset to make the message disappear.

## Checks for code changes

After completing setup:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-acquisition.txt
.\run.cmd test
node tests\test_answer_format.js
node tests\test_research_view.js
node tests\test_intake_view.js
node tests\test_work_view.js
```

The optional acquisition dependency is needed by parts of the test suite. The real reranker test needs the pinned assets installed by setup. Use the test output's actual counts; do not copy a historical number into a new report.

When modifying retrieval or generation, also preserve representative positive, negative, ambiguous and missing-evidence cases. Record the question set, code commit, source/model fingerprints, settings, latency, warnings and failures. Do not treat a rerun on development cases as a new held-out evaluation.

## Suggested work areas for the five-person group

These are possible ownership areas, not claims about anyone's actual contribution:

- Product flow and usability: test both tasks and saved work and improve explanations.
- Sources and provenance: inspect originals, metadata, extraction and amendments.
- Retrieval and evaluation: study missed evidence and prepare reproducible comparisons.
- Application engineering: maintain persistence, rendering, intake and regression tests.
- Documentation and submission: keep diagrams, report, slides and narration consistent.

People can pair or swap areas. For slides and Word files, coordinate one editor per file at a time; Git cannot reliably merge competing edits to those binary formats. Log actual contributions separately from these suggested roles.

## Shared boundaries

Keep `config.json`, workflow databases, uploaded documents, model weights and generated vectors local. Do not edit the frozen package to hide a failing checksum. Source corrections need original-document verification and a versioned intake release; only affected embeddings should need recomputation.

The immediate quality follow-up is the documented current-versus-historical evidence gap. Independent payments review and the provisional acceptance benchmark are also open. More models, bigger context windows or broader graph expansion should be evaluated against evidence, not added merely because the technology is available.

For current evidence and open decisions, use [PROJECT_STATUS.md](../../PROJECT_STATUS.md) and [the release checks](../../evaluation/release_20261027/README.md). Dated experiment folders preserve history; they are not the current product specification.
