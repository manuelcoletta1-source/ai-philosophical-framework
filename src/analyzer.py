import json
from typing import Dict, Any


REQUIRED_FIELDS = ["decision", "cost", "trace", "time"]


def analyze_event(event: Dict[str, Any]) -> Dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in event or not event[field]]

    if not missing:
        status = "valid_operational_event"
    elif len(missing) < len(REQUIRED_FIELDS):
        status = "incomplete_event"
    else:
        status = "non_operational_event"

    return {
        "decision": event.get("decision"),
        "cost": event.get("cost"),
        "trace": event.get("trace"),
        "time": event.get("time"),
        "agent": event.get("agent"),
        "status": status,
        "missing_fields": missing
    }


if __name__ == "__main__":
    sample = {
        "agent": "AI decision system",
        "decision": "Flag a financial transaction as high risk",
        "cost": "Operational review workload",
        "trace": "Risk alert recorded in monitoring system",
        "time": "2026-03-09T12:30:00Z"
    }

    result = analyze_event(sample)
    print(json.dumps(result, indent=2))
