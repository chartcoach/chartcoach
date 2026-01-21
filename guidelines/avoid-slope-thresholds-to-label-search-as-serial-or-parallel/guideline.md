---
id: avoid-slope-thresholds-to-label-search-as-serial-or-parallel
title: Avoid Using a Single Slope Threshold to Classify Search as Serial or Parallel
bibliography: references.bib
description: "Do not classify visual-search behavior as serial/parallel using only\
  \ an RT\xD7set-size slope cutoff (e.g., 10 ms/item)."
labels:
- chart:line
- task:classify
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

Do not use a fixed RT×set-size slope cutoff (e.g., ~10 ms/item) to label a search task as “parallel” vs “serial.”

## The Logic <!-- role: reason -->

A threshold implies separable clusters of slopes (e.g., a bimodal distribution), but the large-scale slope distribution is unimodal, including within subsets like feature and spatial-configuration tasks, so a hard boundary is not supported by observed data.

- **The Principle:** Distribution-based classification requires separable modes, not a continuous overlap.
- **The Evidence:** The paper reports a unimodal distribution of slopes across ~2,500 sessions and explicitly warns that slope-only serial/parallel divisions are futile [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Categorizing a search task/mechanism from behavioral performance.
- **Data Type:** RT as a function of set size (slopes for target-present/target-absent).
- **Audience:** Researchers or analysts interpreting visual search experiments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are only using the cutoff as a *rough descriptive label* and not as evidence for mechanism.
- **Reason:** The paper’s critique targets mechanistic inference; descriptive shorthand may be acceptable if clearly labeled as such [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a simple “one-number” categorization.
- **The Risk:** Without a cutoff, interpretation may require more measures (e.g., ratios) and more nuanced reporting.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring “parallel” because mean slope < 10 ms/item.
- **Why it fails:** Overlapping slope distributions mean the same slope magnitude can arise from different task classes [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** Claims like “slopes were under X ms/item; therefore it’s parallel/serial.”
- **The Test:** Ask: “Is this classification justified by a demonstrated separation in slope distributions?” If not, the rule is broken.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the mechanistic label and report slopes descriptively.
- **Best Fix:** Use multiple diagnostics (e.g., slope + slope ratio patterns) rather than a single slope threshold, consistent with the paper’s findings [@wolfeWhatCan11998].
