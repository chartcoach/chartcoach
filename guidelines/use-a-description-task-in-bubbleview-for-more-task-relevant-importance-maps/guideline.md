---
id: use-a-description-task-in-bubbleview-for-more-task-relevant-importance-maps
title: Use a description task in BubbleView to collect task-relevant importance maps
bibliography: references.bib
description: Pair BubbleView with a description task to encourage deliberate, informative
  clicking and faster convergence with fewer participants.
labels:
- chart:other
- task:describe
- visual:text
- impact:data-quality
- data:multimodal
- audience:researcher
- method:bubbleview
---

## Use a description task to drive deliberate clicking <!-- role: advice -->

Use BubbleView with a “click and describe the image” task when you want clicks to reflect task-relevant inspection rather than unconstrained exploration.

## Why a defined task produces cleaner importance signals <!-- role: reason -->

Adding a concurrent description requirement increases intentionality: participants must gather information sufficient to write a coherent description, so clicks concentrate on informative regions and converge more quickly across participants.

**Mechanism:** The description requirement creates an “effort barrier” that discourages arbitrary clicking and biases clicks toward regions needed to complete the task.

**Evidence:** BubbleView achieved its strongest fixation-approximation results on information visualizations under a description task, accounting for a high fraction of fixations with small participant counts [@kimBubbleViewInterfaceCrowdsourcing2017]. On webpages, description produced higher similarity than free-viewing at smaller participant counts and converged faster, though longer free-viewing time could close the gap [@kimBubbleViewInterfaceCrowdsourcing2017].

**Notes:** This task also yields text descriptions that can be used for quality control or downstream analysis.

## When a description task is appropriate <!-- role: context -->

- **User Goal:** Identify which regions are most important for understanding/communicating image content.
- **Task:** Summarize or explain what the image shows (description while clicking).
- **Data:** Images with interpretable semantic content (e.g., information visualizations, many webpages).
- **Chart Setting:** Crowdsourcing where you want higher-quality clicks with fewer participants.
- **Audience:** Participants capable of producing coherent text in the study language.
- **Success Criterion:** Click maps concentrate on informative elements and approximate fixation-based maps better than free-viewing at the same participant count.

## When not to use a description task <!-- role: exceptions -->

**Break it when:** The images cannot be reasonably or consistently described (e.g., designs needing external context or varied languages). **Why:** The task becomes ill-defined, which can degrade both descriptions and the click patterns they drive [@kimBubbleViewInterfaceCrowdsourcing2017].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Description tasks take substantially longer per image than fixed-time free-viewing, increasing cost. **Risk:** Clicks may overweight readable text regions because they are directly useful for writing descriptions. **Mitigation:** Use the task primarily when task relevance is the goal, and treat outputs explicitly as importance-for-description rather than task-free saliency [@kimBubbleViewInterfaceCrowdsourcing2017].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Applying a description task to stimuli where “what counts as a good description” is ambiguous. **Why it fails:** Participants’ strategies diverge, reducing consistency and interpretability of both clicks and text [@kimBubbleViewInterfaceCrowdsourcing2017].

## Quick tests <!-- role: check -->

**Failure Sign:** Descriptions are generic, short, or inconsistent with clicked regions. **Quick Check:** Spot-check a small set of participant descriptions alongside their click overlays for coherence. **Stronger Test:** Compare convergence of click maps (e.g., similarity as participants increase) between description and free-viewing conditions on a pilot subset [@kimBubbleViewInterfaceCrowdsourcing2017].

## What to do instead <!-- role: fix -->

- Use fixed-time free-viewing when you need task-free exploration rather than task-driven importance.
- Increase free-viewing time on dense images when clicks are too sparse to be useful.
- Filter participants using description quality if you rely on the description task for data quality control.
- Use an alternative defined task (e.g., question answering) if “describe the whole image” is not aligned with your measurement goal [@kimBubbleViewInterfaceCrowdsourcing2017].
