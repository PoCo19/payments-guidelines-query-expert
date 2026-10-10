# Speaker notes: slides 1–4

**Presentation:** Payments_Guidelines_Query_Expert_v3.pptx
**Audience:** Midterm capstone evaluators
**Delivery:** Approximately 2 minutes. Continue with the [notes for slides 5–7](V3_Speaker_Notes_Slides_05-07.md), followed by [slides 8–12](V3_Speaker_Notes_Slides_08-12.md).

## Slide 1 — Project introduction

Hello everyone. We are Team T-27, presenting Payments Guidelines Query Expert.

Our project helps payments professionals ask questions about documented requirements and inspect the sources behind an answer. We have started with NPCI circulars. Today, we will demonstrate the prototype, explain our design choices, and discuss evaluation and next steps.

## Slide 2 — Problem and motivation

Our intended users are product, operations and compliance teams in banks and fintechs.

A question about one feature may require several circulars and later clarifications. Finding a document is only the first step: users must also understand conditions, exceptions and applicability.

Our goal is to simplify that research while keeping supporting evidence visible. Whether this saves users time still needs to be measured.

## Slide 3 — Proposed solution

We use retrieval-augmented generation, or RAG: the system retrieves document evidence before asking a model to draft an answer.

We preserve circular and page identity, combine keyword and semantic search, and use a local model to produce cited answers. Automated checks flag or withhold unsupported claims, but users still need to verify the sources.

The application supports questions, summaries and comparisons. It assists research; it does not make compliance decisions or determine which rule is currently effective.

## Slide 4 — Example user journey

Here, the user asks: “Can I use UPI Tap and Pay at a shop's card machine?” No circular number is needed.

The saved answer identifies conditions, including an NFC-enabled terminal and person-to-merchant transactions. NFC is the contactless technology used for tapping a device.

Citation chips let the user inspect the supporting passages in OC 186A. This demonstrates the question-to-source journey; one example does not establish accuracy.

Next, we explain the data and tools behind this flow.

## Presenter reminders — not part of the spoken script

- NPCI is the initial implemented corpus; broader payments coverage is the product ambition.
- Do not describe time savings or answer accuracy as established outcomes.
- Automated claim checks can make mistakes. A citation makes evidence inspectable; it is not proof that the answer is correct or complete.
- The slide 4 response is a saved application example. Do not describe it as a live model run unless you actually run the question during the presentation.
- The speaker notes across all 12 slides total roughly 1,300 words. Rehearse the complete presentation with speaker handoffs to stay within the 5–10-minute submission window; avoid reading slide text again after delivering the notes.
