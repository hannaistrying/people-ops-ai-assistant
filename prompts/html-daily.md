# People Ops AI Assistant — One-Run HTML Daily Brief (No Notion)

> **Copy this prompt, edit the fields, run it once, and open the resulting HTML file locally.** No Notion account or Notion connector required. The AI assistant needs either authorized source access **or** your sanitized notes. A downloadable file requires an assistant environment that can create files; otherwise save the returned HTML code manually.

## 🔧 EDIT BEFORE RUNNING

```text
USER_NAME: {{USER_NAME}}
ROLE_CONTEXT: {{ROLE_CONTEXT}}
TIMEZONE: {{TIMEZONE}}                     # e.g. America/Toronto
REPORT_DATE: {{REPORT_DATE}}               # YYYY-MM-DD or LAST_COMPLETED_WORKDAY
INPUT_MODE: {{INPUT_MODE}}                 # CONNECTORS | SANITIZED_NOTES
DATA_SOURCES: {{DATA_SOURCES}}             # actually accessible sources, or NONE
SENSITIVE_DATA_RULES: {{SENSITIVE_DATA_RULES}}
OUTPUT_FILENAME: {{OUTPUT_FILENAME}}       # e.g. daily-brief.html
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
