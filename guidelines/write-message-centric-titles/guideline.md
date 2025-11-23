---
id: write-message-centric-titles
title: Write Message-Centric Titles
bibliography: references.bib
description: Ensure titles explicitly state the main message or finding of the visualization
  to improve recall and understanding.
labels:
- visual:text
- impact:recall
- impact:comprehension
- audience:general
- chart:all
---

## The Rule <!-- role: advice -->
Write titles that explicitly state the main finding or message of the visualization, rather than generic descriptions of the data variables.

## The Logic <!-- role: reason -->
According to eye-tracking and recall analysis by [@borkin_beyond_2016], titles are among the most important elements for visualization recognition and recall. They are fixated on 59% of the time during encoding and are the element most likely to be described by users later. When a title includes the main message (e.g., "66% of Americans feel..."), users recall the visualization's message significantly better than when titles are generic (e.g., "Cities"). The title serves as a "semantic association" that helps retrieve the memory of the visualization.

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating a specific insight or narrative.
*   **Data Type:** Any visualization intended for communication rather than pure exploration.
*   **Audience:** All audiences, particularly those viewing static visualizations (infographics, news, reports).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploratory Data Analysis (EDA).
*   **Reason:** In tools designed for pure exploration where the specific insight is not yet known or varies by user query, a prescriptive title may introduce bias or be impossible to generate dynamically.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Neutrality. A message-centric title frames the data interpretation immediately.
*   **The Risk:** If the title is poorly phrased or inaccurate, it will mislead the user more effectively than a generic title because users rely on it heavily for interpretation [@borkin_beyond_2016].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using generic "X vs Y" titles (e.g., "Unemployment Rates 2010-2015").
*   **Why it fails:** It forces the user to decode the visual pattern to find the message, which increases cognitive load and decreases the likelihood of correct message recall.
*   **The Wrong Fix:** Placing the title at the bottom of the chart.
*   **Why it fails:** [@borkin_beyond_2016] found that titles at the top are fixated on more frequently (76% vs 63%) and described more often than those at the bottom.

## How to Check <!-- role: check -->
*   **Visual Sign:** Read the title alone. Does it tell you what the data *says*, or just what the data *is*?
*   **The Test:** Cover the chart and read the title. If you don't know the trend (e.g., "increasing," "declining," "leading"), the title is too generic.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a subtitle that summarizes the trend.
*   **Best Fix:** Rewrite the main header to be a declarative sentence summarizing the insight (e.g., change "Sales by Region" to "West Region Leads Sales Growth").
