---
id: design-information-foraging-views-to-prevent-data-overload-with-topic-specific-structure
title: Present Foraging Data in a Topic-Specific, Problem-Specific Structure
bibliography: references.bib
description: Reduce overwhelm in policy information foraging by structuring heterogeneous
  sources around the policy topic and problem.
labels:
- task:explore
- task:sensemaking
- impact:clarity
- data:heterogeneous
- audience:analyst
- domain:policy-modeling
- stage:information-foraging
---

## The Rule <!-- role: advice -->

In information foraging, organize and visualize heterogeneous sources in a topic-related, problem-specific way that surfaces relations, circumstances, statistics, and policy issues.

## The Logic <!-- role: reason -->

The paper states that without visualization and interactive interfaces, handling heterogeneous sources is “complex and overwhelming because too much data is available,” and emphasizes providing information in a “topic-related, problem-specific way” so policy makers can understand the problem and alternatives [@kohlhammerVisualizationPolicyModeling2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine the need for a policy or a change by understanding evidence and relationships.
- **Data Type:** Mixed sources (open government linked data, statistical databases, other viewpoints/opinions).
- **Audience:** Policy analysts supporting agenda setting and early-stage policy definition.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users already know the precise variable and dataset needed and only require direct lookup.
- **Reason:** Exploratory structuring adds friction to targeted retrieval.

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “complete” raw-data exposure in the default view.
- **The Risk:** Over-curation may hide unexpected but relevant signals if filtering is too aggressive.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Dumping all available datasets into one undifferentiated catalog or dashboard.
- **Why it fails:** It recreates the “too much data” overwhelm the paper warns about [@kohlhammerVisualizationPolicyModeling2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must open many unrelated views to assemble basic context, or they abandon exploration.
- **The Test:** Time how long it takes a user to explain the core problem context and key relationships; if they can’t do it quickly, structure is missing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add topic-first navigation (policy issue → related measures → related sources) and relation highlights.
- **Best Fix:** Use linked/semantic connections to guide exploration and provide overview-to-detail workflows that expose relations between aspects and circumstances for the policy issue [@kohlhammerVisualizationPolicyModeling2012].
