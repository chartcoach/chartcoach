---
id: verify-color-choices-with-simulators-but-dont-trust-them-alone
title: Test Colors with Simulators, Then Add a Second Encoding
bibliography: references.bib
description: Use colorblind simulators to spot risky color pairs, but ensure understanding
  without color by adding another visual variable.
labels:
- chart:multi
- task:validate
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a colorblind simulator to test your visualization, but do not rely on simulation alone—add a second visual encoding (e.g., shape, pattern, line dash) whenever color could be ambiguous.

## The Logic <!-- role: reason -->

Simulators provide an approximate preview, but individual color perception varies; redundancy via a second channel makes the decoding robust even when colors converge under a given deficiency [@muth_colorblindness_2020].

- **The Principle:** Don’t depend on a single fragile channel; use redundant encodings
- **The Evidence:** The article lists multiple simulator tools, then cautions they “aren’t 100% correct” and quotes that the “only bulletproof solution is to encode your data with a second visual variable” like position/shape/patterns [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensure categories/series remain distinguishable for colorblind readers
- **Data Type:** Any chart where color carries meaning (especially thin lines, small marks, legends)
- **Audience:** Public-facing or high-stakes contexts where misreading is costly [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Single-series charts where color is purely decorative and no distinction is required
- **Reason:** No categorical decoding depends on color, so redundancy isn’t necessary [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional design complexity (more styling decisions, more visual elements)
- **The Risk:** Over-encoding can clutter the chart if applied indiscriminately [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Passing a single simulator view and declaring the chart “accessible”
- **Why it fails:** Simulators are approximations and can miss real-world confusion; redundancy is still needed when colors are close [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories become hard to separate in at least one simulated deficiency mode
- **The Test:** Run multiple deficiency simulations and confirm each category is still identifiable without relying only on hue [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase lightness contrast between confusing colors and add direct labels where feasible
- **Best Fix:** Add a second encoding suited to the mark type (shapes for points, dashes/widths for lines, patterns for areas) and re-test [@muth_colorblindness_2020].
