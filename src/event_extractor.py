import re
from typing import Dict, Any


TIME_PATTERN = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"


def extract_time(text: str) -> str | None:
    match = re.search(TIME_PATTERN, text)
    if match:
        return match.group(0)
    return None


def extract_decision(text: str) -> str | None:
    decision_keywords = ["decided", "flagged", "approved", "initiated", "rejected"]

    for keyword in decision_keywords:
        if keyword in text.lower():
            return text
    return None


def extract_trace(text: str) -> str | None:
    trace_keywords = ["logged", "recorded", "alert", "report", "registered"]

    for keyword in trace_keywords:
        if keyword in text.lower():
            return text
    return None


def extract_cost(text: str) -> str | None:
    cost_keywords = ["cost", "delay", "workload", "risk", "impact"]

    for keyword in cost_keywords:
        if keyword in text.lower():
            return text
    return None


def extract_event(text: str) -> Dict[str, Any]:
    return {
        "decision": extract_decision(text),
        "cost": extract_cost(text),
        "trace": extract_trace(text),
        "time": extract_time(text)
    }


if __name__ == "__main__":
    sample_text = """
    The AI system flagged a transaction as high risk and logged an alert in the monitoring system.
    The event was recorded at 2026-03-09T12:30:00Z and initiated a manual review.
    """

    event = extract_event(sample_text)
    print(event)
