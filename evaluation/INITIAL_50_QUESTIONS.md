# Initial 50-question evaluation catalogue

**Payments Guidelines Query Expert | Frozen preliminary benchmark | Documented 4 October 2026**

This catalogue records the original questions and draft expected answers verbatim. It explains the test design and saved retrieval observations; it is not a new evaluation run or a verified payments rulebook. All 50 cases are AI-assisted and awaiting independent review.

## Read this first

- **Question:** the exact input in the frozen dataset.
- **Draft expected answer:** the original reference intent, not an actual model response or an independently approved answer.
- **Source anchor:** a document ID, original source page number and short text fragment used to check retrieval. A fragment locates evidence; it may not support every condition in the draft answer by itself.
- **Observed result:** evidence retrieval only, from the saved 3 October 2026 run. No answer-quality score is implied.
- **Review status:** `draft_requires_independent_review` for every case. Fill the existing [independent review sheet](independent_review.csv); do not overwrite the frozen JSON.

## How 50 questions produce 55 evidence checks

| Case group | IDs | Questions | Expected anchors | Purpose |
|---|---|---:|---:|---|
| Focused questions | RAG-001 to RAG-032 | 32 | 32 | Find a specific requirement or responsibility |
| Summaries | RAG-033 to RAG-038 | 6 | 11 | Find selected passages across a document |
| Comparisons | RAG-039 to RAG-044 | 6 | 12 | Find evidence from both named circulars |
| Negative cases | RAG-045 to RAG-050 | 6 | 0 | Check behaviour when the requested evidence is unavailable or unsuitable |
| **Total** | | **50** | **55** | |

**50 = 44 positive + 6 negative questions. 55 = (33 questions x 1 anchor) + (11 questions x 2 anchors).** The six negative cases are part of the 50, not six additional questions. RAG-036 is the one summary with only one anchor. These are 55 question-to-source checks, not 55 unique documents, unique passages or correct answers.

## Scope, execution and limitations

The set is UPI-focused, with one RuPay credit-card-on-UPI question (RAG-032). It does not establish quality across the entire multi-product corpus. The runner uses the case series when provided, otherwise UPI; thus a blank dataset series does not mean an unfiltered search in this experiment.

RAG-001 to RAG-032 are labelled `development`; RAG-033 to RAG-050 are labelled `reserved_review`. All 50 were run and their aggregate results inspected. The latter label does not establish an untouched held-out test set. New independently reviewed questions are needed for that purpose.

The dataset route is a descriptive label. The saved runner does not force this route; it lets the application route each question and records the observed route. Strict scope limits evidence to the selected circular scope; related scope permits bounded related evidence. Neither scope establishes supersession. The date cutoff filters available issues/revisions; it does not reconstruct all rules legally effective on that date.

The runner uses `mode=evidence`. A positive anchor passes when a returned source has the expected document ID and page, and its whitespace-normalised text contains the recorded quote. A negative case passes the retrieval check when no sources are returned. That is different from testing whether a language model correctly declines to answer after seeing irrelevant evidence.

Most questions explicitly name circulars. The six comparison questions also include hints that closely resemble their draft expected answers. Summary references are generic instructions rather than complete reference summaries. Selected anchors do not establish full summary coverage. These limitations make the set useful for regression checks but weak evidence of general research performance.

Source fragments retain extraction spellings such as "empanelied" to preserve the frozen matching rule. Read the linked Markdown for surrounding context and check original page images/PDFs for critical wording, figures and qualifiers. Current links are taken from the saved inventory; live NPCI availability was not rechecked for this document.

## Saved preliminary results

| Method | Anchors found | Negative cases returning no sources | Median retrieval ms |
|---|---:|---:|---:|
| BM25 | 55/55 | 6/6 | 12.0 |
| Vector | 55/55 | 5/6 | 83.0 |
| Hybrid | 55/55 | 5/6 | 78.0 |
| Hybrid + reranker | 55/55 | 5/6 | 160.5 |

All methods found the selected anchors. RAG-048 returned irrelevant evidence in the three semantic variants, while BM25 returned none. This does not demonstrate perfect answers or establish that BM25 is best for all questions. Timings are from one warmed, interleaved pass and exclude answer generation. Summary/comparison routes bypass reranking; 15 such routes appear in this run, including negative scenarios.

[Saved run and configuration](../output/midsem/evidence/20261003T172349Z/retrieval.json) | [Runner](midsem_check.py) | [Creation provenance](dataset_creation_provenance.txt)

## Question directory

| ID | Question |
|---|---|
| [RAG-001](#rag-001) | Under OC 186A, are PoS tap payments for merchants or person-to-person transfers? |
| [RAG-002](#rag-002) | Can a user disable the PoS tap payment feature after consenting in OC 186A? |
| [RAG-003](#rag-003) | What must happen after device binding before tap payments resume under OC 186A? |
| [RAG-004](#rag-004) | What device-lock requirements does OC 186A set? |
| [RAG-005](#rag-005) | May the PoS tap payment feature be hidden inside another service in OC 186A? |
| [RAG-006](#rag-006) | What does the remitter bank check before each tap payment in OC 186A? |
| [RAG-007](#rag-007) | Who integrates the PoS common library under OC 186A? |
| [RAG-008](#rag-008) | Which PoS terminals may the payee PSP enable for tap payments under OC 186A? |
| [RAG-009](#rag-009) | What phone capability is required for Tap Pay in OC 186? |
| [RAG-010](#rag-010) | Where should the Tap Pay button be placed under OC 186? |
| [RAG-011](#rag-011) | Which initiation mode identifies tap payments in OC 186? |
| [RAG-012](#rag-012) | How must acquiring banks protect NFC tags under OC 186? |
| [RAG-013](#rag-013) | Where are acquiring banks to procure NFC tags under OC 186? |
| [RAG-014](#rag-014) | Who completes a payment in partial delegation under OC 201? |
| [RAG-015](#rag-015) | Who can initiate and complete a fully delegated payment under OC 201? |
| [RAG-016](#rag-016) | May primary and secondary users choose their own apps under OC 201? |
| [RAG-017](#rag-017) | Can a secondary user receive delegation from several primary users under OC 201? |
| [RAG-018](#rag-018) | Which authentication controls apply to secondary users under OC 201? |
| [RAG-019](#rag-019) | Can primary users see secondary-user transactions under OC 201? |
| [RAG-020](#rag-020) | Does OC 201 require an online dispute facility? |
| [RAG-021](#rag-021) | Which secondary-user segments qualify for full-delegation linking under OC 201A? |
| [RAG-022](#rag-022) | What identification details must the primary payer PSP share under OC 201A? |
| [RAG-023](#rag-023) | Whose consent is required before accepting full delegation under OC 201A? |
| [RAG-024](#rag-024) | Who identifies the secondary user by name mobile and official document under OC 201A? |
| [RAG-025](#rag-025) | How frequently must the recycled-number database be refreshed under OC 115E? |
| [RAG-026](#rag-026) | Can consent to seed a UPI Number be taken during a payment under OC 115E? |
| [RAG-027](#rag-027) | Who bears liability for failing to update the numeric mapper under OC 115F? |
| [RAG-028](#rag-028) | When may local mobile-number resolution be used under OC 115F? |
| [RAG-029](#rag-029) | What triggers automatic FASTag replenishment under OC 207? |
| [RAG-030](#rag-030) | Does the PDN exception in OC 207 apply to unrelated merchant categories? |
| [RAG-031](#rag-031) | Which user identifiers must be masked under OC 234? |
| [RAG-032](#rag-032) | How is the linked RuPay card limit selected under circular 022? |
| [RAG-033](#rag-033) | Summarise OC 186A, covering the requirements across its sections. |
| [RAG-034](#rag-034) | Summarise OC 186, covering the requirements across its sections. |
| [RAG-035](#rag-035) | Summarise OC 201, covering the requirements across its sections. |
| [RAG-036](#rag-036) | Summarise OC 201A, covering the requirements across its sections. |
| [RAG-037](#rag-037) | Summarise OC 115F, covering the requirements across its sections. |
| [RAG-038](#rag-038) | Summarise OC 207, covering the requirements across its sections. |
| [RAG-039](#rag-039) | Compare OC 186 and OC 186A: Attribute original NFC capability and later device-lock requirements separately. |
| [RAG-040](#rag-040) | Compare OC 201 and OC 201A: Distinguish original delegation rules and later linking identification requirements. |
| [RAG-041](#rag-041) | Compare OC 115E and OC 115F: Attribute mapper update frequency and later response threshold separately. |
| [RAG-042](#rag-042) | Compare OC 186 and OC 186A: Compare original homepage button and later dedicated standalone feature. |
| [RAG-043](#rag-043) | Compare OC 201 and OC 201A: Compare secondary user security with later consent to additional identification details. |
| [RAG-044](#rag-044) | Compare OC 115E and OC 115F: Explain consent restrictions separately from later complaint-investigation provisions. |
| [RAG-045](#rag-045) | What does OC 999 require? |
| [RAG-046](#rag-046) | Summarise OC 237. |
| [RAG-047](#rag-047) | Compare OC 186 and OC 999. |
| [RAG-048](#rag-048) | Explain quantum photosynthesis and chlorophyll. |
| [RAG-049](#rag-049) | Summarise OC 201A. |
| [RAG-050](#rag-050) | What requirements are in OC 186AA? |

## RAG-001

**Question:** Under OC 186A, are PoS tap payments for merchants or person-to-person transfers?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** P2M only.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **1**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=1).
  Anchor text: Person-to-Merchant (P2M)

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-002

**Question:** Can a user disable the PoS tap payment feature after consenting in OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Yes, opt-out at any time.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **1**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=1).
  Anchor text: ability to opt out at any time

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-003

**Question:** What must happen after device binding before tap payments resume under OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Explicit user consent must be obtained again.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: after each device binding operation

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-004

**Question:** What device-lock requirements does OC 186A set?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Enable device lock; device must be unlocked at initiation.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: device lock is enabled

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-005

**Question:** May the PoS tap payment feature be hidden inside another service in OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** No, a dedicated standalone call-to-action is required.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: shall not be embedded within any other service

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-006

**Question:** What does the remitter bank check before each tap payment in OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Account feature-enablement status.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: before processing each transaction

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-007

**Question:** Who integrates the PoS common library under OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Payee PSP.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **1**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=1).
  Anchor text: Payee PSP shall integrate

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-008

**Question:** Which PoS terminals may the payee PSP enable for tap payments under OC 186A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** NFC-enabled terminals certified to the stated standards.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **1**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=1).
  Anchor text: only on NFC-enabled PoS terminals

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-009

**Question:** What phone capability is required for Tap Pay in OC 186?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** NFC capability.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: NFC capability

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-010

**Question:** Where should the Tap Pay button be placed under OC 186?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Separate call-to-action button on the homepage.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: on the homepage

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-011

**Question:** Which initiation mode identifies tap payments in OC 186?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** 06.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: initiation mode 06

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-012

**Question:** How must acquiring banks protect NFC tags under OC 186?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** NFC Forum Type 2 certification and non-rewritability after personalisation; periodic checks.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: non-rewritable post personalisation

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-013

**Question:** Where are acquiring banks to procure NFC tags under OC 186?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** NPCI empanelled vendors, referencing the cited circulars.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **2**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=2).
  Anchor text: empanelied vendors

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-014

**Question:** Who completes a payment in partial delegation under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Primary user completes it with UPI PIN.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: Primary user shall complete

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-015

**Question:** Who can initiate and complete a fully delegated payment under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** The authorised secondary user, within defined limits.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: initiate and complete UPI transactions

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-016

**Question:** May primary and secondary users choose their own apps under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Yes; independent user journeys and own app choice.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: own choice of UPI app

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-017

**Question:** Can a secondary user receive delegation from several primary users under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Only one primary user; primary can delegate to five secondary users.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: only one primary user

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-018

**Question:** Which authentication controls apply to secondary users under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** App passcode/biometrics mandatory.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: App passcode/ biometrics

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-019

**Question:** Can primary users see secondary-user transactions under OC 201?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Yes, in their UPI app and bank account statement.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **2**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=2).
  Anchor text: visibility of transactions

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-020

**Question:** Does OC 201 require an online dispute facility?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Yes, ODR functionality must be available.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **2**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=2).
  Anchor text: Online Dispute Resolution (ODR)

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-021

**Question:** Which secondary-user segments qualify for full-delegation linking under OC 201A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Specified family members or domestic/small-business employees.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: Domestic or Small Business Employee

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-022

**Question:** What identification details must the primary payer PSP share under OC 201A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Secondary user document type and document ID number, to secondary payer PSP and issuer bank.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: Document Type and Document ID number

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-023

**Question:** Whose consent is required before accepting full delegation under OC 201A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Secondary user consent to the additional document details.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: explicit consent from Secondary User

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-024

**Question:** Who identifies the secondary user by name mobile and official document under OC 201A?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** The primary user issuer bank.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: Issuer Bank of the Primary User

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-025

**Question:** How frequently must the recycled-number database be refreshed under OC 115E?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** At least weekly using MNRL/DIP.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-115E`, source page **1**: [source Markdown](../data/circulars/2025-03-03_OC-115E.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_115_E_FY_2024_25_Addendum_to_circular_on_the_Numeric_UPI_ID_resolution_5bf6b7d3a5.pdf#page=1).
  Anchor text: at least on weekly basis

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-026

**Question:** Can consent to seed a UPI Number be taken during a payment under OC 115E?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** No, not before or during a transaction.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-115E`, source page **1**: [source Markdown](../data/circulars/2025-03-03_OC-115E.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_115_E_FY_2024_25_Addendum_to_circular_on_the_Numeric_UPI_ID_resolution_5bf6b7d3a5.pdf#page=1).
  Anchor text: before or during a transaction

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-027

**Question:** Who bears liability for failing to update the numeric mapper under OC 115F?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** PSP and UPI application.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-115F`, source page **1**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=1).
  Anchor text: liability of the PSP and the UPI Application

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-028

**Question:** When may local mobile-number resolution be used under OC 115F?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Only when Numeric UPI ID Mapper response exceeds one second; stated PSP/app liability remains.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-115F`, source page **1**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=1).
  Anchor text: exceeding one (1) second

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-029

**Question:** What triggers automatic FASTag replenishment under OC 207?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Balance falling below the customer-set threshold.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-207`, source page **1**: [source Markdown](../data/circulars/2024-09-23_OC-207.md) | [original PDF](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf#page=1).
  Anchor text: threshold set by the customer

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-030

**Question:** Does the PDN exception in OC 207 apply to unrelated merchant categories?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** No; only the stated NETC FASTag and RuPay NCMC categories/intended purposes.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-207`, source page **2**: [source Markdown](../data/circulars/2024-09-23_OC-207.md) | [original PDF](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf#page=2).
  Anchor text: only for the mentioned MCCs

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-031

**Question:** Which user identifiers must be masked under OC 234?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** UPI IDs, mobile numbers and account numbers across customer-facing interfaces and communications.

**Settings:** dataset route `clause`; series `blank (runner uses UPI)`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-234`, source page **1**: [source Markdown](../data/circulars/2026-06-05_OC-234.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_234_FY_2026_27_Safeguarding_User_Information_in_UPI_6e5f07f90a.pdf#page=1).
  Anchor text: UPI IDs, mobile numbers, and account numbers

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-032

**Question:** How is the linked RuPay card limit selected under circular 022?

**Test purpose:** Locate the stated requirement in its own circular; review the answer for omitted conditions and correct participant attribution.

**Draft expected answer (verbatim):** Lowest of the issuer card limit, issuer UPI risk limit and customer-set limit.

**Settings:** dataset route `clause`; series `RuPay`; scope `strict`; cutoff `none`; split `development`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-RuPay-022`, source page **1**: [source Markdown](../data/circulars/2023-11-16_2023-RuPay-022.md) | [original PDF](https://www.npci.org.in/uploads/Ru_Pay_I_OC_022_I_FY_23_24_I_Ru_Pay_Credit_Card_Transaction_limit_for_linked_Ru_Pay_Credit_Card_on_UPI_6ab86555e4.pdf#page=1).
  Anchor text: lowest of the following

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-033

**Question:** Summarise OC 186A, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-186A`, source page **1**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=1).
  Anchor text: Payee PSP shall integrate
- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: before processing each transaction

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-034

**Question:** Summarise OC 186, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: NFC capability
- `2023-UPI-186`, source page **2**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=2).
  Anchor text: empanelied vendors

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-035

**Question:** Summarise OC 201, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: only one primary user
- `2024-OC-201`, source page **2**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=2).
  Anchor text: Online Dispute Resolution (ODR)

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-036

**Question:** Summarise OC 201A, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: Document Type and Document ID number

**Saved retrieval observation:** BM25: 1/1 anchors; Vector: 1/1 anchors; Hybrid: 1/1 anchors; Hybrid + reranker: 1/1 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-037

**Question:** Summarise OC 115F, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2026-OC-115F`, source page **1**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=1).
  Anchor text: exceeding one (1) second
- `2026-OC-115F`, source page **2**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=2).
  Anchor text: appropriate investigation

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-038

**Question:** Summarise OC 207, covering the requirements across its sections.

**Test purpose:** Retrieve the selected section/page anchors. Full summary completeness requires an additional human-authored checklist.

**Draft expected answer (verbatim):** Cover the source-supported requirements across all cited pages; report incomplete coverage explicitly.

**Settings:** dataset route `summary`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-207`, source page **1**: [source Markdown](../data/circulars/2024-09-23_OC-207.md) | [original PDF](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf#page=1).
  Anchor text: threshold set by the customer
- `2024-OC-207`, source page **2**: [source Markdown](../data/circulars/2024-09-23_OC-207.md) | [original PDF](https://www.npci.org.in/uploads/NPCI_UPI_OC_207_Auto_replenishment_of_NETC_FAS_Tag_and_Ru_Pay_NCMC_with_UPI_Auto_Pay_375b0d066f.pdf#page=2).
  Anchor text: only for the mentioned MCCs

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-039

**Question:** Compare OC 186 and OC 186A: Attribute original NFC capability and later device-lock requirements separately.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Attribute original NFC capability and later device-lock requirements separately.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: NFC capability
- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: device lock is enabled

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-040

**Question:** Compare OC 201 and OC 201A: Distinguish original delegation rules and later linking identification requirements.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Distinguish original delegation rules and later linking identification requirements.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: only one primary user
- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: Document Type and Document ID number

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-041

**Question:** Compare OC 115E and OC 115F: Attribute mapper update frequency and later response threshold separately.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Attribute mapper update frequency and later response threshold separately.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-115E`, source page **1**: [source Markdown](../data/circulars/2025-03-03_OC-115E.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_115_E_FY_2024_25_Addendum_to_circular_on_the_Numeric_UPI_ID_resolution_5bf6b7d3a5.pdf#page=1).
  Anchor text: at least on weekly basis
- `2026-OC-115F`, source page **1**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=1).
  Anchor text: exceeding one (1) second

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-042

**Question:** Compare OC 186 and OC 186A: Compare original homepage button and later dedicated standalone feature.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Compare original homepage button and later dedicated standalone feature.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2023-UPI-186`, source page **1**: [source Markdown](../data/circulars/2023-12-19_2023-UPI-186.md) | [original PDF](https://www.npci.org.in/uploads/UPI_TAP_and_PAY_OC_186_Introduction_of_UPI_TAP_and_PAY_mode_of_Payments_918962f06b.pdf#page=1).
  Anchor text: on the homepage
- `2026-OC-186A`, source page **2**: [source Markdown](../data/circulars/2026-09-10_OC-186A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_I_OC_No_186_A_I_Enhancement_UPI_Tap_and_Pay_on_Point_of_Sale_Po_S_e695625b85.pdf#page=2).
  Anchor text: shall not be embedded within any other service

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-043

**Question:** Compare OC 201 and OC 201A: Compare secondary user security with later consent to additional identification details.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Compare secondary user security with later consent to additional identification details.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2024-OC-201`, source page **1**: [source Markdown](../data/circulars/2024-08-13_OC-201.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_FY_24_25_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_cf6799f126.pdf#page=1).
  Anchor text: App passcode/ biometrics
- `2025-OC-201A`, source page **1**: [source Markdown](../data/circulars/2025-07-08_OC-201A.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_201_A_FY_2025_26_Introduction_of_UPI_Circle_Delegated_Payments_for_secondary_users_Full_Delegation_Additional_Requirements_ba7e414c1a.pdf#page=1).
  Anchor text: explicit consent from Secondary User

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-044

**Question:** Compare OC 115E and OC 115F: Explain consent restrictions separately from later complaint-investigation provisions.

**Test purpose:** Retrieve both named sources and attribute each requirement separately, without inferring supersession.

**Draft expected answer (verbatim):** Explain consent restrictions separately from later complaint-investigation provisions.

**Settings:** dataset route `compare`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

- `2025-OC-115E`, source page **1**: [source Markdown](../data/circulars/2025-03-03_OC-115E.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_No_115_E_FY_2024_25_Addendum_to_circular_on_the_Numeric_UPI_ID_resolution_5bf6b7d3a5.pdf#page=1).
  Anchor text: before or during a transaction
- `2026-OC-115F`, source page **2**: [source Markdown](../data/circulars/2026-07-30_OC-115F.md) | [original PDF](https://www.npci.org.in/uploads/UPI_OC_115_F_Addendum_to_OC_NPCI_UPI_OC_115_E_2024_25_on_the_Numeric_UPI_ID_334510ae0c.pdf#page=2).
  Anchor text: appropriate investigation

**Saved retrieval observation:** BM25: 2/2 anchors; Vector: 2/2 anchors; Hybrid: 2/2 anchors; Hybrid + reranker: 2/2 anchors.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-045

**Question:** What does OC 999 require?

**Test purpose:** Unavailable reference in this snapshot: do not invent the contents of OC 999.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: no sources returned; Hybrid: no sources returned; Hybrid + reranker: no sources returned.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-046

**Question:** Summarise OC 237.

**Test purpose:** Listed but unavailable content: the saved register records OC 237 without a public PDF. Do not infer its requirements from the listing.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: no sources returned; Hybrid: no sources returned; Hybrid + reranker: no sources returned.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-047

**Question:** Compare OC 186 and OC 999.

**Test purpose:** Incomplete comparison: do not provide a complete comparison when the requested OC 999 evidence is missing.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: no sources returned; Hybrid: no sources returned; Hybrid + reranker: no sources returned.

**Observed application route:** `compare`. Generated-answer correctness: **not scored by this run**.

## RAG-048

**Question:** Explain quantum photosynthesis and chlorophyll.

**Test purpose:** Out-of-domain question: payment circulars should not be treated as evidence about quantum photosynthesis.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: sources returned (negative retrieval check failed); Hybrid: sources returned (negative retrieval check failed); Hybrid + reranker: sources returned (negative retrieval check failed).

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## RAG-049

**Question:** Summarise OC 201A.

**Test purpose:** Date-filter exclusion: OC 201A is excluded under the 2024-12-31 cutoff. Do not silently use a later circular.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `2024-12-31`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: no sources returned; Hybrid: no sources returned; Hybrid + reranker: no sources returned.

**Observed application route:** `summary`. Generated-answer correctness: **not scored by this run**.

## RAG-050

**Question:** What requirements are in OC 186AA?

**Test purpose:** Near-match reference: do not silently substitute OC 186 or 186A for the requested OC 186AA.

**Draft expected answer (verbatim):** Abstain because required evidence is absent.

**Settings:** dataset route `auto`; series `blank (runner uses UPI)`; scope `related`; cutoff `none`; split `reserved_review`.

**Review status:** AI-assisted; independent source and answer review pending.

**Expected source anchors:**

None. Expected behaviour is to decline on the available evidence; the saved retrieval test measures only whether the source list is empty.

**Saved retrieval observation:** BM25: no sources returned; Vector: no sources returned; Hybrid: no sources returned; Hybrid + reranker: no sources returned.

**Observed application route:** `clause`. Generated-answer correctness: **not scored by this run**.

## Review procedure and next evaluation

1. Read the complete source passages, including conditions outside the short anchor. Check the original when extraction is uncertain.
2. Record reviewer identity and source verification in `independent_review.csv`. Record disagreements and resolve them explicitly.
3. Write complete required-fact checklists, especially for summaries and comparisons, in a new benchmark version. Preserve these original 50 cases and their checksum.
4. Capture actual generated answers and exact supplied evidence before scoring with RAGAS. Score displayed answer blocks/claims, not the API status-message field.
5. Keep retrieval, answer completeness/correctness, citation support, appropriate abstention and latency separate. A valid citation ID alone does not prove support.
6. Add new questions without circular-number or answer hints, plus ambiguity and incomplete-source scenarios. Reserve a genuinely unexposed set for final evaluation.

No RAGAS scores or independent-review outcomes have been added by this documentation task.

## Reproducibility

[Frozen questions](rag_cases.json) | [Checksum](rag_cases.sha256) | [Human review sheet](independent_review.csv)

Dataset SHA-256: `a09ceaac119e46119f48ebc1e2f5701a8bbc759bfa40400d5307a736d7c00362`.

Regenerate this catalogue with `python tools/document_initial_benchmark.py`. The builder validates the frozen checksum, case IDs, source-anchor text, local source links and recorded counts before writing this Markdown. These checks establish faithful documentation, not expert verification of the source interpretation.
