---
id: validate-social-influence-separately-from-anchoring-by-delineating-unrelated-signals
title: Validate social influence separately from anchoring by delineating unrelated
  signals
bibliography: references.bib
description: Ensure effects attributed to social proof are not caused by generic numeric
  anchoring from nearby graphics.
labels:
- chart:multiple
- task:evaluate
- visual:layout
- impact:validity
- data:quantitative
- audience:researcher
- custom:experiment-design
---

## Separate or relabel non-social numeric graphics when testing social-proof effects <!-- role: advice -->

When evaluating whether a prior-response distribution affects chart judgments, clearly separate and label any numeric distribution graphics so they cannot be interpreted as relevant social information.

## Why this isolates social proof from generic anchoring <!-- role: reason -->

Numbers and distributions can change estimates via anchoring even if they are not social. By making the distribution clearly unrelated and visually delineated from the judgment task, you can test whether the influence depends on it being perceived as social information.

**Mechanism:** If estimate shifts disappear when the same histogram is presented as unrelated information, the earlier effect is more consistent with social influence than with generic anchoring.

**Evidence:** A validation condition that displayed histograms but labeled them as unrelated to the judgment task and visually delineated the sub-tasks eliminated the increased-error effect seen with biased social histograms, supporting that the earlier result reflected social influence rather than anchoring [@hullmanImpactSocialInformation2011].

**Notes:** This guideline is for study design and product evaluation, not for day-to-day chart presentation.

## When you should apply this in visualization products <!-- role: context -->

- **User Goal:** Assess whether a social feature changes users’ accuracy.
- **Task:** Experimental evaluation of social proof (e.g., “previous answers” widgets).
- **Data:** Quantitative judgment tasks where anchoring is plausible.
- **Chart Setting:** Usability tests, A/B tests, or lab/online experiments for social visualization features.
- **Audience:** Researchers, designers, or analysts evaluating interface effects.
- **Success Criterion:** Internal validity of claims about social influence.

## When not to follow this guideline <!-- role: exceptions -->

**Break it when:** You are not trying to attribute causality (e.g., purely exploratory logging without intervention). **Why:** Delineation and relabeling are unnecessary if causal interpretation is not the goal.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Added design work and potentially less realistic prototypes. **Risk:** Over-separation can reduce ecological validity if real products mix signals. **Mitigation:** Pair the delineated test with a realistic-condition test to triangulate.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Concluding “social proof caused the change” without checking whether any nearby numeric display could have anchored estimates. **Why it fails:** Anchoring can mimic social influence effects.

## Quick ways to validate it worked <!-- role: check -->

**Failure Sign:** The same estimate shift occurs even when the histogram is clearly unrelated to the task. **Quick Check:** Run a condition where the histogram is relabeled as unrelated and separated; compare errors to control. **Stronger Test:** Use multiple unrelated labels and layouts to confirm robustness.

## What to do instead <!-- role: fix -->

- Add a condition where the same histogram is shown but explicitly labeled as unrelated to the chart judgment.
- Visually separate the histogram area from the judgment prompt so it is not read as a cue for the estimate.
- Include comprehension checks to ensure participants interpret the histogram as intended (social vs non-social).
- Compare against a no-histogram control to quantify any remaining anchoring effects.
