# Payments Research Workbench — product implementation, 25 October 2026

**26 October wording update:** [Answers, human sign-off and evaluation](REVIEW_CLARITY_20261026.md) describes the current interface. Human sign-off is optional, review marking does not send a notification, and saved revisions are shown inside History. The implementation record below retains its original terminology.

## Outcome and scope

The existing research assistant now has a clear product entry point at `/work`, with three distinct tasks. This increment improves how users create, inspect, retain and review work. It does not change retrieval ranking, graph expansion, generation prompts in the RAG engine, model selection, embeddings or source content.

| Area | Use it for | Result |
|---|---|---|
| Ask & Research | Explore a question, summarise a document, compare sources | An exploratory answer with inspectable evidence |
| Query Desk | Prepare a response for a payments team | A saved, versioned response with review status and evidence export |
| Change Briefs | Investigate a selected document against a confirmed baseline | Cited findings, analyst classifications, proposed actions and open questions |

The normal research URL `/` is retained. Overview and both workflows are linked from its navigation. The standalone cross-functional orchestration application is unchanged.

## Implemented flows

### Query Desk

1. Define the question, optional product, issue-date cutoff, audience and operating context.
2. Optionally select up to six source documents; otherwise use eligible library evidence.
3. Confirm the request, save it, and generate a cited draft.
4. Read the answer, select citations to inspect evidence, and open extracted pages or the original document link.
5. Edit and save a new version, send it for review, and export the response with evidence and review history.

An existing cited answer in Ask & Research can be saved directly to Query Desk. The server copies the completed local job's answer, source excerpts, warnings, source/model/graph snapshot and original retrieval settings. It does not regenerate an answer at handoff or accept browser-supplied evidence. Stale snapshots, absent jobs and non-answer results are rejected. The job cache is bounded to 50 jobs and one server session: save useful answers before restarting the app. Once saved, work items persist in SQLite.

Regenerating an imported item preserves the original retrieval filters and settings while applying its revised question/product. The original settings are available in request details and export. Audience and operating context are saved for the analyst; they do not silently become model instructions or independently established institutional facts.

### Change Briefs

1. Define the change question and optional scope/context.
2. Select the document under investigation first, then at least one comparison source (six selected documents maximum).
3. Inspect suggested related documents and explicitly confirm the baseline.
4. Generate documented findings using the existing comparison path.
5. Inspect source evidence. Optionally classify accepted generated findings as a documented change, retained requirement or unresolved finding.
6. Record analyst-proposed actions and open questions separately from documented requirements; save, review and export.

Related-source suggestions use existing resolved references and numbering families, with reasons and chronology labels. Unknown dates remain unknown; later documents are explicitly labelled later. Suggestions are bounded to 30 and are not a complete applicability graph. Manual library search remains available across publishers. Neither suffixes nor references establish supersession. Search displays up to 30 converted matches; narrow the title/reference to find a specific document.

Finding classifications are analyst annotations, not automated legal conclusions. They identify immutable generated claims. Editing the answer text clears the labels so classifications cannot silently transfer to different prose. Generic action suggestions remain considerations until internal evidence supports institution-specific impact.

## Shared interface and record controls

- Overview explains the difference between exploratory research, a reviewed response and a change assessment.
- Separate workflow routes and three-step creation forms replace the previous combined form.
- Drafts are readable by default. Editing, request revision, diagnostics and history are progressively disclosed.
- Cited passages sit beside the draft on wider screens and below it on narrower layouts. Citation buttons open the matching evidence card.
- Issue dates and effective-date availability are shown without inferring missing metadata.
- Plain-language next actions distinguish draft, needs review, approved, rejected, needs revalidation, archived and trash states.
- Search, status and location filters help find saved work.
- Archive and recoverable trash retain all versions, review events and approval state. Hidden items must be restored before generation/edit/review. Restore does not bypass source revalidation.
- Version checks reject stale writes; running generation blocks conflicting changes. A refresh can resume the job in the same browser session. Server restarts retain earlier versions and use the existing interrupted-work recovery.
- Unsaved edits block review/generation/export. In-page confirmations protect discard, request replacement and recoverable deletion. Browser navigation also has an unsaved-work warning.
- Model-outage responses are labelled as having no cited answer, and cannot be submitted for review until a valid cited draft exists. No outage message is presented as an AI-generated answer.
- Local reviewer names record attribution, not authenticated enterprise identity. No external replies or business actions are sent.

## Engineering boundaries and compatibility

Changed runtime files: `work_items.py`, `local_jobs.py`, workflow routes/static mapping in `app.py`, `web/work.html`, `web/work.js`, new scoped `web/work.css`, and the navigation/handoff additions in `web/index.html` and `web/app.js`.

A small `work_visibility` table is added to the separate workflow database; existing work-item tables and corpus storage are preserved. Request audience, original research settings and optional finding labels are additive JSON fields in version bodies. No corpus migration or embedding rebuild is required.

New local endpoints: `GET /api/work-related`, `POST /api/work-import` and `POST /api/work-visibility`. Existing localhost, JSON, request-size and origin controls apply. Handoff accepts only a server job ID; visibility mutations use the existing optimistic revision guard.

`scope-check.json` compares this implementation with the frozen 24 October engineering candidate. The Engine class has an identical AST; eight retrieval/graph/support modules are byte-identical. The active configuration hash is recorded. The old candidate ZIP remains immutable and does not contain this interface increment.

A backup of the live workflow database was made before starting the new normal-port app: `data/qa25/live-workflows-before-ui-release.sqlite3`. It contained two work items, six versions and thirteen events. Walkthrough records were kept in a separate QA database. If rolling back code, stop the server first and preserve the current database; old code ignores archive/trash and finding-label metadata and can redisplay hidden items. Restore the pre-increment backup only if intentionally reverting later work as well. Do not run two servers against the same workflow database.

## Verification and what it establishes

- Full Python regression: **457 tests passed**; no skips reported.
- All **four JavaScript suites passed**, including safe rendering, known/unknown citations, saved-work filters, missing dates and advisory/outage states.
- Real localhost API tests cover import provenance, ignored browser-supplied answer text, invalid job IDs, routing, source identifiers, archive/trash/restore and review/version guards.
- New workflow tests cover stale imports, archived mutation rejection, stale approval on restore, preserved retrieval settings, invalid labels and classification reset after text edits.
- Live browser journeys covered guided query creation, missing-baseline rejection, explicit baseline confirmation, related-source suggestions, generation, refresh recovery, source-reader access, review submission, analyst edits, unsaved-export blocking, archive/restore, cancel/trash/restore and downloaded evidence export.
- Live local-model attempts: Query Desk first encountered an unavailable Ollama service, then generated after the installed service was started; a Change Brief and an Ask & Research handoff also completed. The three successful model outputs remained marked **incomplete** by the advisory review. These are engineering walkthroughs, not accuracy scores or an independent benchmark. No genuine source answer was marked approved by the agent.
- Browser console checks on the inspected final workflow page returned no errors.

Evidence: `evaluation/workbench_product_20261025/` contains regression logs, the code-scope comparison, authentic walkthrough records, export verification and screenshots. A native browser confirmation initially stalled automation; replacing it with an in-page dialog resolved the observed interaction and was tested through cancel, trash and restore.

## Open work, deliberately deferred

1. Independently review sources, graph relationships and the held-out acceptance questions/answers, as previously planned and explicitly deferred by the user.
2. Resolve demonstrated substantive answer-quality gaps from that review. Existing incomplete-answer warnings remain meaningful.
3. Run final pilot/release acceptance after the product flows and reviewed quality gates are accepted. This increment is not a new clean-install or full-index-rebuild certification.
4. Refresh the portable handoff for a future release; the 24 October frozen archive is historical. GitHub publication remains excluded.

No larger model, automatic whole-corpus graph expansion, new graph database, auto-generated enterprise impact verdict, public hosting or automatic business action was introduced.
