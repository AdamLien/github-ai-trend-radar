# AI Content And Skills Backlog

This backlog converts the 2026-07-11 discussion into executable work. It intentionally keeps open questions visible instead of pretending the plan is fully settled.

## Operating Assumptions

- Adam wants a reusable skill system, not isolated one-off prompts.
- The first monetizable content direction is AI workflow and knowledge assetization.
- The first technical proof point is PDF/document ingestion with measurable reliability.
- Trend monitoring should support content creation, courses, and consulting, not become a generic news aggregator.

## Open Questions To Grill Before Building Too Much

1. Primary buyer: small business owner, consultant/creator, software team, or content team?
2. First paid offer: workshop, course, template pack, consulting diagnostic, or done-for-you system?
3. Primary language and market: Taiwan Mandarin, global English, or bilingual?
4. Content channel priority: YouTube, newsletter, short video, live workshop, or internal enterprise sales?
5. Tolerance for automation risk: fully manual curation first, or semi-automated daily radar immediately?

## Milestone 1: Stabilize The Skills Monorepo

Goal: make `adam-codex-skills` reliable as the source of truth for local Codex skills.

Tasks:

- [x] Create `adam-codex-skills` repository.
- [x] Add `pdf-ingestion-workflow` skill.
- [x] Add `link-skills.sh`.
- [x] Link `pdf-ingestion-workflow` into `~/.codex/skills`.
- [ ] Add a validation script that runs `quick_validate.py` with the required dependencies.
- [ ] Add a smoke test command for each skill script.
- [ ] Decide whether to commit generated test outputs or keep them ignored.

Acceptance criteria:

- A new Codex task can discover `$pdf-ingestion-workflow`.
- `probe_pdf.py` and `benchmark_pdf_extractors.py` run against a known PDF.
- Repo README explains installation and validation.

## Milestone 2: Turn PDF Workflow Into A Reusable Demo

Goal: turn the PDF ingestion work into a repeatable demo for content and consulting.

Tasks:

- [ ] Create a sanitized sample PDF set.
- [ ] Create demo output: probe report, benchmark CSV, and final recommendation.
- [ ] Add a `demo-pdf-ingestion.md` walkthrough.
- [ ] Record the failure cases: empty MarkItDown output, low-text pages, thick PDF timeout.
- [ ] Add a checklist for when to escalate to OCR/vision.

Acceptance criteria:

- A viewer can understand why MarkItDown alone is insufficient.
- The demo shows measurable comparison between MarkItDown, PyMuPDF, and pypdf.
- The demo can become a YouTube episode or workshop exercise.

## Milestone 3: Build AI Content Radar MVP

Goal: collect AI development trends from RSS/API sources into daily Markdown digests.

Tasks:

- [ ] Create `ai-content-radar` repo or add a new skill/references folder after deciding scope.
- [ ] Draft `feeds.yaml` with primary sources.
- [ ] Fetch RSS/Atom feeds into SQLite.
- [ ] Support YouTube channel RSS.
- [ ] Support GitHub `releases.atom`.
- [ ] Support HNRSS keyword feeds.
- [ ] Support arXiv RSS/API feeds.
- [ ] Generate daily Markdown digest.
- [ ] Add manual relevance scoring fields.

Acceptance criteria:

- Daily digest groups items by source type and topic.
- Each item preserves title, URL, source, published time, and tags.
- The workflow distinguishes primary sources from commentary.

## Milestone 4: Define The First Monetizable Offer

Goal: convert expertise into a clear paid offer.

Candidate offers:

- AI workflow diagnostic for small businesses.
- AI content radar setup for creators or marketing teams.
- PDF/document ingestion and knowledge-base setup.
- AI coding workflow workshop for software teams.
- Two-hour course: AI development toolchain from ingestion to verification.

Tasks:

- [ ] Pick one buyer segment.
- [ ] Write one landing-page promise.
- [ ] Define before/after outcome.
- [ ] Define deliverables and price range.
- [ ] Create one case-study-style demo from the PDF ingestion workflow.
- [ ] Create one course outline from `AI開發工具鏈兩小時課程講稿.md`.

Acceptance criteria:

- Offer can be explained in one sentence.
- Buyer pain is concrete.
- Deliverable is measurable within 1-2 weeks.

## Milestone 5: Add More Skills Only After Reuse Is Proven

Goal: avoid skill sprawl.

Candidate future skills:

- `ai-content-radar-workflow`
- `youtube-research-workflow`
- `codebase-memory-workflow`
- `dbx-readonly-investigation`
- `course-script-builder`

Rule:

Create a new skill only when the workflow repeats at least three times or has enough risk that deterministic scripts/guardrails are justified.

Acceptance criteria:

- Every new skill has a clear trigger, one owner workflow, validation path, and no duplicated instructions.
