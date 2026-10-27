# Review of fourteen frozen-evidence answer pairs

Evidence: `evaluation/improvement_runs/20261017T024213481303Z/capture.json`, indexed by `rows[].id` and `arm`. Baseline has structured evidence off; variant has it on. Context-enriched retrieval is off in both. Review is AI-assisted and awaits independent adjudication. These are development observations, not an accuracy score.

| Case | Baseline observation | Structured observation | Interpretation |
|---|---|---|---|
| X-PAY-001 | Separates outstanding wallet balance from transaction ceiling | Same distinction; adds separate transaction categories | No material advantage established |
| X-PAY-002 | States application and third-year net-worth thresholds and ongoing maintenance | Substantively similar | No material advantage established |
| X-PAY-005 | Answers authentication question but adds old IMPS/RuPay detail | More focused on alternative authentication | Focus improvement; reference anchors are not exhaustive |
| X-PAY-006 | General threshold statement initially omits qualification, followed by exceptions | Exception caveat is explicit in threshold statement | Improved qualification wording in this sample |
| X-PAY-009 | Repeats pre-debit exemption across several claims | Repeats exemption and adds implementation details | Both verbose; not an established quality gain |
| X-PAY-011 | Juxtaposes single-payment and monthly-transfer quantities | Problematic comparison withheld; balance distinction remains | Need consistent comparison dimensions; incomplete status alone is misleading |
| X-PAY-012 | Notes old/new channel differences but risks overstating conflict | Asserts consistency without sufficient relationship evidence | Reconciliation remains unresolved; do not infer supersession |
| X-PAY-015 | Wrongly says no post-debit message is mandated | Wrongly permits skipping post-debit message because pre-debit notice is exempt | Critical unsupported inference in both; automated checker false acceptance |
| X-PAY-016 | Reproduces size-dependent implementation dates | Same | No material advantage established |
| X-PAY-018 | Abstains on private fraud cutoff | Abstains | One successful negative pair only |
| X-BIO-01 | Distinguishes original and increased biometric ceilings and date | Same across three claims | No material advantage established |
| X-DD-01 | Retains later inclusion, withholds earlier exclusion | Reverses chronology, including a repaired claim | Critical structured-arm failure; automated checker false acceptance |
| X-LIMIT-03 | No retained claim; needed category row absent | Says single ceiling absent from excerpts; no actual limit answer | Retrieval miss, not solved by synthesis |
| X-IPO-04 | Distinguishes purpose codes despite shared MCC | Same | No material advantage established |

## Inspectable critical evidence

**X-PAY-015:** citation S8 contains section 6, pre-transaction notification, including its FASTag/NCMC exemption. It does not exempt post-transaction notification. The unselected section 7 in `data/releases/payments-ocr-audit-20261015/sources/intake/4c6be564d4fcf352878e46d6.md` explicitly requires a post-transaction notification. The dataset's post-notification anchor is missed. Inspect both the captured S8 and the missing source clause; matching the subject FASTag is insufficient support for the opposite phase of notification.

**X-DD-01:** S4 states that transactions with the listed response codes are failures and not deemed debit; its continued list is in S2. S1 (OC128A) says the codes were previously excluded and shows 59/K1 as applicable under the updated scenario. The variant reverses this despite retrieving the right documents. Its repaired second claim is also wrong. Source retrieval and quote validation did not protect semantic chronology.

## Independent review fields

For each answer record: reviewer name; source passages inspected; correct/incorrect/uncertain core conclusion; missing material conditions; citation ownership; unnecessary detail; severity; corrected expected answer; adjudication date. Leave these fields pending until a reviewer actually completes them. Speaker assignments or model checking are not independent review.
