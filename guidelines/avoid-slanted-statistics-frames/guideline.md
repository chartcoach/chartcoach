---
id: avoid-slanted-statistics-frames
title: Avoid Selective Data Trends in Titles
bibliography: references.bib
description: Avoid using specific statistics or trends in titles to imply neutrality,
  as this often masks bias.
labels:
- visual:text
- impact:bias-mitigation
- impact:trust
- data:quantitative
- chart:bar
- chart:line
---

## The Rule <!-- role: advice -->
When composing titles for controversial or complex topics, do not cherry-pick specific variables, values, or trends (a "Statistics Frame") to serve as the title. Instead, use an "Open-Ended Frame" that simply states the topic.

## The Logic <!-- role: reason -->
Viewers have an unwarranted conviction in the neutrality of visualizations ("numbers don't lie"). Titles that use "Statistics Frames"—referencing specific data points, variables, or trends—exploit this trust. They appear objective but can frame the narrative just as aggressively as emotional headlines by focusing the user's attention on only *one* aspect of a multi-faceted dataset.
*   **The Principle:** The Subtlety of Slants in Statistics Frames.
*   **The Evidence:** [@kong_frames_2018] found that slanted titles mentioning data variables (e.g., "Budget heading towards $500 billion") were powerful because they appeared neutral, yet they successfully cued viewers to infer specific, biased conclusions while remaining undetected.

## Where to Apply <!-- role: context -->
*   **User Goal:** Presenting a balanced view of a controversial subject.
*   **Data Type:** Datasets with multiple variables or complex trends (e.g., a line chart that fluctuates up and down).
*   **Audience:** Viewers who are likely to skim the content and rely on the title for the "takeaway."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Data Journalism / Opinion Pieces.
*   **Reason:** If the explicit goal is to argue a specific point or highlight a specific insight, a "Statistics Frame" is effective rhetoric. However, this should be recognized as editorializing, not neutral reporting.
*   **Scenario:** Single-Variable Charts.
*   **Reason:** If the chart *only* shows one variable (e.g., "Unemployment Rate"), naming the variable in the title is unavoidable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Narrative strength. "Open-Ended" titles (e.g., "US Defense Budget 1950-2015") are less engaging and provocative than "Statistics" titles (e.g., "Defense Budget Skyrockets").
*   **The Risk:** The viewer may not know what the "insight" is supposed to be and might leave without a clear conclusion.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a question as a title (e.g., "Is the Budget Increasing?").
*   **Why it fails:** [@kong_frames_2018] notes that "Undecided" or question-based titles can imply ambiguity where none exists, or subtly prompt the user to take a stance without providing the necessary context.
*   **The Wrong Fix:** Describing a trend that only tells half the story (e.g., "Budget drops 5%" when it rose 50% the previous year).

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your title contain a number, a percentage, or a direction word (increase/decrease)?
*   **The Test:** If you remove that specific number/trend from the chart, does the rest of the data support a different conclusion? If yes, your title is a biased "Statistics Frame."

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Rewrite the title to describe the *topic* (e.g., "Syrian Refugee Acceptance Rates") rather than the *result* (e.g., "US Accepts Fewer Refugees").
*   **Best Fix:** If you must highlight a specific trend, provide multiple titles or annotations that point out counter-trends or alternative interpretations visible in the same chart.
