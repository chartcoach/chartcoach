---
id: provide-explicit-graph-instructions
title: Provide Explicit Instructions for Reading Graphs
bibliography: references.bib
description: Do not assume graph literacy; provide text or auditory explanations of
  how to interpret the visualization.
labels:
- chart:line
- chart:survival-curve
- task:comprehension
- visual:annotation
- impact:accessibility
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->
Include clear, comprehensible explanations of the graph's meaning and specific conclusions to be drawn. Do not rely on the chart to speak for itself.

## The Logic <!-- role: reason -->
Graph literacy is not universal. Many individuals lack the skills to interpret standard charts like survival curves or box plots. Research shows that providing instructions or detailed verbal descriptions significantly improves attention to critical data points (like the midpoint of a survival curve) and aids decision-making [@lipkus_numeric_2007].

*   **The Principle:** Scaffolding / Guided Interpretation.
*   **The Evidence:** [@lipkus_numeric_2007] notes that instructions were instrumental in interpreting survival graphs for inexperienced people and that verbal explanations made complex genetic graphs more persuasive.

## Where to Apply <!-- role: context -->
*   **User Goal:** Clinical decision making or understanding complex trends over time.
*   **Data Type:** Survival curves, mortality curves, or complex multi-variable plots.
*   **Audience:** Patients, elderly populations, or those with low education levels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Expert-to-Expert communication.
*   **Reason:** If the audience consists entirely of domain experts (e.g., statisticians), over-explaining standard charts creates friction.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space. Explanatory text adds clutter.
*   **The Risk:** If the explanation is biased, it can skew the user's interpretation more than the data itself (e.g., framing effects).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a simple title like "Survival Rates."
*   **Why it fails:** It tells the user *what* the data is, but not *how* to read it (e.g., "The height of the line shows the percentage of people still alive...").

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a paragraph of text or a "How to read this chart" annotation?
*   **The Test:** Show the chart to a layperson without speaking. Can they tell you the conclusion?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a caption summarizing the main takeaway.
*   **Best Fix:** Add a specific annotation explaining the axes and the mechanism of the line (e.g., "As the line goes down, fewer people are surviving").
