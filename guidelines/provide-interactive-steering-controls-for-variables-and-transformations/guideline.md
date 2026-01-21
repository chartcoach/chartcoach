---
id: provide-interactive-steering-controls-for-variables-and-transformations
title: Provide Faceted Steering for Variables and Transformations
bibliography: references.bib
description: Let users include/exclude fields and pick transformations to guide recommendations
  as their interests evolve.
labels:
- chart:gallery
- task:filter
- visual:interaction
- impact:control
- data:tabular
- audience:analyst
- system:mixed-initiative
---

## The Rule <!-- role: advice -->

Give users direct controls to include/exclude variables and choose transformations so they can steer recommendations.

## The Logic <!-- role: reason -->

Voyager frames exploration as mixed-initiative: the system generates suggestions, but analysts’ interests evolve and must be able to adapt the recommendation space through selectable variables and transformation functions [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Human-in-the-loop recommendation steering
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Narrow or redirect recommendations without switching tools
- **Data Type:** Multivariate tables with multiple plausible transformations (bin, aggregate, time unit)
- **Audience:** Analysts conducting iterative EDA

## When to Break It <!-- role: exceptions -->

- **Scenario:** A fully automated “one-click insight” product with no intention of user-driven exploration.
- **Reason:** Steering controls are unnecessary if user intent is not part of the interaction model.

## The Price <!-- role: costs -->

- **The Sacrifice:** More UI complexity in the schema/controls panel.
- **The Risk:** Users may over-constrain and reduce discovery if controls are too prominent or confusing.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing recommendations but no way to exclude irrelevant fields or request specific transformations.
- **Why it fails:** Users can’t focus the gallery, making exploration feel noisy and less effective [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly scroll past the same unwanted suggestions.
- **The Test:** Ask users to “remove this variable from suggestions”; if they can’t do it quickly, steering is inadequate.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add per-field include/exclude toggles and a transformation picker (e.g., MEAN, BIN, time unit).
- **Best Fix:** Make these controls feed directly into the recommendation engine so the gallery updates immediately and predictably [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
