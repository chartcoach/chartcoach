---
id: use-build-one-icon-at-a-time-only-when-you-must-animate-risk-icon-arrays
title: Use build-one-icon-at-a-time animation only if you must animate risk icon arrays
bibliography: references.bib
description: If animation is unavoidable, prefer a simple build animation that adds
  event icons sequentially in a grouped array, because more complex animations did
  not improve outcomes.
labels:
- chart:icon-array
- task:compare
- visual:motion
- impact:clarity
- data:risk
- audience:general
- animation:build
---

## If you animate, use a simple build in a grouped icon array <!-- role: advice -->

If you must use animation in an icon-array risk comparison, use a simple build animation that adds event icons one at a time within a grouped layout.

## Minimal animation avoids the largest observed harms <!-- role: reason -->

A sequential build in a grouped array can add a motion cue without the instability and distraction created by shuffling or scattered layouts. In the tested comparisons, this was the only animated approach that performed comparably to the static grouped control across outcomes.

**Mechanism:** A build animation can direct attention to the accumulating count while preserving a stable grouped structure that supports magnitude reading and comparison.

**Evidence:** Across eight animated formats, the grouped build condition performed about as well as the static grouped control on choice accuracy, gist knowledge, and evaluation ratings, while most other animations showed significant degradations and none showed significant improvements over static grouped displays [@zikmund-fisherAnimatedGraphicsComparing2012].

**Notes:** The results indicate “no advantage over static,” so the main justification for this animation is constraint-driven (e.g., platform expectations), not performance gain.

## Contexts where this constrained choice applies <!-- role: context -->

- **User Goal:** Compare two risks and choose the option with the lower risk profile.
- **Task:** Side-by-side comparison where motion is present for both options.
- **Data:** Part-to-whole risk proportions.
- **Chart Setting:** Digital environment where animation is required or strongly expected.
- **Audience:** General audiences with mixed numeracy.
- **Success Criterion:** Avoid reducing comprehension and user-rated helpfulness relative to static grouped arrays.

## Exceptions where even build animation is not appropriate <!-- role: exceptions -->

**Break it when:** You can present a static grouped icon array instead. **Why:** The tested build animation did not outperform static grouped displays on any outcome [@zikmund-fisherAnimatedGraphicsComparing2012].

## Costs of using build animation <!-- role: costs -->

**Sacrifice:** Animation adds time and can slow the moment when the final comparable values are visible. **Risk:** Users may attend to motion timing rather than the final magnitudes, especially if both sides animate simultaneously. **Mitigation:** Evaluate whether users can accurately answer comparison questions without replaying or waiting.

## Common mistakes with build animations <!-- role: mistakes -->

**Mistake:** Combining build with scattered placement or additional motion effects in the same display. **Why it fails:** More complex animated scattered variants performed worse than the static grouped control and often worse than simpler alternatives [@zikmund-fisherAnimatedGraphicsComparing2012].

## Quick checks for acceptable build performance <!-- role: check -->

**Failure Sign:** Users wait for animation to finish and then still miss which option is higher, or they rate the graphic as unhelpful. **Quick Check:** Freeze the animation on the final frame and see whether performance matches the static grouped version. **Stronger Test:** Test build-vs-static grouped with the same comprehension and choice questions and require no replays [@zikmund-fisherAnimatedGraphicsComparing2012].

## Fixes if animation is hurting comparison <!-- role: fix -->

- Remove animation entirely and present the final grouped icon arrays as static.
- Ensure the end-state is a grouped icon array that remains visible for comparison.
- Avoid adding any shuffling or repeated re-randomization effects.
- Reduce simultaneous competing motion by presenting comparisons only after animations end.
