---
id: limit-chart-complexity
title: Limit Chart Complexity and Avoid Dual Axes
bibliography: references.bib
description: Reduce cognitive load by limiting data categories to five, avoiding decorative
  3D elements, and separating dual axes.
labels:
- impact:accessibility
- impact:cognitive-load
- visual:axes
- visual:3d
- chart:dual-axis
- audience:general
- data:multivariate
---

## The Rule <!-- role: advice -->
Limit chart complexity appropriate to the task. Specifically, do not include more than 5 data categories. Do not use dual Y or X axes without first presenting the two charts separately. Do not encode information along a third spatial dimension (z-axis) unless the data itself is spatially 3D.

## The Logic <!-- role: reason -->
Excessive complexity creates ambiguity and cognitive overload. This guideline is based on the "Understandable" principle of Chartability, ensuring information is presented without ambiguity [@elavsky_how_2022].
*   **The Principle:** Working Memory Limits. Research indicates that effective working memory is limited, suggesting charts should contain no more than five data categories to prevent cognitive overload [@ed_design_guidelines].
*   **The Mechanism:** Dual-axis graphs are often contentious and difficult to interpret because they rely on attentive processing rather than pre-attentive recognition. Presenting them as a single view assumes a level of expertise that cannot be guaranteed for every user [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This advice applies to complex data systems and interfaces where clarity is prioritized over density.
*   **User Goal:** Minimizing cognitive load and ensuring the data is understandable without extensive training.
*   **Data Type:** Multivariate data, categorical data sets, and comparisons of different measures (e.g., different scales on dual axes).
*   **Audience:** Broad audiences, including users with cognitive disabilities or memory limitations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** 3D Data Visualization.
*   **Reason:** If the data itself is inherently 3D (such as spatial data or physical modeling), using the z-axis is appropriate and necessary [@elavsky_how_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need more space to display information, as splitting dual axes requires two separate charts or small multiples.
*   **The Risk:** Excluding categories beyond the top 5 may require interactive filtering or "Other" groupings, potentially hiding long-tail data in the static view.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming the audience consists of "trained experts" who can handle dual axes.
*   **Why it fails:** It is difficult to evaluate an audience's skill level effectively, and even experts may struggle with the cognitive load of dual scales [@elavsky_how_2022].
*   **The Wrong Fix:** Using 3D effects on 2D data (e.g., 3D bar charts) for aesthetic impact.
*   **Why it fails:** This adds unnecessary complexity without conveying additional information.

## How to Check <!-- role: check -->
*   **Visual Sign:** Count the number of distinct categories in the legend or axis. Are there more than 5?
*   **Visual Sign:** Does the chart have a scale on both the left and right vertical axes (dual Y-axis)?
*   **Visual Sign:** Is there a z-axis (depth) applied to non-spatial data?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Filter the dataset to show only the top 5 most relevant categories.
*   **Best Fix:** Split dual-axis charts into two separate charts placed side-by-side or vertically aligned to allow for easier comparison without ambiguity.
