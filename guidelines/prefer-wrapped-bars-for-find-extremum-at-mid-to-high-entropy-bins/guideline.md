---
id: prefer-wrapped-bars-for-find-extremum-at-mid-to-high-entropy-bins
title: Prefer Wrapped Bars for Find-Extremum Across Mid-to-High Entropy Conditions
bibliography: references.bib
description: For find-extremum tasks, wrapped bars rank above standard bars across
  multiple entropy ranges, especially around mid-to-high bins.
labels:
- chart:bar
- task:find-extremum
- visual:length
- impact:accuracy
- data:categorical
- audience:general
- data-characteristic:entropy
- variant:wrapped-bar
- evidence:experiment
- source:zengReviewCollationGraphical2023
---

## The Rule <!-- role: advice -->

For find-extremum tasks on categorical bar charts, prefer wrapped bar charts over standard bar charts across the tested entropy ranges, with strongest observed rank advantages in the mid-to-high entropy conditions (0.76–0.9 and 0.9–1.0).

## The Logic <!-- role: reason -->

Within the extracted results, wrapped variants in specific entropy bins rank above standard variants in the same or comparable settings, implying that wrapping can preserve or improve extremum-finding accuracy even as distributions vary by entropy.

- **The Principle:** Chart-variant selection conditioned on data characteristics (entropy)
- **The Evidence:** In the extracted ranking for find-extremum accuracy (find-extremum-2), wrapped bars at entropy 0.76–0.9 (E-8) and 0.9–1.0 (E-7) rank above the corresponding standard-bar conditions (E-4 and E-3, respectively), and are included in significance pairings where those higher-ranked conditions outperform lower-ranked ones [@karduniBoisWrappedBar2020]. This kind of task- and data-characteristic-conditioned rule is precisely the type of actionable collation targeted for visualization recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify extrema (e.g., smallest category) accurately
- **Data Type:** Categorical (nominal) with quantitative values; you have (or can estimate) an entropy range consistent with the bins used in the study (0.45–0.6, 0.61–0.75, 0.76–0.9, 0.9–1.0)
- **Audience:** General users where accuracy is prioritized

## When to Break It <!-- role: exceptions -->

- **Scenario:** You do not know whether your dataset’s entropy is within the studied bins or your chart design deviates materially from the studied bar variants.
- **Reason:** The extracted guideline is only supported for the entropy-binned conditions represented in the structured record; it should not be generalized beyond those conditions without additional evidence [@karduniBoisWrappedBar2020; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional cognitive decoding of wrapped segments compared to a simple unbroken bar.
- **The Risk:** Users may misinterpret the encoding of large bars if they are unfamiliar with wrapping, even if extremum identification improves.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Applying a wrapped bar chart indiscriminately without considering whether the user’s task is actually find-extremum.
- **Why it fails:** The evidence in the extracted record is tied to find-extremum performance rankings; using it for other tasks is unsupported by this source alone [@karduniBoisWrappedBar2020; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple small bars are hard to distinguish in height while one/few bars dominate the scale.
- **The Test:** Compare extremum-identification accuracy in a quick internal test between standard and wrapped versions; expect the wrapped version to be competitive or better per the reported rankings [@karduniBoisWrappedBar2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If entropy appears mid-to-high (≈0.76–1.0 in the study’s bins) and the task is find-extremum, switch to a wrapped bar chart.
- **Best Fix:** Implement a rule in your recommendation logic: if task=find-extremum and the dataset falls into the studied entropy bins, prioritize wrapped-bar variants above standard-bar variants, reflecting the collated ranking evidence [@zengReviewCollationGraphical2023; @karduniBoisWrappedBar2020].
