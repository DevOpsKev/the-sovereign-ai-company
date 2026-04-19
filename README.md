# The Sovereign AI Company

AI is critical infrastructure. As the global economy fractures, the companies that own their intelligence will define what comes next.

**Download:** [EPUB](https://saicbook.blob.core.windows.net/downloads/sovereign-ai-company.epub) | [PDF](https://saicbook.blob.core.windows.net/downloads/sovereign-ai-company.pdf)

## Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/)
- [Pandoc](https://pandoc.org/)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) (for deployment only)

### Setup

```bash
git clone https://github.com/DevOpsKev/sovereign-ai-company.git
cd sovereign-ai-company
scripts/setup-deps.sh
```

### Pre-commit

Install pre-commit hooks to run linting and formatting checks before each commit:

```bash
pip install pre-commit
pre-commit install
```

### Build

```bash
python3 scripts/build-epub.py
python3 scripts/build-pdf.py --variant both
```

Output:

- `output/sovereign-ai-company.epub`
- `output/sovereign-ai-company.pdf` (screen edition)
- `output/sovereign-ai-company-print.pdf` (print edition)

### Deploy

Infrastructure (one-time):

```bash
scripts/deploy-infra.sh <resource-group-name>
```

Or just push to `main` — GitHub Actions builds and deploys automatically.

## Project Structure

```
sovereign-ai-company/
├── assets/
│   ├── front-cover.png          # EPUB cover
│   ├── front-cover-pdf.png      # Screen PDF cover
│   └── back-cover-pdf.png       # Screen PDF back cover
├── build/
│   └── pdf/
│       └── template.tex         # LaTeX template for PDF output
├── content/
│   ├── front-matter/
│   ├── parts/
│   │   ├── part-1-the-reckoning/
│   │   ├── part-2-the-compute-question/
│   │   ├── part-3-the-model-layer/
│   │   ├── part-4-data-and-jurisdiction/
│   │   ├── part-5-talent-and-capability/
│   │   ├── part-6-the-affirmative-vision/
│   │   └── part-7-the-executive-playbook/
│   ├── epilogue.md
│   └── back-matter/
├── infra/
│   ├── main.bicep               # Azure Blob Storage
│   └── main.bicepparam.json
├── scripts/
│   ├── setup-deps.sh            # Install build dependencies
│   ├── build-epub.py            # Build EPUB from markdown
│   ├── build-pdf.py             # Build PDFs from markdown
│   ├── deploy-infra.sh          # Deploy Azure infrastructure
│   └── install-az-cli.sh        # Install Azure CLI locally
├── epub.css
├── metadata.yaml
├── structure.yaml               # Source of truth for part/chapter order
└── .github/workflows/
    └── build-book.yml           # CI/CD pipeline
```

### `structure.yaml`

The book's part/chapter ordering lives in a single `structure.yaml` at the
repo root. Both build scripts read it to assemble the book — to reorder
chapters, add a part, or rename anything, edit `structure.yaml` and the
corresponding file. No script changes needed.

## CI/CD

Push to `main` triggers the GitHub Actions pipeline which builds the EPUB and PDFs and deploys them to Azure Blob Storage. PRs build and upload artifacts for review but do not deploy.

### Required Secrets

- `AZURE_CREDENTIALS` — Service principal JSON
- `STORAGE_ACCOUNT_NAME` — `saicbook`

## License

Content © Kevin Ryan 2026. All rights reserved.
