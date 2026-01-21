---
id: use-whitespace-as-structure-not-decoration
title: Use White Space to Structure the Chart
bibliography: references.bib
description: Use appropriately sized white space (including bar widths and gaps) to
  preserve readable grouping, hierarchy, and interpretation.
labels:
- chart:bar
- task:compare
- visual:space
- impact:accessibility
- data:categorical
- audience:general
- source:community-practices
---

## The Rule <!-- role: advice -->

Use white space and padded spacing intentionally to create clear grouping and hierarchy; avoid extremes of too much or too little space (e.g., very thin bars with large gaps, or very thick bars with tiny gaps) that make the chart harder to perceive and interpret [@elavskyHowAccessibleMy2022].

## The Logic <!-- role: reason -->

Poor spacing changes how viewers segment and relate marks and labels, which can create perceivable and understandable problems by weakening grouping and visual hierarchy [@elavskyHowAccessibleMy2022]. White space is a functional design element (not “wasted space”) that guides the eye, supports balance, and improves readability by separating and grouping related content [@towardsdatascience_data_visualisation; @misc{calliaweb_whitespace_not}].

- **The Principle:** White space as visual punctuation for grouping and hierarchy
- **The Evidence:** [@towardsdatascience_data_visualisation; @misc{calliaweb_whitespace_not}; @elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for charts where spacing encodes or strongly affects perception of structure.

- **User Goal:** Comparing values and scanning categories without confusion
- **Data Type:** Categorical or binned interval displays where mark width and inter-mark gaps are prominent (e.g., bar charts)
- **Audience:** General audiences, including people who may experience perceivable/understandable barriers from unclear hierarchy [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** None specified in the provided sources.
- **Reason:** The provided evidence does not describe cases where inappropriate spacing would be preferable.

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You may lose flexibility to “pack” more content into the same space if you increase spacing for clarity [@towardsdatascience_data_visualisation; @misc{calliaweb_whitespace_not}].
- **The Risk:** If you over-correct, you may introduce a different spacing extreme (too sparse or too dense), which can still harm readability and interpretation [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Treating white space as wasted space and removing it to “fit everything in.”

- **Why it fails:** Overly tight layouts reduce grouping clarity and readability, undermining hierarchy and making it harder to interpret the chart [@misc{calliaweb_whitespace_not}; @towardsdatascience_data_visualisation; @elavskyHowAccessibleMy2022].

- **The Wrong Fix:** Adding large empty gaps (e.g., very thin bars with oversized intervals) to make the chart look “clean.”

- **Why it fails:** Excessive gaps weaken the ability to compare and relate adjacent marks, creating perceivable and understandable issues [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Bars/marks feel either cramped (hard to distinguish groups and read nearby text) or overly sparse (marks look disconnected; comparisons feel effortful) [@elavskyHowAccessibleMy2022].
- **The Test:** Inspect the chart specifically for spacing extremes on interval-based marks (e.g., thin bars with large gaps, or thick bars with minimal gaps) and judge whether grouping/hierarchy remains clear and readable [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust mark widths and the gaps between marks toward a balanced middle ground so adjacent categories are clearly separated but still visually related for comparison [@elavskyHowAccessibleMy2022].
- **Best Fix:** Rework the layout spacing system (padding, alignment, and grouping) so white space consistently communicates hierarchy and relatedness across the entire chart, treating it as a core design element rather than leftover space [@towardsdatascience_data_visualisation; @misc{calliaweb_whitespace_not}; @elavskyHowAccessibleMy2022].
