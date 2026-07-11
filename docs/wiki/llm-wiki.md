# LLM Wiki

Last updated: 2026-07-11

## Purpose

`adam-codex-skills` is a personal Codex skills monorepo. It stores reusable AI workflows that Adam wants future Codex tasks to apply consistently instead of re-learning from chat history.

The first production workflow is `pdf-ingestion-workflow`, created after local testing showed that MarkItDown is useful but not reliable enough to be the only PDF ingestion path.

## Current Repository Shape

```text
adam-codex-skills/
  CONTEXT.md
  README.md
  requirements.txt
  scripts/
    link-skills.sh
  skills/
    pdf-ingestion-workflow/
      SKILL.md
      agents/openai.yaml
      references/tool-selection.md
      scripts/probe_pdf.py
      scripts/benchmark_pdf_extractors.py
  docs/
    adr/
      0001-use-a-skills-monorepo.md
    wiki/
      llm-wiki.md
    backlog/
      ai-content-and-skills-backlog.md
```

## Important Decisions

- Use a monorepo for Adam's skills.
- Link skills into `~/.codex/skills` instead of making the home directory the source of truth.
- Treat PDF ingestion as a workflow, not a single MarkItDown command.
- Use PyMuPDF as the PDF text extraction baseline.
- Use MarkItDown for Markdown structure, but compare it against a baseline.
- For thick PDFs, sample first/middle/last pages before whole-document work.
- Keep page provenance for RAG, summaries, and course material.

## Current Installed Skill

### `pdf-ingestion-workflow`

Use this skill when handling PDFs, thick PDFs, scanned/image PDFs, MarkItDown conversion, PyMuPDF/pypdf/pdfplumber extraction, page-aware chunks, or PDF editing decisions.

Core workflow:

```text
PDF
  -> classify
  -> page probe
  -> choose extraction path
  -> baseline with PyMuPDF
  -> optional MarkItDown conversion
  -> compare outputs
  -> OCR/vision fallback for low-text pages
  -> page-aware chunks or report
```

Representative commands:

```bash
python skills/pdf-ingestion-workflow/scripts/probe_pdf.py input.pdf --json
python skills/pdf-ingestion-workflow/scripts/benchmark_pdf_extractors.py input.pdf --out-dir outputs/pdf-benchmark
```

## Prior Evidence From 2026-07-11

General PDF test:

- 12 PDFs from `~/Downloads`.
- MarkItDown completed 12/12, but 1 PDF produced 0 characters.
- Some PDFs produced much more MarkItDown text than PyMuPDF/pypdf, suggesting possible duplicate or hidden layout text.
- Conclusion: MarkItDown is a useful converter, not a correctness guarantee.

Thick PDF test:

- 10 thick PDFs, 83-112 pages.
- Whole-document conversion was too slow and got stuck after partial progress.
- Sampled first/middle/last pages instead.
- MarkItDown was practically usable for 9/10 sampled thick PDFs.
- PyMuPDF was the most stable baseline.

## AI Development Course Context

A two-hour course outline was created around this theme:

> AI coding has moved from prompt engineering toward context engineering.

Six-layer model:

1. Planning / Spec: grill-me, Superpowers, OpenSpec.
2. Context Ingestion: MarkItDown, dbx, yt-dlp, PDF/OCR.
3. Code Context Selection: Codebase-Memory-MCP.
4. Context Compression: RTK, Headroom.
5. Agent Orchestration: Homerail, Agents SDK, subagent workflow.
6. Verification: tests, typecheck, runtime proof, human review.

This course can become content, consulting material, or internal training.

## Content Monetization Direction

Recommended positioning:

> AI development workflows and knowledge assetization.

Best early audiences:

- Small and medium business owners who need AI workflow adoption.
- Consultants, instructors, and creators who want to turn expertise into products.
- Software teams that need AI coding workflow discipline.
- Content and marketing teams that need trend radar and script generation.

Do not start as a generic AI news channel. Start as a practical AI workflow channel with evidence, experiments, and reusable systems.

## Next Best Work

Use `docs/backlog/ai-content-and-skills-backlog.md` as the active execution queue.
