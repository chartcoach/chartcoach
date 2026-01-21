---
id: optimize-cognitive-fit-to-task
title: Choose the Visualization That Minimizes Mental Transformations for the Task
bibliography: references.bib
description: "Select displays that directly support the user\u2019s task so they don\u2019\
  t need working-memory-heavy transformations."
labels:
- chart:general
- task:choose
- visual:encoding
- impact:efficiency
- data:general
- audience:general
- concept:cognitive-fit
- mechanism:type-2
---

## The Rule <!-- role: advice -->

Pick (or redesign) the visualization so the answer can be read off directly for the intended task, not computed via extra steps.

## The Logic <!-- role: reason -->

The review synthesizes evidence for cognitive fit: when the visualization does not match the task, people must use working memory to perform corrective transformations, increasing time and error—especially for those with lower working memory capacity [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Tasks like compare, identify extremes, find differences, select best route/option, or disconnect critical nodes
- **Data Type:** Any dataset where multiple representations are possible (tables vs graphs; network layouts; map views)
- **Audience:** Broad audiences, particularly where working memory limits matter

## When to Break It <!-- role: exceptions -->

- **Scenario:** Multi-goal dashboards where one view must serve several different tasks
- **Reason:** A single view can’t be maximally fit for all tasks; tradeoffs are unavoidable [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Flexibility and compactness; you may need multiple views for multiple tasks
- **The Risk:** Over-optimizing for one task can hide information needed for another [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing the most familiar or visually impressive format instead of the most task-aligned
- **Why it fails:** Familiarity and aesthetics can bias selection even when performance is worse [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users have to repeatedly switch attention, compute intermediate values, or translate encodings before answering.
- **The Test:** List the steps required to answer the core question; if it requires many transformations, cognitive fit is likely poor [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap to a representation known (in your context) to better match the task (e.g., map vs table; alternate network layout).
- **Best Fix:** Provide task-specific views or interactions so each key task has a high-fit representation [@padillaDecisionMakingVisualizations2018].
