---
id: visualize-foreground-and-background
title: Visualize Both Foreground and Background Data
bibliography: references.bib
description: Ensure visualizations explicitly show the population at risk, not just
  the affected individuals.
labels:
- chart:icon-array
- visual:layout
- impact:accuracy
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
When designing risk visualizations, explicitly display both the **foreground information** (the number of people harmed/affected) and the **background information** (the total number of people at risk/not affected).

## The Logic <!-- role: reason -->
Biases like denominator neglect occur because the "event" (the numerator) is often more salient than the "non-event" (the denominator). By visually representing the background population, you force the viewer to process the part-to-whole relationship rather than looking at the event count in isolation.

*   **The Principle:** **Superordinate Class Representation**. Visuals allow people to disentangle classes that overlap in ratios, helping them see the "whole" distinct from the "part."
*   **The Evidence:** Research cited in the review supports the hypothesis that graphical formats displaying both foreground and background contribute to focusing attention on the relationship between the numerator and denominator [@garcia-retamero_using_2012].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the likelihood of an event across groups with different sizes.
*   **Data Type:** Medical statistics, accident rates, or any "X out of Y" data.
*   **Audience:** Users with limited working memory or attention, who might otherwise discard the denominator information.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-density time-series data or large-scale aggregate trends.
*   **Reason:** Showing every individual "non-event" data point (the background) is impossible or visual noise in high-volume datasets (e.g., a line chart of infection rates).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual simplicity. You cannot just use a bar chart of "Total Deaths"; you must show the "Total Population" context, which adds graphical density.
*   **The Risk:** Visual clutter if the background population is extremely large compared to the foreground event (e.g., 1 death in 1,000,000 requires a very large background representation).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a pie chart or bar chart that only compares the absolute number of "events" (e.g., a bar chart comparing 80 deaths vs 5 deaths).
*   **Why it fails:** This reinforces denominator neglect by visually emphasizing the magnitude of the numerator while hiding the sample size context [@garcia-retamero_using_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your graphic only show the "black dots" (the bad outcomes)?
*   **The Test:** If you remove the text labels, can the user tell how many people *didn't* get sick/die? If not, you are missing the background info.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a stacked bar chart where the total height represents the total population, and the segment represents the risk.
*   **Best Fix:** Use an icon array where every individual in the sample is represented by a distinct mark (e.g., 800 circles total), with the affected individuals colored differently [@garcia-retamero_using_2012].
