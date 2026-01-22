---
id: run-ctt-item-analysis-to-drop-negative-discrimination-items
title: Run classical test theory item analysis and drop items with negative discrimination
bibliography: references.bib
description: Use item difficulty and discrimination from a tryout sample to identify
  and remove items that work against the test.
labels:
- chart:general
- task:evaluate
- visual:general
- impact:reliability
- data:general
- audience:novice
- method:assessment
---

## Run classical test theory item analysis and drop items with negative discrimination <!-- role: advice -->

After a test tryout, compute item difficulty and item discrimination, and remove items with negative discrimination.

## Why negative discrimination indicates a harmful item <!-- role: reason -->

An item with negative discrimination is answered correctly more often by lower-scoring test takers than higher-scoring ones, suggesting ambiguity, miskeying, or construct mismatch. Removing such items improves the internal coherence of the instrument and supports more meaningful score interpretation.

**Mechanism:** Discrimination aligns item performance with the latent skill the test intends to measure; negative values suggest the item is not measuring the intended ability.

**Evidence:** VLAT used classical test theory indices (difficulty and discrimination) from a tryout sample to evaluate items and removed an item with negative discrimination to improve test quality [@leeVLATDevelopmentVisualization2017].

**Notes:** Retention decisions may also consider reliability impacts, but negative-discrimination items are strong removal candidates.

## When to apply this <!-- role: context -->

- **User Goal:** Improve item quality before finalizing an assessment.
- **Task:** Identify items that do not differentiate higher vs lower performers appropriately.
- **Data:** Tryout response data from a sample similar to the target population.
- **Chart Setting:** Fixed-form test with multiple-choice/true-false items.
- **Audience:** Non-expert test takers; sufficient sample size for stable estimates.
- **Success Criterion:** Item set has mostly positive, meaningful discrimination.

## When not to immediately drop a low-discrimination item <!-- role: exceptions -->

**Break it when:** The item is intentionally easy as a warm-up or to cover an essential blueprint cell and discrimination is low but positive. **Why:** Some easy coverage items may still be desirable for content validity, even if they discriminate weakly.

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Dropping items can reduce coverage of certain visualization types/tasks. **Risk:** Over-optimizing discrimination can bias the test toward harder items and reduce breadth. **Mitigation:** Balance statistical indices with blueprint coverage needs.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Keeping a negative-discrimination item because it “covers an important chart.” **Why it fails:** It can distort total scores and reduce coherence of the measured construct.

## Quick checks <!-- role: check -->

**Failure Sign:** High scorers miss an item that low scorers often get right. **Quick Check:** Compute discrimination for each item and flag any item with D < 0. **Stronger Test:** Review flagged items for ambiguity, miskeying, or mismatch between stem and encoding, then re-tryout revised items.

## What to do with problematic items <!-- role: fix -->

- Recheck the keyed correct answer against the displayed visualization and task.
- Rewrite the stem to remove ambiguity and ensure it targets one task.
- Change response options to reduce distractors that are correct under alternate interpretations.
- Replace the item with a new one targeting the same blueprint cell.
