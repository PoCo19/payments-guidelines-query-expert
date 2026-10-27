# Reproduce the 10 October 2026 handoff

For the current Git checkout, use [the 27 October workbench handoff](GITHUB_HANDOFF_20261027.md). This page documents the historical tag and its original source snapshot.

Repository: https://github.com/PoCo19/payments-guidelines-query-expert
Frozen version: **handoff-2026-10-10.1**. Use this tag when comparing results; `main` can move.

This patch tag adds a Windows path-length preflight check to the original `handoff-2026-10-10` release; the source archive and frozen datasets are unchanged.

## What is included

The application, submission files, source snapshot, setup locks and raw evaluation records are versioned together. The snapshot has **1,929 register records, 1,570 searchable documents, 4,834 page records and 14,480 chunks**, including eight RBI directions. The 359 unavailable/quarantined records remain visible. RBI page numbers represent logical HTML-derived text pages, not PDF pagination.

`handoff/payments-20261010/sources.zip` contains the exact indexed inputs, copied Markdown/inventory files, review annotations and RBI HTML/Markdown acquisition records. `manifest.json` records every file's SHA-256, corpus and registry fingerprints, model digests and dependency/dataset hashes. Source review annotations are preserved; **full independent source and answer review is still pending**. This is an imported snapshot, not a current legal consolidation or a live website mirror.

The archive omits generated databases, embeddings, model weights, personal configuration and private uploads. Historical provenance and evaluation records retain original machine paths to document the original run; they are not used as setup instructions. The portable runtime uses relative paths in `config.handoff.json`.

## Fresh installation on Windows

Install Git, **Python 3.12** (with `python` on PATH) and Ollama. Start Ollama. Choose a short checkout folder, such as `C:\work\payments`; long circular filenames can exceed Windows path limits in deeply nested folders. The restore command checks this before writing.

Run these commands in PowerShell, one line at a time (substitute another short writable folder if needed):

```powershell
git clone --branch handoff-2026-10-10.1 https://github.com/PoCo19/payments-guidelines-query-expert.git C:\work\payments
cd C:\work\payments
python --version
.\handoff.cmd restore
.\setup.cmd
ollama pull qwen3.5:9b
ollama pull qwen3-embedding:0.6b
.\handoff.cmd models
.\.venv\Scripts\python.exe app.py embed --config config.handoff.json
.\handoff.cmd verify
.\.venv\Scripts\python.exe app.py serve --config config.handoff.json
```

Open **http://127.0.0.1:8765**. Keep the server window open. After initial setup, only the last command is needed. To work on code, create a branch with `git switch -c your-name/your-change` because checking out the frozen tag starts with a detached HEAD.

`restore` verifies the archive, restores into `data/releases/payments-handoff-20261010`, reconstructs the chunk/registry fingerprints and validates all 20 mixed-source cases' reference anchors. It makes no model calls and leaves existing `config.json` untouched. Re-running it is safe for unchanged inputs; it refuses to overwrite changed source files. `verify` performs the same integrity checks without restoring. Neither command checks answer correctness or claims that vectors exist.

`setup.cmd` installs the pinned Python dependencies and verified reranker assets. `embed` builds all 14,480 vectors on a fresh computer; there is no transferred embedding cache. Allow time for the initial build and keep Ollama running. Without vectors, keyword source search remains available; this is not equivalent to the saved hybrid evaluation.

`models` checks installed Ollama digests against the original capture and checks reranker files. Model tags can change: if it reports a mismatch, do not describe that run as using identical weights. Record the new digest and evaluate it separately. Exact weights may no longer be obtainable through a tag. Model outputs and timings can vary with hardware, caching and runtime versions even when source/model hashes match.

For later document additions through the browser, copy `config.handoff.json` to the ignored `config.json` and start `run.cmd`. Only do this when you have no personal configuration to preserve; the browser intake activates new releases through local configuration. Keep the frozen handoff configuration unchanged for comparisons.

## Verify and evaluate

In another PowerShell window, from the project folder:

```powershell
.\run.cmd test
.\.venv\Scripts\python.exe evaluation\payments_eval.py --config config.handoff.json --mode evidence
.\.venv\Scripts\python.exe evaluation\payments_eval.py --config config.handoff.json --mode generate
```

Each evaluation writes a new timestamped directory under `evaluation/payments_runs/`. Run one model workload at a time. The optional JavaScript tests require Node.js: `node tests/test_answer_format.js` and `node tests/test_research_view.js`. Four conversion tests need the optional `lxml` dependency and otherwise skip; it is not needed to use already-converted sources.

For RAGAS, run `setup-eval.cmd`, then score a capture with `run-eval.cmd score evaluation/payments_runs/<new-run>/capture.json --metrics faithfulness,context_recall`. This can take much longer than retrieval. Consult [the RAGAS guide](../evaluation/RAGAS_EVALUATION.md) before interpreting scores. Automated checking by the generation model is not independent validation.

## Which evidence to read

| Record | Purpose and limits |
|---|---|
| [Original 50 questions](../evaluation/INITIAL_50_QUESTIONS.md) | Frozen UPI development set: 44 positive cases, 6 negatives, 55 source anchors. Historical measurements belong to their recorded corpus/configuration. |
| [20 mixed-source questions](PAYMENTS_EVALUATION_20_CASES.md) | 17 positive cases, 3 negatives, 34 anchors; AI-assisted references awaiting independent review. |
| [Full mixed-source capture](../evaluation/payments_runs/20261010T081610Z/summary.md) | 20/20 requests completed; 18/34 anchors found; 7/17 positive cases found every anchor; 3/3 negatives abstained. Completion is not correctness. Seven positive cases also abstained. |
| [Mixed-source run inventory](../evaluation/payments_runs/README.md) | Identifies usable captures, interrupted attempts and the five-case RAGAS pilot, including timeouts/skips. |
| [Implementation validation](IMPLEMENTATION_20261010.md) | Request budgets, document intake journeys, test results and unresolved limitations. |
| [Handoff validation](../handoff/VALIDATION.md) | Clean-copy verification and exact checks performed for this handoff. |

The original 50-case scores and the new 20-case scores are different experiments; do not combine them into one accuracy number. Saved captures preserve their original code/config hashes and may precede the final display or packaging fixes. Re-run to measure the tagged code. Do not overwrite earlier captures or silently alter frozen question files.

## Colleague workflow

- Presentation/report collaborators start in [output/midsem/START_HERE.md](../output/midsem/START_HERE.md); Python and Ollama are unnecessary for editing those files. Coordinate one editor per PPTX/DOCX and update matching PDFs.
- Code collaborators branch from the tag, run relevant tests and open a pull request. Public visibility allows reading/cloning; direct write access still needs repository collaborator permission, or colleagues can fork and submit a PR.
- Add source documents through the staged intake documented in [ADDING_DOCUMENTS_QUICKSTART.md](ADDING_DOCUMENTS_QUICKSTART.md). Review provenance, extraction and applicability before activation. Private uploads and generated releases stay ignored.
- Record model hashes, configuration, corpus fingerprints and any changed dependencies alongside new evaluation results. Keep answer quality, retrieval quality, latency and human-review status separate.
