---
name: pdf-ingestion-workflow
description: Classify, extract, benchmark, and validate PDF content for Markdown conversion, RAG ingestion, OCR fallback, and PDF editing decisions. Use when handling PDFs, thick PDFs, scanned/image PDFs, MarkItDown conversion, PyMuPDF/pypdf/pdfplumber extraction, page-aware chunks, or requests to modify PDF files.
---

# PDF Ingestion Workflow

Use this skill before converting, summarizing, chunking, editing, or benchmarking PDFs.

## Decision Flow

1. Classify the PDF before converting it.
   - Thin: 1-20 pages.
   - Thick: more than 20 pages.
   - Text PDF: selectable text is available on most sampled pages.
   - Image/scanned PDF: sampled pages have little or no extractable text.
   - Layout-sensitive: contracts, quotes, invoices, financial tables, slides, catalogs.
2. Probe pages first.
   - Use `scripts/probe_pdf.py` for page count, sampled page text counts, low-text pages, and extraction warnings.
   - For thick PDFs, sample first 3, middle 3, and last 3 pages before attempting whole-document processing.
3. Choose the extraction path.
   - Use PyMuPDF as the baseline text extractor.
   - Use pypdf for split/merge/rotate and as a secondary text extractor.
   - Use MarkItDown for Markdown structure, not as the only source of truth.
   - Use pdfplumber when tables or layout-sensitive extraction matters.
   - Use OCR or vision for scanned/image pages, low-text pages, or visually rich slides.
4. Benchmark risky documents.
   - Use `scripts/benchmark_pdf_extractors.py` to compare MarkItDown, PyMuPDF, and pypdf on sampled pages.
   - Treat empty output, large text deltas, and method timeouts as review flags.
5. Keep page provenance.
   - Preserve page numbers in extracted text and chunks.
   - For RAG, chunk by page or chapter and store source page ranges.

## Normal Operating Rules

- Do not feed a thick PDF to MarkItDown as one blocking operation unless the user explicitly wants a stress test.
- Do not assume successful command completion means useful extraction; inspect character counts and sampled output.
- Use timeouts for per-file work so one damaged or complex PDF does not block a batch.
- If modifying a PDF, render pages to images and visually verify the result before delivery.
- Prefer generating a new polished PDF over patching an existing visually complex PDF.

## Tool Selection

- Read `references/tool-selection.md` when deciding which PDF library to use.
- Use `scripts/probe_pdf.py` for quick inspection.
- Use `scripts/benchmark_pdf_extractors.py` for extractor comparisons.

## Common Commands

Probe one PDF:

```bash
python scripts/probe_pdf.py input.pdf --json
```

Benchmark sampled extraction:

```bash
python scripts/benchmark_pdf_extractors.py input.pdf --out-dir outputs/pdf-benchmark
```

Benchmark without MarkItDown:

```bash
python scripts/benchmark_pdf_extractors.py input.pdf --skip-markitdown --out-dir outputs/pdf-benchmark
```

## Editing Guidance

- Split, merge, rotate, remove pages: use pypdf.
- Add annotations, redact, inspect page geometry, or extract images: use PyMuPDF.
- Generate a new PDF: use reportlab or HTML-to-PDF when design control matters.
- Verify final layout: render with Poppler `pdftoppm` or PyMuPDF page screenshots.
- For contracts, invoices, and quotes, keep an untouched original and write derived outputs separately.
