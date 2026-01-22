---
id: use-target-crowding-inner-crowding-and-deformation-to-anticipate-dot-tracking-difficulty
title: Estimate dot-transition tracking difficulty using target crowding, inner crowding,
  and deformation
bibliography: references.bib
description: Three measurable properties of dot animations predict how hard it will
  be for viewers to track multiple targets and their identities.
labels:
- chart:scatter
- task:track
- visual:motion
- impact:predictability
- data:multivariate
- audience:expert
- animation:evaluation
---

## Quantify tracking difficulty with crowding, inner crowding, and deformation metrics <!-- role: advice -->

Before choosing an animation pacing technique for dot transitions, compute target crowding, inner crowding, and deformation to anticipate tracking difficulty. Use these metrics to compare candidate transition designs under the same duration and pacing.

## Why these three metrics predict tracking performance <!-- role: reason -->

Tracking errors rise when targets get too close to other dots (crowding), when distractors intrude within the region spanned by targets (inner crowding), and when the relative geometry among targets changes rapidly (deformation), especially when identities must be preserved.

**Mechanism:** Close proximity increases confusability between targets and distractors, distractors inside the targets’ spatial envelope interfere with maintaining a stable multi-target representation, and strong changes in inter-target distances make it harder to maintain correspondence (particularly for identity binding).

**Evidence:** In controlled experiments with 30-dot transitions and three targets, higher target crowding and higher inner crowding reduced tracking accuracy for group tracking, and deformation had a measurable detrimental effect; for identity tracking, all three metrics showed clear effects on performance, and deformation particularly increased misidentifications [@chevalierNotsoStaggeringEffectStaggered2014].

**Notes:** Inner crowding harmed end-position tracking but showed a nuanced relationship with identity swaps among trials where targets were successfully selected.

## When to apply these difficulty metrics <!-- role: context -->

- **User Goal:** Maintain correspondence through an animated transition.
- **Task:** Multi-object tracking of points, with or without identity binding.
- **Data:** Point-based marks where many distractors move alongside targets.
- **Chart Setting:** Animated transitions between two states (e.g., scatterplot remapping) where linear interpolation is a reasonable baseline.
- **Audience:** Designers and developers tuning animation techniques; researchers evaluating transitions.
- **Success Criterion:** Predict and reduce tracking errors and misidentifications.

## When these metrics are not sufficient <!-- role: exceptions -->

**Break it when:** The visualization provides stable identity cues throughout the transition (e.g., persistent unique visual encodings) that remove the need for location-based tracking. **Why:** The task is no longer dominated by the perceptual tracking limits these metrics capture.

## Tradeoffs of metric-based evaluation <!-- role: costs -->

**Sacrifice:** Computing and optimizing metrics can constrain animation freedom and add implementation complexity. **Risk:** Optimizing one metric can worsen another (e.g., lowering crowding while increasing deformation). **Mitigation:** Evaluate all three metrics together rather than optimizing only one.

## Common mistakes in using these metrics <!-- role: mistakes -->

- **Mistake:** Optimizing only target crowding and ignoring deformation. **Why it fails:** Some pacing choices can reduce crowding but increase deformation, which can hurt identity tracking [@chevalierNotsoStaggeringEffectStaggered2014].
- **Mistake:** Treating “difficulty” as a single scalar without separating group tracking from identity tracking. **Why it fails:** The metrics can affect NoID (group) and ID (identity) tasks differently, especially for deformation and inner crowding [@chevalierNotsoStaggeringEffectStaggered2014].

## Quick checks to validate metric usefulness in your case <!-- role: check -->

**Failure Sign:** Users frequently swap targets in dense moments or lose correspondence when target geometry changes. **Quick Check:** Compute target crowding/inner crowding/deformation on a linear-interpolation baseline and see whether the worst transitions align with observed user failures. **Stronger Test:** Run a small tracking study using both accuracy and continuous error measures to confirm metric–performance alignment for your dataset [@chevalierNotsoStaggeringEffectStaggered2014].

## What to do if metrics predict high difficulty <!-- role: fix -->

- Reduce target crowding by redesigning the transition to limit close approaches between targets and distractors during motion.
- Reduce deformation by keeping relative distances among tracked targets more stable during the transition when identity binding matters.
- Compare alternative transition designs by jointly inspecting all three metrics rather than relying on perceived smoothness.
