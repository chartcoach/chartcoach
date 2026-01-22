---
id: increase-viewing-time-or-use-description-task-for-information-dense-webpages-in-bubbleview
title: Increase BubbleView viewing time or use a description task for information-dense
  webpages
bibliography: references.bib
description: For dense webpage screenshots, longer viewing times or a defined description
  task improves the similarity of BubbleView clicks to fixation patterns.
labels:
- chart:other
- task:study-design
- visual:layout
- impact:validity
- data:multimodal
- audience:researcher
- method:bubbleview
---

## Use longer time or a defined task for dense pages <!-- role: advice -->

When collecting BubbleView clicks on information-dense webpage screenshots, allocate longer viewing time per image or use a description task rather than short free-viewing.

## Why dense layouts need more time or task structure <!-- role: reason -->

Dense pages contain many potential targets, so limited time can lead to under-sampling and weaker agreement with fixation distributions. More time allows additional deliberate clicks, and a description task concentrates clicks on informative elements and reduces variability.

**Mechanism:** Increasing available time increases the number of inspected regions; adding a task increases consistency by aligning participants’ clicking strategies.

**Evidence:** On webpages, longer free-viewing duration improved similarity metrics compared to shorter duration, and there was a time-by-bubble-size interaction indicating a tradeoff between time and bubble radius [@kimBubbleViewInterfaceCrowdsourcing2017]. For smaller participant counts, the description task produced click maps that converged faster toward fixation patterns than free-viewing [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** Webpage fixation data also exhibited lower inter-observer consistency, which limits the maximum achievable prediction performance.

## When this guideline applies <!-- role: context -->

- **User Goal:** Approximate fixation patterns or derive importance on webpage screenshots.
- **Task:** Free-viewing on webpages, or “click and describe” for task-guided importance.
- **Data:** Text-heavy or mixed-content webpages with high information density.
- **Chart Setting:** Browser-based crowdsourcing with fixed time per image.
- **Audience:** General online participants.
- **Success Criterion:** Click maps stabilize across participants and better match fixation distributions.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You must match a legacy protocol that uses short free-viewing durations and cannot change timing or task. **Why:** Protocol constraints may outweigh the goal of maximizing click-to-fixation similarity [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Longer viewing times increase cost per image. **Risk:** Description tasks can bias attention toward text and increase completion time substantially. **Mitigation:** Use longer free-viewing for closer task-free behavior, and reserve description tasks for cases where task-relevant importance is the goal [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a short free-viewing duration on dense webpages and expecting stable maps. **Why it fails:** Too few clicks are collected to cover the diverse content, reducing similarity and stability [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Heatmaps are fragmented and differ strongly across random participant subsets. **Quick Check:** Compare aggregate click maps produced from two random halves of participants. **Stronger Test:** Plot similarity (to fixation data if available, or to a held-out click subset) as a function of time condition on a pilot [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Increase per-image viewing time for free-viewing on webpages.
- Use a description task when you have fewer participants and need faster convergence.
- Adjust bubble radius upward when time is constrained, and downward when you can afford longer time.
- Separate analyses by webpage subtype (e.g., text-heavy vs pictorial) if variability differs across subtypes [@kimBubbleViewInterfaceCrowdsourcing2017].
