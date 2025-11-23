---
id: provide-alternatives-for-difficult-charts
title: Provide Alternative Views or Formats for Complex Charts
bibliography: references.bib
description: Allow users to transform difficult visualizations (like pie charts) into
  simplified alternatives to support cognitive accessibility.
labels:
- chart:pie
- chart:line
- chart:bar
- impact:accessibility
- impact:flexibility
- audience:cognitive-disability
- visual:marks
---

## The Rule <!-- role: advice -->
Ensure users can adjust the presentation of difficult chart types into accessible alternatives that accomplish the same analytical task. If you use high-risk charts, such as pie charts or line charts without discrete marks, provide controls to transform them into simpler formats or provide alternative explanations.

## The Logic <!-- role: reason -->
Specific chart types pose cognitive difficulties and misinterpretation risks. Research into data accessibility for people with intellectual and developmental disabilities (IDD) indicates that standard visualizations often require adaptation to be effective. By allowing flexibility, you accommodate diverse cognitive needs without removing the original design for other users.
*   **The Principle:** Flexible (POUR+CAF) — Accessibility requires respecting user agency to adjust the presentation [@elavsky_how_2022].
*   **The Evidence:** Research suggests alternative chart types, such as treemaps with pictograms or simplified scatterplots, better match the cognitive needs of people with IDD [@wu_understanding_data_2021].

## Where to Apply <!-- role: context -->
This applies to "high-risk" chart types that are cognitively demanding or prone to misinterpretation.
*   **Chart Types:** Pie charts, line charts lacking discrete marks (dots at data points), and bar charts lacking countable isotypes [@elavsky_how_2022].
*   **Audience:** Users with cognitive disabilities, intellectual and developmental disabilities (IDD), or those requiring lower cognitive load [@wu_understanding_data_2021].
*   **User Goal:** Performing analytical tasks where the default visualization might obscure precise values or trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization is already in its most simplified, accessible form.
*   **Reason:** If the default view already utilizes accessible techniques—such as using discrete marks, limiting categories, or using isotype pictograms—a toggle for an "alternative" view may be redundant [@cu-visualab_state_states].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increased development effort is required to build and maintain multiple views or transformation logic (e.g., logic to convert a pie chart to a stacked bar).
*   **The Risk:** The interface becomes more complex due to the addition of controls or toggles needed to switch between views.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** relying solely on a static image of a complex chart (e.g., a standard pie chart) without options for modification.
*   **Why it fails:** This assumes all users process the geometry (angles/slices) effectively. Without the ability to switch to a linear format (like a bar) or see discrete marks, users with cognitive disabilities may be excluded [@elavsky_how_2022].

## How to Check <!-- role: check -->
*   **Visual Sign:** Identify if the interface uses pie charts, smooth line charts, or standard bar charts.
*   **The Test:** Check if there is a mechanism (button, toggle, or setting) to change the representation (e.g., "View as Table," "Show Points," or "Switch to Bar"). If not, check if a clear alternative explanation is provided alongside the chart [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Provide a static alternative explanation or summary text next to the chart that conveys the same analytical takeaway.
*   **Best Fix:** Implement interactive controls that allow the user to transform the chart type—for example, changing pies into treemaps or stacked bars, adding discrete marks to line intervals, or adding countable isotypes to divide bars [@elavsky_how_2022; @cu-visualab_state_states].
