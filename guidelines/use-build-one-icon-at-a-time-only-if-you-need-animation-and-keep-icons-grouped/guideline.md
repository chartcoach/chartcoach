---
id: use-build-one-icon-at-a-time-only-if-you-need-animation-and-keep-icons-grouped
title: If You Animate, Build Grouped Risk Icons One at a Time
bibliography: references.bib
description: Among tested animations, sequentially building grouped risk icons performed
  closest to static grouped arrays and avoids the largest degradations.
labels:
- chart:icon-array
- task:compare
- visual:motion
- impact:comprehension
- data:probabilistic
- audience:general-public
- animation:build
- domain:health-risk
- source:zikmund-fisher-2012
---

## The Rule <!-- role: advice -->

If you must use animation in a two-risk icon-array comparison, animate only a simple build (icons appear sequentially) and keep the risk icons grouped throughout.

## The Logic <!-- role: reason -->

A build animation can add a clear cue about which risk reaches its final count sooner while preserving an easy-to-parse grouped block; more complex scattered/shuffle motions often distract and reduce accuracy.

- **The Principle:** Add a single, interpretable motion cue without destabilizing spatial structure
- **The Evidence:** The grouped build condition performed as well as the static grouped control on outcomes, while most other animated variants (especially scattered/shuffling) degraded knowledge and/or ratings; no animation beat static grouped overall [@zikmund-fisherAnimatedGraphicsComparing2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Notice a small difference between two risks while still understanding the final magnitude
- **Data Type:** Side-by-side icon arrays with slightly different event counts
- **Audience:** General audiences; especially when you believe motion may help highlight the difference

## When to Break It <!-- role: exceptions -->

- **Scenario:** The comparison is already easy with static grouped arrays and animation is optional
- **Reason:** The study found no significant improvements from animation over static grouped displays, so adding motion is unnecessary for performance [@zikmund-fisherAnimatedGraphicsComparing2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Longer time to reach the final, fully readable state
- **The Risk:** Users may proceed before fully encoding the final counts, or motion may still distract in side-by-side presentation [@zikmund-fisherAnimatedGraphicsComparing2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Combining build with scattering and/or shuffling to “show both randomness and magnitude”
- **Why it fails:** Added motion/complexity tended to lower knowledge accuracy and user ratings compared with static grouped arrays [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple simultaneous motion behaviors (build + shuffle + settle) across two side-by-side arrays.
- **The Test:** Compare performance against a static grouped prototype; if animation does not improve accuracy or ratings, remove it [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove shuffle/scatter motions and keep only a grouped build, then pause on the final grouped state.
- **Best Fix:** Replace the animation with static grouped icon arrays if your goal is accurate two-risk comparison [@zikmund-fisherAnimatedGraphicsComparing2012].
