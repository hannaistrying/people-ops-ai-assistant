> **Publishing note:** This repository currently contains no screenshots. Add only manually reviewed, redacted captures from the actual workflow.

# Screenshot plan for the article

## Recommended order — two-case article

1. **Problem / before:** optional schematic of scattered Slack, email, meetings, notes — **illustration, not a screenshot of private data**.
2. **Architecture:** `assets/architecture.svg` — label it a diagram.
3. **Notion hierarchy:** capture your **synthetic** Month → Week → Day toggle archive. Expand one week, collapse the rest.
4. **Daily Brief:** synthetic screenshot showing overview, Needs Attention and Accomplishments.
5. **Charts:** two real, side-by-side Notion donut chart views using synthetic counts; check both desktop and mobile.
6. **Weekly and Monthly:** synthetic weekly summary and monthly-only Career Evidence. Do not claim the real pilot produced a monthly report: QA found it absent.
7. **HTML alternative:** ready-to-use `examples/screenshots/html-desktop.png` and `html-mobile.png`, captured from the included fictional HTML demo.
8. **Prompt setup:** `examples/screenshots/prompt-configurator.png`, a real capture of the offline configurator.
9. **Parental Leave Handover:** use `examples/screenshots/parental-leave-overview.png` and `parental-leave-handover-table.png` — real captures of the included **synthetic UI mockup**, not of an actual Notion page.
10. **Transparency:** a compact QA scorecard illustrating what passed and what was incomplete, without real employee information.

## Captions you can reuse

- *Figure 1. Architecture of the People Ops AI Assistant: authorized sources, evidence checks, and two output formats.*
- *Figure 2. Example of the nested Notion archive (synthetic data).* 
- *Figure 3. Daily Brief: priorities and verified actions rather than a raw activity log (synthetic data).*
- *Figure 4. Work distribution: share of grouped accomplishments, not hours worked (synthetic data).*
- *Figure 5. HTML Edition: a local, standalone brief without Notion (synthetic data).*

## Privacy checklist before publishing

- Replace all real names, company/customer names, candidate IDs, internal URLs, email addresses, and file paths.
- Do not publish screenshots with real salary, benefits, medical, immigration, disciplinary, or performance information.
- Do not merely blur sensitive text if it could still be recovered from layers or original image metadata; preferably **recreate the screen with synthetic data**.
- Check browser tabs, bookmarks, notifications, profile photos, and page sharing indicators.
- Check alt text, image metadata, Git commit history, and README links.
- Obtain company approval if you intend to describe a real internal workflow or use its screenshots.

**The supplied HTML and parental-leave mockup screenshots are genuine captures of local synthetic demos, not screenshots of Notion or of a real employer system.**
