---
id: mackinlay-expressiveness-principle
title: Visualize All the Facts and Only the Facts
bibliography: references.bib
description: Ensure the chosen visual language expresses all input information without
  implying incorrect additional facts.
labels:
- chart:general
- task:design-selection
- impact:accuracy
- impact:integrity
- data:relational
- source:theory
---

## The Rule <!-- role: advice -->
Choose a visual language that expresses **exactly** the input information—it must encode all the intended facts and, crucially, encode **only** those facts.

## The Logic <!-- role: reason -->
A set of facts is expressible in a visual language only if the language contains a sentence that encodes every fact in the set and encodes *no additional* incorrect facts.
*   **The Principle:** Expressiveness Criteria
*   **The Evidence:** [@mackinlay_automating_1986] demonstrates that expressing additional information (such as implying an order where none exists) is potentially dangerous because users may interpret these geometric relationships as data facts.

## Where to Apply <!-- role: context -->
This applies to the fundamental selection of chart types for any dataset.
*   **User Goal:** Accurate interpretation of data relationships.
*   **Data Type:** Relational data, particularly when distinguishing between nominal (unordered) and ordinal/quantitative (ordered) sets.
*   **Audience:** Any viewer relying on the chart for decision-making.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Standard conventions overwhelm strict logic.
*   **Reason:** Sometimes a convention is so strong (e.g., using an axis for a nominal domain) that users ignore the implied ordering "fact" naturally. [@mackinlay_automating_1986] notes that while axes technically imply order, the convention of ignoring this for nominal labels is standard.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may have to abandon familiar chart types (like bar charts) for specific data types if they imply relationships that don't exist.
*   **The Risk:** Viewers might infer correlations or rankings that are artifacts of the design, not the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a bar chart for nominal (unordered) categories (e.g., Countries).
*   **Why it fails:** The length of the bars and their sequence implies an ordering (Ranking) among the categories that does not exist in the data [@mackinlay_automating_1986].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the geometry (length, slope, position) suggest a relationship (A > B) that isn't in the data table?
*   **The Test:** Ask, "If I rearrange the order of these items, does the meaning of the chart change?" If yes, but the data is unordered, the design is flawed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove connecting lines or ordered geometry if the data is discrete and unordered.
*   **Best Fix:** Switch to a chart type that matches the data structure (e.g., use a plot chart/dot plot instead of a bar chart for nominal data to avoid implying rank by length).
