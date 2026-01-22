---
id: use-tacit-tutorials-to-teach-interactions-by-animating-controls-during-the-narrative
title: Use tacit tutorials to teach interactions by animating and demonstrating controls
  during the narrative
bibliography: references.bib
description: Introduce interactive features implicitly through the story so users
  learn how to explore without heavy instructions.
labels:
- chart:interactive
- task:learn
- visual:motion
- impact:usability
- data:multivariate
- audience:novice
- interaction:tacit-tutorial
---

## Teach interactions with a tacit tutorial inside the narrative <!-- role: advice -->

Introduce interactive controls by demonstrating them as part of the narrative, using coordinated animation and changes that reveal what the interaction does. Prefer this implicit teaching over relying only on explicit instruction text.

## Demonstration reduces the instruction burden and invites exploration safely <!-- role: reason -->

Interactive narrative visualizations can fail when users do not notice or understand available interactions. Demonstrating controls in-context teaches manipulation without interrupting the story, and sets expectations about what interactions will change.

**Mechanism:** Showing the interaction outcome builds a mental model of control-to-effect mappings, enabling confident exploration without external documentation.

**Evidence:** Tacit tutorials are identified as a narrative structure tactic in which interactive components are animated along with the presentation to make manipulation clear; this approach is noted as under-utilized compared to explicit instruction in the analyzed corpus [@segelNarrativeVisualizationTelling2010].

**Notes:** Tacit tutorials can be reinforced later by a direct prompt that invites the user to try the interaction.

## When tacit tutorials are most needed <!-- role: context -->

- **User Goal:** Follow a guided story and then explore within it.
- **Task:** Learn how to use sliders, hover details, filtering, or drill-down without training.
- **Data:** Dense or unfamiliar datasets where unguided interaction is risky.
- **Chart Setting:** Interactive slideshows and martini-glass narratives that later open to exploration.
- **Audience:** Readers unfamiliar with visualization interaction conventions.
- **Success Criterion:** Users discover and correctly use interactions without reading a help page.

## When tacit tutorials may be unnecessary <!-- role: exceptions -->

**Break it when:** The visualization intentionally offers very limited interaction (or none) and the controls are obvious and standard. **Why:** Demonstration adds complexity without meaningful benefit.

## Tradeoffs of tacit tutorials <!-- role: costs -->

**Sacrifice:** Additional design and implementation effort to choreograph demonstrations. **Risk:** Over-animating controls can distract from the story content. **Mitigation:** Demonstrate only the key interactions and keep demonstrations brief.

## Common tacit-tutorial mistakes <!-- role: mistakes -->

- **Mistake:** Adding interactions without ever demonstrating or signaling them. **Why it fails:** Users may not discover the controls or may misuse them.
- **Mistake:** Demonstrating interactions that change multiple things at once without explanation. **Why it fails:** Users cannot infer what the control actually does.

## Checks for interaction learnability <!-- role: check -->

**Failure Sign:** Users do not use key interactions unless explicitly told. **Quick Check:** Watch a first-time user; if they never touch the main control, it needs an in-narrative demonstration. **Stronger Test:** Ask users what each control does after viewing; gaps indicate missing tacit instruction.

## Fixes when interactions are not discovered <!-- role: fix -->

- Animate the control and its effect once during the narrative to demonstrate the mapping.
- Add a short in-context prompt that invites users to try the interaction after the demonstration.
- Reduce the number of controls shown initially and reveal advanced controls later.
- Provide a stimulating default view that implies what interaction might reveal.
