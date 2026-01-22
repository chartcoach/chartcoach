---
id: scope-evaluation-to-10-analytic-tasks
title: Scope visualization requirements and evaluations to the ten low-level analytic
  tasks
bibliography: references.bib
description: Use a shared checklist of ten low-level analytic tasks to specify, compare,
  and evaluate visualization support for analytic activity.
labels:
- chart:general
- task:evaluate
- visual:interaction
- impact:clarity
- data:multivariate
- audience:designer
- complexity:foundational
---

## Use the ten-task checklist as your evaluation substrate <!-- role: advice -->

Define and assess your visualization by explicitly checking support for these ten analytic tasks: Retrieve Value, Filter, Compute Derived Value, Find Extremum, Sort, Determine Range, Characterize Distribution, Find Anomalies, Cluster, and Correlate.

## Why a shared set of analytic primitives improves design evaluation <!-- role: reason -->

Using a small, concrete set of low-level analytic tasks provides a common vocabulary for describing what analytic activity a visualization supports, independent of system-specific interactions (such as zoom). This shifts evaluation from representation features toward whether users can complete the analytic questions they actually pose, and makes capability gaps visible as missing task support rather than vague usability issues.

**Mechanism:** A stable checklist anchors requirements and comparisons in user goals (“answer this kind of question”) instead of interface mechanics, making analytic affordances explicit and comparable across tools.

**Evidence:** A corpus of 196 user-generated analysis questions clustered into ten recurring low-level task types that captured the majority of concrete analytic inquiries made while using information visualization tools [@amarLowlevelComponentsAnalytic2005]. The ten tasks are proposed as a common substrate and informal checklist for discussing and evaluating analytic capabilities of visualization systems [@amarLowlevelComponentsAnalytic2005].

**Notes:** The task list is intentionally system-agnostic and focuses on analytic desires rather than operations like zoom or pan.

## When this ten-task substrate should drive requirements <!-- role: context -->

- **User Goal:** Understand a dataset by answering concrete analytic questions rather than only viewing a representation.
- **Task:** Specify, compare, or evaluate what an information visualization system enables analytically.
- **Data:** Case–attribute tables with multiple variables; may include quantitative, categorical, and temporal attributes.
- **Chart Setting:** Any visualization tool or technique where interaction and views are meant to support analysis.
- **Audience:** Visualization system designers, evaluators, researchers, and practitioners selecting tools.
- **Success Criterion:** Users can reliably complete most question types they naturally ask about the dataset.

## When not to rely on only these ten tasks <!-- role: exceptions -->

**Break it when:** Your primary target is higher-level exploratory sensemaking (e.g., open-ended hypothesis formation or uncertain, value-laden judgments like “best customers” without operational criteria). **Why:** The ten tasks target concrete, low-level inquiries and do not fully cover underspecified criteria or broad “find what matters” exploration.

## Tradeoffs of using a fixed analytic-task checklist <!-- role: costs -->

**Sacrifice:** You may under-specify higher-level reasoning workflows by focusing on low-level question types. **Risk:** Teams may treat the checklist as exhaustive and miss domain-specific tasks not captured in the ten types. **Mitigation:** Treat the list as a baseline substrate and explicitly note any additional domain tasks needed.

## Common ways teams misuse the checklist <!-- role: mistakes -->

**Mistake:** Replacing analytic tasks with system operations (e.g., “supports zoom/filter/history” as the requirements). **Why it fails:** It describes interface mechanics rather than whether users can answer core analytic questions like finding anomalies or characterizing distributions.

## Quick ways to tell whether you applied this correctly <!-- role: check -->

**Failure Sign:** You can describe interactions and views, but you cannot state which of the ten analytic tasks the system supports well or poorly. **Quick Check:** For each of the ten tasks, write one dataset-specific question and verify the system can answer it end-to-end. **Stronger Test:** Use representative users to attempt those questions and record where task completion breaks down.

## What to do instead when the checklist reveals gaps <!-- role: fix -->

- Add explicit features that support missing tasks (e.g., anomaly identification or distribution characterization) rather than only adding more chart types.
- Reframe requirements in the form of user questions and map each question to one or more of the ten tasks.
- Compare candidate tools by rating their support for each of the ten tasks using the same dataset and question set.
- Document compound questions as compositions of tasks (e.g., Compute Derived Value then Sort) so you can test multi-step analytic activity.
