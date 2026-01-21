---
id: use-open-vs-closed-shapes-as-a-primary-category-encoding
title: Encode Categories Using Open vs. Closed Shapes
bibliography: references.bib
description: Use open and closed symbol shapes as a high-level categorical split to
  improve discrimination in dense scatterplot displays.
labels:
- chart:scatter
- task:categorize
- visual:shape
- impact:clarity
- data:categorical
- audience:general
- source:paper
---

## The Rule <!-- role: advice -->

Encode different categories with symbols from different **open vs. closed** shape families (e.g., closed: circle/square/triangle vs. open: plus/asterisk/x).

## The Logic <!-- role: reason -->

Open and closed shapes behave like **separable perceptual categories**: people respond faster and with less interference when competing symbols come from different open/closed families than from the same family, especially under clutter and when discrimination is required inside one plot.

- **The Principle:** Between-category discrimination is easier than within-category discrimination.
- **The Evidence:** Across a flanker task, same/different judgments, and multi-class scatterplot tasks, interference increased when symbols shared the same open/closed family and decreased when they differed [@burlinsonOpenVsClosed2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Separating classes quickly; finding which class has “more,” or which class forms a trend.
- **Data Type:** Multi-class point data (scatterplots) with overlapping or cluttered marks.
- **Audience:** General viewers; time-pressured or error-sensitive analytic settings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Each class is shown in separate plots (small multiples / side-by-side homogeneous plots).
- **Reason:** The paper reports little to no performance difference from open vs. closed symbols when each plot is homogeneous; the advantage appears mainly when symbols must be discriminated within the same display [@burlinsonOpenVsClosed2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may “spend” your strongest shape distinction (open vs. closed) early, leaving fewer highly distinct shape options for additional classes.
- **The Risk:** If you later need many categories, within-family shapes (e.g., multiple closed shapes) may become more confusable.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking two arbitrary shapes because they “look different” without checking whether they’re both open or both closed.
- **Why it fails:** Within-family (same open/closed) symbol pairs showed more interference and slower discrimination than cross-family pairs in perceptual tasks and in single-plot numerosity/trend tasks [@burlinsonOpenVsClosed2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or misclassify points when two symbol types are mixed in the same region.
- **The Test:** Temporarily regroup your legend: if two classes mapped to the same open/closed family are the ones users confuse, you likely violated the rule.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap one class’s symbol so the two most-compared classes are from different open/closed families.
- **Best Fix:** Redesign the symbol set so all “primary” categorical splits in a single plot are cross-family (open vs. closed) rather than within-family [@burlinsonOpenVsClosed2018a].
