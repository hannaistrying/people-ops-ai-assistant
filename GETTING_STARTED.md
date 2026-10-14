# Getting started — People Ops AI Assistant

No coding is required. This is a **prompt-based workflow**, not an installed application or an automatically running agent.

## 1. Check permissions first

Confirm your organization's AI and data-handling policies. Use only approved AI tools and connectors. Never paste sensitive employee records or confidential meeting notes into a public repository or an unapproved service. Connector availability and read/write capabilities depend on your plan, organization, and platform.

## 2. Choose your inputs

You can use any approved combination of sources. Example setup:

| Source | What it contributes | Required? |
| --- | --- | --- |
| Slack | Team conversations, decisions and follow-ups | No |
| Gmail | Email requests and commitments | No |
| Notion | Policy/project context; optionally a **private** report destination | No |
| Granola | Meeting notes and decisions | No |
| Calendar | Meeting context (a scheduled meeting is **not** proof it occurred) | No |

If a connector is unavailable, remove it from the configuration and have the assistant disclose the gap. Do **not** claim an unavailable source was reviewed.

## 3. Choose an output

- **Standalone HTML (simplest):** [prompts/html-daily.md](prompts/html-daily.md) — produces a daily report that you can save and open in a browser. Notion not required.
- **Notion ongoing:** [prompts/notion-ongoing.md](prompts/notion-ongoing.md) — requests daily reports and completed weekly/monthly summaries, subject to connector write support.
- **Historical Notion backfill (advanced):** [prompts/notion-backfill.md](prompts/notion-backfill.md) — asks the assistant to reconstruct prior periods. Backfills may be incomplete and must be checked.

You can also use [setup.html](setup.html), an **offline** prompt configurator. It does not connect to your company systems.

## 4. Customize and run

1. Open the chosen `.md` prompt, copy its full contents into ChatGPT Work or another compatible assistant.
2. Replace every `{{PLACEHOLDER}}` with your role, reporting dates, timezone, and **actually connected** tools. Never use example URLs or private links from someone else's setup.
3. If using Notion, specify only a private destination you are authorized to write to; review its sharing settings before saving anything.
4. Run a **single completed workday** first. Review each claimed accomplishment, source, pending item and classification.
5. Adjust the prompt based on real output; do not assume the first result is complete.

## 5. Expand carefully

For a six-month self-review, use [prompts/performance-review.md](prompts/performance-review.md). For weekly or monthly trends, use [prompts/period-summary.md](prompts/period-summary.md). Both require sufficiently complete, verified evidence.

## 6. Know what success looks like

A useful report distinguishes **completed vs planned**, **verified vs inferred**, and **business impact vs possible impact**. It may flag *Things You Might Have Missed*, *Waiting on Me / Others*, and *Policy Improvement Signals*, but it cannot decide HR policy or performance outcomes.

Try the fictional [HTML example](examples/daily-brief-demo.html) to see the intended presentation. This example is not evidence that a connector run has succeeded.

Before sharing, use the [quality checklist](docs/quality-checklist.md).
