---
id: separate-reference-system-from-data-overlay
title: Pick a Reference System First, Then Design the Data Overlay
bibliography: references.bib
description: "Select the visualization\u2019s reference system (table/graph/map/network)\
  \ before deciding symbol and variable encodings for data overlays."
labels:
- chart:table
- chart:graph
- chart:map
- chart:network
- task:compare
- visual:position
- impact:clarity
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Choose the visualization’s reference system (base map) first, then map data records and attributes onto overlays using graphic symbols and graphic variables.

## The Logic <!-- role: reason -->

The framework distinguishes the base reference system from overlays; separating these decisions prevents conflating “where things go” (structure) with “how they’re encoded” (appearance).

- **The Principle:** Reference-system vs. overlay decomposition
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Building a visualization from a dataset to meet specific insight needs
- **Data Type:** Any dataset where multiple chart families could apply (tables vs. graphs vs. maps vs. networks)
- **Audience:** Designers selecting chart types and encodings systematically

## When to Break It <!-- role: exceptions -->

- **Scenario:** When a fixed reference system is mandated by deployment (e.g., must be a geographic map)
- **Reason:** The base is predetermined, but you still must explicitly design the overlay mappings afterward [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “free-form” experimentation up front
- **The Risk:** Picking the wrong base can force awkward overlays

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding everything with color/size first and hoping a chart type will “fit”
- **Why it fails:** Overlay choices depend on the coordinate system and constraints of the reference system [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Overloaded encodings that fight the structure (e.g., trying to show geography in a nonspatial x–y plot without justification).
- **The Test:** Can you describe (1) the base reference system and (2) each overlay mapping separately? If not, they’re entangled [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Write down the base type (table/graph/map/tree/network) and redraw the visualization starting from that skeleton.
- **Best Fix:** Re-select the base reference system directly from the insight need and data type, then design overlays by mapping variables to symbols and channels [@bornerDataVisualizationLiteracy2019].
