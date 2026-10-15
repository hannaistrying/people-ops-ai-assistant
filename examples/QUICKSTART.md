# First run — fictional data, no connected accounts

Create a synthetic daily brief using only the included notes. You need an AI assistant that can accept a long prompt and return HTML; file creation is helpful but optional. No workplace accounts, Notion, or connectors are needed.

1. Open [Copy this entire fictional demo into your assistant](COPY_PASTE_DEMO.md).
2. On GitHub, choose **Raw**, then copy the entire file into a new chat with your AI assistant and send it. No edits or additional files are needed.
3. Download the generated HTML and open it in your browser. If the assistant returns HTML code, copy the complete document into a plain-text file named `synthetic-daily-brief.html` and open it.
4. Check the result against the expectations below. No account connection or permission change is part of this exercise.

## What to check

- The report visibly says **Synthetic Demo**, uses September 16, 2026, and discloses that only supplied notes were reviewed.
- There are **8 grouped completed actions** from [S1]–[S8]; the two interview schedules in [S2] count as one action.
- Both work-distribution charts total **8**, not the number of messages or open items. A reasonable classification is Recruiting 3, Onboarding 2, People Ops 1, Benefits 1, Events 1; Operational 4, Administrative 3, Strategic 1. Classification can vary if explained.
- Panel coverage, laptop delivery, and the candidate update appear as pending items, not completed outcomes.
- The hiring decision, policy adoption, enrollment outcome, and assay change remain unconfirmed. No invented savings or ROI.
- Source references use the supplied IDs. There are no invented Slack, email, or Notion links.
- Internal navigation, expandable source notes, and Print / Save as PDF work.

The [existing demonstration](daily-brief-demo.html) shows the intended presentation, rather than an exact-output test. AI-generated wording, layout, and classification can vary. This exercise checks behavior on fictional notes; it does not validate live connectors or retrieval completeness.

## Customize after your first run

Use the separate [HTML daily prompt](../prompts/html-daily.md) to configure your own run. The [fictional notes](sample-notes.md) remain available separately. The combined demo bundles that prompt with the fictional configuration and notes; keep it in sync when those sources change.
