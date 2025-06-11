import argparse
import json
import os
from parser.extractor import ResumeExtractor
from pdfminer.high_level import extract_text
import docx

def load_text_from_file(path):
    if path.endswith(".pdf"):
        return extract_text(path)
    elif path.endswith(".docx"):
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type. Use PDF or DOCX.")

def main():
    parser = argparse.ArgumentParser(description="Resume Parser CLI Tool")
    parser.add_argument("-i", "--input", required=True, help="Path to resume PDF/DOCX file")
    parser.add_argument("-o", "--output", default="resume_data.json", help="Path to output JSON file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Input file does not exist.")
        return

    text = load_text_from_file(args.input)
    extractor = ResumeExtractor(text)
    data = extractor.extract_all()

    with open(args.output, "w") as f:
        json.dump(data, f, indent=4)

    if args.verbose:
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
