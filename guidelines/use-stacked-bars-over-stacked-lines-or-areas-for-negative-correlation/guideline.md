---
id: use-stacked-bars-over-stacked-lines-or-areas-for-negative-correlation
title: Use Stacked Bars Over Stacked Lines/Areas for Negative Correlation
bibliography: references.bib
description: For negative correlations, stacked bar charts support more precise correlation
  discrimination than stacked area or stacked line charts.
labels:
- chart:stacked-bar
- chart:stacked-area
- chart:stacked-line
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
---

## The Rule <!-- role: advice -->

When you must use a stacked chart to convey negative correlation, choose stacked bars rather than stacked lines or stacked areas.

## The Logic <!-- role: reason -->

The study’s JND measurements show that viewers discriminate differences in negative correlation more precisely in stacked bars than in stacked areas or stacked lines, implying the stacked-bar form better supports the perceptual cues participants use for this task.

- **The Principle:** Chart form changes the visual features used for discrimination, altering JND
- **The Evidence:** For negative correlation, stacked bar significantly outperformed stacked line and stacked area (both p < 0.001) in Mann–Whitney tests [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which of two negative correlations is stronger using stacked-style graphics.
- **Data Type:** Two quantitative variables represented via stacked encodings (as tested in the paper’s stimulus set).
- **Audience:** Dashboard viewers who need reliable comparative judgments, not just qualitative impressions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are depicting positive correlations with stacked variants under similar constraints.
- **Reason:** Several positive stacked conditions were excluded as unreliable in this study’s methodology, so this specific stacked-bar advantage is established for negative correlation conditions included in analysis [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Stacked bars can be visually heavier and may reduce perceived continuity compared to lines/areas.
- **The Risk:** If your communication goal depends on line/area continuity cues, switching to bars may change what users attend to [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming stacked line/area and stacked bar are interchangeable because they look similar.
- **Why it fails:** The paper reports statistically meaningful JND differences between these forms for negative correlation judgments [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users report relying on “spikiness” or peaks/valleys rather than relative segment amounts when judging stacked lines/areas.
- **The Test:** If your goal is correlation discrimination, compare the modeled JNDs; if stacked bars are lower than your chosen stacked form for the negative r-range, the current choice is likely suboptimal [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace stacked line/area with stacked bars for the correlation judgment view.
- **Best Fix:** Validate the stacked encoding choice with a JND/Weber fit for your exact design parameters and select the lowest-JND stacked variant [@harrisonRankingVisualizationsCorrelation2014a].
