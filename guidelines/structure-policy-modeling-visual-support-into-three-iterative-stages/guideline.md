---
id: structure-policy-modeling-visual-support-into-three-iterative-stages
title: Structure Visual Support into Three Iterative Policy-Modeling Stages
bibliography: references.bib
description: Organize visualization work around information foraging, policy design,
  and impact analysis as an iterative loop.
labels:
- task:plan
- task:analyze
- impact:decision-making
- data:heterogeneous
- audience:policymaker
- domain:policy-modeling
---

## The Rule <!-- role: advice -->

Organize policy-modeling visualization into three iterative stages: information foraging, policy design, and impact analysis, and design the visuals as a loop between them.

## The Logic <!-- role: reason -->

A staged model ensures the visualization system supports distinct needs: (1) finding and relating evidence, (2) aligning requirements and topics during creation, and (3) evaluating and improving outcomes. The paper argues policy modeling needs “topic-related, problem-specific” presentation across stages to prevent overload and enable understanding and alternatives [@kohlhammerVisualizationPolicyModeling2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Moving from problem understanding → drafting/revising a policy → evaluating impact and refining.
- **Data Type:** Heterogeneous sources (statistics, linked data, opinions, simulations).
- **Audience:** Policy analysts and decision-makers in public policy workflows.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single-purpose, one-off communication artifact (for example, a static briefing graphic for a single meeting).
- **Reason:** The three-stage loop presumes an ongoing modeling workflow rather than a standalone deliverable.

## The Price <!-- role: costs -->

- **The Sacrifice:** More design effort to create consistent handoffs between stages.
- **The Risk:** Over-engineering the process when the policy task is small or time-boxed.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Building one generic dashboard for all policy tasks.
- **Why it fails:** It doesn’t match stage-specific needs (evidence exploration vs. requirement alignment vs. impact evaluation) highlighted by the staged model [@kohlhammerVisualizationPolicyModeling2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users use the same view for searching evidence, authoring policy requirements, and evaluating scenarios without clear transitions.
- **The Test:** Ask users to map each screen to one stage; if most screens map to “everything,” the design is not staged.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Label existing views by stage and add stage-specific entry points (Forage / Design / Impact).
- **Best Fix:** Re-architect the UI so each stage has purpose-built views and outputs that feed the next stage in a loop [@kohlhammerVisualizationPolicyModeling2012].
