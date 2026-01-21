---
id: make-chart-space-robust-to-extremes
title: Design Chart Space to Handle Extreme Values and Similarities
bibliography: references.bib
description: Ensure chart spacing remains readable when data includes outliers or
  near-identical values by adapting the view or clearly annotating what is happening.
labels:
- chart:general
- task:explore
- visual:position
- impact:accessibility
- data:quantitative
- audience:novice
- source:chartability
- principle:assistive
- labor:reduction
---

## The Rule <!-- role: advice -->

Design the chart’s spatial encoding so it stays readable under extreme outliers *and* extreme similarity; if it cannot adapt automatically, explicitly annotate the distortion and provide user controls (e.g., sort/divide/filter) to reallocate space.

## The Logic <!-- role: reason -->

Spatial layouts can become unreadable when values are forced to compete for the same limited area—either because one or a few outliers compress everything else into margins, or because very similar values (e.g., nearly overlapping lines) eliminate perceptible separation. Chartability frames this as an *Assistive* requirement: the interface should reduce user labor by adapting the display or making distortions transparent and controllable, rather than leaving users to infer what happened [@elavskyHowAccessibleMy2022]. Thoughtful allocation of white space is a core readability mechanism; treating space as an active design element supports clarity when the visual field is under pressure from extreme distributions [@towardsdatascience_data_visualisation_2].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting patterns and differences without missing compressed or indistinguishable marks.
- **Data Type:** Quantitative data with potential outliers, heavy skew, or values that are extremely close together (including parameter-driven, filtered, or otherwise dynamic outputs).
- **Audience:** Broad audiences, especially users who benefit from reduced cognitive/functional labor in analytical or interactive environments [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is intentionally communicating the presence and dominance of an extreme outlier as the main message.
- **Reason:** Reallocating space could undermine the intended emphasis; in this case, keep the extreme but still make the tradeoff explicit to the user via annotation [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional visual space, extra UI controls, or additional explanatory annotation text [@elavskyHowAccessibleMy2022].
- **The Risk:** Automatic adaptation (or user-driven filtering/dividing) can change what is visible at once, potentially making comparisons across states less straightforward [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving the chart unchanged and assuming users will “notice” that marks are squished by outliers or indistinguishable due to similarity.
- **Why it fails:** It increases user labor and can make the chart effectively unreadable without any indication of why, violating the Assistive intent of reducing cognitive/functional effort [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Most marks are compressed into edges/margins (outlier pressure) or multiple series/marks visually merge (similarity pressure), making differences hard to see.
- **The Test:** Change parameters/filters (or inspect known extrema cases) and verify that either (1) the chart adapts to preserve readable separation or (2) the chart clearly explains the distortion and offers sort/divide/filter controls to redistribute space [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear annotation explaining that outliers or near-identical values are compressing the view and indicate what effect this has on readability [@elavskyHowAccessibleMy2022].
- **Best Fix:** Make the chart adaptive to extrema, and when fully automatic adaptation/annotation isn’t possible (e.g., dynamic data), provide user controls to sort, divide, or filter the space so users can reveal and compare the relevant parts of the data without excessive effort [@elavskyHowAccessibleMy2022].
