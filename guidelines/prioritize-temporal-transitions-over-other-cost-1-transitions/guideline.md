---
id: prioritize-temporal-transitions-over-other-cost-1-transitions
title: Prefer temporal transitions over other single-change transitions when cost
  is equal
bibliography: references.bib
description: If two possible next slides each change only one attribute, choose a
  time-step transition first when it fits the story.
labels:
- chart:multi
- task:sequence
- visual:position
- impact:clarity
- data:temporal
- audience:general
- complexity:intermediate
---

## Use time steps as the default single-change transition when possible <!-- role: advice -->

When multiple candidate next slides each differ from the current slide by only one attribute, prefer a temporal (time-based) transition if a meaningful time variable is available.

## Viewers systematically favor time progression as a next-step logic <!-- role: reason -->

Time provides a widely understood organizing principle that makes the relationship between consecutive slides easy to infer without extra explanation.

**Mechanism:** Temporal ordering provides an intuitive continuity cue that helps viewers interpret consecutive views as successive states of the same phenomenon.

**Evidence:** In cost-constant comparisons (all transitions cost 1), temporal transitions were preferred over granularity, dimension-walk, and measure-walk transitions in participants’ “best next slide” choices [@hullmanDeeperUnderstandingSequence2013].

**Notes:** The study did not separate temporal subtypes (e.g., forward vs reverse time) in the preference analysis.

## Context: When time is present and the story can be told as change over time <!-- role: context -->

- **User Goal:** Understand evolution or progression in the data story.
- **Task:** Compare adjacent states as successive time points.
- **Data:** A recognizable time variable (year, date, period) across multiple views.
- **Chart Setting:** Linear guided narrative where “next” implies continuation.
- **Audience:** General audiences who benefit from common narrative structures.
- **Success Criterion:** Viewers can predict what the next slide will change (time) and track trends.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The intended message is a cross-sectional comparison rather than change over time. **Why:** A temporal step can distract from the key contrast the story is trying to establish.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Other useful organizing logics (e.g., comparing groups or measures) may be delayed. **Risk:** Over-temporal sequencing can feel mechanical if time is not central to the narrative. **Mitigation:** Use temporal steps only when they advance the narrative claim.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Forcing time steps even when the time differences are not meaningful for the story. **Why it fails:** Viewers may infer an unwarranted “trend narrative” and miss the real point.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask why the story is moving through time at all. **Quick Check:** Ask whether “what changed?” can be answered as “the time period” without qualifiers. **Stronger Test:** Compare two candidate sequences (temporal-first vs comparison-first) and ask viewers which is easier to follow.

## Fix: What to do instead <!-- role: fix -->

- Use a dimension-walk transition when the story’s primary contrast is between groups at a fixed time.
- Use a measure-walk transition when the story’s primary contrast is multiple outcomes for the same entities.
- Use a granularity transition when the story’s primary contrast is overview versus detail.
- Provide framing text that makes the organizing principle explicit if you cannot use time as the ordering cue.
