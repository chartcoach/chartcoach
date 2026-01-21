---
id: avoid-assessment-items-that-require-specialized-statistical-knowledge
title: Avoid Assessment Items That Require Specialized Statistical Knowledge
bibliography: references.bib
description: Exclude visualization types whose interpretation depends on domain-specific
  statistical concepts if you are testing general visualization literacy.
labels:
- impact:fairness
- audience:novice
- custom:content-selection
- custom:measurement
---

## The Rule <!-- role: advice -->

Exclude visualization types (or item content) that require specialized statistical knowledge beyond general chart reading when targeting non-expert users.

## The Logic <!-- role: reason -->

If answering depends on outside prerequisite knowledge, test scores confound visualization literacy with unrelated expertise. VLAT explicitly excluded box plots because understanding them relies on statistical concepts (percentiles/quartiles/IQR), which would threaten the intended construct for non-experts.

- **The Principle:** Reduce construct-irrelevant variance
- **The Evidence:** [@leeVLATDevelopmentVisualization2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Measuring general ability to read/interpret common visualizations
- **Data Type:** Charts that can be interpreted directly from axes/marks without specialized formulas
- **Audience:** General public / non-expert adults

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your audience is expected to know the prerequisite statistics (e.g., trained analysts or statistics students).
- **Reason:** In that case, including such charts may be appropriate and aligned to the population. [@leeVLATDevelopmentVisualization2017]

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced coverage of certain widely used analytical plots in expert settings.
- **The Risk:** You may under-measure literacy for audiences who do encounter these charts professionally. [@leeVLATDevelopmentVisualization2017]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the chart but adding a brief definition in the question stem.
- **Why it fails:** It shifts the task toward reading text/instructions rather than interpreting the visualization itself, and introduces uneven help across items. [@leeVLATDevelopmentVisualization2017]

## How to Check <!-- role: check -->

- **Visual Sign:** Participants fail because they “don’t know the term,” not because they misread the graphic.
- **The Test:** For each item, ask: “Could a user answer correctly by reading the visualization alone, without knowing specialized statistical terminology?” [@leeVLATDevelopmentVisualization2017]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace specialized chart types with more broadly learned ones (as VLAT replaced Box Plot).
- **Best Fix:** Re-scope the construct (e.g., “advanced visualization literacy”) and then redesign the blueprint and prerequisites accordingly. [@leeVLATDevelopmentVisualization2017]
