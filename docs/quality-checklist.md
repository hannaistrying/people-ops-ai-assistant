# Quality and release checklist

## Evidence

- [ ] Reporting timezone and historical windows are correct.
- [ ] Original records, not previous AI summaries, support material claims.
- [ ] User actions are separated from team outcomes, plans, and meeting invitations.
- [ ] Later outcomes are not backdated.
- [ ] Counts are deduplicated and reconcile in both work-distribution charts.
- [ ] Confidence labels are accurate; missing source access is disclosed.

## Notion

- [ ] Destination is explicitly authorized and has appropriate access.
- [ ] Month → Week → Day nesting exists with no duplicates.
- [ ] Daily briefs and short weekly/monthly summaries are distinct.
- [ ] Career Evidence appears **only** monthly.
- [ ] Native date mentions, TOC, and chart layout are tested **in the actual UI**.
- [ ] Source & Confidence is a collapsed toggle when supported.
- [ ] All writes were verified; interrupted backfills have a checkpoint.

## HTML

- [ ] File opens offline with no network calls or external libraries.
- [ ] TOC links and `<details>` sections work.
- [ ] Two charts reconcile and remain readable on mobile.
- [ ] Print/PDF view is legible.
- [ ] Output is based on actual accessible sources or clearly marked synthetic notes.
- [ ] Sensitive data is not accidentally saved to a public folder.

## Portfolio

- [ ] All screenshots use synthetic/redacted data and show no real links, addresses, IDs, or confidential details.
- [ ] Results and limitations are described honestly; no production-readiness claim without completed QA.
- [ ] Git history, filenames, image metadata, and commit messages contain no private information.
