---
id: visualize-semantics-not-ontologies
title: Visualize Meaningful Relations, Not Ontologies
bibliography: references.bib
description: Focus on human-centered semantic views that show relationships and dependencies,
  rather than visualizing formal knowledge descriptions.
labels:
- data:semantic
- data:network
- task:explore
- impact:comprehension
- visual:relationship
---

## The Rule <!-- role: advice -->
Design semantic visualizations to show meaningful relations between data entities in a human-centered way. Do not simply visualize the formal structure of the ontology (e.g., the raw OWL hierarchy).

## The Logic <!-- role: reason -->
Semantics visualization is distinct from ontology visualization. While ontology visualization focuses on "visualizing a formal knowledge description," semantics visualization aims for a "comprehensible, interactive view of semantics" [@kohlhammer_toward_2012].
*   **The Principle:** Human-Centered Semantics.
*   **The Evidence:** The goal is to convey "meaningful relations" (semantics) rather than machine readability. This allows users to see correlations, such as linking government data to non-political domains [@kohlhammer_toward_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Information foraging or impact analysis where data from different domains must be connected (e.g., Linked Open Data).
*   **Data Type:** Semantically annotated data, RDF graphs, or linked government data.
*   **Audience:** Stakeholders trying to understand the dependencies between disparate topics (e.g., geography, time, and policy).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is a database architect or knowledge engineer.
*   **Reason:** They specifically need to debug or structure the formal logic of the ontology itself.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You hide the formal logical structure and class hierarchy of the underlying database.
*   **The Risk:** The user may misunderstand the technical strictness of the data relationships if they are presented too casually.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Generating a node-link diagram that displays every class and subclass in the database schema.
*   **Why it fails:** It creates visual clutter and focuses on "machine readability" structures rather than the "human-centered approach for conveying information" [@kohlhammer_toward_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** The visualization looks like a technical schema diagram or a massive, unreadable hairball of nodes.
*   **The Test:** Does the view help the user find a "new relation" between two distinct concepts (e.g., a policy and a demographic statistic), or does it just show how the data is stored?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Filter the graph to show only specific instance connections relevant to the user's search query.
*   **Best Fix:** Use visual abstractions (like categories, timelines, or maps) to represent the semantic links, as seen in the SemaVis framework (Figure 4 in [@kohlhammer_toward_2012]), rather than raw node-link graphs.
