---
id: avoid-color-encoding-of-primary-quantitative-for-accuracy-in-trivariate-point-charts
title: Avoid encoding the primary quantitative field with color when accuracy is required
bibliography: references.bib
description: In trivariate point plots with one categorical and two quantitative fields,
  encoding the primary quantitative variable using color can be less accurate than
  encoding it on position.
labels:
- chart:scatter
- task:retrieve-value
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Keep the primary quantitative field off color when accuracy matters <!-- role: advice -->

Do not encode the primary quantitative field using color in trivariate point charts if the user must answer value questions accurately.

## Why color is a weaker channel for precise quantitative decoding in this setting <!-- role: reason -->

Color-based encodings can make fine-grained quantitative judgments harder, particularly when the task requires precise selection among nearby values.

**Mechanism:** Quantitative decoding from color requires perceptual mapping from a retinal cue to a numeric scale, which is less directly readable than spatial position for many value judgments.

**Evidence:** Designs where the primary quantitative field is encoded with color-saturation (and the categorical field is placed on a positional axis) rank in the worst-performing groups for accuracy on retrieve-value and sort tasks compared to designs that encode the primary quantitative field on x or y [@kimAssessingEffectsTask2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline targets accuracy for value tasks; other tasks may have different tradeoffs.

## When you should apply this <!-- role: context -->

- **User Goal:** Correctly read or compare specific numeric values of the primary quantitative field.
- **Task:** retrieve-value, sort.
- **Data:** One categorical field plus two quantitative fields in a point-mark visualization.
- **Chart Setting:** Static chart where the user reads values from marks and legends/scales.
- **Audience:** Any audience where mistakes are costly (reporting, decision review).
- **Success Criterion:** Lower error rate.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart’s purpose is to show broad patterns rather than precise value decoding. **Why:** The evidence is based on accuracy for specific value questions, not pattern detection.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Moving the primary quantitative field off color consumes a positional channel and may force another field onto a different channel. **Risk:** If color is repurposed for a different field, you might create new interference or congestion. **Mitigation:** Recheck the full encoding set for conflicts after reassignment.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a color scale for the primary numeric field while using x/y for other fields because it “looks compact.” **Why it fails:** It tends to increase errors on value reading and value ordering tasks compared to position encodings.

## Quick tests <!-- role: check -->

**Failure Sign:** People misidentify which of two marked values is larger when only color differs. **Quick Check:** Show two annotated points and ask which has higher primary value; if answers are inconsistent, color is too weak for the primary field. **Stronger Test:** Run a short two-alternative forced choice test for retrieve-value with a positional vs color encoding of the primary field.

## What to do instead <!-- role: fix -->

- Map the primary quantitative field to x or y and move the less critical field to color.
- If color must encode categories, use position for the primary quantitative field and encode the secondary quantitative field with color or size based on the dominant task.
- Split into two charts if you cannot support accurate primary-value decoding while showing all fields in one view.
