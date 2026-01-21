---
id: design-icon-arrays-for-low-numeracy-users-by-reducing-aggregation-burden
title: Reduce Visual Aggregation Burden in Icon Arrays for Low-Numeracy Audiences
bibliography: references.bib
description: Use layouts that minimize mental summation (e.g., sequential blocks)
  because lower numeracy is associated with less accurate proportion estimates.
labels:
- chart:icon-array
- task:estimate
- visual:position
- impact:accessibility
- data:proportion
- audience:low-numeracy
- domain:risk-communication
---

## The Rule <!-- role: advice -->

For low-numeracy audiences, avoid icon-array designs that require mentally adding scattered icons; use arrangements that can be read as a single contiguous part of the whole.

## The Logic <!-- role: reason -->

In the study, numeracy was associated with accuracy: higher numeracy correlated with lower inaccuracy for several tested proportions (notably 6% random and 29% random/sequential), and in the mixed model, each additional point on an 8-item numeracy scale reduced relative inaccuracy while random arrangement increased it [@anckerEffectArrangementStick2011]. Designs that require more cognitive aggregation disproportionately penalize lower-numeracy viewers.

## Where to Apply <!-- role: context -->

- **User Goal:** Extract a proportion from a pictorial display without counting.
- **Data Type:** Binary outcomes (affected vs unaffected) communicated via colored stick figures.
- **Audience:** Mixed literacy/numeracy populations, including patients in clinic settings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You will not ask users to translate the graphic into a numeric percentage (no numeric response/decision depends on it).
- **Reason:** The paper’s outcome was numeric estimation accuracy; if no numeric interpretation is required, this specific limitation may be less consequential [@anckerEffectArrangementStick2011].

## The Price <!-- role: costs -->

- **The Sacrifice:** More structured layouts can reduce the “natural randomness” impression some people prefer.
- **The Risk:** Even with sequential layouts, individual estimates can still vary widely; do not assume perfect comprehension [@anckerEffectArrangementStick2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating icon arrays as automatically “good for low numeracy” regardless of layout.
- **Why it fails:** Layout matters; random arrangements increased relative inaccuracy by about 10% in the mixed model and showed higher variability [@anckerEffectArrangementStick2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Wider spread of estimates among lower-numeracy users, especially with scattered icons.
- **The Test:** Segment quick-estimate results by numeracy (or education as a proxy) and compare error/variance between layouts; if low-numeracy users diverge more with random layouts, redesign [@anckerEffectArrangementStick2011].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from random scatter to sequential blocks.
- **Best Fix:** Pilot-test with lower-numeracy participants using brief exposures and verify reduced error/variance before deployment [@anckerEffectArrangementStick2011].
