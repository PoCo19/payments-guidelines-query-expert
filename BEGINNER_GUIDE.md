# Beginner guide — v0.5.1

## Open and start

In File Explorer paste:

```text
C:\Users\Admin\Documents\Codex\2026-09-23\i-have-a-set-of-circulars
```

Circular Intelligence is a browser application, not a separately installed executable. Open **Ollama** from the Start menu, double-click **run.cmd** in this folder, then open **http://127.0.0.1:8765**. Keep the terminal open. Ctrl+C stops the app; Ollama is separate.

Alternatively, in PowerShell:

```powershell
cd 'C:\Users\Admin\Documents\Codex\2026-09-23\i-have-a-set-of-circulars'
.\run.cmd
```

Use `run.cmd` if `run.ps1` says scripts are disabled. No system execution-policy change is necessary.

## First experiment

Keep **Hybrid · RRF**, **AI draft answer**, and **Include related context** selected. Ask:

> According to OC 186A, what consent must the user give for UPI Tap & Pay on PoS?

Read the claims and click their citations. Each source card explains its inclusion: direct match, recorded reference, same feature, or surrounding passage. OC 186 may appear as a reference of OC 186A, with its own identity and page.

Repeat using **Direct matches only**. For this explicit circular query, sources should come only from OC 186A. A general question can directly match multiple circulars even in this scope.

Choose **Source excerpts** to see retrieval without answer generation. Neural/hybrid retrieval still needs Ollama for query embeddings. **Keyword + Source excerpts** works without Ollama.

## Inspect chunking

Click **Related circulars** or **Read page**. Expand **Indexed chunks & reference provenance**, then an individual chunk. You can inspect text, page, word offsets, section and previous/next links. OC 186A has 14 chunks across two pages. Its consent and opt-out clause stays together.

Heading labels are heuristic: an OCR page header may inherit the preceding section. Review full pages and the saved PDF when exact wording or numbers matter.

## Filters and experiments

- **Product** filters product membership; shared compliance circulars can appear in several products.
- **Feature** uses title/clause rules scoped to products. Labels are heuristic and can miss relevant circulars.
- **Issued by** excludes later issues and known later public revisions. It does not reconstruct effective rules.
- Ask `According to OC 186, how is Tap Pay initiated?` with cutoff `2024-01-01`; the 2026 circular should be absent.
- Ask `What requirements are specified in OC 999?`; no evidence should be returned.
- Compare keyword/neural/hybrid in **Experiments**. The scores cover the supplied retrieval examples, not overall answer correctness.
- **Export notes** downloads Markdown containing the question, filters, claims and attributed evidence.

## Rebuild after changes

The active inputs are `data/all-products-v1/index.json` and `data/all-products-v1/all_circular_pages.jsonl`, selected by `config.json`. The root data files preserve the old corpus. Merely changing a Markdown copy does not change retrieval. Back up and update the structured inputs consistently before rebuilding:

```powershell
.\run.cmd test
.\run.cmd embed
```

Restart the app afterward. Do not rebuild for every question. Changing the embedding model requires rebuilding; changing only the answer model does not.

## Troubleshooting

| Symptom | Action |
|---|---|
| Scripts disabled | Use `run.cmd`. |
| Browser cannot connect | Start the app and check the terminal error. |
| Address already in use | Open the existing app; stop its terminal before starting another copy. |
| Ollama connection/model error | Open Ollama and check `ollama list`. |
| Chroma unavailable | Run `setup.cmd`. |
| Index stale, invalid, not built, or model changed | Run `run.cmd embed`, then restart. |
| First answer slow | Allow time for model loading; the button shows elapsed time. |
| Saved PDF missing | Check `source_pack` in `config.json`. PDFs live in the earlier research pack. |
| Unconvincing answer | Inspect sources and record the failure for evaluation. |

A fresh installation should use Python 3.12 (tested version), `setup.cmd`, and the Ollama models `qwen3.5:9b` and `qwen3-embedding:0.6b`, followed by `run.cmd embed`. Dependencies are pinned in `requirements-lock.txt`. Models are stored by Ollama, outside this project.

## Context settings update

Generation now uses 16,384 context tokens, up to 3,072 output tokens, and an 18,000-character evidence budget. Tested locally; no re-embedding needed. See [tuning results](docs/CONTEXT_TUNING.md). Longer limits permit more detail but do not guarantee accuracy or longer answers.


## New in v0.4

- Keep Question type Automatic for normal use. For broad summaries name a circular: “Summarise OC 186A”. For comparison name each: “Compare OC 186 and OC 186A”. Check the included/total counts under Routing, coverage & claim checks.
- Local reranker is on by default for specific questions. Toggle it off to compare retrieval; summaries/comparisons bypass it.
- A draft appears only after citation and automated support checks. Open the support details to see reasons and source quotations. Withheld claims are separated from the answer; review them against the PDF. Long summaries can take around a minute or more because each claim is checked.
- Source review provides the OCR/date/label/relationship workflow. Follow docs/REVIEW_GUIDE.md. After accepting changes, stop the app, run run.cmd embed and restart. Saving a review does not change a running snapshot immediately.
- For a quick search without generation, select Source excerpts. Keyword retrieval with the CPU reranker works without Ollama; hybrid still needs Ollama embeddings.
- Share HOW_IT_WORKS.md and docs/VALIDATION_V05.md for this release. The existing v0.4 and v0.2 PDFs are historical.


## New in v0.5: finding the right circular

1. Open **Circular library**, choose a product and optionally a **Fiscal year**, then click **Search register**. Results are paginated, 50 per page.
2. Open a circular and inspect the title, product memberships, page text and quality warnings. “Date unknown” is expected for much of the new import; it is not inferred from the fiscal year.
3. Click **Summarise this circular**, then **Find evidence**. The request now uses that exact document ID.
4. For a comparison, use **Add to comparison** in two readers, then click **Find evidence**. Up to four exact documents can be selected. This works even if both are numbered 13.
5. If a typed reference is ambiguous, inspect the offered candidates or narrow Product/Fiscal year. The app will not guess.

Typing a new question clears the exact selection. Inspect the selection panel before running a summary or comparison. Selecting a document clears earlier filters so an old filter does not accidentally hide it.

**Issued by** excludes unknown issue dates, so it can remove most newly imported records. Use Fiscal year for inventory-based filtering. Fiscal year is not proof of when a rule became effective.

A missing-page or unverified-page-count warning means a summary may omit source material. Imported PDFs are not saved locally; use **Official PDF** to inspect the original online. Two known metadata conflicts are excluded from answers pending source review. A missing ZIP attachment is not treated as extracted evidence.

There is no need to rerun ingestion now: all-products-v1 is already active. See docs/MULTI_PRODUCT_IMPORT.md for maintenance and rollback.


## Context-sensitive answers — v0.5.1

Refresh the page to see **Answer style**. Leave it on **Automatic**: a direct answer may be a paragraph, requirements may be a list, and an overview can combine both. You can ask “explain in a paragraph” or “give bullet points,” or choose a format in the selector. The selector overrides a conflicting request in the question. This control applies to AI draft answers only.

Citations remain next to each statement. The support notice now appears once under the answer; individual checks and withheld claims remain below. Export notes keeps the same paragraph/list structure. No database rebuild is required. See docs/ANSWER_FORMATTING.md for examples and validation.
