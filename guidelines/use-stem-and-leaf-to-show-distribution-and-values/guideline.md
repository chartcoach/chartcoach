---
id: use-stem-and-leaf-to-show-distribution-and-values
title: Use Stem-and-Leaf Plots to Show Distributions Without Empty Bars
bibliography: references.bib
description: Use stem-and-leaf plots to show frequency distributions while retaining
  the underlying values.
labels:
- chart:stem-and-leaf
- task:distribution
- visual:text
- impact:clarity
- data:numerical
- audience:analyst
- complexity:intermediate
---

## The Rule <!-- role: advice -->

Use a stem-and-leaf plot instead of a histogram when you want to show both the distribution and the actual values within bins.

## The Logic <!-- role: reason -->

A stem-and-leaf plot bins by significant digits and uses the data itself to indicate frequency, replacing “information-empty” bars and enabling inspection of both distribution shape and bin contents.

- **The Principle:** Preserve data granularity while summarizing frequency
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Inspect clustering and the contents of groups in a numeric distribution
- **Data Type:** Univariate numeric data where digits/bin membership are meaningful
- **Audience:** Analysts performing exploratory data analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** The dataset is too large for legible digit listing
- **Reason:** The plot’s value-as-mark approach becomes unreadable at high volumes [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Scalability and immediate readability for very large datasets
- **The Risk:** Viewers unfamiliar with the format may need brief explanation

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defaulting to histograms and hiding bin contents entirely
- **Why it fails:** You lose the ability to inspect what is inside clusters/bins [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** You need to know “which values make up this bin?” and the histogram can’t answer
- **The Test:** If bin contents matter for interpretation, a stem-and-leaf plot is a candidate [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Bin by the first significant digit and stack the second digit as leaves
- **Best Fix:** Tune binning to the data’s meaningful precision so clusters are visible without overwhelming the display [@heerTourVisualizationZoo2010]
