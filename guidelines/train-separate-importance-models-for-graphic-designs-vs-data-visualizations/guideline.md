---
id: train-separate-importance-models-for-graphic-designs-vs-data-visualizations
title: Train separate importance predictors for graphic designs and for data visualizations
bibliography: references.bib
description: Use domain-specific training signals and architectures because importance
  patterns differ between posters and data visualizations.
labels:
- chart:hybrid
- task:model
- visual:attention
- impact:accuracy
- data:mixed
- audience:researcher
- model:domain-specific
---

## Train separate importance models per domain (designs vs visualizations) <!-- role: advice -->

Train separate importance prediction models for graphic designs and for data visualizations using domain-matched ground truth, rather than assuming one model will generalize across both.

## Why domain-specific training improves importance prediction <!-- role: reason -->

Graphic designs and data visualizations contain different recurring structures and reading behaviors, and the available supervision types differ (element-like importance masks vs click/fixation proxies), so optimizing each model to its domain better captures what people treat as important there.

**Mechanism:** Domain-matched supervision encourages the model to learn the domain’s typical high-importance elements (for example, titles/captions/legends in visualizations; headline/hero and key text in posters) and their spatial distributions.

**Evidence:** The work trained separate FCN models—one on Graphic Design Importance (GDI) annotations for designs and another on BubbleView clicks for visualizations—and each achieved good agreement with its respective ground truth, enabling downstream applications in that domain [@bylinskiiLearningVisualImportance2017].

**Notes:** Training on GDI annotations (rather than clicks) was found more suitable for design applications because GDI better aligned to element boundaries.

## When to split models by domain <!-- role: context -->

- **User Goal:** Achieve reliable importance predictions for a specific content class.
- **Task:** Importance estimation used for retargeting, thumbnailing, or interactive feedback.
- **Data:** Either poster-like layouts with mixed imagery/text, or chart/infographic visualizations with structured explanatory text.
- **Chart Setting:** You can curate domain-specific datasets and expect domain-specific biases (for example, strong title focus in visualizations).
- **Audience:** Developers training and deploying importance predictors in tools or pipelines.
- **Success Criterion:** Higher agreement with the domain’s ground truth and better downstream behavior (cropping/thumbnailing).

## When a single shared model may be acceptable <!-- role: exceptions -->

**Break it when:** You have too little data to train two models and only need coarse importance localization. **Why:** A single model may still provide a weak but usable signal for low-stakes summarization, though domain-specific performance may degrade [@bylinskiiLearningVisualImportance2017].

## Tradeoffs of separate models <!-- role: costs -->

**Sacrifice:** More maintenance, separate datasets, and separate evaluation. **Risk:** Model selection becomes a deployment concern when content is ambiguous (design-like infographic vs chart). **Mitigation:** Use content-type routing or test both and choose the more plausible output.

## Common mistakes when splitting domains <!-- role: mistakes -->

**Mistake:** Training on a supervision type that mismatches the downstream use (for example, clicks when you need element-uniform importance). **Why it fails:** Non-uniform within-element importance can create artifacts for layout-oriented applications [@bylinskiiLearningVisualImportance2017].

## Quick tests for whether the split is necessary <!-- role: check -->

**Failure Sign:** A model trained on one domain consistently overpredicts/underpredicts key elements in the other (for example, overemphasizing map regions or missing unusual text styles). **Quick Check:** Evaluate on a small labeled set from the target domain before committing. **Stronger Test:** Compare downstream task performance (retargeting/thumbnail search) using domain-matched vs mismatched training.

## What to do instead if you cannot maintain two models <!-- role: fix -->

- Train a single model but evaluate separately on each domain and document domain-specific failure patterns.
- Fine-tune a shared backbone with small domain-specific heads using the respective ground truths.
- Use the domain’s supervision type that best matches the intended application output (element-aligned masks for layout edits; click-like maps for attention approximation).
