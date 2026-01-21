---
id: use-bubbleview-clicks-to-crowdsource-importance-maps-when-eye-tracking-is-impractical
title: Use BubbleView Clicks to Crowdsource Image Importance Maps
bibliography: references.bib
description: Collect BubbleView clicks on blurred images to approximate attention/importance
  maps without eye-tracking hardware.
labels:
- task:measure
- task:rank
- visual:attention
- impact:insight
- audience:researcher
- method:BubbleView
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Use BubbleView (blurred image + click-to-reveal bubbles) to crowdsource an importance map when you need attention-like data but cannot run lab eye tracking.

## The Logic <!-- role: reason -->

BubbleView records discrete clicks that reflect conscious choices about where to inspect; aggregating and smoothing click locations yields an “importance map” that can approximate fixation distributions and support element-importance ranking. The paper reports BubbleView clicks accounting for ~75–90% of eye-fixation signal depending on image/task type, and producing reliable importance rankings of elements [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Discrete, intentional sampling of informative regions
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Approximate where people look / what they consider important; rank elements by importance.
- **Data Type:** Static images (natural scenes, webpages, visualizations, graphic designs).
- **Audience:** Researchers/designers needing scalable attention/importance signals.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need true eye-movement dynamics (timing, saccades, fixation durations) or unconscious biases.
- **Reason:** BubbleView only captures discrete click locations, not full oculomotor behavior [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slower interaction than natural viewing; higher per-image time than simple free-viewing.
- **The Risk:** Under-sampling of less “important” regions (participants may never click areas they would briefly glance at) [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating BubbleView as a drop-in replacement for eye tracking in any task.
- **Why it fails:** BubbleView best captures conscious inspection/importance and works best on static images and defined tasks [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Click heatmap is extremely sparse or dominated by a few random points.
- **The Test:** Inspect per-participant click traces in a monitoring view to confirm participants are meaningfully exploring rather than clicking minimally/randomly [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase viewing time per image or recruit more participants.
- **Best Fix:** Add a well-defined task (e.g., description) to encourage intentional, informative clicking and cleaner maps [@kimBubbleViewInterfaceCrowdsourcing2017].
