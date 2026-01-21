---
id: train-importance-models-on-domain-specific-human-importance-data
title: Train Importance Models on Domain-Specific Human Importance Data
bibliography: references.bib
description: Train neural networks to predict pixel-wise importance using human importance
  signals collected in the same visual domain.
labels:
- chart:multiple
- task:predict
- visual:attention
- impact:clarity
- data:mixed
- audience:designer
- method:ml
---

## The Rule <!-- role: advice -->

Train your importance predictor on human importance data from the same domain (e.g., data visualizations vs. graphic designs), not on natural-image saliency data alone.

## The Logic <!-- role: reason -->

Domain-specific layouts (titles, legends, axes, dense text) create attention and importance patterns that differ from natural images, so models trained on natural images can transfer poorly; training on in-domain annotations improves prediction quality.

- **The Principle:** Domain shift in attention/importance cues
- **The Evidence:** The paper trains separate FCN models for graphic designs (GDI annotations) and data visualizations (BubbleView clicks) and shows their predictions outperform natural-image saliency baselines on visualization click prediction, and are representative of eye fixations as well [@bylinskiiLearningVisualImportance2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Predict what content viewers will treat as most important to support summarization, retargeting, thumbnailing, or design feedback
- **Data Type:** Bitmap images of graphic designs or data visualizations with structured elements (titles, labels, legends, marks)
- **Audience:** Designers and tool builders needing automated importance estimates

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have no in-domain human importance data and cannot collect any
- **Reason:** The rule depends on learning in-domain priors; without in-domain supervision, the model cannot be trained as described [@bylinskiiLearningVisualImportance2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** You must collect (or obtain) human importance data (e.g., clicks or annotations) for the target domain
- **The Risk:** Models can inherit biases from the collected modality (e.g., click bias toward text), limiting generalization across tasks [@bylinskiiLearningVisualImportance2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a strong natural-image saliency model “as-is” for charts and assuming it captures importance
- **Why it fails:** The paper reports that such baselines (e.g., Judd, DeepGaze) underperform on visualization importance prediction compared to the in-domain trained model [@bylinskiiLearningVisualImportance2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The model highlights visually “poppy” regions but misses titles/captions/legends that humans focus on
- **The Test:** Compare predicted maps against a small sample of in-domain BubbleView clicks or importance annotations; large mismatches indicate domain shift [@bylinskiiLearningVisualImportance2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Collect a modest in-domain dataset (hundreds to ~1K images) with a scalable proxy like BubbleView clicks
- **Best Fix:** Train separate models per domain/modality (e.g., visualization-click model vs. graphic-design-annotation model) and validate against held-out in-domain ground truth [@bylinskiiLearningVisualImportance2017].
