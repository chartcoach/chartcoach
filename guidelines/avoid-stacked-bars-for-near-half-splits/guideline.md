---
id: avoid-stacked-bars-for-near-half-splits
title: Avoid Stacked Bars for Near-50% Splits
bibliography: references.bib
description: Stacked (integrated) part-to-whole displays increase systematic over/underestimation
  around the implicit 50% boundary.
labels:
- chart:stacked-bar
- task:read-value
- visual:length
- impact:accuracy
- data:proportional
- audience:general
- bias:categorical-repulsion
---

## The Rule <!-- role: advice -->

Avoid stacked (integrated) bar charts when the decision hinges on values near a 50/50 split.

## The Logic <!-- role: reason -->

Integrated context introduces an implicit midpoint category boundary (≈50%) that repulses memory-based reproductions: values below 50% get underestimated and values above 50% get overestimated. This is a categorical perception/repulsion effect that trades lower overall error for systematic bias around the boundary.

- **The Principle:** Categorical perception and repulsion from an implicit reference boundary
- **The Evidence:** Participants’ signed errors showed a reliable repulsion pattern around 50% specifically in integrated/stacked conditions across experiments [@mccolemanNoMarkIsland2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Precisely interpret whether a proportion is below vs. above (or close to) 50% (e.g., “is it basically half?”).
- **Data Type:** Part-to-whole percentages (1–99%) where ~45–55% values matter.
- **Audience:** Any audience where small differences around half are meaningful.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You want to emphasize category membership (“mostly above half” vs “mostly below half”) more than the exact numeric difference.
- **Reason:** The same categorical boundary can improve overall precision while exaggerating separation across the boundary [@mccolemanNoMarkIsland2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** You give up some of the overall accuracy benefit observed for integrated context (lower unsigned error).
- **The Risk:** Switching away from stacked bars may reduce quick part-to-whole comprehension for some tasks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping stacked bars and assuming “more context always means more accurate reading.”
- **Why it fails:** The paper shows context can reduce unsigned error while adding a predictable bias around 50% [@mccolemanNoMarkIsland2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Your key values cluster around the halfway point of a 0–100% scale in a stacked display.
- **The Test:** Identify whether a viewer’s correct judgment would require distinguishing (roughly) 48% vs 52%; if yes, the chart is in the danger zone.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Present the relevant proportion as a standalone mark (without integrated part-to-whole framing) when near-50% accuracy is critical.
- **Best Fix:** Use a non-integrated encoding for the critical comparison (so the midpoint boundary is not visually implied in the same way) and reserve stacked views for cases where near-50% fidelity is not central [@mccolemanNoMarkIsland2021].
