---
id: prefer-different-open-closed-shape-categories-for-correlation-judgments
title: Prefer Different Open/Closed Shape Categories for Correlation Judgments
bibliography: references.bib
description: For correlation judgments in scatterplots, use shape pairs that come
  from different open/closed categories rather than two open shapes.
labels:
- chart:scatter
- task:correlate
- visual:shape
- visual:position
- impact:accuracy
- impact:speed
- data:categorical
- data:quantitative
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

When encoding categories with point shapes in a scatterplot for correlation judgment, prefer a shape pairing from different open/closed categories (e.g., closed+closed or open+closed) over an all-open pairing.

## The Logic <!-- role: reason -->

- **The Principle:** Interference from within-category shape similarity (open vs. closed) can hinder shape-based discrimination during analytic judgments.
- **The Evidence:** In the collated findings summarized by [@zengReviewCollationGraphical2023] from [@burlinsonOpenVsClosed2018], correlation-task performance ranks highest for a closed–closed pairing (triangle+square) and lowest for an open–open pairing (asterisk+cross), with a reported significant difference between best and worst (E-6 > E-1) for both accuracy and time.

## Where to Apply <!-- role: context -->

- **User Goal:** Judge correlation (trend/relationship) between two quantitative axes while distinguishing categories by shape.
- **Data Type:** Two quantitative fields on position (X/Y) plus a nominal category encoded with shape.
- **Audience:** Any audience; especially relevant when you expect time pressure or quick judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking users to judge correlation (e.g., the chart is for lookup/identification rather than relationship assessment).
- **Reason:** The reported ranking and significance are specific to the correlate task in the extracted results [@burlinsonOpenVsClosed2018], as collated by [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may constrain your shape palette (fewer “stylistic” options) by avoiding all-open shape sets.
- **The Risk:** If your system auto-assigns shapes without tracking open/closed category, you may accidentally choose the worst-performing pairing for correlation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Randomly selecting multiple “distinct-looking” open shapes (e.g., asterisk and cross) assuming they will separate well.
- **Why it fails:** The extracted results show the all-open pairing is ranked worst for correlate accuracy/time, indicating interference can persist even when shapes feel visually distinct [@burlinsonOpenVsClosed2018; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories both use open, line-segment-based symbols (e.g., asterisk, cross, plus).
- **The Test:** Replace one category’s shape with a closed shape (e.g., square/triangle) and see if the pairing now matches a higher-ranked open/closed mix per the extracted ordering [@burlinsonOpenVsClosed2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one category’s point symbol from open to closed (or vice versa) so the pair spans open/closed categories.
- **Best Fix:** Implement a shape-assignment rule in your recommender that explicitly tracks “open vs. closed” shape category and avoids all-open pairings for correlation tasks, using the collated rankings as a preference signal [@zengReviewCollationGraphical2023; @burlinsonOpenVsClosed2018].
