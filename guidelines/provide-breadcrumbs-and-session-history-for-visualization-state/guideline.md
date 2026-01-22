---
id: provide-breadcrumbs-and-session-history-for-visualization-state
title: Provide breadcrumbs and saveable, reloadable history for the current visualization
  state
bibliography: references.bib
description: "Make the user\u2019s current location and prior states clear by exposing\
  \ breadcrumbs and a navigable, saveable history of the visualization state."
labels:
- chart:dashboard
- task:navigate
- visual:text
- impact:accessibility
- data:multivariate
- audience:all
- principle:compromising
- interaction:stateful
---

## Make location and history explicit in the visualization state <!-- role: advice -->

Provide clear breadcrumbs for where the user is in the visualization or dashboard, and provide a history the user can navigate plus a way to save and reload the current state. Ensure these cues are communicated as part of the current view and interaction state, not implied by layout alone.

## Why location cues and history reduce confusion and error cost <!-- role: reason -->

When a visualization’s state changes through interaction, users can lose track of where they are and how they got there. Exposing location cues (breadcrumbs) and navigable state history makes the information flow more transparent and error-tolerant, and supports users who rely on different consumption strategies or assistive technologies.

**Mechanism:** Users can re-orient to the current view, reconstruct context, and recover from mistakes by returning to prior states or reloading a known-good state.

**Evidence:** Providing information about a user’s position within a set of pages or views (such as breadcrumbs or step indicators) helps users navigate complex interfaces, especially for users with cognitive impairments or those using assistive technologies [@w3c_understanding_location]. Chartability treats unclear location and history as an accessibility barrier in complex visualization environments and recommends breadcrumbs plus saving, reloading, and history navigation to make state robust and forgivable [@elavskyHowAccessibleMy2022].

**Notes:** This guideline targets clarity of state in complex, multi-view, or interactive visualization environments where the “current view” is not self-evident.

## Where this applies in visualization experiences <!-- role: context -->

- **User Goal:** Maintain orientation while exploring or returning to a specific view or finding within a visualization system.
- **Task:** Move across views, apply filters, drill down, compare states, and share or revisit findings.
- **Data:** Multi-variable or multi-view data where state changes alter what data is shown or how it is framed.
- **Chart Setting:** Dashboards, apps, or stateful interactive charts with filters, linked views, and drill-down navigation.
- **Audience:** Mixed audiences, including users with cognitive accessibility needs and users of assistive technologies.
- **Success Criterion:** The user can always tell what view/state they are in and can return to a prior or saved state without guessing.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is a single, static view with no navigation, no state changes, and no meaningful concept of “where am I” beyond the page itself. **Why:** Breadcrumbs and history do not represent real user state and would add non-functional interface noise.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional UI space and engineering effort to track, label, and persist states. **Risk:** Breadcrumbs or history can become confusing if labels do not match the user’s mental model or if history includes noisy micro-states. **Mitigation:** Keep state representations meaningful and communicative rather than exhaustive.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Relying on visual layout alone to imply “where the user is” without explicit cues. **Why it fails:** Location is not reliably inferable, especially in complex dashboards or when using assistive technologies [@w3c_understanding_location; @elavskyHowAccessibleMy2022].
- **Mistake:** Allowing many state changes but providing no way to return, undo, or reload a known state. **Why it fails:** Users cannot recover from mistakes and cannot reliably reproduce or share a view/state [@elavskyHowAccessibleMy2022].

## Quick tests for unclear location and history <!-- role: check -->

**Failure Sign:** After interacting (filtering, drilling down, switching views), the user cannot tell what view/state they are in or how to return to a prior state. **Quick Check:** Perform several interactions and then attempt to describe the current location/state using only on-screen cues, and attempt to return to the initial state without reloading the page. **Stronger Test:** Ask a user to reach a specific state, leave the visualization, and then return and recover that exact state via saved/reloaded state or history navigation.

## What to do instead <!-- role: fix -->

- Add a breadcrumb trail (or equivalent location indicator) that reflects the user’s position in the visualization’s navigation and view hierarchy.
- Provide back/forward-style history navigation over meaningful visualization states so users can recover from mistakes and re-orient.
- Provide a way to save and reload the current visualization state so users can return to or share a specific configuration.
- Communicate state changes and location cues in a way that remains available as part of the current view/state rather than being transient.
