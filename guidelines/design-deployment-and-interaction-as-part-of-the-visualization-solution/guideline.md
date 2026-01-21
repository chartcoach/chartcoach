---
id: design-deployment-and-interaction-as-part-of-the-visualization-solution
title: Design Interaction and Deployment Together With the Visualization
bibliography: references.bib
description: "Choose deployment medium and interaction techniques (zoom, filter, details-on-demand,\
  \ link-and-brush, etc.) that match the user\u2019s task."
labels:
- task:explore
- impact:usability
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

Select deployment (print vs. interactive devices) and interaction techniques intentionally—zoom, filter, details-on-demand, history, extract, and link-and-brush—based on user tasks.

## The Logic <!-- role: reason -->

The framework treats deployment and interaction as explicit workflow steps: different media and interfaces enable different interactions, which shape what users can successfully interpret.

- **The Principle:** Interaction-capability alignment with tasks and devices
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Exploration, lookup, or iterative sensemaking that benefits from navigation and querying
- **Data Type:** Any dataset where static views cannot answer all questions
- **Audience:** Users working with interactive visual analytics tools or dashboards

## When to Break It <!-- role: exceptions -->

- **Scenario:** Fixed-format publishing where interaction is impossible (e.g., paper)
- **Reason:** You must rely on static encodings and annotation; interaction types become unavailable [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Engineering/design time for interaction and cross-device testing
- **The Risk:** Interaction overload can confuse users if not tied to clear tasks

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding interactivity “because dashboards should be interactive” without mapping it to an insight need
- **Why it fails:** It violates the framework’s task/need-driven approach and can distract from interpretation [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ignore controls or get lost; interactions do not help answer the stated questions.
- **The Test:** For each interaction, state which insight need/task it supports (e.g., filter → subset comparison; details-on-demand → lookup) [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or disable interactions that do not map to a task; keep only the minimum set.
- **Best Fix:** Redesign the deployment and interaction plan as part of the workflow: insight need → visualization → device/UI → interaction set → interpretation support [@bornerDataVisualizationLiteracy2019].
