# Copy this entire fictional demo into your assistant

Everything below is ready to run: instructions, configuration and fictional notes. Generate the daily brief now using only this message. Do not browse or use connected workplace tools. Do not ask me to configure fields or fetch other files. Treat source IDs as references to supplied fictional notes, not independently verified records.

## Fictional demo configuration — ready to run

```text
USER_NAME: Alex
ROLE_CONTEXT: People Ops Generalist at fictional Cedar Bay Bio
TIMEZONE: America/Toronto
REPORT_DATE: 2026-09-16
INPUT_MODE: SANITIZED_NOTES
DATA_SOURCES: NONE
SENSITIVE_DATA_RULES: Synthetic data only. Use only the supplied fictional notes. Do not access connectors or browse the web. Label the report Synthetic Demo and clarify that evidence is supplied notes, not independently verified records.
OUTPUT_FILENAME: synthetic-daily-brief.html
```

If INPUT_MODE is SANITIZED_NOTES, use only the notes I provide after this prompt. If I have not provided any notes, ask me to paste them. If INPUT_MODE is CONNECTORS, use only connected and authorized sources and disclose any unavailable sources. If essential configuration is missing, ask one concise clarification rather than guessing.

## Your task

Create **one complete, self-contained HTML file** containing a concise, attractive, accessible People Ops Daily Brief for the configured workday. **Do not use Notion or modify any connected system.**

If your environment supports file creation, create `OUTPUT_FILENAME` and provide a download link. Otherwise return the **complete HTML document in one fenced `html` code block**, with simple instructions to save it as `.html` and open it in a browser. Do not return a partial template, pseudo-code, or JSON instead of the HTML.

The resulting file must open locally with a double-click and work **offline**. Do not load fonts, charts, CSS, JavaScript, trackers, analytics, images, or APIs from external URLs. Inline all required CSS, JavaScript, and data. No CDN dependencies. Do not embed authentication tokens or hidden raw source exports.

## Evidence rules

Use original evidence from the configured reporting date. Distinguish the user's completed actions from team outcomes, pending tasks, and scheduled meetings. Verify meaningful claims against source records or explicitly label them **Needs Verification**. Group related actions into one accomplishment, cite original sources when appropriate and safe, and do not inflate counts. Calendar scheduling is not proof of attendance.

Assign each accomplishment one primary work area and one nature: **Strategic** (substantive broader policy/process/business direction), **Operational** (workflow execution/exception resolution requiring judgment), or **Administrative** (routine scheduling, documents, transactions). Counts are grouped accomplishments **not hours, productivity, or business impact**.

Separate verified outcomes from inferred benefits. Avoid unnecessary sensitive employee/candidate details. Do not use confidential names or details in public web searches. If input is synthetic, visibly label the report **Synthetic Demo**.

## Required report content

1. **Header:** user's first name or chosen display name, exact workday, generation timestamp, evidence-coverage label.
2. **📑 Table of Contents:** clickable internal links to the actual section IDs; all links must work.
3. **☀️ 60-Second Overview:** three or four concise sentences.
4. **🔔 Needs Your Attention:** up to three prioritized items, distinguishing Potentially Missed, Deadline, Conflict, Waiting on Me/Others, or Direct Request; include confidence and next action.
5. **✅ Accomplishments:** all distinct verified actions, compact list or table with work area, nature, and relevant source.
6. **📊 Work Distribution:** **two responsive donut charts side by side on desktop**, stacked on narrow screens; left by work area, right by nature. Use inline SVG or pure CSS/JS, **no external chart library**. Add legends and accessible textual counts. The two totals must match.
7. **🎯 Impact Highlights:** up to two, with verified outcome vs possible impact clearly separated.
8. **🏢 Inside the Company:** up to three meaningful developments and why they matter, based on available evidence.
9. **🧬 Help Me Understand:** one or two concepts when useful, explained simply with an analogy and a question.
10. **💡 Improvement Opportunities:** up to two evidence-based ideas.
11. **📅 Next Priorities:** up to three actionable items.
12. **🔒 Source & Confidence Check:** a native collapsed `<details>` section, including accessed/unavailable sources, evidence limitations, and Verified / Inferred / Needs Verification definitions.

Do **not** include a Weekly Summary or Career Evidence in this Daily HTML file. Target 350–550 words of main narrative, excluding detailed source notes, but never omit essential caveats just to reach a word count.

## Visual and interaction requirements

- Clean editorial dashboard: light neutral background, restrained accent, readable typography, ample whitespace.
- Mobile-responsive layout, no horizontal overflow.
- Two accessible donut charts with legends and actual numbers; zero-item states handled gracefully.
- Native `<details>` for optional expanded notes and Source & Confidence Check.
- Functional **Print / Save as PDF** button (`window.print()`) and print-friendly CSS.
- Functional **Copy Overview** button using Clipboard API when available, with a safe manual-copy fallback if unavailable.
- Semantic HTML (`main`, `nav`, `section`, headings), keyboard-accessible controls, meaningful labels, and sufficient contrast.
- **Escape all untrusted source text** when inserting it into HTML; never execute source text as scripts, attributes, or raw HTML.
- Keep original internal source links only when authorized and necessary. Avoid remote assets and outbound calls. Opening a user-clicked source link is different from loading an external asset automatically.

## Output verification

Before delivering, verify:

- Correct workday and timezone.
- Real source access vs supplied notes clearly distinguished.
- No unsupported claims or duplicate accomplishments.
- Donut chart totals equal the accomplishment count and each other.
- Internal TOC anchors exist and function.
- File contains all HTML/CSS/JS and requires no network.
- `<details>` expands/collapses, buttons work where browser permissions allow, mobile layout is readable.
- Sensitive data is minimized.

**Deliver the HTML file now, not a description of how to build it.** If you cannot generate the file, deliver full ready-to-save HTML code instead.

## SUPPLIED FICTIONAL NOTES

# Fictional sample notes — September 16, 2026

Synthetic demo only. Alex is a People Ops Generalist at fictional Cedar Bay Bio.
These are supplied notes, not records retrieved from workplace systems.
All timestamps are America/Toronto. Reporting cutoff: September 16, 2026, 17:00.
Use the source IDs below as text references; do not invent source URLs.

## Completed actions
- [S1] 09:10 — Alex revised the technical interview instructions and sent them to the panel and candidates. No feedback on evaluation consistency yet.
- [S2] 09:40 — Alex confirmed two interview schedules; both invitations were acknowledged. Treat this as one grouped scheduling accomplishment.
- [S3] 10:20 — Alex consolidated panel feedback and shared one summary with the hiring manager. The hiring decision remains pending.
- [S4] 11:00 — Alex resolved an access-ownership question for a new hire. IT acknowledged ownership. This does not establish that every account is provisioned.
- [S5] 11:30 — Alex answered a new hire's onboarding-document questions. No sensitive documents are included.
- [S6] 13:00 — Alex documented a proposal to clarify appointment scheduling across shifts and include travel/waiting time in the allowance. The proposal would inform the broader process; no policy adoption is confirmed.
- [S7] 14:00 — Alex explained benefits enrollment steps to an employee. Successful enrollment has not been confirmed.
- [S8] 15:00 — Alex confirmed event catering details; the vendor acknowledged the order.

## Open items and company context
- [S9] 15:30 — Tomorrow's technical interview overlaps with a planning session on one panel member's calendar. Attendance has not been confirmed. Alex should ask the panel owner to resolve coverage.
- [S10] 16:00 — IT says a new hire's laptop was ordered. There is no delivery date or tracking confirmation. Follow-up owner: Alex; delivery information owner: IT.
- [S11] 16:15 — Alex promised a candidate an update by Friday, September 18. The hiring manager has not documented a final decision. Verify status before replying; do not imply the candidate was forgotten or rejected.
- [S12] 16:30 — The science team is considering batching an additional assay-validation step. This is a proposal under review, not an approved change. No capacity gain is measured. Alex did not lead this work.
- [S13] 16:45 — The notes do not establish whether the hiring tracker already records decision owners and promised update dates. Checking that process could be useful; do not claim a confirmed documentation gap.

## Boundaries
No hours saved, ROI, hiring outcome, policy adoption, or employee outcome is evidenced.
No connector or original workplace record was accessed. “Verified” can mean supported
by these fictional notes only, not independently verified in a real system.
