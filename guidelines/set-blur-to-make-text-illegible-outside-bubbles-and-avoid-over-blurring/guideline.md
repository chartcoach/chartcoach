---
id: set-blur-to-make-text-illegible-outside-bubbles-and-avoid-over-blurring
title: "Set Blur So Text Is Illegible Outside Bubbles (But Don\u2019t Over-Blur)"
bibliography: references.bib
description: Choose blur that removes readable detail in the periphery while preserving
  enough context for navigation.
labels:
- task:plan-study
- visual:spatial-resolution
- impact:signal-quality
- audience:researcher
- method:BubbleView
- parameter:blur
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Tune BubbleView’s blur so that fine details (especially text) are not readable without clicking, but keep enough global structure visible to guide where to click next.

## The Logic <!-- role: reason -->

The paper reports selecting blur levels to distort text beyond legibility, forcing deliberate clicks to read. However, very high blur (e.g., sigma ≈ 70 px in their tests) reduced similarity and hindered exploration by removing too much context [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Peripheral degradation should block detail without eliminating scene context
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Make clicks reflect intentional inspection rather than casual reading from the blurred background.
- **Data Type:** Images with text or fine-grained detail (webpages, visualizations, posters).
- **Audience:** Remote participants with varied displays.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your stimulus relies on large-scale visual features (e.g., big shapes/colors) and has little/no text.
- **Reason:** Heavy blur can change what remains visible and bias what gets clicked (elements may already be visible or may disappear) [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Stronger blur can increase effort and reduce exploration efficiency.
- **The Risk:** Over-blurring suppresses contextual cues and shifts clicks away from otherwise-important elements [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing blur aggressively to “force” clicking everywhere.
- **Why it fails:** Too much blur harms navigation and lowers agreement/performance [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Participants appear to click randomly or complain they cannot orient themselves.
- **The Test:** Pilot: verify text is unreadable in the blurred view while major layout/objects are still discernible [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce blur until participants can recognize layout/objects but still cannot read fine text.
- **Best Fix:** Re-pilot blur per stimulus class and standardize within a dataset, as done in the paper’s experiments [@kimBubbleViewInterfaceCrowdsourcing2017].
