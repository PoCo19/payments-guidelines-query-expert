# Payments Guidelines Query Expert

Evidence-grounded research for payments teams. Search payment circulars, ask questions with citations, and summarise or compare selected documents while inspecting the original evidence.

**Initial corpus: NPCI circulars; local expansion now includes eight core RBI directions.** The active local library covers multiple NPCI products and the RBI snapshots collected on 9 October 2026. The original 50-case UPI evaluation is preserved; a separate 20-case RBI–NPCI development set now tests broader questions. This is a local research assistant, not an authoritative compliance decision-maker.

## Reproducible colleague handoff

Use the **handoff-2026-10-10.1** Git tag and [step-by-step handoff guide](docs/COLLEAGUE_HANDOFF.md). The source archive includes the NPCI corpus and eight RBI direction snapshots, with hash-checked restoration, portable configuration and saved evaluation records.

## Mid-sem submission

[Submission package and remaining checklist](output/midsem/START_HERE.md) · [Current validation](docs/MIDSEM_VALIDATION.md) · [Project flow](HOW_IT_WORKS.md)

The eight-slide presentation follows the supplied AI/ML sample structure. A three-page report explains module choices, trade-offs, observed findings and future evaluation. Review copies await team identity and contribution details. Recording and portal submission remain pending.

The active local corpus has 1,929 register records, 1,570 searchable documents, 4,834 page records and 14,480 chunks. The eight RBI records use logical HTML-derived text pages, not physical PDF pages. A fresh Git clone includes the frozen source archive; run `handoff.cmd restore` to restore the expanded corpus. Generated release databases remain excluded from Git. It is an imported snapshot, not a live archive mirror. Shared circulars may belong to multiple products.

## Run

Open Ollama, then double-click **run.cmd** in this folder. Open **http://127.0.0.1:8765** and keep the server running. In PowerShell use `.\run.cmd`; no execution-policy change is needed. For a fresh clone, follow [collaboration and setup instructions](CONTRIBUTING.md). Models and vector indexes must be installed or rebuilt locally.

Choose a product or use the Guideline library. Open an exact circular, select **Summarise this circular** or **Add to comparison**, then click **Ask question** (or **Find passages** in Source excerpts mode). Repeated numbers across products/years require disambiguation. Missing pages and unverified metadata remain visible.

Answers now adapt between paragraphs, bullets and mixed layouts while retaining per-claim citations and checking. Leave **Answer style** on Automatic or select a preference. Refresh the browser after upgrading. [Formatting guide](docs/ANSWER_FORMATTING.md).

## Project map

- [Current submissions](output/midsem/START_HERE.md): editable slides, report, PDFs and narration.
- [Collaboration guide](CONTRIBUTING.md): team editing, local setup and checks.
- [Project flow](HOW_IT_WORKS.md): chunking, retrieval, generation and source checks.
- [Architecture](docs/ARCHITECTURE_V05.md): metadata, storage and evidence handling.
- [Evaluation evidence](output/midsem/evidence/README.md): saved cases and measured results.
- [Initial 50-question catalogue](evaluation/INITIAL_50_QUESTIONS.md): exact questions, draft answers, source anchors, saved observations and review guidance.
- [Local RAGAS evaluation](evaluation/RAGAS_EVALUATION.md): capture generated answers, score them with Ollama and review failures.
- [10 October implementation and validation](docs/IMPLEMENTATION_20261010.md): answer budgets, mixed-source evaluation, browser import and remaining findings.
- [20-question RBI–NPCI catalogue](docs/PAYMENTS_EVALUATION_20_CASES.md): questions, exact anchors, draft answers and failure modes.
- [Add documents in the browser](docs/ADDING_DOCUMENTS_QUICKSTART.md): upload, review, build, activate and roll back.
- [Add or revise documents](docs/DOCUMENT_INTAKE.md): staged intake, automatic embedding reuse, validation, activation and rollback.
- [RBI expansion source map](docs/RBI_PAYMENTS_SOURCE_MAP.md): official source map and applicability caveats; eight core directions are integrated locally.
- [Local model comparison](docs/LOCAL_MODEL_OPTIONS.md): hardware-based shortlist and a reproducible timing runner.
- [Topic research across sources](docs/TOPIC_RESEARCH.md): publisher-neutral selection, optional entity context, qualifications and omission checks.
- `web/` and root Python modules: the current RAG application.
- `data/all-products-v1/`: indexed text inputs, raw Markdown and inventory records. Generated vectors and databases are ignored.
- `tests/` and `evaluation/`: regression tests and reproducible evaluations.
- `tools/`: import, index activation and current submission authoring utilities.

Older release copies are preserved in the ignored `.local-archive/` directory on the original machine. They are not needed by colleagues. The separate feature-workflow code is retained for reference and is outside the capstone submission; personal workspaces and uploads are excluded from Git.

## Commands

| Command | Purpose |
|---|---|
| `run.cmd` | Start the local browser app. |
| `run.cmd launch` | Start UPI Feature Workspace V2 on port 8766. |
| `run.cmd test` | Run the automated regression suite, including document intake and model benchmarking. |
| `run.cmd validate` | Validate the expanded candidate, source hashes and retrieval. |
| `run.cmd live-check` | Seven product generation cases and two abstention checks. |
| `run.cmd evaluate` | Historical 12-case retrieval smoke set; not a new-product benchmark. |
| `run.cmd embed` | Rebuild the active vectors/registry after reviewed input changes. |
| `run.cmd reranker` | Verify/download pinned reranker files. |
| `setup.cmd` | Prepare the pinned Python environment on a fresh installation. |
| `ingest.cmd --help` | Add reviewed local PDF/Markdown documents through staged releases. |

The handoff inputs restore to `data/releases/payments-handoff-20261010/`, selected by `config.handoff.json` (also the fresh-clone default). Existing `config.json` overrides the default and is preserved. The original `data/index.json` and page JSONL preserve the prior corpus. Raw copied Markdown does not change retrieval unless structured input is rebuilt. See the import guide before refreshing a dataset or moving reviews between versions.

## Verified scope

The 10 October implementation check discovered 255 Python tests: 251 passed and four optional conversion tests skipped. See [handoff validation](handoff/VALIDATION.md) for the additional packaging checks. Historical NPCI-only checks found 55/55 UPI anchors under an explicit UPI filter; the expanded 20-case evaluation found 18/34 anchors and abstained on 3/3 negatives. These are different datasets and configurations. Neither result establishes answer accuracy; independent review remains pending.

359 register entries remain unavailable/quarantined; two known metadata conflicts are excluded from retrieval. New issue dates are generally unknown, missing pages remain flagged, and new original PDFs are external links. Inference is local; official source links open externally when clicked. The app binds to localhost. No live website synchronization or effective-rule determination is claimed.


## Separate workflow experiment

The UPI Feature Workspace remains available through `run-launch.cmd` on port 8766. Its implementation and stored workspaces are preserved, but it is outside the selected capstone submission. See [V2 product guide](docs/FEATURE_WORKSPACE_V2.md).

### Adding new documents

See [the beginner walkthrough](docs/ADDING_DOCUMENTS_QUICKSTART.md) for the actual eight-document RBI intake, what each stage does, and how embeddings are reused. Full mechanics and rollback are in [document intake](docs/DOCUMENT_INTAKE.md).
