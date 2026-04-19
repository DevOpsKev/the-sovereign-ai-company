#!/usr/bin/env python3
"""Build The Sovereign AI Company EPUB from markdown sources."""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
OUTPUT_DIR = REPO_ROOT / "output"
COVER_IMAGE = REPO_ROOT / "assets" / "front-cover.png"
METADATA = REPO_ROOT / "metadata.yaml"
CSS = REPO_ROOT / "epub.css"

BOOK_SLUG = "sovereign-ai-company"

# Ordered content files
FRONT_MATTER = [
    "front-matter/copyright.md",
    "front-matter/disclaimer.md",
    "front-matter/authors-note.md",
]

# Update chapter filenames to match the files in content/chapters/
# as you write them. Order here is the order they appear in the book.
CHAPTERS = [
    "chapters/01 - Chapter One.md",
    "chapters/02 - Chapter Two.md",
    "chapters/03 - Chapter Three.md",
    "chapters/04 - Chapter Four.md",
    "chapters/05 - Chapter Five.md",
    "chapters/06 - Chapter Six.md",
    "chapters/07 - Chapter Seven.md",
    "chapters/08 - Chapter Eight.md",
    "chapters/09 - Chapter Nine.md",
    "chapters/10 - Chapter Ten.md",
    "chapters/11 - Chapter Eleven.md",
    "chapters/12 - Chapter Twelve.md",
]

BACK_MATTER = [
    "back-matter/references-sources.md",
]


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


def main():
    """Build the EPUB."""
    print("Building The Sovereign AI Company EPUB...\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"{BOOK_SLUG}.epub"

    # Collect all content files in order
    all_files = []
    for f in FRONT_MATTER + CHAPTERS + BACK_MATTER:
        path = CONTENT_DIR / f
        if not path.exists():
            print(f"  Warning: {f} not found, skipping")
            continue
        all_files.append(str(path))

    if not all_files:
        print("Error: no content files found.")
        sys.exit(1)

    # Build pandoc command
    cmd = [
        "pandoc",
        "--output", str(output_file),
        "--metadata-file", str(METADATA),
        "--css", str(CSS),
        "--toc",
        "--toc-depth=1",
    ]

    # Include cover only if the file exists (placeholder repos won't have one yet)
    if COVER_IMAGE.exists():
        cmd.extend(["--epub-cover-image", str(COVER_IMAGE)])
    else:
        print(f"  Warning: cover image not found at {COVER_IMAGE}, building without one")

    cmd += all_files

    print(f"  Sources: {len(all_files)} files")
    subprocess.run(cmd, check=True)

    size_kb = output_file.stat().st_size / 1024
    print(f"  Output: {output_file.name} ({size_kb:.0f} KB)")
    print("\nDone.")


if __name__ == "__main__":
    check_deps()
    main()
