# V1 demonstration and beginner walkthrough

## Open the application

Double-click `run-launch.cmd` in the project folder and open **http://127.0.0.1:8766**. Keep the server window open. Start Ollama if you want live model drafts. Enter your reviewer name; use Product owner initially.

Choose **Create simulated pilot**. This prepares a fictional UPI LITE brief, six cited facts, two partners, two controls and four readiness tasks. The control and partner examples do not represent real NPCI records.

## Demonstrate the complete workflow

1. **Feature facts:** Read the six facts and quotations. Enter a review note and approve the current baseline. In a real workspace, add relevant evidence first and use **Extract facts with local AI** or manual fact entry. Extraction questions need a recorded disposition before approval.
2. **Team deliverables:** Select Customer Success and generate a draft. Choose **local AI** to use Qwen, or **template demo** for a fast, deterministic demonstration. Wait for the queue to complete. Inspect source summaries, proposals and supporting evidence.
3. **Review:** Edit content if needed. Resolve open questions and record how you resolved them; source support still needs human checking. Record the team review. Repeat for Marketing, BD and Risk. Switching roles illustrates the respective responsibilities; it does not create separate user accounts.
4. **Readiness:** Open each task. Enter an owner and completion evidence. For a course demonstration, label the evidence synthetic rather than pretending real work was performed. Complete Risk before BD because BD has a Risk prerequisite. Complete Customer Success and Marketing as well.
5. **Launch decision:** Check that all gates pass. Record the product owner's reasoned decision. This creates an internal record only.
6. **History & export:** Inspect revisions and download the Markdown launch pack. It contains facts, citations, team outputs, task evidence, registers and the decision.

## Demonstrate why orchestration matters

After completing the pilot, go to **Evidence & inputs** and change a control's scope. The Risk draft becomes stale, its completed task reopens, and the dependent BD task reopens. Unaffected Marketing and Customer Success drafts remain approved. The prior launch decision now requires review.

Regenerate and review Risk, recheck its completion evidence, complete the dependent BD task again and record a fresh launch decision. The history retains earlier deliverables and the change events.

Then demonstrate a broader change: edit a shared feature fact. Baseline approval is cleared and team drafts that received that fact become stale. Review the fact and reapprove the baseline before regenerating those drafts.

## Use your actual circular collection

On **Evidence & inputs**, search for a feature such as `UPI lite`. Expand a result, inspect the excerpt and import it. The application retains the document, chunk and page identifiers, issue date when known, original source URL and a content hash. Review the original circular in the research app where necessary. A retrieved passage does not establish the current applicable rule by itself.

For a feature-specific trial, create a fresh launch and import only relevant evidence. Add actual internal partner/control context only when you are authorised to use it locally. The current application has no authenticated multi-user access controls.

## What to explain to your course group

The RAG layer helps locate evidence. The new business layer coordinates what happens after evidence is reviewed: specialist drafts, human decisions, execution tasks and change impact. The queue and dependency rules are ordinary Python logic; the local model performs bounded extraction and drafting. This makes the results traceable and the workflow repeatable.

Use [the concise product brief](LAUNCH_PRODUCT_BRIEF.md) for sharing. Keep [the technical guide](LAUNCH_ORCHESTRATOR_V1.md) for setup and implementation questions. The existing five-page Circular Intelligence PDF describes the underlying research application, not this new orchestrator.
