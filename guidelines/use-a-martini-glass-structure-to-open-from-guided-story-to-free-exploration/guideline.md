---
id: use-a-martini-glass-structure-to-open-from-guided-story-to-free-exploration
title: Use a martini glass structure to move from author-driven narrative to reader-driven
  exploration
bibliography: references.bib
description: Start with a guided path and messaging, then open up interactivity after
  the narrative to enable discovery without losing orientation.
labels:
- chart:interactive
- task:explore
- visual:annotation
- impact:engagement
- data:multivariate
- audience:novice
- narrative:structure
---

## Move from guided narrative to open exploration using a martini glass structure <!-- role: advice -->

Begin with an author-driven narrative path that communicates key observations, then explicitly open into a reader-driven phase with freer interaction for exploration. Preserve orientation cues so users can explore without losing their place relative to the story.

## Staged release of interactivity balances comprehension and discovery <!-- role: reason -->

Full interactivity from the start can overwhelm readers and dilute the intended narrative, while no interactivity can prevent verification and personal inquiry. A staged structure allows the author to establish framing and meaning before handing control to the reader.

**Mechanism:** Early constraint supports comprehension and narrative flow; later freedom supports verification, question generation, and deeper engagement, with orientation aids preventing narrative loss.

**Evidence:** The martini glass structure is characterized as a common hybrid pattern: a tight author-driven “stem” followed by a reader-driven “glass” for free exploration after the narrative completes [@segelNarrativeVisualizationTelling2010].

**Notes:** Orientation aids can include a consistent visual platform, progress indicators, or persistent controls that reflect the current state.

## When the martini glass structure fits <!-- role: context -->

- **User Goal:** Learn the main story quickly and then investigate details or alternatives.
- **Task:** Guided walkthrough followed by exploratory filtering, time selection, or hover inspection.
- **Data:** Rich datasets where key findings should be communicated before exploration.
- **Chart Setting:** Web interactives that can transition from narrative frames to an exploratory mode.
- **Audience:** General audiences who need scaffolding before analysis-like interaction.
- **Success Criterion:** Users can explain the main takeaways and also perform their own checks.

## When not to use this structure <!-- role: exceptions -->

**Break it when:** The audience is primarily analysts who need immediate, unconstrained exploration. **Why:** The guided stem delays access to the exploratory capabilities they came for.

## Tradeoffs of the martini glass approach <!-- role: costs -->

**Sacrifice:** Some immediacy and flexibility at the beginning. **Risk:** If the stem is too long, users may never reach exploration; if too short, the narrative framing may be insufficient. **Mitigation:** Keep the guided portion focused on a small set of key observations.

## Common martini-glass mistakes <!-- role: mistakes -->

- **Mistake:** Opening full interactivity immediately with little narrative framing. **Why it fails:** Users can digress and miss the intended story.
- **Mistake:** Never opening the experience after the guided portion. **Why it fails:** Users cannot verify claims or pursue their own questions.

## Checks for balance between stem and glass <!-- role: check -->

**Failure Sign:** Users either feel lost during exploration or feel trapped in a presentation. **Quick Check:** Identify the moment where exploration becomes available and whether it is clearly signaled. **Stronger Test:** Observe whether users reach the exploration phase and successfully answer a self-generated question.

## Fixes when the transition to exploration fails <!-- role: fix -->

- Add an explicit prompt at the end of the narrative inviting exploration and naming a concrete interaction to try.
- Keep progress indicators visible so users can return to earlier narrative points after exploring.
- Constrain interactions during the stem to single-frame interactivity and broaden them later.
- Provide a summary or synthesis at the end to re-anchor users after exploration.
