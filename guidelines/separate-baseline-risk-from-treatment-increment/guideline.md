---
id: separate-baseline-risk-from-treatment-increment
title: Separate Baseline Risk from Treatment-Added Risk
bibliography: references.bib
description: Show baseline risk first, then highlight the additional (incremental)
  risk caused by treatment to prevent misattribution.
labels:
- task:compare
- task:explain
- chart:pictograph
- visual:color
- impact:clarity
- impact:fairness
- audience:novice
- data:risk
- domain:health
- source:fagerlinHelpingPatientsDecide2011
---

## The Rule <!-- role: advice -->

Distinguish baseline risk from the incremental risk due to treatment; do not present only the total risk in the treatment group.

## The Logic <!-- role: reason -->

If you show only total risk under treatment, patients may incorrectly attribute all of that risk to the treatment; separating baseline from incremental risk reduces mistaken attribution and can reduce worry and perceived likelihood of side effects (especially when combined with pictographs).

- **The Principle:** Prevent causal misattribution in risk interpretation
- **The Evidence:** Patients may misread total risk as treatment-caused; incremental risk framing (baseline + added risk) reduced worry and perceived likelihood when paired with pictographs [@fagerlinHelpingPatientsDecide2011].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand what risk exists anyway vs what risk is added by a therapy.
- **Data Type:** Side effects or complications that also occur without treatment (baseline incidence).
- **Audience:** Patients evaluating whether harms are “caused by” treatment.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the paper.
- **Reason:** Not specified.

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires extra explanation and/or more visual elements (e.g., two-step display).
- **The Risk:** Confusion if the incremental approach is not clearly visualized; the paper notes knowledge benefits required combining this approach with pictographs [@fagerlinHelpingPatientsDecide2011].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting “70% risk with drug” without showing how much risk exists without the drug.
- **Why it fails:** Patients may assume the drug solely caused the risk [@fagerlinHelpingPatientsDecide2011].
- **The Wrong Fix:** Showing baseline and treated risks as two unrelated numbers without highlighting the added portion.
- **Why it fails:** It doesn’t clearly communicate “what changed” due to treatment [@fagerlinHelpingPatientsDecide2011].

## How to Check <!-- role: check -->

- **Visual Sign:** Only one figure for the treated group; no baseline comparator; no “additional” segment.
- **The Test:** Ask, “Can the reader tell how much of the risk is present without treatment?” If not, the display fails.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the baseline risk next to the treatment risk and explicitly label “additional risk due to treatment.”
- **Best Fix:** Use a pictograph that first shows baseline risk, then adds a distinct color to represent incremental risk (as in the paper’s example) [@fagerlinHelpingPatientsDecide2011].
