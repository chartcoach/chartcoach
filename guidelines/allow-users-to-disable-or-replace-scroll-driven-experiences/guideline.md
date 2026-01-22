---
id: allow-users-to-disable-or-replace-scroll-driven-experiences
title: Let users disable or replace scroll-driven experiences (infinite scroll, parallax,
  scrollytelling)
bibliography: references.bib
description: "Provide a user-controlled way to adjust or opt out of scroll-driven\
  \ experiences, with a non-scroll alternative such as \u201CLoad more\u201D or \u201C\
  Next\u201D for keyboard-only use."
labels:
- chart:interactive
- task:navigate
- visual:motion
- impact:accessibility
- data:sequential
- audience:screen-reader
- interaction:scroll
- principle:flexible
---

## Control or opt out of scroll-driven interaction <!-- role: advice -->

Provide a way for users to adjust or opt out of scroll-driven experiences, including infinite scrolling, parallax scrolling, and “scrollytelling”. Offer a non-scroll alternative such as “Load more” or “Next” that can be used with a keyboard only.

## Why scroll control improves accessibility <!-- role: reason -->

Scroll-driven interfaces can force content changes that the user cannot easily pause, predict, or control, which reduces user agency and can make operation and comprehension harder when navigation depends on keyboard interaction and assistive technology workflows.

**Mechanism:** Giving explicit controls to pause, stop, adjust, or replace scroll-driven changes shifts the experience from system-driven progression to user-driven progression, improving operability and reducing the burden of tracking content changes.

**Evidence:** User control over long-running changes and the ability to turn off features like infinite scrolling are accessibility-supporting practices that reduce burden from uncontrolled content changes [@inclusivedesignprinciples_give_control_2]. This requirement is included as a Flexible heuristic for accessible data experiences that should respect user needs and interaction constraints [@elavskyHowAccessibleMy2022].

**Notes:** This applies to the interaction pattern (scroll-driven progression), not to whether the visualization is static or interactive overall.

## Where scroll opt-out is required <!-- role: context -->

- **User Goal:** Move through content at their own pace while retaining orientation and control.
- **Task:** Navigate a data story or dashboard section-by-section without losing place.
- **Data:** Sequential or staged content revealed by scrolling; potentially long or unbounded content lists.
- **Chart Setting:** Web or app experiences that use infinite scroll, parallax effects, or scroll-linked transitions to reveal or update charts.
- **Audience:** Users who rely on keyboard-only navigation or assistive technologies, and users who benefit from reduced interaction load.
- **Success Criterion:** All content and functionality remain reachable and usable without mandatory scroll-driven progression.

## When you might not need an opt-out <!-- role: exceptions -->

**Break it when:** The visualization has no scroll-driven behavior (no infinite scroll, parallax, or scrollytelling progression). **Why:** There is nothing to adjust or replace in the interaction pattern.

## Tradeoffs of providing scroll alternatives <!-- role: costs -->

**Sacrifice:** Additional design and engineering effort to implement parallel navigation paths. **Risk:** The alternative path can fall out of feature parity with the scroll-driven path. **Mitigation:** Treat the non-scroll option as a first-class navigation mode during development and testing.

## Common ways teams fail this guideline <!-- role: mistakes -->

**Mistake:** Using infinite scrolling as the only way to reach more content. **Why it fails:** Users cannot reliably control progression or reach all content using keyboard-only navigation.

## Quick ways to check compliance <!-- role: check -->

**Failure Sign:** More content appears only after scrolling, and there is no visible control to proceed without scrolling. **Quick Check:** Try to use only Tab, Shift+Tab, Enter, and arrow keys to progress through the entire scroll-driven experience without using a mouse or trackpad. **Stronger Test:** Verify that every scroll-triggered reveal or transition has an equivalent, keyboard-operable “Load more” or “Next” control path that reaches the same content and functionality.

## Practical fixes for scroll-driven experiences <!-- role: fix -->

- Provide a visible toggle or setting that disables scroll-driven progression and switches to step-based navigation.
- Replace infinite scroll with an explicit “Load more” control that is keyboard-operable.
- Provide “Next” and “Previous” controls that allow users to move through scrollytelling steps without scrolling.
- Ensure the opt-out path preserves access to the same content and interactions as the scroll-driven path.
