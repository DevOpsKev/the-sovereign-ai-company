#!/usr/bin/env python3
"""
The Sovereign AI Company PDF Build Script

Reads structure.yaml at the repo root to determine part/chapter ordering.
Assembles front matter, parts (with raw-LaTeX \\part{} markers), chapters,
epilogue, and back matter into a single markdown file with raw LaTeX
injections for structural control, then passes it to pandoc + XeLaTeX.

Usage:
  python scripts/build-pdf.py [--git-hash HASH] [--build-date DATE] [--variant screen|print|both]

Output:
  output/sovereign-ai-company.pdf        (screen: RGB, cover, clickable links)
  output/sovereign-ai-company-print.pdf  (print: no cover, black links)
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

# === CONFIGURATION ===

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
METADATA_FILE = REPO_ROOT / "metadata.yaml"
STRUCTURE_FILE = REPO_ROOT / "structure.yaml"
TEMPLATE_FILE = REPO_ROOT / "build" / "pdf" / "template.tex"
COVER_IMAGE = REPO_ROOT / "assets" / "front-cover-pdf.png"
BACK_COVER_IMAGE = REPO_ROOT / "assets" / "back-cover-pdf.png"
OUTPUT_DIR = REPO_ROOT / "output"
BOOK_TITLE = "sovereign-ai-company"

# Fonts — TeX Gyre ships with texlive-fonts-recommended
MAIN_FONT = "TeX Gyre Pagella"      # Palatino — elegant prose serif
SANS_FONT = "TeX Gyre Heros"        # Helvetica — clean headings
FONT_SIZE = "10.5pt"


def check_deps():
    """Verify pandoc and xelatex are available."""
    for cmd, pkg in [("pandoc", "pandoc"), ("xelatex", "texlive-xetex")]:
        try:
            subprocess.run([cmd, "--version"], capture_output=True, check=True)
        except FileNotFoundError:
            print(f"Error: {cmd} not found. Install {pkg}.")
            sys.exit(1)


def load_structure() -> dict:
    """Load structure.yaml from the repo root."""
    if not STRUCTURE_FILE.exists():
        print(f"Error: {STRUCTURE_FILE} not found.")
        sys.exit(1)
    with STRUCTURE_FILE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def raw_latex(code: str) -> str:
    """Wrap LaTeX code in a pandoc raw block."""
    return f"\n```{{=latex}}\n{code}\n```\n"


def preprocess_front_matter(content: str) -> str:
    """Prepare front matter markdown for PDF.

    - Strip pandoc div wrappers (::: {.class} ... :::)
    - Mark headings as unnumbered and unlisted (keep out of TOC)
    """
    content = re.sub(r'^:::\s*\{[^}]*\}\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^:::\s*$', '', content, flags=re.MULTILINE)

    content = re.sub(
        r'^(#+\s+.+?)(\s*\{[^}]*\})?\s*$',
        r'\1 {.unnumbered .unlisted}',
        content,
        flags=re.MULTILINE,
    )

    return content.strip()


def preprocess_back_matter(content: str) -> str:
    """Prepare back matter markdown for PDF.

    - Mark top-level heading as unnumbered (but keep in TOC)
    """
    content = re.sub(
        r'^(#\s+.+?)(\s*\{[^}]*\})?\s*$',
        r'\1 {.unnumbered}',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    return content.strip()


def read_file(relative_path: str) -> str | None:
    """Read a content file, returning None if missing."""
    path = CONTENT_DIR / relative_path
    if not path.exists():
        print(f"  Warning: {relative_path} not found, skipping")
        return None
    return path.read_text(encoding="utf-8")


def assemble_markdown(structure: dict) -> str:
    """Assemble all content into a single markdown string.

    Structure:
      [front matter — unnumbered, not in TOC]
      \\tableofcontents
      \\mainmatter
      [for each part:
         \\part{Title}
         [chapters]]
      [epilogue — unnumbered chapter, in TOC]
      \\backmatter
      [references]
    """
    sections: list[str] = []

    # --- Front matter ---
    print("  Front matter:")
    for f in structure.get("front_matter", []):
        content = read_file(f)
        if content is None:
            continue
        processed = preprocess_front_matter(content)

        # Copyright page: small text, pushed to bottom
        if "copyright" in f.lower():
            processed = (
                raw_latex(
                    "\\thispagestyle{empty}\n"
                    "\\vspace*{\\fill}\n"
                    "\\begingroup\\small\\setlength{\\parskip}{4pt}"
                )
                + "\n\n"
                + processed
                + "\n\n"
                + raw_latex("\\endgroup\\cleardoublepage")
            )

        sections.append(processed)
        print(f"    [ok] {f}")

    # --- TOC + mainmatter switch ---
    sections.append(raw_latex("\\tableofcontents\n\\mainmatter"))

    # --- Parts + chapters ---
    for part in structure.get("parts", []):
        part_dir = part["dir"]
        part_title = part["title"]
        print(f"  Part {part['number']} — {part_title}:")

        # Escape LaTeX special characters in the part title. Book titles
        # shouldn't contain these, but be defensive.
        safe_title = (
            part_title
            .replace("\\", "\\textbackslash{}")
            .replace("&", "\\&")
            .replace("%", "\\%")
            .replace("$", "\\$")
            .replace("#", "\\#")
            .replace("_", "\\_")
        )
        sections.append(raw_latex(f"\\part{{{safe_title}}}"))

        for chap_file in part["chapters"]:
            content = read_file(f"{part_dir}/{chap_file}")
            if content is None:
                continue
            sections.append(content.strip())
            print(f"    [ok] {chap_file}")

    # --- Epilogue (unnumbered, in TOC, still in mainmatter) ---
    epilogue_file = structure.get("epilogue")
    if epilogue_file:
        print("  Epilogue:")
        content = read_file(epilogue_file)
        if content is not None:
            # Mark the H1 as unnumbered so LaTeX doesn't prefix it and it
            # appears in the TOC as a peer of the chapters.
            processed = re.sub(
                r'^(#\s+.+?)(\s*\{[^}]*\})?\s*$',
                r'\1 {.unnumbered}',
                content,
                count=1,
                flags=re.MULTILINE,
            )
            sections.append(processed.strip())
            print(f"    [ok] {epilogue_file}")

    # --- Back matter ---
    print("  Back matter:")
    sections.append(raw_latex("\\backmatter\n\\raggedright"))
    for f in structure.get("back_matter", []):
        content = read_file(f)
        if content is None:
            continue

        # Insert zero-width spaces after / - _ in URLs so LaTeX can break them
        def add_url_breaks(match):
            url = match.group(0)
            url = url.replace("/", "/\u200B")
            url = url.replace("-", "-\u200B")
            url = url.replace("_", "_\u200B")
            return url

        content = re.sub(
            r'https?://[^\s)\]>]+',
            add_url_breaks,
            content,
        )
        sections.append(preprocess_back_matter(content))
        print(f"    [ok] {f}")

    return "\n\n".join(sections)


def build_pdf(variant: str, git_hash: str | None, build_date: str | None, structure: dict):
    """Build a single PDF variant."""
    is_print = variant == "print"
    suffix = "-print" if is_print else ""
    output_file = OUTPUT_DIR / f"{BOOK_TITLE}{suffix}.pdf"

    print(f"\n{'='*60}")
    print(f"  Building: {output_file.name} ({variant})")
    print(f"{'='*60}\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Scanning content...")
    assembled = assemble_markdown(structure)

    if not assembled.strip():
        print("ERROR: No content found.")
        sys.exit(1)

    assembled_path = OUTPUT_DIR / "assembled.md"
    assembled_path.write_text(assembled, encoding="utf-8")
    print(f"\nAssembled markdown: {assembled_path}")
    print(f"Length: {len(assembled)} chars, {assembled.count(chr(10))} lines")

    cmd = [
        "pandoc",
        str(assembled_path),
        "--pdf-engine=xelatex",
        "--top-level-division=chapter",
        "-o",
        str(output_file),
    ]

    if TEMPLATE_FILE.exists():
        cmd.append(f"--template={TEMPLATE_FILE}")
    if METADATA_FILE.exists():
        cmd.append(f"--metadata-file={METADATA_FILE}")

    cmd.extend(
        [
            f"--variable=mainfont:{MAIN_FONT}",
            f"--variable=sansfont:{SANS_FONT}",
            f"--variable=fontsize:{FONT_SIZE}",
        ]
    )

    if is_print:
        cmd.append("--variable=print:true")
    else:
        if COVER_IMAGE.exists():
            cmd.extend(
                [
                    "--variable=include-cover:true",
                    f"--variable=cover-image:{COVER_IMAGE}",
                ]
            )
        if BACK_COVER_IMAGE.exists():
            cmd.extend(
                [
                    "--variable=include-back-cover:true",
                    f"--variable=back-cover-image:{BACK_COVER_IMAGE}",
                ]
            )

    if git_hash:
        cmd.append(f"--variable=git-hash:{git_hash}")
    if build_date:
        cmd.append(f"--variable=build-date:{build_date}")

    print(f"\nPandoc command:\n  {' '.join(cmd)}\n")
    print("Running pandoc + xelatex...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"ERROR:\n{result.stderr}")
        print(f"\nDEBUG: Check {assembled_path} for the assembled markdown")
        sys.exit(1)

    size_kb = output_file.stat().st_size / 1024
    print(f"Done: {output_file} ({size_kb:.1f} KB)")

    assembled_path.unlink(missing_ok=True)

    return output_file


def main():
    parser = argparse.ArgumentParser(description="Build The Sovereign AI Company PDFs")
    parser.add_argument("--git-hash", help="Short git commit hash")
    parser.add_argument("--build-date", help="Build date (YYYY-MM-DD)")
    parser.add_argument(
        "--variant",
        choices=["screen", "print", "both"],
        default="both",
        help="Which variant(s) to build (default: both)",
    )
    args = parser.parse_args()

    structure = load_structure()

    variants = ["screen", "print"] if args.variant == "both" else [args.variant]
    for v in variants:
        build_pdf(v, args.git_hash, args.build_date, structure)

    print(f"\n{'='*60}")
    print("  All builds complete.")
    print(f"{'='*60}")


if __name__ == "__main__":
    check_deps()
    main()
