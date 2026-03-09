# Dataset Analysis

The AI Philosophical Framework includes a tool for analyzing entire datasets of operational events.

This tool evaluates each event in a JSONL dataset and produces a summary of validation results.

The dataset analyzer is implemented in:

src/dataset_analyzer.py

---

## Purpose

The dataset analyzer allows researchers and developers to evaluate large collections of events.

Each event is analyzed according to the framework structure:

Decision · Cost · Trace · Time

The analyzer determines whether each event is:

- a valid operational event
- an incomplete event
- a non-operational event

---

## Dataset Format

Datasets must be provided in **JSONL format**.

JSONL means that each line contains one JSON object representing an event.

Example:

{"agent":"AI system","decision":"Flag transaction","cost":"Operational review","trace":"Risk alert recorded","time":"2026-03-09T12:30:00Z"}

---

## Running the Analyzer

Example command:

python src/dataset_analyzer.py dataset/operational-events.jsonl

The tool will process every event in the dataset.

---

## Output

The analyzer produces a summary report such as:

{ "total_events": 100, "valid_operational_event": 72, "incomplete_event": 21, "non_operational_event": 7 }

This provides a quick overview of dataset quality.

---

## Use Cases

Dataset analysis may support:

- validating new datasets
- evaluating event extraction pipelines
- auditing operational logs
- measuring dataset completeness
- preparing training data for AI systems

---

## Future Extensions

Future versions of the dataset analyzer may include:

- per-agent statistics
- event-type distribution
- missing field analysis
- decision chain reconstruction
- RDF dataset export



