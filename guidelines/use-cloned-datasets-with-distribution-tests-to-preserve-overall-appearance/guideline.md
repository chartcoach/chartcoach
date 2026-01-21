---
id: use-cloned-datasets-with-distribution-tests-to-preserve-overall-appearance
title: Use Distribution Similarity Tests to Create Visually Similar Clones
bibliography: references.bib
description: "For anonymization-style use, enforce distribution similarity (e.g.,\
  \ K\u2013S tests) so the clone keeps the original\u2019s overall shape."
labels:
- chart:scatter
- task:anonymize
- visual:position
- impact:privacy
- data:bivariate
- audience:expert
- custom:anonymization
---

## The Rule <!-- role: advice -->

If you need altered points but a similar-looking plot, only accept perturbed datasets that pass distribution similarity tests on x and y (e.g., Kolmogorov–Smirnov thresholds).

## The Logic <!-- role: reason -->

- **The Principle:** Matching full distributions (not just means/correlation) preserves overall appearance more reliably.
- **The Evidence:** The paper describes using K–S tests within the acceptance check so the resulting dataset has a similar shape to the original, enabling “cloned” plots for anonymization-like purposes [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Replace individual points while keeping the aggregate visual structure similar (e.g., for sharing).
- **Data Type:** Scatterplots where marginal distributions along x and y are important to preserve visually.
- **Audience:** Practitioners generating shareable variants of sensitive point data.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your goal is to create dramatically different visual forms while holding a few summary stats constant.
- **Reason:** Strong distribution similarity constraints will prevent major appearance changes [@matejkaSameStatsDifferent2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced flexibility; fewer perturbations will be acceptable.
- **The Risk:** Preserving marginals may still allow changes in joint structure; viewers might over-assume equivalence beyond what was tested.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Preserving only regression/correlation and means while ignoring marginal distribution shape.
- **Why it fails:** You can keep the same regression properties yet produce visibly different spreads or shapes; the paper motivates broader checks for similarity [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The clone’s overall cloud looks shifted, stretched, or differently distributed along an axis.
- **The Test:** Run the chosen distribution tests on x and y between original and candidate clone and confirm they meet the stated threshold [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Tighten the acceptance criterion by adding x and y distribution tests to the constraint check.
- **Best Fix:** Combine distribution similarity constraints with the desired preserved summaries (e.g., means/SDs/correlation) so both numeric summaries and overall appearance are maintained [@matejkaSameStatsDifferent2017].
