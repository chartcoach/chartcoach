---
id: use-pairwise-likert-when-triplets-are-too-expensive
title: Use Pairwise Likert Ratings When Triplets Are Too Expensive
bibliography: references.bib
description: If you cannot afford exhaustive triplets, collect pairwise Likert similarity
  ratings to build perceptual kernels with comparable agreement.
labels:
- chart:any
- task:evaluate
- visual:color
- visual:shape
- visual:size
- impact:efficiency
- data:categorical
- audience:designer
- method:crowdsourcing
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

When time or budget is constrained, estimate perceptual kernels using **pairwise Likert similarity ratings** rather than triplets.

## The Logic <!-- role: reason -->

Pairwise Likert ratings require fewer total judgments than exhaustive triplets and, in the paper’s comparisons, produced kernels with **similar average agreement** to triplet matching across palettes—at lower overall experiment duration and cost [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Direct pairwise scaling is a practical compromise when ordinal triplets are too costly.
- **The Evidence:** The authors report comparable average rank correlations among L5/L9 and Tm kernels, while pairwise ratings are cheaper overall due to fewer judgments [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly obtain a usable perceptual kernel for a palette to support design tooling.
- **Data Type:** Palettes of moderate size where exhaustive triplets would be too slow/costly.
- **Audience:** Tool teams or researchers running crowd studies under budget limits.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need maximal robustness and lowest variance across participants.
- **Reason:** Triplet matching had lower cross-subject variance and higher robustness in sensitivity analyses [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Lower per-judgment simplicity; participants must map perception onto a discrete rating scale.
- **The Risk:** Ratings can be limited by the number of Likert levels and by between-subject internal scale differences (the paper flags this as a known issue, even though effects were not clearly visible in their results) [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a Likert scale without helping participants distribute ratings across the scale.
- **Why it fails:** Participants may compress responses, increasing noise and reducing effective resolution; the paper mitigates this by showing a matrix of completed ratings for review/adjustment [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** Many pairs receive the same rating despite clear perceptual differences.
- **The Test:** Inspect the histogram of ratings for heavy pile-ups at a single value; if present, participants likely underused the scale (the paper’s interface design aims to prevent this) [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide participants an overview of stimuli and allow revisiting prior ratings.
- **Best Fix:** If feasible, switch to triplet matching for lower variance and better robustness [@demiralpLearningPerceptualKernels2014a].
