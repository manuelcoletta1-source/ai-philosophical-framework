import json
import sys
from pathlib import Path
from typing import Dict, Any, List

from analyzer import analyze_event


def load_jsonl(file_path: Path) -> List[Dict[str, Any]]:
    events = []

    with file_path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(f"Warning: invalid JSON on line {line_number}: {exc}")

    return events


def summarize_results(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    summary = {
        "total_events": len(results),
        "valid_operational_event": 0,
        "incomplete_event": 0,
        "non_operational_event": 0
    }

    for result in results:
        status = result.get("status")
        if status in summary:
            summary[status] += 1

    return summary


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python src/dataset_analyzer.py <events.jsonl>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    events = load_jsonl(file_path)
    results = [analyze_event(event) for event in events]
    summary = summarize_results(results)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
