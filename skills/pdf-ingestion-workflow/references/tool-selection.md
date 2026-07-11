# PDF Tool Selection

## Extraction

| Task | Preferred Tool | Notes |
|---|---|---|
| Baseline text extraction | PyMuPDF | Fast and reliable for page-aware text. |
| Secondary text extraction | pypdf | Useful for comparison; can fail on some malformed PDFs. |
| Markdown conversion | MarkItDown | Good for structure, but must be compared against a baseline. |
| Tables | pdfplumber | Use when rows, columns, invoices, or financial tables matter. |
| Scanned pages | OCR or vision | Do not rely on text extractors when page text count is low. |

## Modification

| Task | Preferred Tool | Notes |
|---|---|---|
| Split, merge, rotate, delete pages | pypdf | Low risk for page-level operations. |
| Redact, annotate, inspect geometry | PyMuPDF | Verify visually after each edit. |
| Generate new PDF | reportlab | Best when structured layout matters. |
| Validate rendering | Poppler or PyMuPDF | Render pages to PNG and inspect. |

## Flags That Need Human Review

- MarkItDown output is empty.
- MarkItDown output differs from PyMuPDF by more than 50 percent in character count.
- More than 25 percent of sampled pages have fewer than 80 extractable characters.
- Any method times out on a sampled page set.
- PDF contains financial, legal, invoice, medical, or HR content.
