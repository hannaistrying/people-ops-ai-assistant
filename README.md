# People Ops AI Assistant 🌿

**A practical, no-code starter kit for turning authorized workplace context into a useful People Ops daily brief, work insights, and evidence for performance reviews.**

Built around a real People Ops workflow. You can adapt the prompts to ChatGPT Work or another assistant (such as Claude) **if your plan, organization, and connected tools support the required access and actions**.

## What it helps with

- **Daily progress and business impact:** capture completed work and its observed outcomes, not just meetings or to-do lists.
- **Work mix:** distinguish HR / People Ops work from administrative, operational, and leadership-support work. Counts are not timesheets.
- **Company context:** surface relevant developments from conversations and documents you are allowed to access, and explain why they matter.
- **Industry vocabulary:** explain unfamiliar biotech or other domain terminology in accessible language, using analogies.
- **HR policy improvement signals:** identify recurring employee questions and possible documentation gaps for **human review**, without editing policies autonomously.
- **Performance-review evidence:** collect source-backed accomplishments for later six-month or annual reviews.
- **Things You Might Have Missed / Waiting on Me or Others:** surface follow-ups, owners, and blockers, with explicit uncertainty.

## How it works

**Connect your tools → customize a prompt → run the assistant → review the evidence → save a report.**

For example, you might connect **Slack** (team communication), **Gmail** (email), **Notion** (documentation and optional report destination), and **Granola** (meeting notes). These are **examples, not mandatory dependencies**. Connector availability, permissions, and capabilities vary by platform and organization.

The prompts are **not** an installed agent, an automatic scheduled workflow, or an HR decision-making system. You initiate runs in your AI assistant, unless you separately configure supported scheduling.

## Get started in 3 minutes

1. Review your company's AI and data-handling rules. Connect only approved services with least-privilege access.
2. Open the [offline prompt configurator](setup.html) or choose one of the prompt files below. Replace the `{{PLACEHOLDER}}` values for your role, sources, reporting period, and destination.
3. Run the prompt, review cited evidence and uncertainties, and correct any misattributions before sharing or saving.

| Workflow | Output | Prompt |
| --- | --- | --- |
| **Notion ongoing** | Daily reports, weekly/monthly aggregation when supported | [notion-ongoing.md](prompts/notion-ongoing.md) |
| **Notion backfill** | Historical archive with checkpoints | [notion-backfill.md](prompts/notion-backfill.md) |
| **Standalone HTML** | Downloadable daily brief, no Notion needed | [html-daily.md](prompts/html-daily.md) |

See [Customization](docs/customization.md) and [Quality checklist](docs/quality-checklist.md).

## Example and screenshots

[Open the fictional HTML example](examples/daily-brief-demo.html) by downloading it locally. **This example is synthetic, not a screenshot of the author's real workplace.**

Actual workflow screenshots will be added only after a manual privacy review. See [Screenshot guidelines](docs/screenshots.md). Until then, the repository intentionally contains no screenshots.

## Data safety and accuracy

- **Never upload real employee/candidate records, internal Slack threads, meeting notes, tokens, or private Notion links to GitHub.**
- Only retrieve information the current user is authorized to see. Prompt instructions are not access controls.
- Distinguish **Verified / Inferred / Needs Verification**; do not invent business impact or mark future work as completed.
- AI-generated insights about policy gaps or people processes require human review. Do not automate employment decisions.
- Long historical backfills may be incomplete. The original pilot's Notion backfill was **partial** (9 of 22 weekdays, 2 of 5 weeks, no monthly summary). Do not present it as production-ready.

## Project structure

```text
setup.html                 Offline prompt configurator
prompts/
  notion-ongoing.md        Daily / weekly / monthly workflow
  notion-backfill.md       Historical backfill with checkpoints
  html-daily.md            Single-run HTML daily brief
examples/
  daily-brief-demo.html    Fictional example (not real company data)
  screenshots/README.md   Placeholder for reviewed real captures
assets/
  architecture.svg        Workflow diagram
docs/
  customization.md        How to personalize
  quality-checklist.md    Quality and accuracy checks
  screenshots.md          Redaction and publication checklist
  github-publish.md       Upload instructions
tests/
  test_demo.py            Basic demo checks
```

## License

[MIT](LICENSE). Contributions are welcome, but never submit real employee data or internal company materials.

> **Separate project:** Parental Leave AI Handover will have its own repository, documentation, and templates. It is intentionally not included here.
