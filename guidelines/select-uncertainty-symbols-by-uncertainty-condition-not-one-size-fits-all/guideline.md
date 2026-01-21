---
id: select-uncertainty-symbols-by-uncertainty-condition-not-one-size-fits-all
title: Select Uncertainty Symbols by Uncertainty Condition, Not One-Size-Fits-All
bibliography: references.bib
description: Pick different uncertainty symbol sets for space, time, and attribute
  uncertainty categories based on tested intuitiveness/performance.
labels:
- chart:map
- task:choose-encoding
- visual:encoding
- impact:correctness
- data:spatiotemporal
- audience:expert
- domain:uncertainty-visualization
---

## The Rule <!-- role: advice -->

Choose uncertainty symbol sets separately for each uncertainty condition (space/time/attribute × accuracy/precision/trustworthiness) rather than reusing one generic symbol for all.

## The Logic <!-- role: reason -->

Both experiments found statistically significant differences across uncertainty conditions in intuitiveness (Experiment #1) and in accuracy and response time for the map aggregation task (Experiment #2), showing that users do not interpret or use uncertainty symbols equally well across conditions [@maceachrenVisualSemioticsUncertainty2012].

- **The Principle:** Condition-dependent signification effectiveness
- **The Evidence:** Experiment #1 and #2 across-series significance tests [@maceachrenVisualSemioticsUncertainty2012]

## Where to Apply <!-- role: context -->

- **User Goal:** Correct interpretation and efficient use of uncertainty across multiple components (space/time/attribute)
- **Data Type:** Data products that expose multiple uncertainty types/conditions
- **Audience:** Users who need to reason with uncertainty (GIScience-like users in the study)

## When to Break It <!-- role: exceptions -->

- **Scenario:** The interface must be extremely simple and can only support one uncertainty cue.
- **Reason:** Multiple encodings can add complexity; the paper’s trade-off discussion implies simplicity can matter for performance [@maceachrenVisualSemioticsUncertainty2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** More legend space and design work.
- **The Risk:** Users may need to learn several symbol metaphors/encodings.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the same symbol (e.g., one saturation ramp) for all uncertainty kinds.
- **Why it fails:** The study shows both intuitiveness and task performance vary by condition and encoding choice [@maceachrenVisualSemioticsUncertainty2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users perform well for one uncertainty kind but poorly for another using the same encoding.
- **The Test:** Evaluate accuracy/RT (or comprehension) separately for each uncertainty condition you expose.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap in the most intuitive abstract/iconic “winner” per condition identified via user testing (as done between Experiment #1 and #2).
- **Best Fix:** Build a condition-to-encoding mapping table in your design system and validate it with representative tasks [@maceachrenVisualSemioticsUncertainty2012].
