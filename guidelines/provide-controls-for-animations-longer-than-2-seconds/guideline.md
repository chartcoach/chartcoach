---
id: provide-controls-for-animations-longer-than-2-seconds
title: Provide pause, stop, and restart controls for animations longer than 2 seconds
  (including loops)
bibliography: references.bib
description: If an animation in a data visualization runs longer than 2 seconds or
  loops, users must be able to pause or stop it, and longer state-transition animations
  must be restartable.
labels:
- chart:interactive
- task:explore
- visual:motion
- impact:accessibility
- data:any
- audience:all
- category:flexible
- disability:vestibular
- disability:cognitive
---

## Animation controls for long or looping motion <!-- role: advice -->

Provide pause, stop, and start controls for any animation that lasts more than 2 seconds or loops in a data visualization. If an animation communicates a transition in the data state and lasts more than 2 seconds, also provide a way for the user to restart the animation from the beginning.

## User-controlled motion supports flexible access needs <!-- role: reason -->

User-controlled playback prevents time-based presentation changes from forcing users to track moving content at a pace they cannot tolerate or follow, and it allows users to re-run explanatory transitions until they understand the change.

**Mechanism:** Giving direct controls over motion reduces the access burden created by automatic time progression and supports users who need to slow down, stop, or repeat moving content to operate and perceive the visualization comfortably.

**Evidence:** Accessibility-focused heuristics for data visualizations require that longer or looping animations can be paused or stopped, and that longer state-transition animations can be restarted to support user control and robust access across user settings and needs [@elavskyHowAccessibleMy2022]. Providing user control to pause, stop, or adjust long-running animations is an inclusive design requirement aimed at improving accessibility and reducing negative effects of uncontrolled motion [@inclusivedesignprinciples_give_control].

**Notes:** This guideline concerns animations used for explanation, presentation, or transitions, not instantaneous visual updates.

## When this triggers in a visualization experience <!-- role: context -->

- **User Goal:** Understand or operate a visualization without being forced to follow motion at a fixed pace.
- **Task:** Read and interpret animated encodings or learn changes introduced via animated transitions.
- **Data:** Any; especially when changes are communicated through animated state transitions.
- **Chart Setting:** Any visualization with motion, including video-style explanations, looping effects, or animated transitions between states.
- **Audience:** Users with diverse accessibility needs, including those affected by motion, attention, or processing load.
- **Success Criterion:** Users can pause or stop long/looping motion, and can restart long explanatory/state-transition animations on demand.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization contains no animations longer than 2 seconds and no looping animations. **Why:** The triggering condition for requiring playback controls is not present.

## Tradeoffs of adding animation controls <!-- role: costs -->

**Sacrifice:** Additional interface elements and implementation effort are required to expose playback controls and restart behavior. **Risk:** Controls may add visual or interaction complexity if not integrated coherently with the visualization’s existing interaction model. **Mitigation:** Keep controls minimal and clearly tied to the animation being controlled.

## Common ways this fails in practice <!-- role: mistakes -->

**Mistake:** Letting a long or looping animation run automatically with no way to pause or stop it. **Why it fails:** Users cannot control motion that may interfere with perceiving or operating the visualization [@elavskyHowAccessibleMy2022; @inclusivedesignprinciples_give_control].\
**Mistake:** Using a long animated transition to explain a data-state change without providing a restart option. **Why it fails:** Users who miss part of the transition cannot re-run the explanation to reconstruct what changed [@elavskyHowAccessibleMy2022].

## Quick ways to test for missing animation controls <!-- role: check -->

**Failure Sign:** An animation runs for more than 2 seconds (or loops) and there is no obvious way to pause or stop it, or a long transition cannot be replayed from the beginning. **Quick Check:** Watch the visualization for 5–10 seconds and try to find and use pause/stop/start controls for any ongoing animation. **Stronger Test:** Trigger any state-transition animation repeatedly and verify you can pause/stop it mid-way and restart it to replay the full transition.

## Remediations that satisfy the requirement <!-- role: fix -->

- Add explicit pause and stop controls for any animation longer than 2 seconds or any looping animation.
- Add a start or replay control that restarts longer-than-2-second state-transition animations from the beginning.
- Replace long, automatic explanatory animations with a user-triggered playback interaction that the user can start, pause, and stop.
- Provide a non-animated alternative presentation of the same explanation or transition outcome when animation controls cannot be integrated cleanly into the existing interface.
