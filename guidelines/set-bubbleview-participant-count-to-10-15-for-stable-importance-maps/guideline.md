---
id: set-bubbleview-participant-count-to-10-15-for-stable-importance-maps
title: "Recruit 10\u201315 Participants per Image for Stable BubbleView Maps"
bibliography: references.bib
description: "Use roughly 10\u201315 crowd participants per image to reach near-asymptotic\
  \ map quality in BubbleView."
labels:
- task:plan-study
- impact:cost-efficiency
- audience:researcher
- method:BubbleView
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

Plan for about 10–15 BubbleView participants per image as a default to get stable, high-quality importance maps.

## The Logic <!-- role: reason -->

Across experiments, BubbleView maps improved with more participants but showed diminishing returns; on visualizations, 10–15 participants achieved ~97–98% of the extrapolated performance limit, and across image types 10–15 participants often accounted for ~75–90% of fixation signal depending on task/stimulus [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Aggregation quickly averages out individual noise
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Balance budget/time against reliability of importance maps.
- **Data Type:** Static images where you aggregate across participants.
- **Audience:** MTurk-style crowdsourcing studies.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Highly variable stimuli/tasks (low inter-observer consistency), or you need very fine-grained ranking of many small elements.
- **Reason:** More participants may be required to stabilize estimates when attention is inherently inconsistent [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Cost scales linearly with participants.
- **The Risk:** Over-collecting yields minimal gain after the early plateau [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Collecting very large N by default “to be safe.”
- **Why it fails:** The paper shows rapid saturation for BubbleView; money is better spent on better task definition or adequate viewing time [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Heatmaps look nearly unchanged when adding more participants.
- **The Test:** Compute map similarity (e.g., split-half stability or NSS/CC versus a held-out set) as you add participants; stop when gains flatten [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** If unstable at 10–15, add participants in small batches (e.g., +5) and re-check stability.
- **Best Fix:** If instability persists, change task design (e.g., description) or increase viewing time for complex images [@kimBubbleViewInterfaceCrowdsourcing2017].
