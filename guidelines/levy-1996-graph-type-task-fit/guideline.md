---
id: levy-1996-graph-type-task-fit
title: Use Line Graphs for Trends and Bar Graphs for Details
bibliography: references.bib
description: Users prefer line graphs for seeing trends and bar graphs for reading
  specific details.
labels:
- chart:line
- chart:bar
- task:trend-analysis
- task:detail-retrieval
- impact:clarity
- audience:general
---

## The Rule <!-- role: advice -->
Select line graphs when the goal is to convey general trends or relationships, and select bar graphs when the goal is to examine specific details or point values.

## The Logic <!-- role: reason -->
User preferences for graph types are strongly correlated with the intended rhetorical purpose of the visualization. In multiple experiments, subjects systematically judged line graphs as more appropriate for revealing trends ("the gist"), whereas bar graphs were judged superior for revealing detailed relationships ("the nitty-gritty").
*   **The Principle:** Task-Format Correspondence
*   **The Evidence:** In Experiments 1 and 2, @levy_gratuitous_1996 found that subjects chose line graphs for "trend" scenarios and bar graphs for "detail" scenarios with high consistency.

## Where to Apply <!-- role: context -->
This rule applies when choosing between standard 2D chart types for quantitative data.
*   **User Goal:** Distinguishing between high-level pattern recognition vs. precise value extraction.
*   **Data Type:** Quantitative data (time-series or categorical) where a choice between connected points (lines) or distinct shapes (bars) is possible.
*   **Audience:** General audiences, corporate boards, or analysts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data represents discrete, unordered categories where a connected line implies a non-existent continuity.
*   **Reason:** While not explicitly tested as a failure mode in this paper, the preference for lines relies on the "trend" concept; if no trend exists logic applies, the preference may not hold.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Using a line graph for details may make individual points harder to isolate visually. Using a bar graph for trends may visually clutter the "shape" of the data with vertical ink.
*   **The Risk:** Mismatching the type (e.g., bars for trends) may slow down the user's ability to grasp the intended message immediately.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a bar graph to show a long time-series trend.
*   **Why it fails:** Subjects in the study associated bar graphs with digging into details, potentially distracting from the overall slope or pattern @levy_gratuitous_1996.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using vertical bars to show a smooth curve? Are you using a line to connect unrelated discrete items?
*   **The Test:** Ask yourself: "Is the main point of this slide the slope (trend) or the exact height (detail)?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Toggle the chart type in your software from Bar to Line (or vice versa) based on the primary question the chart answers.
*   **Best Fix:** If both are needed, provide a trend line for the overview and a table or annotated bar chart for the specific data points of interest.
