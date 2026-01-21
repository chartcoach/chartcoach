---
id: use-element-aligned-importance-annotations-to-support-layout-applications
title: Use Element-Aligned Importance Annotations to Support Layout Applications
bibliography: references.bib
description: Prefer importance supervision that aligns to whole design elements when
  the downstream task operates on elements.
labels:
- chart:multiple
- task:retarget
- visual:attention
- impact:layout
- data:mixed
- audience:designer
- method:annotation
---

## The Rule <!-- role: advice -->

If your downstream design task manipulates or preserves discrete elements (e.g., retargeting/cropping posters), train and/or supervise importance with element-aligned annotations rather than point-like clicks.

## The Logic <!-- role: reason -->

Element-aligned importance maps act like a soft segmentation of important regions, which better supports operations like cropping/retargeting that should preserve entire titles or blocks instead of fragments.

- **The Principle:** Alignment between supervision granularity and application granularity
- **The Evidence:** The paper trains the graphic-design model on GDI “mask most important regions” annotations (more uniform over elements) and states this better supports design applications than BubbleView clicks, which are not uniform within elements and can cut off parts of text/elements [@bylinskiiLearningVisualImportance2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Retarget/crop graphic designs while preserving key elements (titles, main imagery, callouts)
- **Data Type:** Poster-like single-page designs with discrete blocks
- **Audience:** Designers and tool builders implementing automatic retargeting or summarization

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your goal is to model attention at fine spatial resolution (e.g., reading patterns within a text block)
- **Reason:** Element-level uniformity can hide within-element variation that matters for attention modeling [@bylinskiiLearningVisualImportance2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Collecting element-aligned masks can be slower or require clearer participant instruction than click collection
- **The Risk:** Uniform masks may over-simplify importance when only parts of an element truly draw attention [@bylinskiiLearningVisualImportance2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using click-based maps directly as a cropping energy for element-preserving retargeting
- **Why it fails:** Click maps are non-uniform across elements; downstream methods may remove or truncate parts of text/graphics even when the element is “important” overall [@bylinskiiLearningVisualImportance2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Retargeted outputs clip through text lines or slice key graphical elements
- **The Test:** Overlay importance maps on element bounding boxes and verify high-importance regions cover entire key elements rather than small hotspots [@bylinskiiLearningVisualImportance2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Post-process importance maps to be more uniform within detected elements (e.g., aggregate importance per element region)
- **Best Fix:** Train (or fine-tune) on element-aligned ground truth (like GDI masks) when the application requires preserving whole elements [@bylinskiiLearningVisualImportance2017].
