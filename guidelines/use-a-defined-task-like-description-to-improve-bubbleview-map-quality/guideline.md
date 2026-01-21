---
id: use-a-defined-task-like-description-to-improve-bubbleview-map-quality
title: Use a Defined Task (e.g., Description) to Improve BubbleView Quality
bibliography: references.bib
description: Add a directed task to make BubbleView clicks more intentional and consistent,
  especially with fewer participants or complex stimuli.
labels:
- task:describe
- task:measure
- visual:attention
- impact:signal-quality
- audience:researcher
- method:BubbleView
- source:kimBubbleView2017
---

## The Rule <!-- role: advice -->

When possible, give participants a defined task (such as describing the image) while using BubbleView, instead of pure free-viewing.

## The Logic <!-- role: reason -->

A directed task adds an “energy barrier” that discourages random exploration and pushes participants to click informative regions needed to complete the task. The paper finds BubbleView best approximates fixations under defined tasks (notably descriptions for information visualizations) and that description can converge faster than free-viewing when participant counts are small [@kimBubbleViewInterfaceCrowdsourcing2017].

- **The Principle:** Task constraints increase intentionality and inter-participant consistency
- **The Evidence:** [@kimBubbleViewInterfaceCrowdsourcing2017]

## Where to Apply <!-- role: context -->

- **User Goal:** High-quality importance maps with limited participants/budget.
- **Data Type:** Information-dense images (e.g., visualizations, webpages) that benefit from careful inspection.
- **Audience:** Studies where participants can reasonably articulate what they see.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The stimulus cannot be reliably described (e.g., ambiguous graphic designs, mixed languages, insufficient context).
- **Reason:** The task may be ill-defined and introduce noise or frustration [@kimBubbleViewInterfaceCrowdsourcing2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** More time per image (and higher cost), since participants click and write.
- **The Risk:** Bias toward text-heavy/semantic regions relevant to description over purely perceptual salience [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “describe the image” on images where description is not feasible or comparable across participants.
- **Why it fails:** Inconsistent interpretations reduce consistency and can distort what gets clicked [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Descriptions are short/low-effort and clicks look scattered or minimal.
- **The Test:** Enforce a minimum description length and spot-check description quality as a proxy for engagement [@kimBubbleViewInterfaceCrowdsourcing2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add/raise a minimum character requirement for descriptions.
- **Best Fix:** Choose a task that matches the stimulus (description for visualizations/webpages; free-viewing for designs where description is ill-defined) [@kimBubbleViewInterfaceCrowdsourcing2017].
