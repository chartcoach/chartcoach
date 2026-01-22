---
id: avoid-faceted-row-when-speed-matters-in-trivariate-point-charts
title: Avoid row-faceted point charts when completion time is critical
bibliography: references.bib
description: Row faceting can preserve accuracy but tends to increase completion time
  in common tasks for trivariate point-based encodings.
labels:
- chart:scatter
- task:retrieve-value
- visual:facet
- impact:speed
- data:categorical
- audience:general
- complexity:intermediate
---

## Prefer single-panel encodings over row faceting when speed matters <!-- role: advice -->

Avoid using row faceting for the categorical field in trivariate point charts when users need to answer questions quickly.

## Why row faceting slows comparisons <!-- role: reason -->

Faceting splits information across multiple small panels, which increases the effort of scanning and comparing across categories.

**Mechanism:** Users must visually search across multiple panels and reconcile axes across panels, which adds time overhead even if value decoding remains accurate.

**Evidence:** Row-faceted designs (categorical field on row) ranked worse on time than many non-faceted alternatives, despite reasonable accuracy, indicating a time cost associated with faceting in the tested tasks [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

**Notes:** The evidence is about completion time, not about aesthetics or preference.

## When you should apply this <!-- role: context -->

- **User Goal:** Rapidly answer questions about a quantitative variable across categories.
- **Task:** retrieve-value, sort, find-extremum, aggregate.
- **Data:** Categorical field that could be faceted into multiple rows plus two quantitative fields.
- **Chart Setting:** Static display where multiple facets may not fit in the viewport simultaneously.
- **Audience:** Operational dashboard users, analysts doing quick reads.
- **Success Criterion:** Lower completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Overplotting in a single panel makes categories unreadable and accuracy becomes the priority. **Why:** Faceting can trade time for clarity by separating points into distinct panels.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding faceting can increase overplotting and category confusion in dense datasets. **Risk:** A single panel can become visually congested, especially as category count or points per category rise. **Mitigation:** Reduce congestion through data reduction (sampling/aggregation) or by limiting the number of categories shown at once.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using row faceting as the default way to “make everything visible” in one view. **Why it fails:** It can slow down even simple questions by forcing cross-panel scanning.

## Quick tests <!-- role: check -->

**Failure Sign:** Users scroll or repeatedly shift attention between multiple panels before answering. **Quick Check:** Count how many facet rows are visible without scrolling; if not all, expect time costs. **Stronger Test:** Time a small set of retrieve-value and find-extremum questions with and without row faceting.

## What to do instead <!-- role: fix -->

- Use a single-panel design with category encoded in a non-facet channel (e.g., color-hue for categories).
- Reduce the number of categories shown concurrently so a single-panel view remains readable.
- Provide separate views for different categories only when the user’s workflow supports slower, more deliberate comparison.
