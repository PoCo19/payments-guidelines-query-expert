# Context-sensitive answer formatting — v0.5.1

The earlier application asked Qwen for factual claims and always displayed those claims in an HTML bullet list. Prompt wording alone could not change that fixed renderer. v0.5.1 separates the evidence-checking structure from the visible answer structure.

## Using it

Leave **Answer style → Automatic** for normal questions. The model is instructed to use prose for explanations/direct answers, bullets for parallel requirements, numbered lists for supported procedures, and a mixture when an overview plus details is useful. Automatic mode can also follow an explicit request in your question, such as “in a paragraph” or “as bullet points.”

Choose **Paragraphs**, **Bullet points**, or **Paragraphs + bullets** to override the automatic choice. The selector takes precedence over conflicting prose in the question. It applies only to AI draft answers. A one-claim mixed answer may remain a paragraph: the application never invents an introduction to fill a layout.

Refresh the browser to load the new UI. No corpus rebuild or model download is needed. **Export notes** preserves the same paragraphs, bullet lists and numbered lists with citation labels.

## How it works

1. Qwen returns the existing plain-text claims/citations plus a `layout` referencing their one-based positions. Each block is `paragraph`, `bullets` or `steps`. There is no separate unchecked introduction, heading or conclusion field.
2. Citation validation and the existing per-claim support checks run as before. The engine gives claims stable draft indices so removal cannot accidentally point a layout entry at another claim.
3. The formatter verifies that the proposed layout includes every draft claim exactly once and uses only permitted block types. It then removes withheld claims and empty blocks. Only checked text is eligible for display when support checking is enabled.
4. Invalid/missing layout falls back to a deterministic presentation of the retained claims. Explicit styles are enforced even if the model chooses another shape. Mixed layouts are repaired after filtering when possible.
5. The shared browser/export renderer joins claims into readable paragraphs or renders list items. Citations stay next to their statements. Model text is escaped as plain text; arbitrary HTML/Markdown is not executed. One compact support notice replaces a repetitive label after every sentence; detailed checks remain inspectable below.

This uses the existing generation call, not a second rewriting call. Presentation never paraphrases the checked claims afterward. The remaining limitation is prose quality: awkward transitions, repetition, excess claims or imperfect brevity can still occur. Formatting is not an answer-correctness guarantee.

## Implementation and validation

`answer_format.py` defines the output schema, guidance, explicit request handling and layout validation/fallback. `app.py` validates claims before producing `answer_blocks`. `web/answer_format.js` shares safe HTML and Markdown rendering; `web/app.js` connects the selector, answer display and export.

**103 Python tests pass** (93 existing plus 10 formatting tests). Tests cover invalid references, duplicate/omitted claims, withheld-claim removal, explicit styles, empty answers, mixed-layout repair and backend check ordering. The Node renderer tests cover prose, unordered/ordered lists, mixed content, citations, empty output, export structure and markup escaping.

Live local-model tests returned:

| Request | Result | Retained claims | Time |
|---|---|---:|---:|
| Brief direct question, Automatic | One paragraph | 1 | 15.06 s |
| Three requirements, bullet request | Bullet list | 3 | 17.73 s |
| Overview plus requirements, Mixed | Paragraph + bullet list | 6 | 36.95 s |

All three used the model's valid layout and passed automated support checks. The mixed response exceeded the requested number of details, so precise length control remains imperfect. Timings are individual observations, not a benchmark. Full evidence is in `reports/v051_live_formatting.json`; tests are in `reports/v051_unit_tests.txt`. The corpus fingerprint is unchanged. The pre-change code/config/UI/docs are preserved under `versions/v0.5.0/`.
