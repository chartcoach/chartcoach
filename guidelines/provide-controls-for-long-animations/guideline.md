---
id: provide-controls-for-long-animations
title: Provide Playback Controls for Long Animations
bibliography: references.bib
description: Ensure animations lasting longer than 2 seconds or those that loop include
  mechanisms to pause, stop, and restart.
labels:
- visual:animation
- visual:motion
- impact:accessibility
- impact:usability
- task:control
- audience:general
---

## The Rule <!-- role: advice -->
Ensure that any animation within a data visualization that lasts longer than 2 seconds, or any animation that loops automatically, is accompanied by controls to pause, stop, and start the motion. For animations depicting transitions in data states that exceed this duration, provide a mechanism for the user to start the sequence over.

## The Logic <!-- role: reason -->
This guideline falls under the "Flexible" principle of accessibility, which focuses on robust user agency and the ability to adjust the presentation of a data experience. Users must be able to control how content changes to accommodate diverse needs.
*   **The Principle:** Give Control (Flexible).
*   **The Evidence:** According to Chartability `[@elavsky_how_2022]`, flexible heuristics require that lower-level system preferences be respected and that users maintain agency over the interface. Specifically, `[@inclusivedesignprinciples_give_control]` notes that allowing users to control long-running animations or infinite scrolling reduces motion sickness and cognitive load.

## Where to Apply <!-- role: context -->
This applies to data interfaces utilizing motion to convey information or narrative.
*   **User Goal:** Consuming "video-style" narrative visualizations or explanatory animations.
*   **Data Type:** Dynamic data transitions or looping simulations.
*   **Audience:** Users with cognitive disabilities, vestibular disorders, or those who simply need more time to process visual changes.

## When to Break It <!-- role: exceptions -->
The source specifically delimits the duration for this requirement.
*   **Scenario:** Short state transitions.
*   **Reason:** If an animation lasts less than 2 seconds (e.g., a quick ease-in of bars on a chart load), explicit playback controls are not required by this heuristic `[@elavsky_how_2022]`.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate must be allocated for playback interface elements (buttons, toggles, or scrubbers).
*   **The Risk:** Increased engineering complexity is required to manage the state of the animation (e.g., preserving data state when paused).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Disabling the animation entirely for all users without offering it as an option.
*   **Why it fails:** This removes the "Assistive" value of the visualization, where motion might help users understand changes in data density or distribution `[@elavsky_how_2022]`.
*   **The Wrong Fix:** Providing a "stop" button that resets the data rather than pausing it.
*   **Why it fails:** The user loses the context of the current frame they were trying to examine.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for movement that loops or extends beyond a brief moment.
*   **The Test:** Observe the animation. Does it last longer than 2 seconds? If yes, attempt to pause or stop it using available controls. If it is a transition, look for a way to restart it `[@elavsky_how_2022]`.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a simple "Pause/Play" toggle button for looping animations.
*   **Best Fix:** For narrative data stories, implement full playback controls (Play, Pause, Reset, and potentially a scrubber) to give users complete temporal control over the data presentation.
