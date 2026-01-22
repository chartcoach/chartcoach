---
id: use-bubbleview-clicks-to-approximate-eye-fixations-on-static-images
title: Use BubbleView mouse clicks to approximate eye fixations on static images
bibliography: references.bib
description: Collect discrete clicks on blurred static images to approximate fixation-based
  attention and importance maps without eye-tracking hardware.
labels:
- chart:other
- task:measure-attention
- visual:focus+blur
- impact:measurement
- data:multimodal
- audience:researcher
- method:bubbleview
---

## Use BubbleView clicks as a fixation proxy on static images <!-- role: advice -->

Use BubbleView’s blur-plus-click “bubble” interface to collect discrete mouse clicks as a proxy for where people would fixate on a static image.

## Why discrete clicks can approximate fixation locations <!-- role: reason -->

BubbleView adds an effortful step (choosing where to click) that converts attention into explicit, spatially localized samples. Aggregating many users’ clicks and smoothing them produces an “importance map” that is comparable to fixation maps, while being easier to deploy online than hardware eye tracking.

**Mechanism:** Discrete clicks act as intentional sampling of regions that users choose to inspect at full resolution, and aggregated click density can approximate fixation density over image regions.

**Evidence:** Across multiple experiments and image types, BubbleView click maps achieved high similarity to ground-truth fixation maps and accounted for a large fraction of fixations with modest participant counts [@kimBubbleViewInterfaceCrowdsourcing2017]. BubbleView also supported ranking elements by importance in ways that aligned closely with fixation-based rankings [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** BubbleView is designed for static images; it does not capture temporal fixation sequences or saccade dynamics.

## When to use BubbleView instead of eye tracking <!-- role: context -->

- **User Goal:** Approximate where viewers look, or derive an importance map, without lab eye-tracking hardware.
- **Task:** Attention/importance measurement on images; task-guided viewing (e.g., describing content) or constrained free-viewing.
- **Data:** Static images (visualizations, webpages, photos, graphic designs).
- **Chart Setting:** Online/crowdsourced study; limited budget; need to scale across many images/participants.
- **Audience:** Researchers and practitioners who need aggregate attention/importance rather than precise eye movement time series.
- **Success Criterion:** Click maps correlate strongly with fixation maps or reliably rank elements by importance.

## When not to follow this approach <!-- role: exceptions -->

**Break it when:** You need time-resolved eye movement measures (fixation duration, saccades, scanpaths) rather than aggregate spatial attention. **Why:** BubbleView produces discrete click locations and does not preserve natural eye-movement dynamics [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Interaction is slower than natural viewing, increasing per-image time compared to eye tracking or mouse-move methods. **Risk:** Clicks reflect conscious selection and may under-sample quick glances or systematic gaze biases. **Mitigation:** Treat outputs as an importance map (task-relevant inspection) rather than a full replacement for eye movement recordings [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Interpreting BubbleView click maps as a full substitute for all eye-tracking measures. **Why it fails:** BubbleView is validated primarily for spatial distributions and importance ranking, not full eye-movement behavior [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Click maps are sparse, inconsistent, or miss key semantic regions expected to be inspected. **Quick Check:** Inspect per-image aggregated click heatmaps and a few participant click sequences to see whether clicks cluster on meaningful elements. **Stronger Test:** Compute similarity between click maps and any available fixation data using standard map-comparison metrics (e.g., correlation-style and fixation-prediction-style scores) [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Run conventional lab eye tracking if you require fixation timing, scanpath order, or saccade measures.
- Use BubbleView with a more defined task (e.g., description) when free-viewing clicks are too noisy for your images.
- Increase viewing time per image for dense layouts (e.g., webpages) if click maps are not converging well.
- If you must use mouse movements, plan for post-processing to separate points of interest from transition traces rather than treating raw trajectories as attention [@kimBubbleViewInterfaceCrowdsourcing2017].
