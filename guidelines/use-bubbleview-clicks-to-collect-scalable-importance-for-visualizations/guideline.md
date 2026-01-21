---
id: use-bubbleview-clicks-to-collect-scalable-importance-for-visualizations
title: Use BubbleView Clicks to Collect Scalable Importance for Visualizations
bibliography: references.bib
description: Collect crowdsourced BubbleView clicks as a practical proxy for attention/importance
  on data visualizations.
labels:
- chart:multiple
- task:collect
- visual:attention
- impact:scalability
- data:mixed
- audience:researcher
- method:crowdsourcing
---

## The Rule <!-- role: advice -->

When you need large-scale importance data for data visualizations, collect BubbleView click maps instead of eye tracking.

## The Logic <!-- role: reason -->

BubbleView’s blurred-image + click-to-reveal interaction produces click patterns correlated with where people look, enabling large datasets at lower cost and without lab equipment.

- **The Principle:** Crowdsourced interaction as an attention proxy
- **The Evidence:** The paper collects BubbleView clicks for 1,411 MASSVIS visualizations and confirms BubbleView data is representative of eye fixation patterns; their model trained on clicks also predicts eye fixations reasonably well [@bylinskiiLearningVisualImportance2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Build training data for an importance/attention predictor for charts/infographics
- **Data Type:** Diverse visualization images (news, government reports, common chart types)
- **Audience:** Researchers and practitioners who cannot run lab eye-tracking studies

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your application requires true free-viewing fixation dynamics (timing/scanpaths) rather than aggregated spatial importance
- **Reason:** BubbleView yields click-based exploration maps that differ from fixations in distribution and interaction intent [@bylinskiiLearningVisualImportance2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Click maps can differ from fixation maps (e.g., clicks can be more concentrated around text)
- **The Risk:** The collected modality may bias the learned model toward what people click to read/interpret, not necessarily what they glance at [@bylinskiiLearningVisualImportance2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating BubbleView clicks as identical to eye fixations without validation
- **Why it fails:** The paper notes systematic differences (e.g., concentration around text; non-uniformity across elements) even when rankings are similar [@bylinskiiLearningVisualImportance2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Click heatmaps show tight hotspots on text while eye-fixation maps (if you sample them) are broader or include other regions
- **The Test:** For a small subset, compare BubbleView maps to available fixation maps using similarity metrics (e.g., CC/KL as used in the paper) [@bylinskiiLearningVisualImportance2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase participants per visualization and smooth aggregated clicks (the paper blurs clicks with a Gaussian to match fixation-map format)
- **Best Fix:** Train on BubbleView for scale, but validate and calibrate against a smaller eye-tracking set when fixation fidelity is critical [@bylinskiiLearningVisualImportance2017].
