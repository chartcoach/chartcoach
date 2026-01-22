---
id: predict-importance-from-bitmap-with-fcn-for-graphic-designs-and-visualizations
title: Predict per-pixel importance directly from the bitmap using a fully convolutional
  network (FCN)
bibliography: references.bib
description: Use an FCN on the rendered image (not source vectors/DOM) to estimate
  a per-pixel importance map for designs and visualizations.
labels:
- chart:hybrid
- task:prioritize
- visual:attention
- impact:automation
- data:mixed
- audience:designer
- model:neural-network
---

## Predict per-pixel importance from the rendered bitmap using an FCN <!-- role: advice -->

Predict an importance heatmap directly from the rendered bitmap of a graphic design or data visualization using a fully convolutional network (FCN), without requiring the original vector/structural representation.

## Why bitmap-to-importance FCNs work for design content <!-- role: reason -->

An FCN can learn visual and semantic regularities in designs (for example, how titles, captions, legends, and prominent elements tend to appear) and output a dense map aligned to pixels, making it usable as a general-purpose signal for downstream layout operations.

**Mechanism:** Learning from human-derived importance signals lets the network associate recurring high-level element patterns (especially text regions) with higher predicted importance, while preserving spatial localization because the model is fully convolutional.

**Evidence:** Two FCN models trained on crowdsourced importance signals produced importance maps that aligned well with ground truth importance for both data visualizations and graphic designs, outperforming or matching natural-image saliency baselines on these domains [@bylinskiiLearningVisualImportance2017]. The bitmap-based models enabled downstream tasks (retargeting, thumbnailing, interactive feedback) with minimal extra processing while remaining fast enough for interactive use [@bylinskiiLearningVisualImportance2017].

**Notes:** Separate models were trained per domain (graphic designs vs data visualizations) to better match domain-specific viewing/importance patterns.

## When bitmap-to-importance prediction is the right tool <!-- role: context -->

- **User Goal:** Automatically identify what content is likely to be perceived as most important in a design or visualization.
- **Task:** Prioritize regions for summarization, cropping, resizing, or design feedback.
- **Data:** Mixed content (text + graphics + marks), often with structured elements but only a rendered image available.
- **Chart Setting:** Bitmap-only pipelines, large libraries of existing images, or interactive tools needing fast recomputation.
- **Audience:** Designers, visualization authors, or systems that need automatic prioritization without manual labeling.
- **Success Criterion:** Importance maps correlate with human importance data and are usable as an input signal for downstream operations.

## When not to rely on bitmap-only importance prediction <!-- role: exceptions -->

**Break it when:** You need guarantees about preserving whole semantic elements (for example, entire labels or icons) rather than pixel-level regions. **Why:** The predicted map is pixel-based and may assign non-uniform importance within an element, which can cause partial cutoffs in downstream edits [@bylinskiiLearningVisualImportance2017].

## Tradeoffs of bitmap-only importance maps <!-- role: costs -->

**Sacrifice:** You give up explicit knowledge of the underlying element structure (layers, DOM, vector objects). **Risk:** The model can inherit dataset biases (for example, overemphasizing text such as titles) and may underweight certain visuals in some cases. **Mitigation:** Treat the map as a prioritization signal and validate with small user checks for high-stakes outputs.

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Assuming a pixel-importance map implies clean element segmentation. **Why it fails:** Importance may vary within a single text block or visual object, which can be problematic for element-preserving edits [@bylinskiiLearningVisualImportance2017].

## Quick tests for whether the importance map is usable <!-- role: check -->

**Failure Sign:** The map consistently highlights irrelevant background regions or misses the title/primary explanatory text. **Quick Check:** Verify that the highest-importance regions cover expected key elements (often titles/captions/legends in visualizations, primary headline/hero in posters). **Stronger Test:** Compare downstream outputs (cropping/thumbnail) against a small preference study on representative samples.

## What to do instead if you need structured preservation <!-- role: fix -->

- Add an element-aware constraint stage that prevents cutting through detected text regions before applying the importance map.
- Use the importance map to rank or choose among element-level candidates rather than directly operating at the pixel level.
- Collect or infer lightweight element structure (for example, bounding boxes) and aggregate pixel importance within each element to drive decisions.
