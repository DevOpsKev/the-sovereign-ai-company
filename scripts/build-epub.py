#!/usr/bin/env python3
"""Build The Sovereign AI Company EPUB from markdown sources.

Reads structure.yaml at the repo root to determine part/chapter ordering.
Assembles front matter, parts (with part-heading markers), chapters,
epilogue, and back matter into a single markdown file, then passes it
to pandoc.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
OUTPUT_DIR = REPO_ROOT / "output"
COVER_IMAGE = REPO_ROOT / "assets" / "front-cover.png"
METADATA = REPO_ROOT / "metadata.yaml"
STRUCTURE = REPO_ROOT / "structure.yaml"
CSS = REPO_ROOT / "epub.css"

BOOK_SLUG = "sovereign-ai-company"

# Roman numerals for part numbering (1–10 covers any realistic book)
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def check_deps():
    """Verify pandoc is available."""
    try:
        subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            check=True,
        )
    except FileNotFoundError:
        print("Error: pandoc not found. Run scripts/setup-deps.sh first.")
        sys.exit(1)


def load_structure() -> dict:
    """Load structure.yaml from the repo root."""
    if not STRUCTURE.exists():
        print(f"Error: {STRUCTURE} not found.")
        sys.exit(1)
    with STRUCTURE.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def roman(n: int) -> str:
    """Convert an integer to a Roman numeral (1–10)."""
    return ROMAN[n] if 0 < n < len(ROMAN) else str(n)


def read_file(relative_path: str) -> str | None:
    """Read a content file relative to CONTENT_DIR."""
    path = CONTENT_DIR / relative_path
    if not path.exists():
        print(f"  Warning: {relative_path} not found, skipping")
        return None
    return path.read_text(encoding="utf-8")


def part_heading(part: dict) -> str:
    """Build the markdown H1 that marks a part boundary in the EPUB."""
    num = roman(part["number"])
    title = part["title"]
    # The .part class is styled by epub.css to distinguish parts visually.
    # .unnumbered prevents pandoc from adding its own numbering.
    return f"# Part {num} — {title} {{.part .unnumbered}}\n"


def assemble_markdown(structure: dict) -> str:
    """Assemble all content into a single markdown string for pandoc."""
    sections: list[str] = []

    # Front matter
    print("  Front matter:")
    for f in structure.get("front_matter", []):
        content = read_file(f)
        if content is None:
            continue
        sections.append(content.strip())
        print(f"    [ok] {f}")

    # Parts + chapters
    for part in structure.get("parts", []):
        part_dir = part["dir"]
        print(f"  Part {part['number']} — {part['title']}:")
        sections.append(part_heading(part).strip())
        for chap_file in part["chapters"]:
            content = read_file(f"{part_dir}/{chap_file}")
            if content is None:
                continue
            sections.append(content.strip())
            print(f"    [ok] {chap_file}")

    # Epilogue
    epilogue_file = structure.get("epilogue")
    if epilogue_file:
        print("  Epilogue:")
        content = read_file(epilogue_file)
        if content is not None:
            sections.append(content.strip())
            print(f"    [ok] {epilogue_file}")

    # Back matter
    print("  Back matter:")
    for f in structure.get("back_matter", []):
        content = read_file(f)
        if content is None:
            continue
        sections.append(content.strip())
        print(f"    [ok] {f}")

    return "\n\n".join(sections)


def main():
    """Build the EPUB."""
    print("Building The Sovereign AI Company EPUB...\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{BOOK_SLUG}.epub"

    structure = load_structure()
    print("Scanning content...")
    assembled = assemble_markdown(structure)

    if not assembled.strip():
        print("Error: no content found.")
        sys.exit(1)

    # Write assembled markdown to a temp file so pandoc can consume it.
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(assembled)
        assembled_path = Path(tmp.name)

    try:
        cmd = [
            "pandoc",
            "--output", str(output_file),
            "--metadata-file", str(METADATA),
            "--css", str(CSS),
            "--toc",
            "--toc-depth=1",
            str(assembled_path),
        ]

        if COVER_IMAGE.exists():
            cmd.insert(-1, f"--epub-cover-image={COVER_IMAGE}")
        else:
            print(f"  Warning: cover image not found at {COVER_IMAGE}, building without one")

        print(f"\n  Sources: {len(structure.get('parts', []))} parts, "
              f"{sum(len(p['chapters']) for p in structure.get('parts', []))} chapters")
        subprocess.run(cmd, check=True)
    finally:
        assembled_path.unlink(missing_ok=True)

    size_kb = output_file.stat().st_size / 1024
    print(f"  Output: {output_file.name} ({size_kb:.0f} KB)")
    print("\nDone.")


if __name__ == "__main__":
    check_deps()
    main()
