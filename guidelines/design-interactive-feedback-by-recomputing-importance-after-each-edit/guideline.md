---
id: design-interactive-feedback-by-recomputing-importance-after-each-edit
title: Design Interactive Feedback by Recomputing Importance After Each Edit
bibliography: references.bib
description: Provide real-time feedback in design tools by recomputing predicted importance
  maps after layout and style changes.
labels:
- chart:multiple
- task:iterate
- visual:attention
- impact:workflow
- data:mixed
- audience:designer
- method:interactive
---

## The Rule <!-- role: advice -->

In interactive design tools, recompute and display predicted importance after each user edit (move/resize/style) to show how the change shifts element importance.

## The Logic <!-- role: reason -->

Fast feed-forward inference enables near-real-time importance updates, and the model’s rankings track how importance changes under common manipulations (position/size), making it suitable as immediate feedback during iteration.

- **The Principle:** Real-time predictive feedback for attention/importance management
- **The Evidence:** The paper demonstrates an interactive prototype that updates importance maps as users modify elements, and reports that predicted importance correlates with human importance rankings across fine-grained design variants (e.g., changing element size/location) [@bylinskiiLearningVisualImportance2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Iteratively adjust layout and styling to control what viewers notice first
- **Data Type:** Graphic designs with editable elements (text blocks, images, shapes)
- **Audience:** Designers (especially when exploring alternative layouts quickly)

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot meet interactive latency (updates feel slow) on target hardware for typical canvas sizes
- **Reason:** The feedback loop depends on fast recomputation; otherwise it interrupts workflow [@bylinskiiLearningVisualImportance2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Compute budget during editing (GPU/CPU time)
- **The Risk:** Users may over-optimize for model-predicted importance rather than communication goals, especially if the model has learned dataset biases (e.g., strong emphasis on titles/text) [@bylinskiiLearningVisualImportance2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a static “importance” overlay that does not update with edits
- **Why it fails:** It cannot reflect how changes in size/location affect predicted importance, undermining the core benefit demonstrated in the paper [@bylinskiiLearningVisualImportance2017].

## How to Check <!-- role: check -->

- **Visual Sign:** After moving/resizing a key element, the importance overlay remains unchanged or updates too slowly to be useful
- **The Test:** Make a large, obvious change (e.g., enlarge and isolate a text block); the importance ranking should shift accordingly and update within an interactive time window (the paper reports ~100ms at ~600×450 on a Titan-X GPU) [@bylinskiiLearningVisualImportance2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Downscale the canvas for inference during interaction and refine at full resolution on idle
- **Best Fix:** Use an efficient fully convolutional model and hardware acceleration so each edit triggers a fast feed-forward pass, enabling continuous feedback as shown in the paper [@bylinskiiLearningVisualImportance2017].
