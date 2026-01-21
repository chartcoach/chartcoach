---
id: visually-distinguish-user-selected-from-system-suggested-fields
title: Visually Distinguish Selected Fields From Suggested Fields
bibliography: references.bib
description: Use consistent visual tokens to show which variables are user-chosen
  versus system-added in each chart.
labels:
- chart:gallery
- task:browse
- visual:annotation
- impact:orientation
- data:multivariate
- audience:analyst
- system:mixed-initiative
---

## The Rule <!-- role: advice -->

In every recommended chart, clearly mark which variables were selected by the user versus suggested by the system.

## The Logic <!-- role: reason -->

Mixed-initiative systems require users to understand what the system contributed. Voyager uses different capsule styles (solid vs dashed) for selected vs suggested variables to reduce confusion and support scanning across charts [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Attribution and interpretability in mixed-initiative interfaces
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly scan a gallery and understand what changed between views
- **Data Type:** Recommendations that may augment the selection with new fields
- **Audience:** Analysts exploring unfamiliar datasets

## When to Break It <!-- role: exceptions -->

- **Scenario:** The system shows only user-constructed views (no recommendations).
- **Reason:** There is no ambiguity to resolve.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional visual chrome (tokens, borders) in each thumbnail.
- **The Risk:** Overly prominent tokens can compete with the chart itself.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Listing fields in a tooltip or details panel only.
- **Why it fails:** Users can’t efficiently compare charts at a glance while browsing [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users treat system-added variables as if they intentionally selected them.
- **The Test:** Ask users to identify which fields they chose in a shown chart; hesitation indicates insufficient differentiation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use two distinct token styles for selected vs suggested variables in the chart header.
- **Best Fix:** Add hover highlighting for the same variable across the gallery to reinforce consistent variable identity during scanning [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
