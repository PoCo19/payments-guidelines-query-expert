# Start here: Payments Guidelines Query Expert

This guide is for teammates joining the project for the first time. You do not need to understand the code before reading it.

We are building a local research assistant for people working with payment guidelines. It finds relevant document passages, uses a language model to explain them, and attaches citations so a person can check the evidence. The current documents are NPCI circulars and eight RBI direction snapshots. The intended product scope is broader payments research.

**Current status: a supervised development prototype.** The 28 October product-clarity increment simplifies the product and fixes a demonstrated context-selection gap. Generated answers still need source inspection; independent acceptance is pending. See the [current verification and limitations](docs/PRODUCT_MATURITY_20261028.md).

## Read in this order

| Guide | What you will learn | Approximate reading time |
|---|---|---|
| [Project flow](docs/team/PROJECT_FLOW.md) | What we built, how documents become answers, and why each module exists | 10 minutes |
| [Concepts in plain language](docs/team/CONCEPTS.md) | RAG, embeddings, Chroma, reranking, graph links, citations and evaluation | 8 minutes |
| [How to run](HOW_TO_RUN.md) | First-time Windows setup, everyday startup and troubleshooting | 10 minutes; downloads/indexing take additional time |
| [Using the application](docs/team/USING_THE_APP.md) | The two tasks, saved work and optional human sign-off | 8 minutes |
| [Working together](docs/team/WORKING_TOGETHER.md) | Where the code lives, how to make a change, and how to report a failure | 8 minutes |

You can read the guides and work on the presentation/report without installing models. Running the complete assistant requires the local runtime and model setup. Each teammate's computer must build its own vector index; the repository does not contain model weights or private saved work.

## Two tasks, one shared evidence engine

**Ask a question:** explain a requirement, summarise or compare documents, then inspect citations. Save a useful answer without generating it again.

**Understand a change:** choose the document to investigate, confirm earlier/comparison sources, and generate a cited summary of changes, conditions and unresolved points.

**Saved work** is where both results live. You can reopen, edit, export, archive or restore them. Human sign-off and History are optional supporting controls, not another AI task.

Use the [six-minute demonstration](docs/team/DEMONSTRATION.md) to explain the distinction to the group.

## What to say when explaining the project

> We use pretrained local models to retrieve and explain payment guidelines with source attribution. Our current corpus covers NPCI and selected RBI snapshots. The system includes hybrid retrieval, bounded graph assistance, evidence checks and two tasks with optional saved work. Human review and independent evaluation remain necessary, especially for current limits, applicability and amendments.

Do not claim that the project knows every current rule, that Graph RAG covers every document relationship, or that passing software tests proves the answers are correct.

## Where to find the current version

Use GitHub `main` and record the commit with `git rev-parse HEAD`. Follow [HOW_TO_RUN.md](HOW_TO_RUN.md), which uses `config.workbench.json` and the 27 October source package. Older dated guides and the mid-sem slides are retained as historical records; their counts, limitations and startup paths may describe earlier versions.

For exact evidence, see [current project status](PROJECT_STATUS.md), [the source handoff](docs/GITHUB_HANDOFF_20261027.md), and [additional checks and known failures](evaluation/release_20261027/README.md).
