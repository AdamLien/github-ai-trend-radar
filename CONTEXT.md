# Adam Codex Skills

This context defines the language for Adam's personal Codex skill system: reusable workflows, scripts, and operating rules that turn repeated AI work into durable local capabilities.

## Language

**Skill Repo**:
A version-controlled repository that stores multiple Codex skills and their reusable resources.
_Avoid_: prompt folder, random skills folder

**Skill**:
A self-contained Codex capability with a `SKILL.md` entrypoint and optional scripts, references, or assets.
_Avoid_: prompt, macro

**Workflow Skill**:
A skill that tells Codex how to decide, sequence, validate, and hand off a recurring workflow.
_Avoid_: one-shot prompt

**LLM Wiki**:
A compact, source-oriented knowledge file written for future LLM sessions to quickly recover the project purpose, current decisions, and next actions.
_Avoid_: full documentation site, chat transcript

**Backlog**:
A prioritized list of next implementation steps with acceptance criteria and open questions.
_Avoid_: idea dump, TODO pile

**Content Radar**:
A feed-driven system for collecting AI development trends, clustering topics, and turning selected items into scripts, courses, or consulting material.
_Avoid_: news scraper, trend dump

**PDF Ingestion**:
The workflow for probing, extracting, comparing, and validating PDF content before using it for summaries, RAG, courses, or knowledge bases.
_Avoid_: PDF conversion

**Page-Aware Chunk**:
An extracted content chunk that preserves source page numbers or page ranges for verification and citation.
_Avoid_: plain chunk

**Baseline Extractor**:
The first trusted text extraction path used as a comparison anchor before accepting secondary conversion output.
_Avoid_: final truth
