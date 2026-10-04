# UPI Feature Workspace V2 — user guide

## Start and choose a workspace

Double-click `run-launch.cmd` in the project folder, keep the window open and open **http://127.0.0.1:8766**. Start Ollama for AI drafting. The original research application remains available through `run.cmd` on port 8765.

Choose **New workspace** and select an existing feature review, feature change or new feature launch. Enter a clear name and objective. Alternatively, use **Try the example** to explore an existing-feature review with fictional sources and a sample transaction rule.

Your reviewer name appears at the top right. Click it to change the name or review role. Product owner can complete the demonstration across all teams; the other roles illustrate team responsibilities. Role selection is not a login system.

## 1. Sources

Use one of the three source methods:

- **UPI circulars:** Search the existing local collection, expand **Read excerpt**, then choose **Add to workspace**. Already-added passages are marked.
- **Upload document:** Choose PDF, DOCX, Markdown or UTF-8 text, up to 5 MB. Review the extracted text, its title and intended team, then add it. Text-bearing PDFs are supported; scanned PDFs need OCR first. DOCX extraction reads text/table paragraphs, not images or comments.
- **Paste text:** Enter a source title, choose its intended use and paste the relevant excerpt.

Shared evidence feeds the feature brief and all teams. Team-specific evidence only enters that team's drafting context. Use **Transaction Risk only** for internal rule documents. Keep each source to at most 24,000 relevant characters. If an upload is longer, the preview explicitly shows only its first 24,000 characters; edit the excerpt before adding it.

Saved sources can be expanded and removed. Removing a source removes its derived facts, returns linked rules to proposed status and reopens affected reviews. The confirmation explains these effects.

## 2. Feature brief

Choose **Draft brief with AI**, or **Add a fact** manually. Facts have a supporting source and quotation. In the fact editor, **Read selected source** shows the source text beside the citation fields.

Review the facts and resolve any questions with recorded answers or decisions. Enter a review note, then choose **Approve brief & continue**. If you change the facts later, current approval is cleared and affected team work needs review again.

If a quotation is rejected, the error stays in the editor. Select the correct source or copy its exact wording; your other fields remain intact.

## 3. Team work

Choose **Local AI** or **Example templates** in the drafting menu. Templates are labelled examples and are not a model fallback. Use **Prepare all team drafts** to queue four workflows, or prepare a single team's draft.

Review the content and supporting evidence. Use **Edit draft** to correct wording, supporting facts or unresolved questions. Record the change rationale. Then enter a review note and approve the draft or request changes. Team approval means the document was reviewed; action completion is recorded separately.

For **Partners & BD**, open **Partner register** to add the participant context. Ready/live stage claims need recorded evidence.

For **Transaction Risk**, use the **Transaction rules** tab to add relevant rules. Record the condition, action, applicability, owner and evidence. Documented/active/retired rules need source support; active status also needs internal evidence and a deployment/configuration note. The **Assessment** tab contains the draft and a finding for every saved rule. The application does not discover live NPCI configurations or deploy changes.

Without internal rule evidence, Risk can discuss candidate scenarios and missing information; it cannot establish current rule coverage. Add internal source documents through Sources before claiming an existing configuration.

## 4. Actions & review

Click **Update** beside an action to set its owner, due date, status, prerequisites and evidence. Completion requires the current brief/team approvals, an owner, evidence and completed prerequisites. In the example, participant review depends on transaction-rule review.

The final review is available once all required work is complete. Existing-feature/change workspaces use **Complete review**; new launches use **Record launch decision**. Neither action launches a product, publishes content, sends messages or changes a transaction engine.

Use **Export review pack** from this screen or Activity. The Markdown file includes the brief, team drafts, transaction-rule assessments, actions and decision.

## Changes, history and deletion

Input changes reopen affected reviews and completed actions. A pending AI result is not applied if its inputs or the existing review changed while it ran. Activity shows drafting progress, failures and previous versions. **Try again** retries a failed/interrupted job in its recorded drafting mode; no hidden fallback is used.

Delete a workspace from its home card or **Workspace settings**. Type the exact workspace name. This permanently removes that workspace, history and queued work; exported files, backups and the circular collection are unaffected. A running model call may finish in the background, but its result cannot recreate the deleted workspace.

If another update arrives while you are editing, the app preserves your form and offers **View latest version**. Navigating away asks before discarding unsaved changes.

## Common recovery steps

| What you see | What to do |
|---|---|
| Local AI offline | Open Ollama, then use **Help & how it works → Refresh AI connection**, or explicitly choose example templates. |
| Brief approval needed | Follow **Review feature brief**. If using a team role, use **Change review role** to switch to Product owner for the local demonstration. |
| Source quotation does not match | Use **Read selected source** in the editor and correct the quotation/source. |
| Draft needs an update | Review changed facts if needed, then prepare a new draft for that team. |
| Input budget exceeded | Remove unrelated sources or create a narrower workspace. Source removal can invalidate dependent work. |
| Task prerequisites incomplete | Open the prerequisite action and complete its review/evidence first. The overview points to the next required task. |
| Workspace changed | Refresh before applying edits; an outdated revision is not silently saved. |

For a concise explanation to share with colleagues, use [the V2 product brief](FEATURE_WORKSPACE_V2.md).
