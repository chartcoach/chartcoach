---
id: choose-visualization-discipline-by-human-vs-computer-role-in-policy-modeling
title: "Choose information design, information visualization, semantics visualization,\
  \ visual analytics, or KDD based on human\u2013computer role"
bibliography: references.bib
description: Select visualization approaches for policy modeling by matching the needed
  balance of human judgment and automated computation.
labels:
- chart:framework
- task:select
- visual:interaction
- impact:clarity
- data:heterogeneous
- audience:expert
- domain:policy-modeling
- complexity:conceptual
---

## Select the visualization discipline by required automation versus human control <!-- role: advice -->

Choose among information design, information visualization, semantics visualization, visual analytics, and knowledge discovery in databases based on how much automated processing versus human interaction the policy task requires. Match the method to the transformation needed from data to insight.

## Why human–computer role matching improves method fit <!-- role: reason -->

Policy tasks range from communication-focused presentation to heavy automated discovery; mismatching methods can either overwhelm users with raw complexity or hide key judgment calls behind automation. A human–computer role spectrum clarifies when to emphasize communication, interactive exploration, semantic meaning, interactive algorithm steering, or largely automatic discovery.

**Mechanism:** Role-based selection reduces friction by aligning interaction burden and computational support to the task’s complexity and the user’s expertise.

**Evidence:** Visualization methodologies for policy modeling are categorized as information design, information visualization, semantics visualization, visual analytics, and knowledge discovery in databases, ordered by increasing computer role and decreasing human role [@kohlhammerVisualizationPolicyModeling2012].

**Notes:** Semantics visualization is highlighted as especially relevant due to growing semantically annotated and linked government data.

## When role-based selection applies <!-- role: context -->

- **User Goal:** Decide how to support a specific policy activity with visualization and analysis.
- **Task:** Communicate essentials; browse aggregated outcomes; explore semantic relations; steer complex algorithms; run automated extraction.
- **Data:** Heterogeneous sources, including linked data and semantically annotated datasets.
- **Chart Setting:** Tools ranging from static communication artifacts to interactive VA workbenches to automated pipelines.
- **Audience:** Mixed stakeholders with heterogeneous skills, knowledge, and preferences.
- **Success Criterion:** Appropriate balance of transparency, control, and computational power for the task.

## When not to use the role spectrum <!-- role: exceptions -->

**Break it when:** The task is strictly constrained to one mandated method (for example, an existing automated pipeline with fixed outputs). **Why:** Method choice is not available, so the spectrum cannot guide selection.

## Tradeoffs and risks of role-based selection <!-- role: costs -->

**Sacrifice:** Upfront effort to map tasks to roles and capabilities. **Risk:** Over-emphasizing automation can reduce user understanding; over-emphasizing manual control can overload users. **Mitigation:** Reassess role balance as the process moves from foraging to design to impact analysis.

## Common failures in method selection <!-- role: mistakes -->

**Mistake:** Using a single visualization approach for every stage and task. **Why it fails:** Policy modeling spans communication, exploration, semantic understanding, and complex analysis with different role needs.

## Quick tests for correct method fit <!-- role: check -->

**Failure Sign:** Users either cannot act because the system is too automated, or cannot keep up because the system is too manual. **Quick Check:** Identify whether the task’s bottleneck is computation or interpretation, then verify the chosen method supports that bottleneck. **Stronger Test:** Observe a stakeholder session and confirm the tool matches their required level of control and expertise.

## What to do instead when the method fit is unclear <!-- role: fix -->

- Prototype two approaches at different points on the human–computer spectrum and compare stakeholder usability.
- Add interaction points that let users influence automated steps if visual analytics is needed.
- If semantics is central, introduce a semantic layer and views that expose relations and dependencies.
- If communication is central, prioritize information design artifacts over exploratory tooling.
