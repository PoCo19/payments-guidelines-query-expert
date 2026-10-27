# Payments workbench — engineering candidate

This guide applies to the frozen **24 October archive**, not the latest Git checkout. For the current repository use [the 27 October colleague handoff](docs/GITHUB_HANDOFF_20261027.md).

This package reproduces the local Payments Query Desk and Change-Impact Brief prototypes. It is an engineering candidate, **not an independently accepted payments product**. Graph links, expected answers and material qualifications still need the payments review described in `docs/ACTION_ITEMS_20261022.md`.

## Reproduce this version

1. Extract the complete archive into a short path, for example `C:\work\payments`. Python 3.12 (64-bit) and Ollama are the tested prerequisites.
2. Before changing files, run `python tools\verify_candidate.py`. It verifies packaged file hashes.
3. Run `setup.cmd` to create `.venv` and install the pinned runtime dependencies. The reranker files are included and checked. For all developer tests, also install `requirements-acquisition.txt` in that environment.
4. Start Ollama. Install `qwen3.5:9b` and `qwen3-embedding:0.6b` if missing, then run `.venv\Scripts\python.exe tools\verify_candidate.py --models`. The recorded digests must match; matching tag names alone are insufficient. Model weights are not inside the archive.
5. Run `.venv\Scripts\python.exe -X utf8 app.py embed`. This creates a **new complete Chroma index** from the bundled content-addressed embedding cache. It checks the installed embedding-model digest. The original Chroma index is not shipped.
6. Run `.venv\Scripts\python.exe tools\verify_candidate.py --models --index`, then `run.cmd`. Open `http://127.0.0.1:8765/work`.

All operational paths in the candidate configuration are relative to its folder. Keep the original `config.json` if verifying the frozen candidate; later source/model changes form a new version. The `source_pack` folder contains available local originals; other originals remain linked at their recorded source URLs. An external URL's future availability is outside the local verification.

## What is included

- Current code, source snapshot, maintained graph, source-review annotations, dependency locks and reranker files.
- Verified embedding cache for the same source text and embedding-model digest; a new index must be built locally.
- Development evaluations, engineering verification records and the unscored independent-review pack.
- Available local original PDFs and the retained provenance of other source documents.

Personal workflow databases, synthetic intake/recovery databases, installed environments, Ollama weights and active Chroma indexes are excluded. The older orchestration code is retained for regression compatibility and is not exposed in this workbench navigation. Historical reports retain their original results and paths; use the current engineering closeout for current status.

## Working boundary

Use one app process per workflow database. Inspect source evidence before approving a response. Local reviewer names record attribution, not authentication. Drafts and exports carry review status; changes to sources or model/graph configuration trigger revalidation. Neither workflow sends external replies or changes live transaction controls.

Do not equate a successful startup, passing software tests, or a latency target with correct payments advice. Independent acceptance remains pending. This archive has not been published to GitHub.
