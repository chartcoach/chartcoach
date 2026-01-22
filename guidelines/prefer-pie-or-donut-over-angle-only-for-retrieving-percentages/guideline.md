---
id: prefer-pie-or-donut-over-angle-only-for-retrieving-percentages
title: Prefer a pie or donut chart over an angle-only diagram for retrieving a percentage
  value
bibliography: references.bib
description: For reading a single part-to-whole percentage, full pie/donut charts
  are more accurate than angle-only variants.
labels:
- chart:pie
- chart:donut
- task:retrieve-value
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- comparison:within-chart-type
---

## Use full pie/donut wedges instead of angle-only depictions for percent readout <!-- role: advice -->

Use a standard pie chart or donut chart (filled wedge) rather than an angle-only drawing when you need readers to report the percentage shown.

## Angle-only depictions increase error for percentage readout <!-- role: reason -->

Angle-only depictions remove other cues (segment area and arc length) that viewers can use to estimate proportions, which increases variability and error in percent judgments.

**Mechanism:** With only angle information, the viewer has fewer redundant perceptual cues to triangulate the percentage, so estimates become less stable.

**Evidence:** In a percentage readout task, the baseline pie and baseline donut were more accurate than both angle-only variants (angle-only pie and angle-only donut), with significant differences reported between each baseline and each angle-only chart. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

**Notes:** This guideline concerns accuracy for retrieving a single percentage value, not preference or speed.

## Where this applies: reading a single part-to-whole percentage from a radial graphic <!-- role: context -->

- **User Goal:** Read off a percentage value (part-to-whole) from a visual.
- **Task:** Retrieve value.
- **Data:** One quantitative proportion shown as a single highlighted segment against the remainder.
- **Chart Setting:** Static display (e.g., report, slide, dashboard tile) where the viewer enters or states the percent.
- **Audience:** General audiences with mixed visualization familiarity.
- **Success Criterion:** Lower estimation error (higher accuracy).

## When not to follow it <!-- role: exceptions -->

**Break it when:** The design must intentionally show only an angle cue (e.g., as a teaching or demonstration artifact), and estimation accuracy is not a success criterion. **Why:** This guideline optimizes for accuracy in value retrieval, which is not the goal in that scenario.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up a minimalist aesthetic that angle-only depictions can provide. **Risk:** Using fuller wedges can increase visual weight and reduce space for adjacent annotations. **Mitigation:** Keep the design simple (few segments) and rely on clear highlighting of the target segment.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Replacing a pie/donut wedge with only two rays (or an implied angle) and expecting equal readout accuracy. **Why it fails:** Angle-only variants showed higher error than baseline pie/donut designs for retrieving the percentage. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers frequently confuse the intended portion or give widely varying estimates for the same value. **Quick Check:** Show the graphic to a few colleagues and ask them to report the percent; if responses spread noticeably, treat the design as failing. **Stronger Test:** Run a small internal study measuring absolute error across the intended range of percentages.

## What to do instead <!-- role: fix -->

- Use a baseline pie chart or baseline donut chart with a filled wedge for the highlighted portion.
- If you must keep a radial aesthetic, ensure the highlighted segment still has a filled area (not just rays) so multiple cues remain available.
- Reduce ambiguity by keeping the display to two segments (highlighted part and remainder) when the goal is a single percent readout.
