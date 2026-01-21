---
id: control-long-animations
title: Provide User Controls for Long Animations
bibliography: references.bib
description: Ensure any animation longer than 2 seconds or looping can be paused or
  stopped, and let users restart long state-transition animations.
labels:
- chart:interactive
- task:explore
- visual:motion
- impact:accessibility
- data:any
- audience:general
- principle:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Provide pause and stop controls for any animation that lasts more than 2 seconds or loops; if an animation communicates a data-state transition and lasts more than 2 seconds, provide a way for the user to start it over. [@elavskyHowAccessibleMy2022]

## The Logic <!-- role: reason -->

Long-running motion is a user-controlled preference issue: giving users direct control over how content changes reduces the access burden and accommodates users who need to pause, stop, adjust, or avoid motion to use the experience effectively. [@elavskyHowAccessibleMy2022]

- **The Principle:** User control over motion and change
- **The Evidence:** [@inclusivedesignprinciples_give_control]

## Where to Apply <!-- role: context -->

This advice applies whenever motion is part of the visualization experience. [@elavskyHowAccessibleMy2022]

- **User Goal:** Following an explanation, understanding a transition, or tracking changes in the data state over time
- **Data Type:** Any data shown with explanatory, video-style, looping, or state-transition animations
- **Audience:** People who may need to reduce motion, pause to process information, or replay transitions for comprehension

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization contains no animations, no looping motion, and no animations longer than 2 seconds. [@elavskyHowAccessibleMy2022]
- **Reason:** The rule is not applicable when the triggering condition (long or looping animation) is absent. [@elavskyHowAccessibleMy2022]

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional UI elements (controls) and implementation effort to support pausing, stopping, and restarting. [@elavskyHowAccessibleMy2022]
- **The Risk:** If controls are added without being clear and discoverable, users may still experience uncontrolled motion or be unable to replay key transitions. [@elavskyHowAccessibleMy2022]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving long or looping animations always-on and assuming users can simply “wait it out.” [@elavskyHowAccessibleMy2022]
- **Why it fails:** It removes user control over how content changes, which the guideline explicitly requires. [@inclusivedesignprinciples_give_control]

## How to Check <!-- role: check -->

- **Visual Sign:** An explanatory or looping animation continues for more than 2 seconds with no visible pause/stop control, or a long transition plays once with no restart option. [@elavskyHowAccessibleMy2022]
- **The Test:** Watch the visualization for any looping motion or any animation segment exceeding 2 seconds and verify that pause/stop controls exist; for long data-state transitions, verify a restart control is available. [@elavskyHowAccessibleMy2022]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a visible pause/stop control that halts any >2s or looping animation. [@elavskyHowAccessibleMy2022]
- **Best Fix:** Provide a complete set of controls—pause, stop, and (when transitions communicate state) restart—so users can control and replay long animated explanations or state changes on demand. [@elavskyHowAccessibleMy2022]
