---
id: analyze-before-you-visualize-clean-transform-and-model-data
title: Analyze and Transform Data Before Visualizing
bibliography: references.bib
description: Clean, transform, and analyze data (statistical, temporal, geospatial,
  topical, relational) before mapping it to visuals.
labels:
- task:trend
- task:compare
- data:temporal
- data:geospatial
- data:network
- impact:correctness
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Before choosing encodings, preprocess and analyze the dataset as needed—clean errors, handle missing data, and run the analysis type that matches the insight need.

## The Logic <!-- role: reason -->

The framework separates “analyze” from “visualize”: most datasets require cleaning and domain-appropriate analyses (statistical/temporal/geospatial/topical/relational) to produce interpretable inputs for visualization.

- **The Principle:** Workflow separation of analysis vs. visual encoding
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Turning raw records into decision-ready patterns (distributions, trends, relationships)
- **Data Type:** Real-world datasets with ambiguity, missing values, or required derivations (e.g., geocoding, aggregation, network extraction)
- **Audience:** Analysts and students building charts “from scratch”

## When to Break It <!-- role: exceptions -->

- **Scenario:** Teaching or quick demos where the dataset is already curated and analysis-ready
- **Reason:** The “analyze” step is still present, but may be trivial; skipping it is only safe when preprocessing is unnecessary [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Time and tooling investment before anything is “visible”
- **The Risk:** Overprocessing can obscure raw variability if done without aligning to the insight need

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Visualizing dirty data to “let the chart reveal problems”
- **Why it fails:** Errors, duplicates, and missingness can masquerade as patterns, undermining interpretation [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Unexpected spikes, gaps, or impossible values; maps with points in the wrong region; networks with duplicated nodes.
- **The Test:** Audit: missing values, duplicates, anomalies, and whether required transformations (e.g., geocoding) were performed [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Apply basic cleaning (deduplicate, correct obvious errors, mark/handle missing values) and rerun the visualization.
- **Best Fix:** Choose and document the correct analysis pipeline (statistical/temporal/geospatial/topical/relational) that operationally supports the stated insight need [@bornerDataVisualizationLiteracy2019].
