---
id: explicitly-encode-deltas
title: Explicitly Encode Deltas for Comparison Tasks
bibliography: references.bib
description: Directly visualizing the difference between data points significantly
  improves search efficiency and accuracy compared to showing individual values.
labels:
- chart:bar
- chart:dot-plot
- task:compare
- task:search
- visual:position
- visual:length
- impact:efficiency
---

## The Rule <!-- role: advice -->
Directly encode the numeric differences (deltas) between data values rather than relying on the viewer to compare individual data points mentally.

## The Logic <!-- role: reason -->
Perceiving the relationship between two separate items is a serial, cognitively expensive process. When viewers must extract a relation (like the difference between two bars) from individual values, response times slow down significantly as more data is added.
*   **The Principle:** Direct Encoding vs. Relative Extraction. Directly representing the delta turns a complex relational task into a simple feature search.
*   **The Evidence:** In visual search tasks, finding a specific relation (e.g., an increase) was 49-95% faster when encoded as deltas. Accuracy in judging proportions improved by 30%, and error rates in estimating average differences dropped by 25% [@nothelfer_measures_2020].

## Where to Apply <!-- role: context -->
This rule is critical when the primary user task involves identifying, counting, or averaging changes or differences.
*   **User Goal:** Searching for specific trends (e.g., "Which category increased?"), judging the prevalence of a trend (e.g., "Did more categories rise or fall?"), or estimating the average magnitude of change.
*   **Data Type:** Paired data values (e.g., Year 1 vs. Year 2, Pre-test vs. Post-test).
*   **Audience:** Users performing rapid data exploration or making decisions based on magnitude of change.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user must filter by the original absolute values.
*   **Reason:** Delta encodings strip away the context of the "base" value. For example, if a user needs to find "the average increase for values that started above 50," a delta-only chart makes this impossible because the starting value is invisible [@nothelfer_measures_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the context of the individual data values (e.g., you can see a score improved by 10 points, but not whether it went from 50 to 60 or 90 to 100).
*   **The Risk:** Bias in estimation. Participants in Experiment 3 tended to systematically underestimate the average difference when viewing delta encodings [@nothelfer_measures_2020].
*   **Space:** Displaying deltas often requires additional screen real estate if the absolute values must also be shown.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing two bar charts side-by-side and expecting users to spot the differences efficiently.
*   **Why it fails:** Visual processing of relations between individual items is "staggeringly inefficient," taking 164-266ms longer per additional data pair compared to only 8-135ms for deltas [@nothelfer_measures_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart require the user's eye to ping-pong between two points to determine the magnitude of difference?
*   **The Test:** Ask a viewer to identifying the largest change in the dataset. If they have to scan every pair individually to do math in their head, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a label explicitly stating the numeric change next to the paired values.
*   **Best Fix:** Create a dedicated visualization for the differences (e.g., a bar chart of changes) positioned alongside or overlaid on the absolute values.
