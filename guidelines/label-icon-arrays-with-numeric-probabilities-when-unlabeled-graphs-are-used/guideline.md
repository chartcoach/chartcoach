---
id: label-icon-arrays-with-numeric-probabilities-when-unlabeled-graphs-are-used
title: Label icon arrays with numeric probabilities when unlabeled visual estimation
  could mislead
bibliography: references.bib
description: Unlabeled icon arrays can be misinterpreted with high person-to-person
  variability, especially when icons are randomly scattered.
labels:
- chart:icon-array
- task:read-value
- visual:annotation
- impact:clarity
- data:proportion
- audience:general-public
- domain:risk-communication
---

## Add numeric labels when icon-array interpretations must be correct <!-- role: advice -->

Add an explicit numeric percentage (or probability) label to an icon array when viewers’ unaided visual estimates could drive decisions or comparisons. Do not rely on an unlabeled icon array alone for communicating precise proportions.

## Visual estimation shows high variability and arrangement-driven bias <!-- role: reason -->

Even when average estimates are close to the truth, wide variability across individuals and systematic biases from arrangement can cause substantial misinterpretation, meaning viewers may not reliably recover the intended proportion from the picture alone.

**Mechanism:** People round, guess, and differ in perceptual aggregation ability; dispersed arrangements further increase error and variance, so the same image can yield different numeric interpretations.

**Evidence:** Under time pressure with unlabeled graphics, estimates varied widely, and random arrangements produced larger overestimation and variability than sequential ones for most proportions [@anckerEffectArrangementStick2011]. The observed variability was large enough that many viewers confused proportions that differed by 11 percentage points in random-arrangement displays [@anckerEffectArrangementStick2011].

**Notes:** This guideline addresses interpretation of proportion, not downstream “risk perception” in a fully labeled scenario.

## When unlabeled graphics could be taken as exact values <!-- role: context -->

- **User Goal:** Learn or recall a specific risk magnitude.
- **Task:** Read a proportion from an icon array and map it to a number.
- **Data:** Proportions where moderate differences matter or where overestimation would be harmful.
- **Chart Setting:** Patient education, decision aids, consent materials, or any high-stakes communication.
- **Audience:** Broad audiences, including people with lower numeracy.
- **Success Criterion:** Viewers can state the intended probability without large dispersion or systematic bias.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The graphic is explicitly framed as qualitative (for example, “small,” “medium,” “large”) and numeric precision is intentionally not provided. **Why:** A numeric label would contradict the intended qualitative-only message [@anckerEffectArrangementStick2011].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Labels add visual clutter and reduce the “purely visual” nature of the display. **Risk:** Viewers may focus on the number and ignore the distributional meaning of the icons. **Mitigation:** Treat the number as a concise caption that accompanies (not replaces) the visual.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming the audience will infer the correct percent from an unlabeled icon array because the mean estimate is close. **Why it fails:** High between-person variance means many individuals still misread the value [@anckerEffectArrangementStick2011].
- **Mistake:** Using unlabeled random-scatter icon arrays for large proportions and expecting accurate first impressions. **Why it fails:** Random arrangements can inflate perceived size, especially at high proportions [@anckerEffectArrangementStick2011].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users’ guessed percentages cluster on round numbers (often ending in 0 or 5) and spread widely for the same graphic. **Quick Check:** Ask a small sample to provide a percentage after brief viewing and examine the spread and bias. **Stronger Test:** Compare comprehension with and without the numeric label under the expected viewing time [@anckerEffectArrangementStick2011].

## Fix: What to do instead <!-- role: fix -->

- Add a clear numeric percentage adjacent to the icon array.
- If space is limited, include the percentage as a short caption directly under the array.
- Use a sequential (blocked) arrangement to reduce dependence on counting or aggregation before labeling.
- When comparing two risks, label both with numbers so the viewer can verify the visual difference.
