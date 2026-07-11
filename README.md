# adam-codex-skills

Personal Codex skills monorepo.

## Layout

```text
skills/
  pdf-ingestion-workflow/
    SKILL.md
    agents/openai.yaml
    scripts/
    references/
scripts/
  link-skills.sh
```

## Install Locally

Link all skills into Codex:

```bash
/Users/adamlien/Documents/Workspace/adam-codex-skills/scripts/link-skills.sh
```

## Current Skills

- `pdf-ingestion-workflow`: classify PDFs, probe pages, benchmark extraction paths, and choose MarkItDown/PyMuPDF/pypdf/OCR workflows.

## Project Docs

- `CONTEXT.md`: domain glossary for this skills repo.
- `docs/wiki/llm-wiki.md`: compact LLM handoff wiki for future Codex tasks.
- `docs/backlog/ai-content-and-skills-backlog.md`: active backlog for skills, AI content radar, and monetization work.
- `docs/adr/`: architectural decisions.
