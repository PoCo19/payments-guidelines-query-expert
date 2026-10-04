# V2 flow audit and implementation direction

3 October 2026. User request: a polished, intelligible product; aligned menus; errors that point to real controls; workspace deletion; support for existing features and uploaded documents; Risk focused on UPI transaction rules.

## Captured audit

The existing local application was captured in Edge at 1440 × 1000. Screenshots were opened and inspected before these findings were recorded. This is a scoped UX audit, not full accessibility certification.

1. **Workspace overview — needs restructuring.** The large repeated title, description and metrics consume over half the viewport. A long undifferentiated blocker list competes with the journey. Duplicate titles in the sidebar lack useful context, and deletion is absent. [Screenshot](../output/launch-v2/audit/01-overview.png).
2. **Evidence — difficult to navigate.** Search, pasted sources, uploads, partner records and control records share one long page. The evidence tab follows the drafting tab although evidence is required first. Technical details dominate user-facing copy. [Screenshot](../output/launch-v2/audit/02-evidence.png).
3. **Readiness — actions too hidden.** Completion forms are collapsed, the global error region is far from the triggering form, and the page assumes a pilot launch. There is no targeted route from each blocker to its owning control. [Screenshot](../output/launch-v2/audit/03-readiness.png).

Visible strengths: consistent green/cream palette, readable text, distinct status badges and explicit source citations. Accessibility risks to address: error placement/focus, long-page navigation, clear labels and keyboard-accessible dialogs. Screen-reader behaviour was not established from screenshots.

## V2 design

- Product: **UPI Feature Workspace**, supporting existing-feature reviews, feature changes and new launches.
- Workspace home with type, updated time, progress and an explicit delete action with confirmation.
- Compact, aligned navigation: Overview; Sources; Feature brief; Team work; Actions & review; Activity.
- One recommended next action, derived from actual workflow state. Inline form errors remain with the control that caused them.
- Sources from the existing UPI knowledge base, text/Markdown, text-bearing PDF/DOCX uploads, or pasted evidence. Extraction is previewed before import.
- Team documents remain source-grounded drafts; technical metadata moves into details views.
- Transaction Risk gets a structured internal rule register and rule-by-rule applicability/recommendation output. Uploaded internal evidence is necessary to claim an active configuration. Public circulars do not reveal the current NPCI rule engine.
- Preserve existing workspaces and V1 history. Keep the V1 backup in `backups/launch-v1-20261003/`.

Acceptance: end-to-end existing-feature and new-workspace journeys, contextual errors, deletion including active jobs, file validation, source import, exact citations, rule assessment, review/change propagation, responsive layout, browser checks, live-model checks and updated user documentation.
