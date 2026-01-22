---
id: minimize-attribute-changes-between-consecutive-visualizations
title: Minimize changes in data attributes between consecutive visualizations
bibliography: references.bib
description: Reduce cognitive load in narrative visualization by limiting how many
  data attributes change from one slide to the next.
labels:
- chart:multi
- task:sequence
- visual:layout
- impact:clarity
- data:multivariate
- audience:general
- complexity:intermediate
---

## Minimize consecutive-slide attribute changes <!-- role: advice -->

When moving from one visualization to the next, change as few of these attributes as possible at a time: independent variable, dependent variable (measure), time, and level of granularity (filtering/detail).

## Attribute-consistency reduces perceived transition difficulty <!-- role: reason -->

Keeping most attributes constant across a transition preserves continuity and makes it easier for viewers to relate the two states as part of one story, instead of re-parsing a new view from scratch.

**Mechanism:** Fewer concurrent changes reduce the conceptual “distance” viewers must bridge to understand what differs and what stays the same across slides.

**Evidence:** In forced-choice sequencing judgments, viewers strongly preferred lower “transformation cost” transitions (fewer attribute changes) over higher-cost transitions, indicating that minimizing changes is perceived as better sequencing [@hullmanDeeperUnderstandingSequence2013].

**Notes:** The paper operationalizes “cost” as the count of attribute changes needed to transform one visualization state into the next.

## Applies when building linear narrative sequences from multiple views <!-- role: context -->

- **User Goal:** Follow a linear story across multiple visualizations without losing the thread.
- **Task:** Understand how a dataset changes across slides and make comparisons across adjacent states.
- **Data:** A set of related views that vary by measure, dimension, time, or aggregation/filter level.
- **Chart Setting:** Slideshow-style or step-based interactive narrative with “Next/Previous” progression.
- **Audience:** Mixed literacy audiences, including non-experts.
- **Success Criterion:** Viewers can explain what changed between slides quickly and correctly.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The story requires a deliberate “jump” to introduce a new phase or topic. **Why:** The narrative goal may prioritize contrast or surprise over continuity.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Slower narrative progression because you may need more slides to reach a distant point. **Risk:** Overuse can feel repetitive if too little changes for too long. **Mitigation:** Use the smallest number of slides that still keep each transition simple.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Changing time, measure, and the compared group all at once between two slides. **Why it fails:** Viewers must disentangle multiple simultaneous differences, increasing perceived transition difficulty.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers cannot summarize the difference between two adjacent slides in one short sentence. **Quick Check:** For any adjacent pair, count how many of {dimension, measure, time, granularity} changed; if more than one changed, treat it as risky. **Stronger Test:** Show two adjacent slides to a pilot viewer and ask “what changed?”; if they mention the wrong attribute, the transition is likely too costly.

## Fix: What to do instead <!-- role: fix -->

- Insert an intermediate slide that changes only one attribute before introducing the next change.
- Keep the same independent variable while you change only the measure (or vice versa), rather than changing both together.
- Keep time constant while introducing a new breakdown (dimension) before moving time forward/backward.
- Adjust filtering/aggregation in its own step before switching measures or dimensions.
