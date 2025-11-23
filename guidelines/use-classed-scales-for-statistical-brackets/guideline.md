---
id: use-classed-scales-for-statistical-brackets
title: Use Classed Scales to Show Statistical Brackets
bibliography: references.bib
description: Use binned color scales when the goal is to communicate specific statistical
  thresholds or group regions by performance criteria.
labels:
- visual:color
- impact:storytelling
- task:categorize
- data:quantitative
- chart:choropleth
---

## The Rule <!-- role: advice -->
Use a classed color scale if your objective is to show whether data points fall into specific statistical buckets, such as "above/below average" or specific quantiles.

## The Logic <!-- role: reason -->
Classed scales simplify the data by grouping values into predefined ranges. This turns the map into a "communication device" that emphasizes the classification system itself rather than the raw data pattern [@muth_classed_vs_unclassed_2021]. It allows the reader to instantly see if a region satisfies a specific condition (e.g., "Is this county above the national average?") without interpreting a subtle color shade.

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating specific statements like "These areas have cancer mortality rates two standard deviations above the mean."
*   **Audience:** Readers who need to make binary or categorical judgments (e.g., Pass/Fail, High/Low) rather than see subtle variations.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploring general geographical patterns.
*   **Reason:** If the goal is to show broad trends (e.g., "Temperatures are generally higher in the South"), a classed map obscures the data's natural transitions and nuance.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Nuance. You lose the ability to see differences within a class. A value at the very bottom of a bin looks identical to a value at the very top of the same bin.
*   **The Risk:** Readers may perceive abrupt borders where none exist in reality, purely because of where the class breaks were set.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a continuous scale with a legend that marks the average.
*   **Why it fails:** Readers still have to judge whether a specific color shade is slightly lighter or darker than the reference point, which is cognitively difficult compared to a distinct color step.

## How to Check <!-- role: check -->
*   **The Test:** Ask a specific question about a region, such as "Is this region in the top 10%?" If you have to guess based on color intensity, you should be using a classed scale.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a stepped color scale.
*   **Best Fix:** Define custom break values (e.g., National Average) to ensure the color changes exactly where the statistical significance lies.
