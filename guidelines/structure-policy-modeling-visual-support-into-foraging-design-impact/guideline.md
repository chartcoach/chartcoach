---
id: structure-policy-modeling-visual-support-into-foraging-design-impact
title: Structure policy-modeling visual support into information foraging, policy
  design, and impact analysis
bibliography: references.bib
description: Organize visualization work in policy modeling around three iterative
  stages to align methods with needs.
labels:
- chart:workflow
- task:plan
- visual:layout
- impact:clarity
- data:heterogeneous
- audience:expert
- domain:policy-modeling
- complexity:conceptual
---

## Structure visual work by the three-stage policy-modeling loop <!-- role: advice -->

Structure visualization support around iterative stages of information foraging, policy design, and impact analysis. Keep the stages connected so insights from later stages can update earlier ones.

## Why stage-based structuring improves policy visualization use <!-- role: reason -->

A stage model makes it explicit that different points in policy modeling require different kinds of visual access to heterogeneous information, from exploring and relating issues, to ensuring requirements coherence, to evaluating impacts. This creates a stable scaffold for selecting and integrating visualization with analysis methods instead of treating visualization as a one-off postprocessing step.

**Mechanism:** Stage separation reduces “one visualization fits all” mismatches by mapping distinct user intents (explore → compose → evaluate) to distinct visual and analytic needs.

**Evidence:** A simplified policy-modeling process is defined as three iterative stages—information foraging, policy design, and impact analysis—each requiring visualization to handle heterogeneous sources and support understanding of problems and alternatives [@kohlhammerVisualizationPolicyModeling2012].

**Notes:** The stages are iterative; the process is explicitly described as a loop.

## When the three-stage structuring applies <!-- role: context -->

- **User Goal:** Define a policy need, create/revise a policy, and evaluate its potential or actual effects.
- **Task:** Explore relationships and issues; align topics and requirements; compare scenarios and performance.
- **Data:** Heterogeneous sources, including statistics, linked open government data, opinions, and simulation outputs.
- **Chart Setting:** Interactive systems supporting exploration, authoring, and evaluation across iterations.
- **Audience:** Policy analysts and policy makers with varying expertise in analytic methods.
- **Success Criterion:** Reduced overwhelm from too much data; better understanding of problems and alternative solutions.

## When not to follow this stage structure <!-- role: exceptions -->

**Break it when:** The work is limited to communicating a single already-set decision without exploration or evaluation. **Why:** The three-stage loop targets iterative modeling and analysis rather than one-way presentation.

## Tradeoffs and risks of stage-based structuring <!-- role: costs -->

**Sacrifice:** Additional design overhead to maintain continuity and handoffs between stages. **Risk:** Artificially forcing tasks into stages can hide cross-cutting questions that span foraging, design, and impact. **Mitigation:** Allow iteration and backtracking as first-class actions.

## Common ways stage-based policy visualization fails <!-- role: mistakes -->

**Mistake:** Treating visualization as only an after-the-fact reporting layer. **Why it fails:** It prevents interactive sense-making across heterogeneous data during definition, design, and evaluation.

## Quick tests for correct stage coverage <!-- role: check -->

**Failure Sign:** Users can view results but cannot explore relations, shape a design, or evaluate impacts within the same workflow. **Quick Check:** Verify there is at least one visualization interaction supporting each of foraging, design, and impact analysis. **Stronger Test:** Walk through one policy question end-to-end and confirm insights can feed back to earlier steps.

## What to do instead when stage structuring is hard <!-- role: fix -->

- Provide separate views or modes labeled by foraging, design, and impact goals.
- Add a mechanism to carry findings forward (for example, saving entities, assumptions, or scenarios between stages).
- Introduce an explicit iteration control that lets users return to earlier stages without losing context.
- If only one stage is feasible, narrow the product scope to that stage and remove implied support for the others.
