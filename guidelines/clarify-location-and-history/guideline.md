---
id: clarify-location-and-history
title: Provide Clear Location Breadcrumbs and Navigation History
bibliography: references.bib
description: "Make the user\u2019s current location and prior states in a visualization\
  \ system clear, and enable saving, reloading, and navigating history."
labels:
- chart:dashboard
- task:navigate
- visual:layout
- impact:accessibility
- data:multivariate
- audience:general
- principle:compromising
- source:chartability
---

## The Rule <!-- role: advice -->

Show users where they are and how they got there: provide clear location cues (e.g., breadcrumbs) and support saving, reloading, and navigating visualization state/history.

## The Logic <!-- role: reason -->

- **The Principle:** Location transparency reduces disorientation and makes complex systems more robust and error-tolerant by helping users understand their position and recover or retrace steps through prior states [@elavskyHowAccessibleMy2022].
- **The Evidence:** Guidance to provide information about a user’s location within a set of pages (e.g., breadcrumbs or step indicators) supports navigation in complex interfaces, especially for users with cognitive impairments or those using assistive technologies [@w3c_understanding_location].

## Where to Apply <!-- role: context -->

- **User Goal:** Keep track of “where am I?” while moving through views, filters, drill-downs, or multi-step exploration in a visualization system [@elavskyHowAccessibleMy2022].
- **Data Type:** Visualizations embedded in multi-view or multi-state environments (e.g., dashboards or apps) where the “current view and state” can change [@elavskyHowAccessibleMy2022].
- **Audience:** Users navigating complex interfaces, including people using assistive technologies and people with cognitive accessibility needs [@elavskyHowAccessibleMy2022; @w3c_understanding_location].

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single, static visualization view with no navigation across views and no state changes to preserve.
- **Reason:** If there is no meaningful “location” within a set of pages/views and no history to traverse, breadcrumbs and history controls do not apply [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional interface elements and implementation work to expose state, history, and save/reload behavior [@elavskyHowAccessibleMy2022].
- **The Risk:** Poorly communicated or cluttered location/history UI can add complexity instead of reducing it [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying on the user to infer location from visual context alone (e.g., changing a view without indicating the new position/state).
- **Why it fails:** The “current location in a system is not easy to understand” without explicit cues, which undermines robust, forgivable navigation and makes it harder to recover or retrace steps [@elavskyHowAccessibleMy2022; @w3c_understanding_location].

## How to Check <!-- role: check -->

- **Visual Sign:** After navigating or interacting, the interface provides no clear indicator of the current position within the overall experience, and there is no obvious way to return to or reproduce a prior state [@elavskyHowAccessibleMy2022].
- **The Test:** Change the visualization state (e.g., switch views or apply an interaction that changes what’s shown), then try to (1) identify your location in the system and (2) return to a previous state or reload the current state; if you cannot do these reliably, location/history is unclear [@elavskyHowAccessibleMy2022; @w3c_understanding_location].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit location cues that indicate the user’s current position within the set of views/pages (e.g., a breadcrumb or step indicator) [@w3c_understanding_location; @elavskyHowAccessibleMy2022].
- **Best Fix:** Provide a complete, communicated state model that includes breadcrumbs plus the ability to save, reload, and navigate history for the visualization’s current view and interaction state [@elavskyHowAccessibleMy2022; @w3c_understanding_location].
