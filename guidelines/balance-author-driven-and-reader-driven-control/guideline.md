---
id: balance-author-driven-and-reader-driven-control
title: Balance Author-Driven and Reader-Driven Control Explicitly
bibliography: references.bib
description: Decide how much narrative control you keep versus how much exploration
  you allow, and design consistently to that balance.
labels:
- task:communicate
- task:explore
- impact:clarity
- custom:author-driven
- custom:reader-driven
- audience:general
---

## The Rule <!-- role: advice -->

Choose an explicit point on the author-driven ↔ reader-driven spectrum, and align ordering, messaging, and interactivity to match that choice.

## The Logic <!-- role: reason -->

The paper frames narrative visualization as a tradeoff between author-imposed narrative flow (linear ordering, heavy messaging, limited interactivity) and reader discovery (no prescribed ordering, minimal messaging, free interactivity). Consistency across these levers prevents the experience from feeling directionless or over-scripted.

- **The Principle:** Narrative flow vs. discovery is governed by the combined design of ordering, messaging, and interactivity.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Either (a) efficient storytelling or (b) guided discovery without losing the intended message.
- **Data Type:** Any, especially complex datasets where unguided exploration can overwhelm.
- **Audience:** General audiences consuming journalistic/educational stories.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are intentionally creating an exploratory “data tool” experience with minimal authorial interpretation.
- **Reason:** Strongly reader-driven designs may purposefully avoid messaging and ordering [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** You can’t maximize both tight narrative control and unlimited exploration at once.
- **The Risk:** If you offer exploration without guidance, readers may miss the intended takeaway; if you over-author, they may not trust or engage with the data [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many interactive controls to a story without adding narrative scaffolding.
- **Why it fails:** The paper’s case study critique shows exploration power without sufficient guidance makes it hard to draw meaningful conclusions [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Either (a) the piece feels like a locked presentation with decorative hover states, or (b) it feels like a tool with no story.
- **The Test:** Identify your intended “main message” in one sentence; then verify the interface either ensures it is encountered (author-driven) or provides strong prompts/checkpoints to support it (hybrid) [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce interaction scope during core narrative segments; add messaging checkpoints.
- **Best Fix:** Adopt a named hybrid structure (martini glass, interactive slideshow, or drill-down story) and redesign ordering/messaging/interactivity to match [@segelNarrativeVisualizationTelling2010].
