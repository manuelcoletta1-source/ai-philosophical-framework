# Installation

The AI Philosophical Framework includes a minimal software layer that can be executed locally.

The current version does not require external dependencies and runs with the Python standard library.

---

## Requirements

Python 3.8 or newer.

You can verify your Python version with:

python --version

---

## Clone the Repository

Clone the repository using Git:

git clone https://github.com/your-username/ai-philosophical-framework.git

Then move into the project directory:

cd ai-philosophical-framework

---

## Project Structure

Key directories include:

docs/  
Documentation and conceptual explanations.

ontology/  
Ontology definitions.

schema/  
JSON schemas for operational events.

dataset/  
Structured datasets of operational events.

examples/  
Example event files.

rdf/  
Semantic ontology and example RDF data.

src/  
Software modules for event analysis.

---

## Running the Event Analyzer

The framework includes a command-line interface for analyzing operational events.

Example:

python src/cli.py examples/ai-agent-event.json

This command reads the JSON event and evaluates it according to the framework structure.

---

## Expected Output

The analyzer produces a report describing the event:

- decision
- cost
- trace
- time
- agent
- validation status
- missing fields (if any)

Example status values include:

valid_operational_event  
incomplete_event  
non_operational_event

---

## Testing Other Events

You can run the analyzer on other example files:

python src/cli.py examples/human-decision.json

python src/cli.py examples/institutional-decision.json

python src/cli.py examples/minimal-event.json

---

## Extending the Tool

Developers may extend the framework by:

- adding new validation rules
- implementing dataset analysis
- integrating RDF querying
- building AI-assisted event extraction

The current implementation provides a minimal executable foundation.
