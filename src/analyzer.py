import json
from typing import Dict, Any

from validator import validate_event


def analyze_event(event: Dict[str, Any]) -> Dict[str, Any]:
    validation = validate_event(event)

    return {
        "decision": event.get("decision"),
        "cost": event.get("cost"),
        "trace": event.get("trace"),
        "time": event.get("time"),
        "agent": event.get("agent"),
        "status": validation["status"],
        "missing_fields": validation["missing_fields"],
        "is_valid": validation["is_valid"]
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
