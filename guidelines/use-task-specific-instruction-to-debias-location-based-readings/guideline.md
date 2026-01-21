---
id: use-task-specific-instruction-to-debias-location-based-readings
title: Teach Users to Focus on the Distribution Center, Not Track-Location Overlap
bibliography: references.bib
description: Use task-specific instruction and practice to reduce overlap-driven judgments
  in ensemble hurricane track displays.
labels:
- chart:ensemble
- task:assess-risk
- visual:annotation
- impact:reduce-bias
- data:uncertainty
- audience:novice
- domain:hurricane-forecast
---

## The Rule <!-- role: advice -->

When decisions depend on a specific location, provide task-specific instruction (with examples) that users should judge risk by proximity to the center of the track distribution and should not base judgments on whether a single line overlaps the location.

## The Logic <!-- role: reason -->

- **The Principle:** Knowledge-driven processing can partially override visual salience, especially when instruction targets a specific, known error pattern.
- **The Evidence:** Task-specific video instruction that explained the collocation effect and included practice reduced the collocation effect more than general visualization instruction (about a 61% reduction vs. no instruction), but did not fully eliminate it [@padillaPowerfulInfluenceMarks2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Choosing between locations (e.g., assets, towns) for preparation, resource allocation, or evacuation emphasis.
- **Data Type:** Ensemble track display used as a static decision aid (e.g., in reports, dashboards, or briefings).
- **Audience:** Novice or mixed audiences who may not spontaneously adopt the “distribution center” strategy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot reasonably deliver training/practice (e.g., a single fleeting graphic with no supporting space/time).
- **Reason:** The intervention is instructional; without delivery, it cannot work as intended.

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires time and attention (instructional overhead).
- **The Risk:** Even explicit, “frank” instruction will not fully remove the bias; residual collocation effects can remain [@padillaPowerfulInfluenceMarks2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing only general background on forecasting without explicitly addressing the overlap misconception.
- **Why it fails:** General visualization instruction reduces the bias, but less than instruction that explicitly names and practices overcoming the collocation effect [@padillaPowerfulInfluenceMarks2020].

## How to Check <!-- role: check -->

- **Visual Sign:** After instruction, users still rate “on-line” locations higher than matched “off-line” locations.
- **The Test:** Compare on-line vs off-line damage ratings before/after instruction; if the difference persists, the visualization still induces collocation bias [@padillaPowerfulInfluenceMarks2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add two worked examples: one where a line overlaps a farther-from-center location and one where it doesn’t, emphasizing the center-of-distribution decision rule.
- **Best Fix:** Integrate short instruction plus practice questions into onboarding/training and combine with display tuning (e.g., moderate ensemble member counts) to reduce the visual pull of any one line [@padillaPowerfulInfluenceMarks2020].
