---
id: minimize-changes-between-consecutive-views
title: Minimize Attribute Changes Between Consecutive Visualizations
bibliography: references.bib
description: Keep consecutive narrative-visualization states similar by changing as
  few data attributes as possible per step.
labels:
- task:sequence
- impact:clarity
- impact:comprehension
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Change only one key data attribute at a time between consecutive visualizations (e.g., time **or** measure **or** dimension **or** granularity), keeping the others constant.

## The Logic <!-- role: reason -->

Explainability and perceived fit between consecutive views improves when the audience can infer a connection with minimal “transformation cost” between states.

- **The Principle:** Maintaining consistency via low transition (transformation) cost
- **The Evidence:** The paper formalizes transformation cost as the number of attribute changes between states and finds strong user preference for lower-cost transitions in pairwise choices [@hullmanDeeperUnderstandingSequence2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Follow a linear narrative across multiple charts (e.g., slideshow-style storytelling)
- **Data Type:** Multivariate data where time, dimensions, measures, and hierarchical levels can vary
- **Audience:** General audiences and mixed-expertise groups

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intend a deliberate “jump cut” to signal a new episode/topic in the story.
- **Reason:** The paper’s rule targets smooth state-to-state comprehension; a hard shift may be rhetorically intentional even if costlier [@hullmanDeeperUnderstandingSequence2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need more slides/steps to reach your destination view.
- **The Risk:** The sequence can feel slow or repetitive if overused.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Changing time, measure, and grouping all at once in the next slide.
- **Why it fails:** It increases transformation cost, which the audience is less likely to prefer as an immediate next step [@hullmanDeeperUnderstandingSequence2013].

## How to Check <!-- role: check -->

- **Visual Sign:** View-to-view, multiple encodings/axes/categories/filters change simultaneously.
- **The Test:** For each transition, list what changed among {time, independent dimension, dependent measure, granularity}; if more than one changed, you likely violated the rule.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Insert an intermediate slide that changes only one attribute.
- **Best Fix:** Re-plan the sequence as a path where each consecutive pair differs on a single attribute, matching the paper’s transition types and low-cost objective [@hullmanDeeperUnderstandingSequence2013].
