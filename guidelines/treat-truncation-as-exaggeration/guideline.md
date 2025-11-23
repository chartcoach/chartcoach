---
id: treat-truncation-as-exaggeration
title: Treat Y-Axis Truncation as an Exaggeration Technique in All Chart Types
bibliography: references.bib
description: Truncating the y-axis increases perceived effect size severity equally
  in both bar and line charts.
labels:
- chart:bar
- chart:line
- visual:axis
- impact:bias
- task:compare
- data:quantitative
---

## The Rule <!-- role: advice -->

Assume that truncating the y-axis (starting from a non-zero value) will exaggerate the perceived severity of data differences, regardless of whether you use a bar chart or a line chart.

## The Logic <!-- role: reason -->

While conventional wisdom often suggests that truncating the y-axis is "dishonest" for bar charts but acceptable for line charts, empirical evidence suggests the perceptual impact is similar for both. 
*   **The Principle:** Perceived Severity. As summarized in the review by Zeng and Battle [@zeng_review_2023], experiments conducted by Correll et al. demonstrate that increased truncation leads to increased perceived severity of effect sizes.
*   **The Evidence:** In controlled experiments, Correll et al. [@correll_truncating_2020] found no significant effect of visualization design (bar vs. line) on the perceived effect size. Both chart types produced inflated subjective importance of differences when the axis was truncated.

## Where to Apply <!-- role: context -->

*   **User Goal:** When the user needs to make subjective judgments about the importance or magnitude of a change (e.g., "Is this sales increase significant?").
*   **Data Type:** Quantitative data where the absolute magnitude of values matters as much as the relative difference.
*   **Audience:** General audiences who rely on visual pattern matching rather than reading specific numerical labels.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Visualizing small variations in data with a large baseline offset (e.g., human body temperature or stock market fluctuations).
*   **Reason:** In these specific domains, small absolute changes have massive semantic significance. As noted by Correll et al. [@correll_truncating_2020], designers must align the visual scale with the "meaningful effect size" of the domain, rather than adhering to a dogmatic zero-baseline rule.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Including zero can compress small but real variations into a flat line, making them difficult to distinguish.
*   **The Risk:** Truncating the axis risks misleading the viewer into believing a trivial change is a major trend.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Switching from a truncated bar chart to a truncated line chart to avoid "lying."
*   **Why it fails:** Correll et al. [@correll_truncating_2020] show that the "bias" (exaggeration of effect) persists in line charts just as it does in bar charts.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the y-axis start at a value other than zero?
*   **The Test:** Check the aspect ratio of the change. If the visual difference looks dramatic, ask if the numerical difference carries the same weight in the real world.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Reset the y-axis to zero if the absolute magnitude is the primary story.
*   **Best Fix:** Determine the "meaningful effect size" for your specific domain. If a 5% change is catastrophic, truncation is appropriate to highlight it; if a 5% change is noise, include zero to minimize it.
