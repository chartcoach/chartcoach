---
id: use-2d-histograms-when-scatterplots-overlap
title: Use a 2D Histogram When Scatter Plot Points Overlap
bibliography: references.bib
description: Replace overplotted scatter plots with a 2D histogram to reveal density
  patterns.
labels:
- chart:2d-histogram
- task:correlate
- visual:color
- impact:clarity
- data:multivariate
- audience:mainstream
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

If your scatter plot is unreadable due to overlapping points, switch to a 2D histogram.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Binning converts stacks of overlapping marks into an interpretable density field.
- **The Evidence:** The post advises using a 2D histogram when a scatter plot’s message “gets lost in a sea of overlapping dots,” noting it’s sometimes called a heatmap (with naming caveats) [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Seeing the relationship between two variables when there are many observations.
- **Data Type:** High-density bivariate data with substantial overplotting.
- **Audience:** Mainstream readers when a scatter plot fails due to overlap [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need to identify and label specific individual observations.
- **Reason:** Binning aggregates points into cells, reducing visibility of individual cases (the post presents 2D histograms as an alternative when individual dots overwhelm the view) [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You lose per-point detail.
- **The Risk:** Bin size choices can change the apparent pattern; readers may focus on bins rather than exact positions [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Persisting with a scatter plot and hoping transparency alone will solve heavy overlap.
- **Why it fails:** In severe overplotting, dots still merge into an ambiguous mass; the post recommends changing chart type [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Dense areas appear as solid blobs; you can’t infer density structure.
- **The Test:** If removing point outlines or changing opacity still doesn’t reveal density, it’s time for a 2D histogram [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the scatter plot into a 2D histogram.
- **Best Fix:** Use a 2D histogram as the primary chart when overlap is intrinsic to the dataset and density is the message [@muth_chart_types_guide_2025].
