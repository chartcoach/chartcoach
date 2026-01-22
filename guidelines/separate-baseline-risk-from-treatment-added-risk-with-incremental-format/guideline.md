---
id: separate-baseline-risk-from-treatment-added-risk-with-incremental-format
title: Separate baseline risk from treatment-added risk using an incremental risk
  format
bibliography: references.bib
description: Show baseline risk first, then visually add the incremental risk attributable
  to treatment to prevent attribution errors.
labels:
- chart:pictograph
- task:attribute
- visual:color
- impact:trust
- data:probabilistic
- audience:novice
- domain:healthcare
---

## Show baseline risk and incremental treatment risk as distinct parts <!-- role: advice -->

When communicating side effects or complications, present baseline risk separately and then add the incremental risk caused by treatment as an additional component, ideally in a pictograph.

## Incremental framing reduces mistaken causal attribution <!-- role: reason -->

If people see only the total risk in a treatment group, they may attribute all of it to the treatment, inflating perceived harm and worry; separating baseline from incremental risk clarifies what the intervention changes.

**Mechanism:** Distinct baseline and added components help viewers correctly assign causality and avoid treating preexisting risk as treatment-caused risk.

**Evidence:** Presenting side effect risk as baseline plus incremental risk, especially combined with pictographs, reduces worry and perceived likelihood of side effects compared with presenting total risk alone [@fagerlinHelpingPatientsDecide2011].

**Notes:** The incremental approach is most effective when paired with pictographs rather than text alone.

## When incremental risk displays apply <!-- role: context -->

- **User Goal:** Judge whether treatment harms are worth treatment benefits.
- **Task:** Attribute risk correctly to baseline vs treatment.
- **Data:** Baseline risk without intervention and total risk with intervention (so incremental difference is defined).
- **Chart Setting:** Decision aids and counseling where side effects overlap with common background symptoms.
- **Audience:** Patients likely to assume “treatment caused it” without explicit separation.
- **Success Criterion:** Users can state what portion of risk exists without treatment and what portion is added by treatment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Baseline risk is unknown or not meaningfully estimable for the patient group. **Why:** You cannot defensibly partition total risk into baseline plus incremental components.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires more explanation and often more space (two-step presentation). **Risk:** Poor color/legend choices can make the two components blend together. **Mitigation:** Keep the two components visually distinct and label them with matching text.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Showing only total side-effect risk for the treatment group. **Why it fails:** People may treat the entire risk as treatment-caused.
- **Mistake:** Presenting incremental risk in text but showing only total risk visually. **Why it fails:** The visual can dominate interpretation and undo the intended separation.

## Quick tests <!-- role: check -->

**Failure Sign:** Users say the treatment “causes” the full displayed risk. **Quick Check:** Ask “What would the risk be without treatment?” and see if the display supports a correct answer. **Stronger Test:** Compare user estimates of treatment-caused risk against the true incremental difference.

## What to do instead <!-- role: fix -->

- Show baseline risk in one display or layer before introducing treatment effects.
- Add a second distinct layer/color to represent only the additional cases due to treatment.
- Label the incremental portion explicitly as “additional risk caused by treatment.”
- If a graph is not possible, use two aligned frequency statements: baseline first, then baseline plus incremental.
