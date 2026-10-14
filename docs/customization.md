# Customize the prompts before running

Every prompt starts with an **EDIT BEFORE RUNNING** block. Search for `{{` to find all variables.

| Variable | Required | Example (fictional) | Why it matters |
| --- | --- | --- | --- |
| `{{USER_NAME}}` | Yes | Alex | Whose work is being summarized |
| `{{ROLE_CONTEXT}}` | Yes | People Ops Generalist at a biotech startup | Relevant scope, categories, terminology |
| `{{TIMEZONE}}` | Yes | America/Toronto | Correct day boundaries and deadlines |
| `{{DATA_SOURCES}}` | Yes | Slack, Gmail, Calendar, Notion; no Granola | Never assume a connector is installed |
| `{{REPORT_DATE}}` | HTML | most recent completed workday | Date of the accomplishments, not necessarily generation date |
| `{{NOTION_PAGE_URL}}` | Notion | https://www.notion.so/... | **Only** authorized write destination |
| `{{REPORT_MONTH}}` | Backfill | 2026-09 | Historical month to process |
| `{{WORKWEEK_DAYS}}` | Notion | Monday–Friday | Weekend/holiday behavior |
| `{{SENSITIVE_DATA_RULES}}` | Yes | Omit health, pay, immigration and performance details | Privacy constraints |
| `{{INPUT_MODE}}` | HTML | CONNECTORS or SANITIZED_NOTES | Whether to retrieve data or use user-provided notes |

### Connectors

The prompts are **connector-agnostic**. Examples such as Slack, Gmail, Notion, Granola and Google Calendar are suggestions, not prerequisites. Change the list to tools you actually have. If a source cannot be accessed, the report must say so; it must not claim to have searched it.

### Notion permissions

1. Create a private **test page** before attempting a write.
2. Confirm the page and any supporting chart database permissions manually; a connector may not expose sharing settings.
3. Start with read-only analysis. Grant the narrowest possible write permission **only** to the destination when your integration supports that scope.
4. Use a synthetic dataset for public screenshots. **Do not publish your real Notion page URL or internal source links.**

### What “one-click HTML” means

The HTML prompt asks an AI assistant to produce a downloadable, standalone `.html` file in one run. After the file exists, double-click/open it in a browser. It does **not** install connectors, access private accounts without permission, or run unattended. If the assistant cannot create a file, it should return full HTML code that the user can save as `.html`.

### Data quality

An accomplishment is one meaningfully grouped, **verified** completed action. Counts are not standardized time or productivity measures. Distinguish administrative (routine processing), operational (executing or resolving a workflow with judgment), and strategic (substantive input to broader policy/process/business direction). Track later outcomes on their actual dates.
