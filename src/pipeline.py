import json
import sys
from pathlib import Path

from analyzer import analyze_event
from event_extractor import extract_event


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python src/pipeline.py <input.txt>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")
    event = extract_event(text)
    report = analyze_event(event)

    output = {
        "input_file": str(file_path),
        "extracted_event": event,
        "analysis_report": report
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
