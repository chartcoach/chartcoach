---
id: use-scatterplots-to-show-relationships-between-variables
title: Use Scatter Plots to Show Correlations Between Two Variables
bibliography: references.bib
description: Scatter plots help explore and communicate how two measures relate across
  observations.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:insight
- data:multivariate
- audience:mainstream
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a scatter plot when your main question is how two variables relate across observations.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Plotting pairs as points reveals association patterns (clusters, trends, outliers) that are hard to see in tables or single-variable charts.
- **The Evidence:** The post recommends scatter plots to explore and show how categories relate (e.g., tax rates vs life expectancy, turnout vs extremist support) and notes bubble charts as a sized-symbol variant [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Understanding correlation/relationship, spotting outliers.
- **Data Type:** Two quantitative variables measured for multiple observations (countries, districts, etc.).
- **Audience:** Mainstream readers, with awareness that this is more complex than basic charts [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** Points overlap so much that patterns are hidden.
- **Reason:** The post suggests switching to a 2D histogram when the message gets lost in overlapping dots [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Higher cognitive load than bars/lines for many readers.
- **The Risk:** Overplotting can obscure density and mislead about distributions [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Keeping a scatter plot even when most points sit on top of each other.
- **Why it fails:** Overlap hides the actual structure; the post recommends a 2D histogram in that case [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Large blobs of points where you can’t tell whether there are 5 points or 500.
- **The Test:** If you can’t visually judge where the data is dense versus sparse, treat it as an overplotting problem and try a 2D histogram [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce overlap by changing the display to a 2D histogram (heatmap-like binning).
- **Best Fix:** Use a 2D histogram specifically when overlap prevents the relationship from being seen, as recommended in the post [@muth_chart_types_guide_2025].
