---
id: use-bar-position-over-length-for-four-value-recall
title: Use bar-position instead of length when viewers must recall four quantitative
  values
bibliography: references.bib
description: For immediate recall of four values, a bar-position encoding showed less
  bias than a length encoding.
labels:
- chart:bar
- task:retrieve
- visual:position
- visual:length
- impact:bias
- data:quantitative
- audience:general
- complexity:advanced
---

## Prefer bar-position over length to reduce bias for 4-value recall <!-- role: advice -->

When viewers must reproduce four quantitative values immediately after a brief view, prefer a bar chart position encoding over a length encoding to reduce systematic bias.

## Why bar-position can reduce bias vs length in 4-value recall <!-- role: reason -->

In immediate reproduction from memory, encodings can differ more in systematic error (bias) than in raw channel “precision” rankings, and the same viewer can show different bias patterns across encodings.

**Mechanism:** A bar-position encoding can produce reproduced values that deviate less systematically from the true values than a length encoding under brief exposure and redraw.

**Evidence:** For the retrieve-value reproduction task with 4 marks, bar-position (E-7) had significantly less bias than length (E-11) under the Bayesian significance threshold (pair E-7 better than E-11 appears in the bias significance pairs) [@mccolemanRethinkingRanksVisual2022; @zengReviewCollationGraphical2023].

**Notes:** This guideline targets bias (systematic over/underestimation), not necessarily overall accuracy/error.

## When this bias-focused rule applies <!-- role: context -->

- **User Goal:** Recall and reproduce multiple values without systematic over/underestimation.
- **Task:** Retrieve Value (immediate reproduction from memory).
- **Data:** Quantitative values with 4 marks.
- **Chart Setting:** Brief exposure and then redraw/reproduction (glance-like).
- **Audience:** General audiences.
- **Success Criterion:** Lower bias in reproduced values.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The design cannot support a position baseline (space constraints or required layout prevents bars). **Why:** The recommendation requires bar-position as the primary quantitative channel.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Bars can take more vertical space than some alternatives and may constrain dense layouts. **Risk:** Optimizing for bias may not optimize for overall accuracy/error in every setting. **Mitigation:** Decide whether your priority is bias reduction or absolute error before choosing the encoding.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using this result to justify replacing all length encodings with bar charts for any task. **Why it fails:** The evidence is specific to immediate reproduction of four values, not general reading or comparison tasks.

## Quick checks <!-- role: check -->

**Failure Sign:** Users consistently overshoot or undershoot recalled values (systematic bias) more in one encoding than another. **Quick Check:** Ask users to reproduce four values after a short glance and compare mean signed error between encodings. **Stronger Test:** Run a small controlled A/B test and estimate bias with a Bayesian or bootstrap approach similar to your evaluation plan.

## What to do instead <!-- role: fix -->

- Switch from a length encoding to a bar-position encoding for the quantitative values.
- Reduce the number of marks shown if the task is recall-heavy and bias is high.
- Add redundancy only through task workflow (e.g., allow re-checking) if immediate recall is not essential.
- If bars are infeasible, validate alternatives with the same reproduction-style test on your target display and data range.
