---
id: use-mid-bar-markers-to-improve-bar-height-comparison-accuracy
title: Mark bars at mid-height (not only at the baseline) when eliciting percent-of-height
  estimates
bibliography: references.bib
description: Mid-bar markers can slightly reduce error in percent-of-height judgments
  compared to baseline-only markers.
labels:
- chart:bar
- task:compare
- visual:annotation
- impact:accuracy
- data:quantitative
- audience:general
- annotation:marker
---

## Place the comparison marker in the middle of the bar for percent judgments <!-- role: advice -->

When you mark bars for a percent-of-height estimation task, place the marker in the middle of the bar rather than only at the bottom. Use a consistent marker placement across conditions if you are comparing designs.

## Mid-bar markers provide an internal reference point <!-- role: reason -->

A mid-bar marker provides an additional visual anchor that can make ratio estimation slightly easier, and inconsistent marker placement can confound comparisons between chart designs.

**Mechanism:** A marker at mid-height supplies a salient internal reference that supports estimation and reduces reliance on baseline-only decoding.

**Evidence:** In percent-of-height estimation tasks, placing the marking dot in the middle of the bar reduced absolute error relative to placing it at the bottom (post hoc estimate reported with confidence interval). [@talbotFourExperimentsPerception2014; @zengReviewCollationGraphical2023]

**Notes:** The marker-position effect was smaller than alignment/separation effects but large enough to affect comparisons between chart variants if marker placement differs.

## Context: When this applies <!-- role: context -->

- **User Goal:** Estimate one marked bar’s height as a percent of another marked bar.
- **Task:** Ratio estimation with marked target bars.
- **Data:** Quantitative values encoded by bar height.
- **Chart Setting:** Bar charts where marks/dots are used to indicate which bars to compare.
- **Audience:** General audiences performing visual estimation.
- **Success Criterion:** Reduced absolute estimation error and fair comparison across chart designs.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** Adding markers would clutter the display or compete with other necessary annotations. **Why:** The marker can add visual noise that undermines readability in dense layouts.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional annotation introduces visual elements that must be managed consistently. **Risk:** Inconsistent marker placement across charts can change task difficulty and mislead design comparisons. **Mitigation:** Standardize marker placement rules across all compared charts.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Comparing bar-chart variants while changing how target bars are marked (e.g., bottom dots in one condition, mid-bar dots in another). **Why it fails:** Marker placement changes task difficulty, confounding the comparison.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users interpret the marker as indicating a different quantity (e.g., the middle of the bar rather than the bar’s total height). **Quick Check:** Ask a colleague what the marker means after a 5-second glance. **Stronger Test:** Run a small study with the same tasks using bottom vs. mid-bar markers and compare absolute error.

## Fix: What to do instead <!-- role: fix -->

- Standardize marker placement across all bar-chart variants used for the same task.
- Remove markers and instead isolate the bars to be compared using layout (e.g., showing only the two bars).
- Use a single consistent visual emphasis method for targets across conditions.
- Provide explicit textual labels for the compared values when precision is required.
