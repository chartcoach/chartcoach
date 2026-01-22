---
id: treat-omissions-as-rhetorical-not-neutral
title: Treat information omissions and loss as rhetorical choices, even when used
  for simplification
bibliography: references.bib
description: Assume that leaving data out (variables, ranges, outliers, definitions)
  can steer interpretation as strongly as what is shown.
labels:
- chart:general
- task:interpret
- visual:scope
- impact:integrity
- data:multivariate
- audience:general
- custom:rhetoric-information-access
---

## Treat omissions as interpretation-shaping decisions <!-- role: advice -->

Document what information is not shown (variables, ranges, exceptions, definitions, and interaction paths) and assume those omissions affect what conclusions viewers find plausible.

## Why omissions steer interpretation <!-- role: reason -->

Narrative visualizations frequently simplify by withholding potentially complicating information, and users often cannot detect what is missing without strong context. Omissions therefore function rhetorically by narrowing the space of interpretations and reducing the chance that alternative explanations will be considered.

**Mechanism:** Missing context and missing data reduce the viewer’s hypothesis set; the viewer then fills gaps using prior beliefs and conventions, which can align with (or diverge from) the implied story.

**Evidence:** The paper identifies “information access rhetoric” as a cluster of techniques where simplification through omission (for example, variable selection, thresholding, and ambiguity in definitions) materially shapes interpretation [@hullmanVisualizationRhetoricFraming2011a]. It also notes that knowledge assumptions and omitted provenance can make implied propositions necessary for decoding the intended message [@hullmanVisualizationRhetoricFraming2011a].

**Notes:** Omissions can be desirable for clarity, but still have directional effects.

## When omission-awareness applies <!-- role: context -->

- **User Goal:** Decide what the data supports and what it does not.
- **Task:** Evaluate completeness, fairness, or robustness of a narrative claim.
- **Data:** Rich datasets where multiple variables, ranges, or subgroup definitions are possible.
- **Chart Setting:** Any explanatory chart, infographic, or scrollytelling piece.
- **Audience:** Viewers likely to assume the display is comprehensive unless told otherwise.
- **Success Criterion:** Viewers can distinguish “not shown” from “does not exist.”

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization’s purpose is intentionally narrow and explicitly stated as such (for example, a focused single-metric explainer with clear scope). **Why:** The rhetorical risk from omission is reduced when scope is explicit and accepted.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space and attention for stating scope and definitions. **Risk:** Overloading the presentation with caveats can reduce engagement. **Mitigation:** Keep omission disclosure scoped to what would plausibly change the main interpretation.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using axis thresholding or filtering without signaling what range or subset was excluded. **Why it fails:** Viewers may infer stronger differences or cleaner trends than warranted.
- **Mistake:** Leaving category membership ambiguous (for example, overlapping demographic definitions) in a way that enables multiple incompatible readings. **Why it fails:** Viewers may select the reading that best fits their priors.

## Quick tests <!-- role: check -->

**Failure Sign:** A reasonable viewer could ask “Compared to what else?” or “Who is included?” and the visualization cannot answer from what is shown.\
**Quick Check:** List three plausible alternative variables/ranges/definitions; if any would change the takeaway, the omission is rhetorically significant.\
**Stronger Test:** Show the visualization to a colleague and ask what they assume was excluded.

## What to do instead <!-- role: fix -->

- Add a concise scope statement describing what is included and excluded.
- Define ambiguous categories where overlap could change interpretation.
- Annotate where data was thresholded, aggregated, or filtered by default.
- Provide a path (link, menu, or note) to the omitted context when it is likely to affect conclusions.
