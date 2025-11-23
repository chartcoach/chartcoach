---
id: visualize-part-to-whole-context
title: Visualize the Denominator for Accuracy
bibliography: references.bib
description: Use part-to-whole visualizations to promote accurate risk assessment
  rather than numerator-only charts.
labels:
- chart:icon-array
- chart:stacked-bar
- task:assess-risk
- visual:part-to-whole
- impact:accuracy
- data:probability
- audience:patient
---

## The Rule <!-- role: advice -->
When presenting risk data where comprehension and accuracy are the goals, use graphs that explicitly display the denominator (the whole population) alongside the numerator (the affected group), rather than displaying the numerator alone.

## The Logic <!-- role: reason -->
Visualizing the numerator without the denominator emphasizes the magnitude of the risk event itself, which can alarm users and drive behavior change, but it often degrades the user's ability to judge the actual likelihood of the event. By contrast, showing the part-to-whole relationship allows the user to visually compare the risk against the non-event, promoting accurate probability judgments [@ancker_rethinking_2007].

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing the true likelihood of a medical side effect or disease risk.
*   **Data Type:** Probability or frequency data (e.g., "10% risk" or "10 in 100").
*   **Audience:** Patients or health consumers who need to make informed decisions based on realistic expectations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is purely to motivate risk-averse behavior (e.g., smoking cessation).
*   **Reason:** Graphs that depict numerators alone (e.g., a bar chart showing only the number of people who get cancer) emphasize the risk and are more likely to promote risk-related behavior changes, even if they reduce statistical accuracy [@ancker_rethinking_2007].

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visual impact of the "risk" is diluted by the presence of the "non-risk" data.
*   **The Risk:** The user may perceive the risk as less urgent or significant than intended if the denominator is very large.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a simple bar chart that only measures the height of the risk (e.g., a bar 10 units high for 10%).
*   **Why it fails:** This hides the context of the total population, making it difficult for the user to visually assess the proportion [@ancker_rethinking_2007].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart contain visual elements representing the people who *do not* experience the outcome?
*   **The Test:** If you remove the axis labels, can you still see what proportion of the total group is affected?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a second bar representing the "non-event" population next to the risk bar.
*   **Best Fix:** Use a stacked bar chart or an icon array (pictograph) where the risk subset is visually nested within or stacked against the total population.
