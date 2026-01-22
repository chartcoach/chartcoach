---
id: add-data-redundancy-by-labeling-values-to-improve-recall
title: Add data redundancy by labeling quantitative values when precise recall matters
bibliography: references.bib
description: Presenting values in more than one encoding is associated with higher-quality
  recall descriptions.
labels:
- chart:general
- task:read-value
- visual:text
- impact:comprehension
- data:quantitative
- audience:general
- strategy:redundancy
---

## Repeat key numbers in text when exact values are important <!-- role: advice -->

When viewers need to remember or report specific quantities, redundantly encode key values using text labels or additional quantitative encodings alongside the main marks.

## Why data redundancy improves recall <!-- role: reason -->

Redundant quantitative cues make exact values easier to retrieve and describe later, increasing the likelihood that viewers encode numeric details rather than only qualitative impressions.

**Mechanism:** Providing the same quantitative information through multiple channels reduces decoding demands and supports later reconstruction of the details.

**Evidence:** Visualizations with data redundancy had higher average recall-description quality than those without, and data redundancy appeared substantially more often among the best-described visualizations than among the worst-described ones [@borkinMemorabilityVisualizationRecognition2016].

**Notes:** Data redundancy can co-exist with message redundancy; both were linked to better recall quality.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Remember exact values or compare quantities precisely.
- **Task:** Read values; recall specific numeric facts later.
- **Data:** Quantitative values where particular numbers matter (not just direction).
- **Chart Setting:** Explanatory charts in reports/briefings where numbers may be quoted.
- **Audience:** Mixed audiences, including those who may not infer values accurately from axes.
- **Success Criterion:** Recall descriptions include correct numeric details or close paraphrases.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization contains too many marks for readable labels. **Why:** Dense labeling can overwhelm the display and reduce overall legibility.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Clean layout and available space near marks. **Risk:** Too many numbers can increase clutter and reduce attention to the broader pattern. **Mitigation:** Redundantly label only the most decision-relevant values.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Labeling every value in a dense chart. **Why it fails:** The added text competes with the data encoding and makes scanning harder.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers describe trends but omit or misremember key quantities. **Quick Check:** Ask for the top two numbers someone remembers after a brief view. **Stronger Test:** Compare recall-description quality and accuracy for a labeled vs. unlabeled version.

## What to do instead <!-- role: fix -->

- Label only key marks (extremes, endpoints, totals) rather than every mark.
- Provide a small callout with the most important numbers if direct labels would clutter.
- Simplify the chart (aggregate or reduce categories) to make selective labeling feasible.
- Use message redundancy (explicit takeaway text) if the pattern matters more than the numbers.
