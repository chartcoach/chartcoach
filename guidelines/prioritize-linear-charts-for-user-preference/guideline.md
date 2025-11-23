---
id: prioritize-linear-charts-for-user-preference
title: Prioritize Linear Layouts for User Satisfaction
bibliography: references.bib
description: Users rate linear bar charts higher than radial charts for visualizing
  daily patterns.
labels:
- chart:bar
- chart:radial
- impact:preference
- audience:general
- data:temporal
---

## The Rule <!-- role: advice -->
Choose linear layouts over radial layouts to maximize user preference ratings.

## The Logic <!-- role: reason -->
Users generally prefer visualizations that allow them to complete tasks accurately and efficiently.
*   **The Principle:** Perceived usability often correlates with actual performance; when users struggle with radial orientations, their satisfaction scores drop.
*   **The Evidence:** In user studies comparing linear and radial designs for daily data, the single 24-hour linear bar chart (E-4) received the highest overall user preference rankings, significantly outperforming radial alternatives (E-1 and E-2) [@waldner_comparison_2020]. This contradicts the assumption that radial charts are preferred for their aesthetic novelty in this context [@zeng_review_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Consuming information in a dashboard or report where user satisfaction and perceived ease of use are metrics of success.
*   **Data Type:** 24-hour quantitative data.
*   **Audience:** Non-expert users or general public.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience specifically requests a "clock" visualization for stylistic branding reasons.
*   **Reason:** Client constraints or branding guidelines may override general user preference data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You forego the "circular" aesthetic that some designers find visually interesting.
*   **The Risk:** The design may look "standard" or "boring" compared to a rose chart, though it will be more liked by users trying to read the data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming users find radial charts more "engaging" or "fun" because they look like clocks.
*   **Why it fails:** Evidence shows that users rate the linear versions higher, likely because they are easier to read [@waldner_comparison_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the interface using a radial chart primarily for "engagement"?
*   **The Test:** Survey a small sample of users comparing the radial version against a linear version; evidence suggests they will likely prefer the linear one.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace the radial widget with a linear bar chart.
*   **Best Fix:** Use a clean, well-labeled 24-hour linear bar chart (Design E-4).
