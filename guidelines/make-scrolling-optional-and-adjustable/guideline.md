---
id: make-scrolling-optional-and-adjustable
title: Provide Alternatives and Controls for Scrolling Experiences
bibliography: references.bib
description: Make infinite, parallax, and scrollytelling interactions adjustable or
  optional, with a non-scrolling alternative for navigation.
labels:
- chart:interactive
- task:navigate
- visual:motion
- impact:accessibility
- data:multimodal
- audience:general
- category:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Make scrolling-driven experiences adjustable or optional. Provide a non-scrolling alternative (e.g., “Load more” / “Next”) so users can progress without continuous scrolling.

## The Logic <!-- role: reason -->

Scrollable storytelling patterns can remove user agency by forcing content changes through motion and continuous interaction, which increases effort and can make the experience unusable for some people. Chartability frames this as a **Flexible** requirement: designs must respect user control and allow people to choose how content progresses [@elavskyHowAccessibleMy2022].

- **The Principle:** User control over content changes
- **The Evidence:** [@elavskyHowAccessibleMy2022] [@inclusivedesignprinciples_give_control_2]

## Where to Apply <!-- role: context -->

This advice is designed for scrolling-as-interaction patterns.

- **User Goal:** Progress through content and reach all information and functionality without being forced into continuous scrolling.
- **Data Type:** Long-form, sequential narrative content tied to scroll position (e.g., “scrollytelling”), or feeds that extend as you scroll (infinite scroll).
- **Audience:** Anyone, especially users relying on keyboard-only operation or who need reduced motion and predictable navigation [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The experience does not use scrolling to trigger content changes (no infinite scroll, no parallax, no scroll-triggered transitions).
- **Reason:** There is no scrolling experience to adjust or replace, so the rule does not apply [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less “seamless” narrative flow and potentially more visible UI (buttons/controls).
- **The Risk:** Maintaining two pathways (scroll-driven and step-based) can increase implementation and QA effort [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping infinite/parallax/scrollytelling as the only way to progress and calling it “accessible” because it works with a mouse or trackpad.
- **Why it fails:** It still denies user control and may not be workable for keyboard-only users who need discrete, controllable progression [@elavskyHowAccessibleMy2022] [@inclusivedesignprinciples_give_control_2]

## How to Check <!-- role: check -->

- **Visual Sign:** Content keeps moving/advancing as you scroll, with no clear way to stop, slow down, or switch to a step-based progression.
- **The Test:** Try to complete the experience using only a keyboard. If you cannot reliably progress through all content using discrete controls like “Next”/“Load more,” the rule is broken [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit controls that replicate scroll progression (e.g., “Next section,” “Previous,” “Load more”) and make the scroll-driven behavior optional.
- **Best Fix:** Provide a fully equivalent non-scrolling path for all content and interactions (step-based navigation), while keeping scroll-driven motion as an opt-in enhancement under user control [@elavskyHowAccessibleMy2022] [@inclusivedesignprinciples_give_control_2]
