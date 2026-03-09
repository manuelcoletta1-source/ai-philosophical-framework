import json
import sys
from pathlib import Path

from analyzer import analyze_event


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python src/cli.py <event.json>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    try:
        with file_path.open("r", encoding="utf-8") as f:
            event = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: invalid JSON in file: {file_path}")
        sys.exit(1)

    result = analyze_event(event)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
