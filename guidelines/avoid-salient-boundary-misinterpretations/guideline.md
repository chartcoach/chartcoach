---
id: avoid-salient-boundary-misinterpretations
title: Avoid Salient Boundaries When They Imply False Containment
bibliography: references.bib
description: Do not add strong boundaries that make viewers treat continuous uncertainty
  as a contained region.
labels:
- chart:map
- task:judge-uncertainty
- visual:boundary
- impact:accuracy
- data:uncertainty
- audience:novice
- bias:containment
- mechanism:type-1
---

## The Rule <!-- role: advice -->

Do not use prominent enclosed boundaries to represent continuous uncertainty if “inside vs. outside” is not a true categorical distinction.

## The Logic <!-- role: reason -->

Boundaries trigger a containment heuristic: viewers treat values inside the boundary as categorically similar and outside as categorically different. The review shows this can mislead judgments for uncertainty displays (e.g., bounded circles vs. graded fades; bounded cones vs. path ensembles) [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Reasoning about probabilities, uncertainty, risk, or “how likely is X at location Y?”
- **Data Type:** Continuous spatial uncertainty, forecast uncertainty, positional uncertainty
- **Audience:** General public and non-expert decision makers

## When to Break It <!-- role: exceptions -->

- **Scenario:** The data truly are categorical (a real threshold rule) and the decision is “in/out”
- **Reason:** Then containment is the intended semantics and a boundary can support correct categorization [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate “region” readability; may feel less map-like
- **The Risk:** Graded encodings can be harder to read quickly without training [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a bold outline to “help visibility” of an uncertainty region
- **Why it fails:** The outline becomes the salient cue and encourages categorical, not probabilistic, interpretations [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users talk as if uncertainty is “contained” (e.g., “it won’t happen outside the circle/cone”).
- **The Test:** Ask users to compare two points equidistant from the center but one just outside the boundary; if they treat it as drastically different, the boundary is driving a containment bias [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce boundary salience (lighter stroke, less contrast) or remove the enclosing outline.
- **Best Fix:** Use a graded uncertainty depiction (e.g., fading/representative samples) that does not create an artificial “edge” [@padillaDecisionMakingVisualizations2018].
