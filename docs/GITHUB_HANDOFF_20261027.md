# Current colleague handoff — 27 October 2026

This is a **development build for collaboration**, not a production-ready or independently accepted payments advisor. It includes Ask & Research, Query Desk, Change Briefs, maintained graph-assisted retrieval and adaptive answer presentation. The separate orchestration experiment is retained but outside the workbench flow.

## Fresh checkout

Use a short path such as `C:\work\payments` because source filenames can exceed Windows path limits in deeply nested folders. Install Python 3.12, Git and Ollama first.

```powershell
git clone https://github.com/PoCo19/payments-guidelines-query-expert.git C:\work\payments
cd C:\work\payments
.\setup.cmd
.\.venv\Scripts\python.exe tools\handoff.py restore --workbench
ollama pull qwen3.5:9b
ollama pull qwen3-embedding:0.6b
.\.venv\Scripts\python.exe tools\handoff.py models --workbench
.\.venv\Scripts\python.exe app.py embed --config config.workbench.json
.\.venv\Scripts\python.exe tools\handoff.py verify --workbench
.\.venv\Scripts\python.exe app.py serve --config config.workbench.json
```

`setup.cmd` also downloads the pinned reranker; it does not install Ollama model weights. The source package contains no vectors: `embed` builds the local index. Without it, do not describe keyword retrieval as equivalent to the hybrid results.

Open `http://127.0.0.1:8765/work` for the workbench or `/` for exploratory research. The local model service must remain running. Model tags can change: the model verification command checks digests against the package, not just names.

Use `config.workbench.json` for this frozen source release. For browser-based source intake, first copy it to the ignored `config.json` only if you have no personal configuration to preserve, then use `run.cmd`. Neither restore nor verification replaces existing personal configuration or modified source files.

## What is shared

- Current application code, frontend, tests and documentation.
- `handoff/workbench-20261027/sources.zip`: the corrected indexed source snapshot, Markdown, metadata and retained RBI acquisition provenance.
- Matching maintained graph in `pilot/upi_extended_graph_v3.json`; its hash is pinned with the source package. Automatic whole-corpus graph expansion remains not selected.
- Development evaluations, source-repair audit records and the provisional independent-review pack. Historical observations retain their original dates, configuration paths and limitations.

Private workflow databases, personal configuration, QA servers/databases, environments, embeddings, model weights and generated whole-corpus graph candidates stay local. Available original PDFs are not all bundled; use the documented source URLs and acquire missing originals for independent review. Indexed Markdown alone is not proof of complete original-source extraction.

The 10 October source handoff and 24 October engineering archive remain historical snapshots. Their setup instructions do not describe this current Git checkout. The large engineering ZIP is not published here.

## Additional checks and known issue

The additional 27 October smoke cases rejected gibberish, an unrelated cooking question and an invented circular without claims. The IPO response retained the cumulative-versus-single-mandate distinction and OC127 context. These observations are development evidence, not independent acceptance.

**Open regression:** “What is UPI Lite? Answer briefly.” returned 2023 transaction/balance figures without distinguishing them from later provisions. The indexed OC169A dated 27 February 2025 contains different UPI Lite limits and separates UPI Lite X. That newer evidence was absent from this answer's retrieved context. Its automated completeness check was unavailable. Do not rely on this build for unattended current-limit advice. The saved record is `evaluation/release_20261027/short_explanation.json`; this finding has not been hidden or scored as a quality pass.

Human source/graph review, benchmark scoring and resolution of answer-quality failures remain open. Optional in-product human sign-off is separate from those evaluation tasks. No external replies or transaction-rule changes are automated.

## Development checks

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-acquisition.txt
.\run.cmd test
node tests\test_answer_format.js
node tests\test_research_view.js
node tests\test_intake_view.js
node tests\test_work_view.js
```

Use a branch for collaboration, record the commit used for each experiment, and keep the frozen source/config files unchanged when comparing results. See `evaluation/release_20261027/README.md` for the publication checks and their limits.

The clean-source checkout passed 465 Python tests and four JavaScript suites using the existing pinned test environment and hash-verified reranker assets. Restoration reproduced the source/registry fingerprints, 14,480 chunks and 20 existing case anchors, and validated the maintained graph. This check did not repeat a fresh dependency installation or build all embeddings.
