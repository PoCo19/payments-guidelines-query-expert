# Isolated browser verification — 24 October 2026

Application: `data/qa24/app`, local port 8782, fresh pinned environment and rebuilt index. All mutations below affected disposable engineering records, not the user's workbench database. Browser automation used the real application and local model; it did not inject answers or approve real payments findings.

| Journey | Observed result |
|---|---|
| Query Desk | Created IPO question, generated v2, reopened after application restart, inspected OC127 passage and its original-source link, saved an engineering note as v3, submitted for review, downloaded Markdown. |
| Impact brief | Selected OC226A followed by OC226, generated cited findings, opened source reader, edited unresolved-review questions as v3, submitted and downloaded Markdown. Analyst suggestions stayed separate from source requirements. |
| Ambiguity | “What is Tap and Pay?” returned a UPI/RuPay clarification with no source-backed answer and disabled review submission. |
| Clarification | Revised to “What is UPI Tap and Pay?” with product UPI; old answer cleared into v3 and generation produced v4 with evidence. Earlier versions remained available. |
| Persistence and states | Both edited substantive drafts reached Needs review at v3. No original-source or qualification-review checkbox was checked; no approval or independent reviewer identity was recorded. |
| Browser console | No error/warning entries were observed after the checked journeys. |

Saved exports: [Query Desk](browser-query-export.md), [impact brief](browser-impact-export.md). Saved screenshots/DOM: `browser-impact.png`, `browser-impact-dom.txt`, `browser-query.png`, `browser-query-dom.txt`, `browser-clarification-dom.txt`, `browser-clarified-dom.txt`.

The query and impact answers remained visibly incomplete. The clarified Tap & Pay response was labelled draft; this is not independent validation of its historical limits or their current applicability. Do not infer an answer-accuracy percentage from these browser checks. Original-source links were displayed, but remote website availability was not tested. Approval, rejection and stale-approval semantics are covered by the software tests rather than fabricated payments approvals in this browser run.
