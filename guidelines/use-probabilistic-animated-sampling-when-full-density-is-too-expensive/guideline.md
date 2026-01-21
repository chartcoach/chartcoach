---
id: use-probabilistic-animated-sampling-when-full-density-is-too-expensive
title: Use Animated Probabilistic Plots to Summarize Uncertain Data Without Full KDE
bibliography: references.bib
description: Animate repeated random samples from the underlying uncertainty model
  so stable regions indicate high density and flicker reveals outliers.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:summarize
- visual:animation
- impact:performance
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When computing a full density plot is too slow, display an animated probabilistic plot that repeatedly samples from the data’s modeled PDF and replaces old samples over time.

## The Logic <!-- role: reason -->

Repeated random sampling produces marks distributed like the underlying PDF without explicitly computing it. Over time, high-density regions look stable while low-probability regions flicker, drawing attention to potential outliers; accumulating samples also converges toward a histogram approximation of the PDF.

- **The Principle:** Monte Carlo sampling for perceptual stability + outlier flicker
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly understand distribution structure and locate outliers in very large uncertain datasets
- **Data Type:** Uncertain multivariate data where sampling is easy (e.g., equal-weight mixture over points; independent per-variable normals)
- **Audience:** Expert analysts needing interactive performance

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must interpret a static frame precisely (e.g., reporting a final figure without animation)
- **Reason:** A single random sample frame can contain false patterns; stability emerges across time/accumulation [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Deterministic repeatability and immediate accuracy in any single frame
- **The Risk:** Viewers may over-interpret transient random structures if animation/accumulation is insufficient [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Show only one set of random samples as a “summary”
- **Why it fails:** One sample can introduce false patterns and does not reliably reflect the PDF [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Patterns appear and disappear dramatically between frames, with no stable regions forming
- **The Test:** Watch the plot over time; credible high-density structure should remain relatively stable while rare events flicker [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase sample count per frame and continuously refresh samples (replace old with new)
- **Best Fix:** Accumulate frames into a floating-point buffer to form a line/point density histogram that converges toward the PDF [@fengMatchingVisualSaliency2010].
