# Resume Parser CLI Tool

A production-ready NLP-powered resume parser with GitHub integration.

## Features

- Extracts:
  - Skills (NER + keyword matching)
  - Companies
  - Degrees
  - Phone numbers (regex)
  - Emails (regex)
- Command-line interface using `argparse`
- Supports PDF and DOCX resumes
- GitHub CI integration
- Pull Request template suggestions

## Usage

```bash
python -m parser.cli -i demo_resumes/sample_resume.pdf -o output.json -v
