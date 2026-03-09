# Software Layer

The AI Philosophical Framework includes a minimal software layer for analyzing operational events.

This layer provides a first executable implementation of the framework.

Directory:

src/

---

## Purpose

The software layer is designed to evaluate whether an event satisfies the minimal operational structure of the framework:

Decision · Cost · Trace · Time

It provides a simple mechanism to:

- read event data
- validate required fields
- generate an analysis report
- classify the event

---

## Modules

### `src/validator.py`

This module checks whether an event contains the required fields.

Required fields:

- decision
- cost
- trace
- time

Validation outcomes include:

- `valid_operational_event`
- `incomplete_event`
- `non_operational_event`

---

### `src/analyzer.py`

This module builds an analysis report for an event.

The report includes:

- decision
- cost
- trace
- time
- agent
- status
- missing fields
- validity result

---

### `src/cli.py`

This module provides a command-line interface.

It allows event files in JSON format to be analyzed directly from the terminal.

Example usage:

`python src/cli.py examples/ai-agent-event.json`

---

## Example Output

A valid event may produce output such as:

- decision identified
- cost identified
- trace identified
- time identified
- status: `valid_operational_event`

If required fields are missing, the output will indicate which fields are absent.

---

## Current Scope

The software layer is intentionally minimal.

It does not yet include:

- natural language parsing
- automatic event extraction from text
- RDF querying
- AI-assisted inference
- batch dataset analysis

Its current purpose is to provide a small executable core for the framework.

---

## Future Extensions

Possible future extensions include:

- batch validation of datasets
- natural language event extraction
- integration with RDF and SPARQL
- event scoring
- decision chain analysis
- AI-assisted classification

The goal is to evolve from a minimal executable validator into a broader operational analysis toolkit.
