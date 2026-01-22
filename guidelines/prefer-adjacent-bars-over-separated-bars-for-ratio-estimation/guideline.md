---
id: prefer-adjacent-bars-over-separated-bars-for-ratio-estimation
title: Place bars adjacent when viewers must estimate relative heights
bibliography: references.bib
description: Adjacent bars support more accurate percent/ratio judgments than separated
  bars in bar charts.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- layout:spacing
---

## Keep compared bars adjacent for percent-of-height judgments <!-- role: advice -->

Place the bars being compared next to each other when viewers need to estimate one bar’s height as a percentage of another. Avoid layouts that require comparing bars that are far apart on the x-axis.

## Reduced spatial separation lowers comparison error <!-- role: reason -->

Spatial separation makes it harder to visually align and compare bar endpoints, increasing error in ratio judgments.

**Mechanism:** Greater distance between bars increases the perceptual effort to align bar tops and maintain both values in attention, which degrades relative height estimation accuracy.

**Evidence:** Absolute error is higher for separated-bar comparisons than for adjacent-bar comparisons in bar charts, with separation contributing most of the observed “separation effect.” [@talbotFourExperimentsPerception2014; @zengReviewCollationGraphical2023]

**Notes:** The separation penalty is especially pronounced when the reference (taller) bar is short.

## Context: When this applies <!-- role: context -->

- **User Goal:** Estimate how big one category is relative to another.
- **Task:** Percent/ratio estimation between two bars (e.g., “the shorter marked bar as a percent of the taller marked bar”).
- **Data:** Quantitative values split across nominal categories.
- **Chart Setting:** Static bar chart where two specific bars must be compared.
- **Audience:** General audiences performing quick visual judgments.
- **Success Criterion:** Lower absolute estimation error.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Adjacent placement would falsely imply ordering, grouping, or contiguity that is not present in the categories. **Why:** The layout may improve comparison accuracy but introduce a misleading structural cue.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adjacent placement can constrain category ordering and reduce flexibility in grouping or faceting. **Risk:** Forcing adjacency may distort other analytical goals (e.g., preserving a meaningful original category order). **Mitigation:** Make ordering/grouping explicit through labels or separators if adjacency is required.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Spreading categories across multiple separated regions (or panels) while expecting precise cross-bar percent judgments. **Why it fails:** Increased distance directly increases error for relative height estimation.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** People hesitate or give inconsistent answers when asked “about what percent is A of B?” for distant bars. **Quick Check:** Measure the pixel distance between the two compared bars; if they are not near neighbors, expect worse accuracy. **Stronger Test:** Run a small pilot asking percent-of-height questions on adjacent vs. separated layouts and compare absolute error.

## Fix: What to do instead <!-- role: fix -->

- Reorder categories so the bars that must be compared are adjacent.
- Use a design that co-locates the two compared bars within the same local group.
- Split the view into a focused comparison view that shows only the relevant bars for the judgment task.
- Add a dedicated comparison view that repeats the two bars side-by-side for the specific percent question.
