---
id: warn-against-size-inferences-from-cone-style-summaries
title: Explicitly Prevent Size Inferences from Cone-Style Uncertainty Summaries
bibliography: references.bib
description: If you must use a cone summary, actively prevent users from interpreting
  it as storm growth.
labels:
- chart:map
- chart:uncertainty
- task:interpret
- visual:shape
- impact:clarity
- data:geospatial
- audience:novice
- domain:weather
---

## The Rule <!-- role: advice -->

If you use a cone-style summary display, explicitly prevent and test for the interpretation that the cone shows physical storm-size growth over time.

## The Logic <!-- role: reason -->

The cone’s expanding boundary is a salient feature that novices naturally map to “getting larger,” producing systematic misunderstandings about what the display encodes.

- **The Principle:** Salient boundaries invite literal spatial/size interpretations in geospatial contexts
- **The Evidence:** Cone viewers made larger size-change judgments and were significantly more likely to self-report that the display shows the hurricane getting larger over time than ensemble viewers [@padillaEffectsEnsembleSummary2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand forecast uncertainty without confusing it with physical storm properties
- **Data Type:** Geospatial uncertainty summaries with explicit boundaries (cones, envelopes)
- **Audience:** Novice audiences in public communication contexts

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not communicating to novices, or your audience is trained and verified to interpret the encoding correctly in your context.
- **Reason:** The guideline targets novice misinterpretations demonstrated in the study population [@padillaEffectsEnsembleSummary2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional explanatory burden and need for comprehension testing.
- **The Risk:** Over-explaining may reduce speed of consumption for users who already understand the display [@padillaEffectsEnsembleSummary2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming the cone is “intuitive” because it is common.
- **Why it fails:** The study shows a reliable, intuitive-but-wrong inference about size growth driven by salience, despite the cone’s standard usage [@padillaEffectsEnsembleSummary2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Users describe the cone as the hurricane “widening” or “bigger later.”
- **The Test:** Include a comprehension question like “Does the display show the hurricane getting larger over time?”; elevated “yes” indicates failure [@padillaEffectsEnsembleSummary2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit messaging that the cone represents uncertainty in the center track, not storm size, and validate with a quick comprehension check.
- **Best Fix:** Replace the cone with an ensemble display when feasible for your audience and communication goal [@padillaEffectsEnsembleSummary2017].
