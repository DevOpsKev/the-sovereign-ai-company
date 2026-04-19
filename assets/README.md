# Assets

Drop cover images into this folder before the first build. The build scripts
reference these three files by name:

| File                     | Used by           | Purpose                                       |
| ------------------------ | ----------------- | --------------------------------------------- |
| `front-cover.png`        | `build-epub.py`   | EPUB cover (embedded in the .epub file)       |
| `front-cover-pdf.png`    | `build-pdf.py`    | Screen PDF full-bleed front cover             |
| `back-cover-pdf.png`     | `build-pdf.py`    | Screen PDF full-bleed back cover              |

## Sizing

The PDF trim size is **5.25in × 8in** (standard trade paperback), set in
`build/pdf/template.tex`. The `front-cover-pdf.png` and `back-cover-pdf.png`
images are stretched to the full paper size via `\paperwidth` and
`\paperheight`, so supply them at the correct aspect ratio (5.25:8) and a
print-safe resolution (300 DPI → 1575 × 2400 px).

`front-cover.png` is used for the EPUB cover; common reader guidance is at
least 1600 px on the long edge at a 1:1.5–1:1.6 aspect ratio.

## Missing files

If a cover image is missing:

- `build-epub.py` will print a warning and build without an embedded cover.
- `build-pdf.py` will skip the cover page (screen variant) and back cover
  page respectively — the print variant never includes covers anyway.

This means the build pipeline won't fail just because you haven't finalised
the art yet.
