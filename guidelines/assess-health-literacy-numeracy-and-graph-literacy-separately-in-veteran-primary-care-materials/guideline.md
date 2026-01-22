---
id: assess-health-literacy-numeracy-and-graph-literacy-separately-in-veteran-primary-care-materials
title: Assess health literacy, numeracy, and graph literacy separately when designing
  materials for veterans in primary care
bibliography: references.bib
description: Treat health literacy, numeracy, and graph literacy as distinct user
  capabilities when designing or selecting patient-facing materials for veterans.
labels:
- chart:any
- task:communicate-risk
- visual:any
- impact:accessibility
- data:any
- audience:patient
- population:veterans
---

## Use separate screens for literacy, numeracy, and graph literacy needs <!-- role: advice -->

Assess and design for health literacy, numeracy, and graph literacy as separate constraints rather than assuming strength in one implies strength in the others.

## Why separating literacy, numeracy, and graph literacy improves fit <!-- role: reason -->

Different patient-facing materials rely on different skills (reading/comprehension, manipulating numbers, and interpreting graphs), so treating them as one “literacy” variable can hide mismatches between what a material demands and what users can do.

**Mechanism:** Separating capabilities reduces the chance that a visually or numerically demanding display is given to people who can read the text but cannot reliably extract meaning from numbers or graphs (or vice versa).

**Evidence:** In a veteran primary-care sample, health literacy, objective numeracy, and graph literacy were related but not identical, with only moderate-to-strong correlations rather than equivalence (e.g., health literacy with objective numeracy; graph literacy with objective numeracy) [@rodriguezHealthLiteracyNumeracy2013]. The same sample showed substantial prevalence of inadequate health literacy alongside lower numeracy and graph literacy among those with inadequate health literacy [@rodriguezHealthLiteracyNumeracy2013].

**Notes:** This guideline is about scoping and requirements: what skill a specific chart or handout requires should be treated explicitly.

## When this applies in patient education and decision support <!-- role: context -->

- **User Goal:** Understand health information well enough to make or participate in a care decision.
- **Task:** Interpret quantities (probabilities, counts, dosages) and/or interpret a graphical display.
- **Data:** Quantitative health information, especially probabilities, frequencies, or comparisons.
- **Chart Setting:** Patient education handouts, after-visit summaries, shared decision-making aids, clinic kiosks/portals.
- **Audience:** Veterans in primary care with mixed skill levels in reading, numeracy, and graph comprehension.
- **Success Criterion:** Users can correctly interpret the intended message from text, numbers, and any graphs.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The artifact contains no quantitative comparisons and no visual encodings (plain-language text only). **Why:** Numeracy and graph literacy demands are not present, so separating them adds no design value.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More upfront effort to map each artifact’s demands to distinct skills. **Risk:** Over-segmentation can complicate deployment if teams try to maintain too many versions. **Mitigation:** Keep the separation at the requirements level even if you ship one simplified version.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Treat “health literacy” as a single gate and assume graph comprehension follows from reading ability. **Why it fails:** The population shows distinct variation across health literacy, numeracy, and graph literacy rather than a single unified skill [@rodriguezHealthLiteracyNumeracy2013].
- **Mistake:** Validate only the wording of content and skip validating the numbers/graphs. **Why it fails:** Quantitative and graphical interpretation abilities vary and can be lower in important subgroups [@rodriguezHealthLiteracyNumeracy2013].

## Quick tests <!-- role: check -->

**Failure Sign:** Users can paraphrase the text but cannot answer simple “what does this number/graph imply?” questions. **Quick Check:** Ask users to extract one value and one comparison from the graph and to explain what it means in their own words. **Stronger Test:** Run a brief comprehension check that includes both numeric and graph questions, not just reading questions.

## What to do instead <!-- role: fix -->

- Inventory each patient-facing artifact and label whether it primarily demands reading comprehension, numeracy, graph interpretation, or a combination.
- Remove or replace graphical elements that require inference if the key message can be delivered without graph reading.
- Offer an alternative representation (text-only or number-only) for the same message when graph interpretation is not essential.
- Add a short comprehension prompt (e.g., one extraction question) as a lightweight check before relying on a graph for decision support.
