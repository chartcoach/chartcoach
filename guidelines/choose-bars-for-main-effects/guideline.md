---
id: choose-bars-for-main-effects
title: Use Bar Graphs for Main Effects and Discrete Comparisons
bibliography: references.bib
description: Bar graphs support mental averaging and discrete comparisons better than
  line graphs, offering more interpretative flexibility.
labels:
- chart:bar
- task:summarize
- visual:proximity
- impact:comprehension
- data:multivariate
- audience:general
---

## The Rule <!-- role: advice -->
Use clustered bar graphs when you want viewers to identify main effects (overall averages) or make discrete comparisons between the legend variable and the axis variable.

## The Logic <!-- role: reason -->
Bar graphs rely on the Gestalt principles of **proximity** (grouping bars by the x-axis category) and **similarity** (grouping bars by color/legend).
*   **The Principle:** This grouping reduces working memory load, allowing viewers—particularly those with high graphicacy skills—to mentally average the bars to find "main effects" (e.g., "Overall, condition A is higher than B") [@shah_bar_2011].
*   **The Evidence:** Viewers are more likely to describe main effects and "z–y interactions" (comparisons of the legend variable within an x-axis category) with bar graphs because the format is less biased toward slope than line graphs.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to assess overall differences between groups (main effects) or compare specific adjacent values (discrete comparisons).
*   **Data Type:** Multivariate data where the x-axis is categorical or where discrete values are more important than trends.
*   **Audience:** Audiences with at least moderate graphical literacy (graphicacy), as mental averaging still requires skill.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the specific rate of change (slope) or the interaction between variables is the most critical insight.
*   **Reason:** Line graphs make interactions visually "pop" via slope differences, whereas bar graphs require the user to cognitively construct the interaction by comparing height differences across groups [@shah_bar_2011].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate visual salience of trends and interactions.
*   **The Risk:** The viewer interprets the data as a set of isolated facts rather than a cohesive system of relationships.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming a bar graph makes the "main effect" obvious to everyone.
*   **Why it fails:** Research shows that even with bar graphs, low-skilled users struggle to mentally compute averages or identify main effects without explicit aid [@shah_bar_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the bars grouped tightly by the x-axis category?
*   **The Test:** Can you easily visually estimate the average height of all "blue" bars vs. all "red" bars? If yes, the format supports the main effect.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure the bars to be compared are placed in close proximity.
*   **Best Fix:** If the main effect is the key insight, plot the averages directly rather than forcing the user to mentally compute them from a multivariate bar chart.
