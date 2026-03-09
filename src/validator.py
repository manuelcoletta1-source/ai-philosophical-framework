from typing import Dict, Any, List


REQUIRED_FIELDS = ["decision", "cost", "trace", "time"]


def missing_fields(event: Dict[str, Any]) -> List[str]:
    return [field for field in REQUIRED_FIELDS if field not in event or not event[field]]


def validate_event(event: Dict[str, Any]) -> Dict[str, Any]:
    missing = missing_fields(event)

    if not missing:
        status = "valid_operational_event"
    elif len(missing) < len(REQUIRED_FIELDS):
        status = "incomplete_event"
    else:
        status = "non_operational_event"

    return {
        "is_valid": len(missing) == 0,
        "status": status,
        "missing_fields": missing
    }
