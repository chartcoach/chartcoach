---
id: separate-system-interactions-from-analytic-tasks
title: Describe requirements in analytic tasks rather than system-specific interactions
bibliography: references.bib
description: Keep task descriptions system-agnostic by stating the analytic goal (e.g.,
  filter, correlate) instead of interface actions (e.g., zoom).
labels:
- chart:general
- task:requirements
- visual:interaction
- impact:portability
- data:multivariate
- audience:designer
- custom:system-agnostic
---

## State analytic goals without embedding interface operations <!-- role: advice -->

Write requirements and evaluations in terms of the analytic tasks users need to complete, not in terms of tool actions such as zooming or other system-specific operations.

## Why system-agnostic task framing improves comparability <!-- role: reason -->

Interface operations are implementation choices and vary across tools, while analytic tasks capture what users are trying to learn from data. When requirements are written as operations, teams can build feature-complete interfaces that still fail to support core analytic activity; when written as analytic tasks, teams can compare different representations and interactions by whether they enable the intended inquiries.

**Mechanism:** Task-level descriptions preserve intent while allowing multiple interface realizations, making it easier to reason about coverage and gaps across systems.

**Evidence:** A set of ten low-level analytic tasks is intentionally defined without system-specific operations (e.g., excluding “zoom”) to focus on user goals independent of particular visualization paradigms [@amarLowlevelComponentsAnalytic2005]. The tasks are proposed as a vocabulary for discussing and evaluating analytic capabilities of information visualization systems [@amarLowlevelComponentsAnalytic2005].

**Notes:** Operations like “filter” are included only when framed as an analytic desire (finding cases meeting conditions), not as a particular UI gesture.

## Where this separation matters most <!-- role: context -->

- **User Goal:** Select, design, or compare visualization systems based on analytic capability.
- **Task:** Requirements writing, evaluation criteria creation, or cross-tool benchmarking.
- **Data:** Any dataset where users will perform lookups, subset selection, aggregation, ranking, distribution reading, anomaly finding, clustering, or correlation.
- **Chart Setting:** Multi-view dashboards, interactive visual analytics tools, or any system with multiple possible interactions.
- **Audience:** Designers, evaluators, procurement teams, and researchers.
- **Success Criterion:** Requirements remain valid even if the UI paradigm changes.

## When interface-operation requirements can be acceptable <!-- role: exceptions -->

**Break it when:** You are documenting a fixed UI for implementation or training where the interaction itself is the deliverable. **Why:** In those cases, the system operation is part of the product specification rather than a proxy for analytic intent.

## Tradeoffs of avoiding UI-language in requirements <!-- role: costs -->

**Sacrifice:** You may need additional mapping work from analytic tasks to concrete UI features. **Risk:** Stakeholders may feel requirements are “too abstract” without specifying interactions. **Mitigation:** Pair each analytic task requirement with an example user question and acceptance test.

## Common mistakes when trying to be system-agnostic <!-- role: mistakes -->

**Mistake:** Listing generic interaction features and assuming they imply analytic support (e.g., “has filtering, zoom, details-on-demand”). **Why it fails:** The presence of interactions does not guarantee that users can complete tasks like characterizing distributions or finding anomalies.

## Quick checks for system-agnostic task descriptions <!-- role: check -->

**Failure Sign:** Removing the tool name from the requirement makes the statement meaningless. **Quick Check:** Replace every UI verb (zoom, pan, click) with the intended task verb (filter, retrieve, compute) and see if the requirement still reads correctly. **Stronger Test:** Validate that each requirement maps to at least one of the ten analytic tasks and has a pass/fail user-question test.

## What to do instead when stakeholders demand UI specifics <!-- role: fix -->

- Write the requirement as an analytic task first, then add a separate implementation note listing candidate interactions.
- Use dataset-specific questions as acceptance tests for each task rather than specifying gestures.
- Document compound tasks explicitly as sequences so UI choices can be optimized per step.
- If an interaction is essential, justify it by the analytic task it enables and test that task directly.
