---
id: set-bubbleview-blur-to-make-text-illegible-outside-bubbles-and-avoid-over-blurring
title: Set BubbleView blur to make text illegible outside bubbles, and avoid over-blurring
bibliography: references.bib
description: Choose a blur sigma that removes legible detail in the periphery while
  preserving enough context to guide exploration.
labels:
- chart:other
- task:study-design
- visual:blur
- impact:data-quality
- data:experimental
- audience:researcher
- method:bubbleview
---

## Tune blur to remove legibility but keep context <!-- role: advice -->

Choose a BubbleView blur level that makes fine details (especially text) unreadable unless clicked, and avoid blur so strong that participants lose contextual cues for where to click.

## Why blur must balance concealment and guidance <!-- role: reason -->

Blur is meant to mimic reduced peripheral acuity: it should prevent reading or fine discrimination outside the bubble while still providing enough structure to guide meaningful exploration. Excessive blur removes too much context and harms click-map similarity.

**Mechanism:** Moderate blur enforces focused sampling while preserving scene/layout structure; excessive blur collapses structural cues and reduces the ability to target relevant regions.

**Evidence:** In the experiments, blur sigmas were manually selected per dataset to distort text beyond recognition, and very strong blur (e.g., a high sigma condition) reduced similarity when approximating other attention traces [@kimBubbleViewInterfaceCrowdsourcing2017]. Across image types, blur values in a moderate range were used successfully, while overly strong blur hindered exploration [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** The paper varied blur in pixels rather than visual degrees, so calibration depends on displayed image size.

## When this blur-setting rule applies <!-- role: context -->

- **User Goal:** Ensure clicks represent intentional inspection rather than reading from the blurred background.
- **Task:** Description tasks where reading is needed, or free-viewing where semantic identification should require clicking.
- **Data:** Images containing text or small detailed elements.
- **Chart Setting:** Online study with variable viewing conditions; you control the displayed image resolution.
- **Audience:** General online participants.
- **Success Criterion:** Participants cannot reliably read text without clicking, but can still locate likely regions to inspect.

## When not to follow this blur-setting approach <!-- role: exceptions -->

**Break it when:** Your stimulus relies on coarse, large-scale features that remain interpretable under blur and you want to capture more “global” attention. **Why:** Enforcing illegibility may distort the natural strategy for those stimuli [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Higher blur can slow exploration and reduce coverage of the image. **Risk:** Over-blurring can suppress clicks on elements that become indistinguishable from the background. **Mitigation:** Pilot multiple blur levels and inspect whether key elements remain discoverable [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Maximizing blur to “force” clicking everywhere. **Why it fails:** Too little context makes it harder to decide where to click, reducing map quality and similarity to other attention measures [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Participants click randomly or repeatedly in uninformative areas, or systematically miss expected elements. **Quick Check:** Show the blurred-only stimulus to yourself and confirm you can locate layout structure but cannot read text. **Stronger Test:** Run a small pilot with two blur levels and compare click-map stability and coverage across participants [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Decrease blur if participants appear lost or fail to find major semantic regions.
- Increase blur if participants can read or identify small details without clicking.
- Adjust blur separately for datasets with very different text sizes or resolutions.
- Use a longer viewing time rather than extreme blur to improve exploration on dense stimuli [@kimBubbleViewInterfaceCrowdsourcing2017].
