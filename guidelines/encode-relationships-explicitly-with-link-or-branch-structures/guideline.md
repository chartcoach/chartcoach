---
id: encode-relationships-explicitly-with-link-or-branch-structures
title: Encode Key Relationships Explicitly with Links or Branching Structures
bibliography: references.bib
description: "Show relationships (e.g., cause\u2013risk\u2013location) directly using\
  \ link/branch encodings rather than leaving users to infer them."
labels:
- chart:network
- task:relate
- visual:connection
- impact:insight
- data:relational
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Represent important relationships directly using Link or Branch structures, and limit what you draw to the most meaningful subset.

## The Logic <!-- role: reason -->

Big health data tasks often require discovering non-explicit relationships among elements. Explicit link/branch encodings make relationships perceptible and support hypothesis generation; but relationship counts can explode, so filtering to salient relationships (e.g., above a quantile) keeps the view interpretable. [@olaSimpleChartsDesign2016]

- **The Principle:** Make relationships perceptible while managing relational overload
- **The Evidence:** [@olaSimpleChartsDesign2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand how risks contribute to causes, or how locations relate to risks/causes for a demographic group
- **Data Type:** Relational/attribution data (cause–risk attribution; multi-entity links)
- **Audience:** Analysts exploring mechanisms and intervention points

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is purely univariate ranking or distribution reading with no need to reason about relationships.
- **Reason:** Relationship encodings add complexity without supporting the user’s immediate goal. [@olaSimpleChartsDesign2016]

## The Price <!-- role: costs -->

- **The Sacrifice:** Visual complexity increases; dense link sets can occlude labels and marks.
- **The Risk:** Without filtering, the visualization can become unreadable due to too many connections. [@olaSimpleChartsDesign2016]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Drawing all possible links between entities.
- **Why it fails:** The number of relationships becomes large and obscures patterns; users cannot isolate meaningful structure. [@olaSimpleChartsDesign2016]

## How to Check <!-- role: check -->

- **Visual Sign:** Connections form a dense tangle where individual relationships cannot be followed.
- **The Test:** Try tracing a single entity’s top relationships; if you cannot reliably follow them, you need relationship reduction or restructuring. [@olaSimpleChartsDesign2016]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Filter relationships to a salient subset (e.g., only top quantile as done in the paper’s demography relationship view).
- **Best Fix:** Use a structured relationship layout (e.g., coordinate axes for facets + links between them, or branch-out from one entity) and support interaction to reveal latent relationships on demand. [@olaSimpleChartsDesign2016]
