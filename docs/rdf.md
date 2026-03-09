# RDF Representation

The AI Philosophical Framework includes a semantic representation using RDF and OWL.

These formats allow the framework to function as a formal ontology and to integrate with knowledge graph systems.

The RDF representation is written using **Turtle syntax**.

Directory:

rdf/

---

## Purpose

The RDF layer provides:

- a formal ontology of the framework
- machine-readable semantic relationships
- compatibility with semantic web tools
- support for knowledge graph systems

JSON schemas describe the **structure of events**.

RDF describes the **semantic meaning of the concepts**.

---

## Files

The RDF directory currently contains two main files.

### Ontology

rdf/apf.ttl

This file defines the ontology structure, including:

Classes:

- OperationalEvent
- OpposableAct
- DecisionChain
- Agent
- Cost
- Trace

Properties:

- hasAgent
- hasDecision
- hasCost
- hasTrace
- hasTime
- hasContext
- hasStatus
- partOfDecisionChain

---

### Example Instances

rdf/examples.ttl

This file contains example operational events expressed as RDF triples.

These examples demonstrate how events can be represented using the ontology.

---

## Example RDF Event

Example in Turtle syntax:

apf:Event001 a apf:OperationalEvent ;
    apf:hasAgent apf:HumanResearcher ;
    apf:hasDecision "Publish a new research framework on GitHub" ;
    apf:hasCost "Time investment and intellectual effort" ;
    apf:hasTrace "Repository created and documentation published" ;
    apf:hasTime "2026-03-09T13:15:00Z"^^xsd:dateTime .

This event follows the same operational structure used throughout the framework:

Decision  
Cost  
Trace  
Time

---

## Relationship to JSON Schemas

The project includes two complementary representations.

JSON schemas  
Used for structured data validation and datasets.

RDF / OWL  
Used for semantic modeling and knowledge graph integration.

Both representations describe the same conceptual framework.

---

## Extension

New classes, properties, or example events may be added to the RDF layer.

Contributions should remain consistent with the minimal operational structure:

Decision  
Cost  
Trace  
Time
