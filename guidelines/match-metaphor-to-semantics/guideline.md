---
id: match-metaphor-to-semantics
title: Match Visual Metaphors to Data Semantics
bibliography: references.bib
description: Select chart types that visually afford the interpretation you want to
  convey (e.g., lines for continuous trends, bars for discrete values).
labels:
- chart:line
- chart:bar
- task:compare
- task:communicate
- impact:comprehension
- visual:shape
---

## The Rule <!-- role: advice -->
Select graphical marks based on their semantic "affordances": use lines when you want to imply continuity and trends, and use bars or dots when you want to imply discrete comparisons, even if the underlying data is identical.

## The Logic <!-- role: reason -->
Visual channels do not just convey values; they convey concepts. The choice of mark acts as a visual metaphor that primes the user's interpretation.
*   **The Principle:** **The Congruence Principle**. The content and format of the graphic should correspond to the content and format of the concepts conveyed [@bertini_why_2020].
*   **The Evidence:** [@bertini_why_2020] highlight studies showing that identical data plotted as bars leads to descriptions of "discrete comparisons," while lines lead to descriptions of "trends." A scatter plot invites correlation judgments, while aligned bar charts invite metric comparisons.

## Where to Apply <!-- role: context -->
*   **User Goal:** communicating a specific narrative or relationship (e.g., "sales are rising" vs. "sales were higher in Q1 than Q2").
*   **Data Type:** Quantitative data that can be interpreted either as a time-series/trend or as distinct categories.
*   **Audience:** General audiences where the *message* is as important as the raw data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strict Neutrality.
*   **Reason:** If you absolutely must avoid suggesting a relationship (like a trend between categorical variables) that doesn't exist, avoid connecting lines.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may constrain the user's thinking. A line chart might make it harder for a user to notice that individual points are missing or irregular.
*   **The Risk:** Using the wrong metaphor (e.g., a line chart for nominal categories) creates a false affordance of continuity.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a scatter plot for everything to be "neutral" and "precise."
*   **Why it fails:** It strips the data of semantic meaning. As [@bertini_why_2020] argue, a scatter plot of countries (donations vs. receipts) invites correlation analysis, whereas paired bars invite comparison of the two metrics per country.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using connected lines for distinct categories? Are you using floating dots for a continuous time series?
*   **The Test:** Ask a user to describe the chart. If they say "It goes up," you've successfully encoded a trend. If they say "A is bigger than B," you've encoded discrete comparison.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add or remove connecting lines between points.
*   **Best Fix:** Choose the chart type (Bar vs. Line) that matches the verbal description you want the user to form (Discrete vs. Continuous) [@bertini_why_2020].
