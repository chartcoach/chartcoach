---
id: prioritize-low-cost-transitions
title: Prioritize Low-Transformation-Cost Transitions
bibliography: references.bib
description: Prefer transitions that require fewer attribute changes because audiences
  choose them more often as the next step.
labels:
- task:sequence
- impact:preference
- impact:clarity
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

When choosing what visualization comes next, pick the option with the lowest transformation cost relative to the current view.

## The Logic <!-- role: reason -->

Audiences systematically prefer lower-cost transitions: in the study, cost-1 transitions were much more likely to be chosen than cost-2 or cost-3 transitions as the next slide, indicating a strong preference for consistency [@hullmanDeeperUnderstandingSequence2013].

- **The Principle:** Transformation cost as audience-perceived transition difficulty
- **The Evidence:** Mechanical Turk results show strong dispreference for higher-cost transitions vs. cost-1 (and no clear preference difference between cost-2 and cost-3) [@hullmanDeeperUnderstandingSequence2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide between multiple candidate next slides from the same starting slide
- **Data Type:** Any narrative set where multiple attributes can change between views
- **Audience:** Broad audiences; especially helpful for non-designers authoring stories

## When to Break It <!-- role: exceptions -->

- **Scenario:** A high-cost next view is necessary to introduce the next “chapter” of the narrative.
- **Reason:** The paper’s cost model optimizes local transitions; story structure may occasionally require larger jumps [@hullmanDeeperUnderstandingSequence2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to reorder content purely by thematic preference.
- **The Risk:** Over-optimizing for low cost can reduce narrative pacing (too incremental).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking the next slide based on what is “most interesting,” ignoring how many attributes changed.
- **Why it fails:** Audience preference in the paper is tied strongly to lower transition cost for immediate adjacency [@hullmanDeeperUnderstandingSequence2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers need extra explanation to understand why slide B follows slide A.
- **The Test:** Count attribute changes (time/dimension/measure/granularity); if there exists a candidate next slide with fewer changes that still advances the story, prefer it.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder adjacent slides so each step reduces the number of changed attributes.
- **Best Fix:** Treat your slides as nodes and choose a low-cost path through them (the paper’s graph-driven sequencing approach) [@hullmanDeeperUnderstandingSequence2013].
