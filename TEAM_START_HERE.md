# Start here: Payments Guidelines Query Expert

This guide is for teammates joining the project for the first time. You do not need to understand the code before reading it.

We are building a local research assistant for people working with payment guidelines. It finds relevant document passages, uses a language model to explain them, and attaches citations so a person can check the evidence. The current documents are NPCI circulars and eight RBI direction snapshots. The intended product scope is broader payments research.

**Current status: a development build for collaboration.** The software has been tested, but its answers are not independently accepted as reliable payments advice. A recent broad UPI Lite question returned historical limits despite a later amendment being available in the library. That failure is documented, not treated as solved.

## Read in this order

| Guide | What you will learn | Approximate reading time |
|---|---|---|
| [Project flow](docs/team/PROJECT_FLOW.md) | What we built, how documents become answers, and why each module exists | 10 minutes |
| [Concepts in plain language](docs/team/CONCEPTS.md) | RAG, embeddings, Chroma, reranking, graph links, citations and evaluation | 8 minutes |
| [How to run](HOW_TO_RUN.md) | First-time Windows setup, everyday startup and troubleshooting | 10 minutes; downloads/indexing take additional time |
| [Using the application](docs/team/USING_THE_APP.md) | Ask & Research, Query Desk, Change Briefs and the meaning of review | 8 minutes |
| [Working together](docs/team/WORKING_TOGETHER.md) | Where the code lives, how to make a change, and how to report a failure | 8 minutes |

You can read the guides and work on the presentation/report without installing models. Running the complete assistant requires the local runtime and model setup. Each teammate's computer must build its own vector index; the repository does not contain model weights or private saved work.

## Three tasks the user can perform

**Ask & Research:** explore a question, inspect original wording, summarise a document or compare selected sources.

**Query Desk:** keep a question and its answer, inspect evidence, refine the wording, and export the saved response. Human sign-off is optional.

**Change Briefs:** compare a document with selected earlier sources, inspect documented findings, and separately record possible actions and unresolved questions. It does not decide what a bank must implement automatically.

These tasks share one RAG engine. They are not three independently trained models.

## What to say when explaining the project

> We use pretrained local models to retrieve and explain payment guidelines with source attribution. Our current corpus covers NPCI and selected RBI snapshots. The system includes hybrid retrieval, bounded graph assistance, evidence checks and two saved-work workflows. Human review and independent evaluation remain necessary, especially for current limits, applicability and amendments.

Do not claim that the project knows every current rule, that Graph RAG covers every document relationship, or that passing software tests proves the answers are correct.

## Where to find the current version

Use GitHub `main` and record the commit with `git rev-parse HEAD`. Follow [HOW_TO_RUN.md](HOW_TO_RUN.md), which uses `config.workbench.json` and the 27 October source package. Older dated guides and the mid-sem slides are retained as historical records; their counts, limitations and startup paths may describe earlier versions.

For exact evidence, see [current project status](PROJECT_STATUS.md), [the source handoff](docs/GITHUB_HANDOFF_20261027.md), and [additional checks and known failures](evaluation/release_20261027/README.md).
