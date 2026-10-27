# Payments Guidelines Query Expert

Evidence-grounded research for payments teams. Search payment circulars, ask questions with citations, and summarise or compare selected documents while inspecting the original evidence.

**Initial corpus: NPCI circulars; local expansion now includes eight core RBI directions.** The active local library covers multiple NPCI products and the RBI snapshots collected on 9 October 2026. The original 50-case UPI evaluation is preserved; a separate 20-case RBI–NPCI development set now tests broader questions. This is a local research assistant, not an authoritative compliance decision-maker.

## Payments Research Workbench

Automatic answer style now supports optional evidence tables alongside prose and lists. Formatting is preserved in unedited saved answers and exports, with citations and existing warnings. [Adaptive presentation and its limits](docs/ADAPTIVE_ANSWER_PRESENTATION_20261026.md).

Open `/work` for the overview, Query Desk and Change Briefs. Ask & Research remains at `/`. The [25 October implementation guide](docs/WORKBENCH_PRODUCT_20261025.md) explains the guided flows, source-preserving handoff, review states and recovery controls. Verification records: [product checks](evaluation/workbench_product_20261025/README.md). These workflows remain supervised; independent answer acceptance is pending.

**26 October interface clarification:** answers, edits and evidence exports are the main flow. Human sign-off is optional and collapsed; History retains earlier snapshots. In-product sign-off is separate from the 50-case benchmark and independent evaluation. [What each check means](docs/REVIEW_CLARITY_20261026.md).

## Reproducible colleague handoff

**Current GitHub development build:** use the [27 October colleague handoff](docs/GITHUB_HANDOFF_20261027.md) and `config.workbench.json`. It packages the corrected source snapshot with the maintained graph and current workflows. [Additional tests and open quality findings](evaluation/release_20261027/README.md) include a broad UPI Lite question that returned historical limits; this is not a production-ready release.

**Frozen engineering candidate (24 October; predates the interface increment):** Payments Query Desk and Change-Impact Briefs support saved drafts, source inspection, versioned human review and evidence exports. [Engineering verification](docs/ENGINEERING_CLOSEOUT_20261024.md) passed 445 Python tests, four JavaScript suites, isolated installation/rebuild/recovery and browser checks. [Portable engineering candidate setup](ENGINEERING_START.md) includes matching sources, graph, cached embeddings and evaluation records. It is not a pilot-approved release: all 20 warm latency responses remained marked incomplete, and independent payments acceptance is pending.

The maintained graph remains a supported bounded retrieval component; automatic whole-corpus expansion is not selected. Retrieval development evidence does not establish answer correctness.

The corrected OC185B passage is searchable in the active OCR-audit source release and the 27 October workbench handoff. [Historical source repair](docs/SOURCE_REPAIR_AND_GRAPH_DECISION_20261014.md). No additional source or embedding changes were made for the workflow implementation. The older Git tag below predates the workflows; use the current colleague guide for the latest checkout.

Use the **handoff-2026-10-10.1** Git tag and [step-by-step handoff guide](docs/COLLEAGUE_HANDOFF.md). The source archive includes the NPCI corpus and eight RBI direction snapshots, with hash-checked restoration, portable configuration and saved evaluation records.

## Mid-sem submission

[Submission package and remaining checklist](output/midsem/START_HERE.md) · [Current validation](docs/MIDSEM_VALIDATION.md) · [Project flow](HOW_IT_WORKS.md)

The eight-slide presentation follows the supplied AI/ML sample structure. A three-page report explains module choices, trade-offs, observed findings and future evaluation. Review copies await team identity and contribution details. Recording and portal submission remain pending.

The active local corpus has 1,929 register records, 1,570 searchable documents, 4,834 page records and 14,480 chunks. The eight RBI records use logical HTML-derived text pages, not physical PDF pages. A fresh Git clone includes the frozen source archive; run `handoff.cmd restore` to restore the expanded corpus. Generated release databases remain excluded from Git. It is an imported snapshot, not a live archive mirror. Shared circulars may belong to multiple products.

## Run

Open Ollama, then double-click **run.cmd** in this folder. Open **http://127.0.0.1:8765** and keep the server running. In PowerShell use `.\run.cmd`; no execution-policy change is needed. For a fresh clone, follow [collaboration and setup instructions](CONTRIBUTING.md). Models and vector indexes must be installed or rebuilt locally.

Open **Payments workbench** in the navigation for Query Desk and Change-Impact Briefs.

Choose a product or use the Guideline library. Open an exact circular, select **Summarise this circular** or **Add to comparison**, then click **Ask question** (or **Find passages** in Source excerpts mode). Repeated numbers across products/years require disambiguation. Missing pages and unverified metadata remain visible.

Answers now adapt between paragraphs, bullets and mixed layouts while retaining per-claim citations and checking. Leave **Answer style** on Automatic or select a preference. Refresh the browser after upgrading. [Formatting guide](docs/ANSWER_FORMATTING.md).

## Project map

- [Current submissions](output/midsem/START_HERE.md): editable slides, report, PDFs and narration.
- [Collaboration guide](CONTRIBUTING.md): team editing, local setup and checks.
- [Project flow](HOW_IT_WORKS.md): chunking, retrieval, generation and source checks.
- [Supported graph and supervised workflows](docs/SUPERVISED_WORKBENCH_20261020.md): current decision, review states, intake validation and remaining gates.
- [Historical graph experiment](docs/GRAPH_PILOT_EXTENDED_20261014.md): original 40-case comparison and limitations.
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


### Graph-assisted evidence retrieval

The active local app includes bounded graph expansion for the supported UPI circular families, within Related context. Unrelated queries, strict searches and selected-document operations retain their existing paths. This improves access to linked evidence; it does not guarantee correct interpretation. See [integration, validation and rollback](docs/GRAPH_INTEGRATION_20261016.md). The older colleague handoff snapshot remains unchanged until a new source package is prepared.
