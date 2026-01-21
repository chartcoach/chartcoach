---
id: make-chart-state-changes-easy-to-follow
title: Animate Meaningful Chart Changes With Object Constancy
bibliography: references.bib
description: "When chart data or state changes meaningfully, use object-constant transitions\
  \ (250ms\u20132s) and announce state changes to screen reader users."
labels:
- chart:interactive
- task:track-change
- visual:motion
- impact:clarity
- impact:accessibility
- data:dynamic
- audience:general
- accessibility:screen-reader
- principle:understandable
- source:chartability
---

## The Rule <!-- role: advice -->

When a chart’s data or state changes meaningfully, animate the transition to preserve object constancy (no faster than 250ms and no longer than 2s), and announce the state change to screen reader users [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016].

## The Logic <!-- role: reason -->

Animations that preserve object constancy make it easier to follow what changed by keeping a stable “identity” for marks across updates, rather than forcing users to re-interpret a new scene from scratch [@amr_structuring_and_2016]. Chartability frames this as an Understandable requirement because unclear updates increase cognitive load and ambiguity, and it also requires equivalent change information for screen reader users via announcements [@elavskyHowAccessibleMy2022].

- **The Principle:** Object constancy in chart updates
- **The Evidence:** [@amr_structuring_and_2016] [@elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

Use this when the visualization updates and the user needs to understand what changed.

- **User Goal:** Following changes in values, selections, filters, or system state across updates
- **Data Type:** Dynamic or interactive data views where chart marks or their values change
- **Audience:** Any audience, including screen reader users who need changes announced [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart’s data/state change is not meaningful
- **Reason:** Animating trivial changes adds unnecessary work and distraction without improving comprehension [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More implementation effort to build object-constant transitions and add screen reader announcements [@elavskyHowAccessibleMy2022].
- **The Risk:** If timing is poorly chosen (too fast/slow), updates may become harder to follow or frustrating [@amr_structuring_and_2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Re-rendering the chart instantly (no transition), causing marks to “jump” or appear as a new chart
- **Why it fails:** Users lose continuity and must rediscover what changed without object constancy [@amr_structuring_and_2016].
- **The Wrong Fix:** Animating outside the 250ms–2s range (e.g., extremely fast flashes or prolonged transitions)
- **Why it fails:** Too-fast transitions are hard to follow; too-long transitions frustrate users and slow comprehension [@amr_structuring_and_2016].
- **The Wrong Fix:** Updating visuals without announcing the change for screen reader users
- **Why it fails:** Non-visual users may not learn that state changed or what changed, creating an unequal and confusing experience [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Updates look like abrupt replacements (or sluggish, drawn-out animations) where it’s unclear which marks correspond across states.
- **The Test:** Trigger a meaningful update (e.g., filter/selection/state change) and verify (1) the transition duration is between 250ms and 2s and preserves mark identity, and (2) the change is announced to screen reader users [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a transition for meaningful updates and set its duration within 250ms–2s; add an announcement that communicates the state change to screen reader users [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016].
- **Best Fix:** Redesign the update so marks maintain identity across states (object constancy), use a duration within 250ms–2s, and ensure all meaningful state changes are announced to screen reader users [@elavskyHowAccessibleMy2022] [@amr_structuring_and_2016].
