# Payments Guidelines Query Expert

Evidence-grounded research for payments teams. Search payment circulars, ask questions with citations, and summarise or compare selected documents while inspecting the original evidence.

**Initial corpus: NPCI circulars.** The implemented dataset covers multiple NPCI products. Preliminary evaluation focuses on UPI; other payment networks and regulatory sources remain future extensions. This is a local research assistant, not an authoritative compliance decision-maker.

## Mid-sem submission

[Submission package and remaining checklist](output/midsem/START_HERE.md) · [Current validation](docs/MIDSEM_VALIDATION.md) · [Project flow](HOW_IT_WORKS.md)

The eight-slide presentation follows the supplied AI/ML sample structure. A three-page report explains module choices, trade-offs, observed findings and future evaluation. Review copies await team identity and contribution details. Recording and portal submission remain pending.

The current corpus has 1,921 register records, 1,562 searchable documents, 4,826 page records and 14,060 chunks. It is an imported snapshot, not a live archive mirror. Shared circulars may belong to multiple products.

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
| `run.cmd test` | Run all 170 automated tests (103 research + 2 evaluation metrics + 65 separate workspace tests). |
| `run.cmd validate` | Validate the expanded candidate, source hashes and retrieval. |
| `run.cmd live-check` | Seven product generation cases and two abstention checks. |
| `run.cmd evaluate` | Historical 12-case retrieval smoke set; not a new-product benchmark. |
| `run.cmd embed` | Rebuild the active vectors/registry after reviewed input changes. |
| `run.cmd reranker` | Verify/download pinned reranker files. |
| `setup.cmd` | Prepare the pinned Python environment on a fresh installation. |

Active inputs are in `data/all-products-v1/`, selected by `config.json`. The original `data/index.json` and page JSONL preserve the prior corpus. Raw copied Markdown does not change retrieval unless structured input is rebuilt. See the import guide before refreshing a dataset or moving reviews between versions.

## Verified scope

103 tests pass. Both evaluated retrieval modes retain 55/55 UPI anchors under an explicit UPI filter. Product-isolation checks cover all 12 groups. Seven live product examples and two negative cases were exercised. These are developer checks, not expert answer-accuracy scores or a guarantee of zero defects.

359 register entries remain unavailable/quarantined; two known metadata conflicts are excluded from retrieval. New issue dates are generally unknown, missing pages remain flagged, and new original PDFs are external links. Inference is local; official source links open externally when clicked. The app binds to localhost. No live website synchronization or effective-rule determination is claimed.


## Separate workflow experiment

The UPI Feature Workspace remains available through `run-launch.cmd` on port 8766. Its implementation and stored workspaces are preserved, but it is outside the selected capstone submission. See [V2 product guide](docs/FEATURE_WORKSPACE_V2.md).
