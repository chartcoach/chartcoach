---
id: teach-interactivity-with-tacit-tutorials-not-just-instructions
title: Teach Interactivity with Tacit Tutorials, Not Just Instructions
bibliography: references.bib
description: Demonstrate how interaction works through the narrative itself so users
  learn by watching.
labels:
- task:learn
- impact:usability
- custom:interactivity-onboarding
- audience:general
---

## The Rule <!-- role: advice -->

Introduce interactive controls via a tacit tutorial: demonstrate interactions through animated, narrative-driven examples before expecting users to use them.

## The Logic <!-- role: reason -->

The paper identifies tacit tutorials as under-used but valuable: by animating components and showing the effect during the narrative, users learn interaction capabilities without needing heavy explicit instruction. The Budget Forecasts case exemplifies how the narrative itself teaches later interactive use.

- **The Principle:** Demonstration embedded in narrative lowers the barrier to interaction.
- **The Evidence:** [@segelNarrativeVisualizationTelling2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Follow a story and then interact meaningfully (e.g., explore a slider or hover details).
- **Data Type:** Interactive narratives with non-obvious controls (sliders, drill-down, filters).
- **Audience:** General audiences unfamiliar with the interaction model.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Interaction is extremely standard and obvious in-context (e.g., simple next/prev buttons only).
- **Reason:** A tacit tutorial may be unnecessary overhead when affordances are already clear [@segelNarrativeVisualizationTelling2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** More authoring effort to choreograph demonstrations.
- **The Risk:** Overlong tutorials can delay access to the story content [@segelNarrativeVisualizationTelling2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying only on dense instructional text (“Click here to…”) or assuming users will discover controls.
- **Why it fails:** The paper notes under-utilization of tacit tutorials and reports failures when users are dropped into interaction without orientation [@segelNarrativeVisualizationTelling2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Users don’t use key interactions or don’t notice them.
- **The Test:** Observe first-time users; if they never touch the main control your story depends on, onboarding failed [@segelNarrativeVisualizationTelling2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a brief animated cue showing the control being manipulated once.
- **Best Fix:** Integrate the interaction into the narrative sequence (tell → show → prompt the user to try) [@segelNarrativeVisualizationTelling2010].
