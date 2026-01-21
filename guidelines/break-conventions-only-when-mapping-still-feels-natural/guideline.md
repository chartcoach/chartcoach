---
id: break-conventions-only-when-mapping-still-feels-natural
title: If You Break Convention, Keep the Mapping Intuitive
bibliography: references.bib
description: When you deviate from standard formats, preserve intuitive mappings between
  magnitude and visual variables.
labels:
- chart:any
- task:interpret
- visual:mapping
- impact:comprehension
- data:any
- audience:novice
- complexity:advanced
---

## The Rule <!-- role: advice -->

If you must break graph conventions, preserve intuitive mappings: “more” should still look like more via position/length/area in ways that match common knowledge.

## The Logic <!-- role: reason -->

- **The Principle:** Viewers rely on general world knowledge and learned graphical conventions to interpret mappings automatically.
- **The Evidence:** The paper notes that conventions often mirror real-world experience (e.g., stacks get taller), and that violating expectations can mislead interpretation [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding an unusual visualization without misreading directionality or magnitude.
- **Data Type:** Any case requiring a novel encoding.
- **Audience:** Mixed or novice audiences where misinterpretation risk is high.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the domain has its own strong alternative convention (a different “intuitive” mapping for that audience).
- **Reason:** The “intuitive” mapping depends on what the audience has learned and expects [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some design freedom in the novel format.
- **The Risk:** Even with intuitive mapping, novelty can still slow reading.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a novel mapping that contradicts expectations (e.g., shaded region interpreted as “size of threat” when it actually means uncertainty).
- **Why it fails:** Viewers apply default interpretations to common visual metaphors like shaded regions [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers confidently report the wrong concept (e.g., interpreting uncertainty as physical size).
- **The Test:** Ask viewers what the most salient visual element “means” before explaining. If answers don’t match intent, the mapping is not intuitive.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit, nearby explanation of what the visual encoding represents.
- **Best Fix:** Redesign to align with existing expectations (or use a conventional chart) so the intended concept is the default interpretation [@zacksDesigningGraphsDecisionMakers2020].
