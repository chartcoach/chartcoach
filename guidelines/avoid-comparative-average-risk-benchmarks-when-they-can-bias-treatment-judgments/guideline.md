---
id: avoid-comparative-average-risk-benchmarks-when-they-can-bias-treatment-judgments
title: Avoid adding average-risk comparisons when they can bias judgments about treatment
  effectiveness
bibliography: references.bib
description: Comparative risk information can be persuasive and distort treatment
  judgments; use it cautiously or omit it.
labels:
- chart:none
- task:interpret
- visual:text
- impact:trust
- data:probabilistic
- audience:novice
- domain:healthcare
---

## Use comparative “average risk” information sparingly because it can persuade <!-- role: advice -->

Do not include “average person” risk comparisons by default when presenting a patient’s risks and options, especially if the comparison could shift judgments about how effective a treatment is.

## Comparative benchmarks can change interpretation, not just inform it <!-- role: reason -->

Comparative risk frames provide a salient standard that can alter worry and decisions, potentially pulling attention away from the absolute benefit–harm tradeoff that should drive preference-sensitive choices.

**Mechanism:** People interpret their risk through relative standing (“higher than average” or “lower than average”), which can bias evaluations of interventions even when the absolute risk reduction is unchanged.

**Evidence:** Comparative risk perceptions often predict worry and behavior, and presenting above- vs below-average risk information can increase perceived medication effectiveness and endorsement despite equal absolute risk reduction [@fagerlinHelpingPatientsDecide2011].

**Notes:** Comparative information may feel helpful, but it functions as a persuasive frame.

## When this caution applies <!-- role: context -->

- **User Goal:** Decide whether an intervention’s benefits outweigh its harms.
- **Task:** Evaluate treatment effectiveness and decide whether to act.
- **Data:** Personalized absolute risk estimates and optional benchmark (population average) risk.
- **Chart Setting:** Decision aids for screening, prevention, or treatment where baseline risk varies across people.
- **Audience:** Patients likely to interpret “above average” as a cue to act.
- **Success Criterion:** Choices are based on the patient’s own absolute benefits and harms, not their rank vs others.

## When not to follow it <!-- role: exceptions -->

**Break it when:** A benchmark is necessary for users to interpret what a single absolute number means and no other interpretive aid is feasible. **Why:** Some users cannot evaluate an isolated probability without a reference point.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Without benchmarks, some users may feel unsure how to interpret a number emotionally. **Risk:** Removing comparisons can reduce perceived relevance. **Mitigation:** Emphasize the absolute benefit–harm balance for the patient’s decision instead of rank-based messaging.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Presenting “you are higher than average risk” as a prominent callout near treatment recommendations. **Why it fails:** It can bias perceived effectiveness and push action independent of absolute benefit.

## Quick tests <!-- role: check -->

**Failure Sign:** Users justify the decision mainly by saying they are above or below average. **Quick Check:** Remove the benchmark and see whether the decision rationale shifts to absolute benefits/harms. **Stronger Test:** In a pilot, test versions with and without comparative risk and look for changes in perceived treatment effectiveness.

## What to do instead <!-- role: fix -->

- Focus the display on the patient’s absolute risks with and without the intervention.
- If a reference is needed, use within-option baselines (baseline vs treated) rather than population averages.
- Prompt users to compare benefits and harms directly for their situation.
- Keep any benchmark information visually de-emphasized relative to absolute risk changes.
