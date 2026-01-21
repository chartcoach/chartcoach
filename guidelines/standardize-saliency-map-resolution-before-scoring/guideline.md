---
id: standardize-saliency-map-resolution-before-scoring
title: Standardize Saliency Map Resolution Before Scoring
bibliography: references.bib
description: Resize all model saliency maps to the original stimulus resolution using
  a fixed method before computing evaluation metrics.
labels:
- chart:none
- task:preprocess
- visual:position
- impact:fairness
- data:spatial
- audience:expert
- pipeline:resizing
---

## The Rule <!-- role: advice -->

Before scoring, resize every model’s saliency map to the **original stimulus resolution** using a consistent interpolation method.

## The Logic <!-- role: reason -->

Models output maps at different resolutions; scoring them at mismatched scales changes how saliency values align with fixation points and alters metric values, confounding comparisons.

- **The Principle:** Comparable spatial support for point-wise scoring
- **The Evidence:** The paper notes models produced different map resolutions and reports they resized outputs to the original image size using nearest-neighbor interpolation for fair evaluation [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Fair head-to-head comparison of saliency models
- **Data Type:** Saliency maps and fixation coordinates defined in the stimulus pixel space
- **Audience:** Benchmark builders and evaluators

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your evaluation metric is explicitly multi-resolution or scale-invariant and operates in a shared feature space.
- **Reason:** Then pixel-space alignment may not be the scoring basis; otherwise, you still need a common coordinate system [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potential interpolation artifacts or loss of fine structure from low-res maps.
- **The Risk:** Different interpolation choices can subtly advantage certain map types; inconsistency undermines fairness [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Scoring maps “as is” at their native resolution or resizing each model differently.
- **Why it fails:** Fixation coordinates are in the original image space; misalignment changes measured saliency at fixation points [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Fixations appear shifted relative to saliency hotspots when overlaid.
- **The Test:** Overlay fixations on the resized map; confirm peaks and coordinates align in the same pixel grid [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Resize all saliency maps to W×H once, prior to any metric computation.
- **Best Fix:** Publish a benchmark preprocessing spec (exact resizing method) and apply it uniformly across all submissions [@borjiQuantitativeAnalysisHumanModel2013].
