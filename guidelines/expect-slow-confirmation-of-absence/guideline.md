---
id: expect-slow-confirmation-of-absence
title: Budget Double the Time for Negative Search
bibliography: references.bib
description: Users take more than twice as long to confirm a target is missing than
  to find a target that is present.
labels:
- task:verification
- impact:efficiency
- data:categorical
- visual:layout
- context:dashboards
---

## The Rule <!-- role: advice -->
When designing tasks where the user must verify that a specific data point (like an error flag) is *not* present, assume the task will take at least twice as long as finding a point that *is* present. Design explicit "All Clear" indicators rather than forcing the user to scan an empty field.

## The Logic <!-- role: reason -->
Visual search is essentially a "self-terminating" process. When a target is found, the search stops. When a target is absent, the user must (theoretically) check every item or exhaust their patience before quitting.
*   **The Principle:** Target-Absent vs. Target-Present Asymmetry.
*   **The Evidence:** Across 1 million trials, the average ratio of target-absent slopes to target-present slopes was greater than 2:1. This holds true regardless of whether the search was easy (feature) or hard (spatial configuration) [@wolfe_what_1998].

## Where to Apply <!-- role: context -->
*   **User Goal:** Verifying "system health," checking for outliers, or ensuring no data quality errors exist.
*   **Data Type:** Large sets of items, tables, or status grids.
*   **Audience:** Operators or auditors who need to certify that a condition is *not* met.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset is extremely small (subitizing range, < 5 items).
*   **Reason:** In very small sets, the processing difference is negligible in absolute time.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. You need to add a summary indicator (e.g., a big green checkmark) rather than just showing the data plot.
*   **The Risk:** If you rely solely on the plot, users may prematurely quit searching and assume the target is absent when they simply missed it (false negative).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming that because a "red dot" pops out instantly, the *absence* of a red dot is instantly recognized.
*   **Why it fails:** While finding the red dot is fast, confirming there are *zero* red dots requires a longer scan of the distractors to ensure one isn't hiding, with a slope ratio > 2.0 compared to the search [@wolfe_what_1998].

## How to Check <!-- role: check -->
*   **Visual Sign:** A dashboard that looks "clean" when everything is fine, but provides no explicit positive confirmation of safety.
*   **The Test:** Ask a user, "Are there any errors?" Measure the time it takes them to answer "No" versus the time it takes them to point to an error when one exists.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a summary header stating "0 Errors Found."
*   **Best Fix:** Aggregate the data. Instead of asking the user to scan 1,000 points for a failure, pre-process the search and display the status explicitly.
