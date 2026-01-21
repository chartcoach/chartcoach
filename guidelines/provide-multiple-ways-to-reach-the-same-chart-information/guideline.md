---
id: provide-multiple-ways-to-reach-the-same-chart-information
title: Provide Multiple Ways to Reach the Same Chart Information
bibliography: references.bib
description: Ensure users can reach the same chart information through more than one
  navigation or interaction path, especially in complex dashboards and stateful flows.
labels:
- chart:dashboard
- chart:interactive
- task:navigate
- task:find
- impact:accessibility
- impact:usability
- audience:all
- category:compromising
- source:standards
---

## The Rule <!-- role: advice -->

Provide at least two different processes to reach the same chart information or state; do not require a single, specific sequence of steps (e.g., only one path through filters, view transitions, or pages).

## The Logic <!-- role: reason -->

Requiring one exact process forces users to rely on memory, tolerate brittle UI flows, and navigate only one information architecture route; providing alternative paths increases tolerance and transparency for different user strategies and assistive-technology navigation patterns in data interfaces [@elavskyHowAccessibleMy2022].

- **The Principle:** Multiple ways reduce reliance on a single navigation method and make content easier to locate.
- **The Evidence:** [@w3c_understanding_multiple_2]

## Where to Apply <!-- role: context -->

This advice is designed for chart experiences that embed information inside multi-step UI flows.

- **User Goal:** Reaching a specific view/state or finding a specific insight in an exploratory experience (e.g., arriving at the same filtered result).
- **Data Type:** Any, when access depends on application state (filters, transitions, multi-page dashboards).
- **Audience:** Users with disabilities and assistive technologies, and anyone who benefits from alternative navigation paths in complex analytical products [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart/content does not participate in any complex UI flow (no state changes, no multi-page navigation, no filter-driven states).
- **Reason:** If there is no process-gated state to reach, the “single process” failure condition does not apply [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More design and engineering effort to support parallel controls or paths (e.g., adding search, alternate UI controls, or parallel navigation).
- **The Risk:** If alternative paths are implemented inconsistently, users may reach the same state but with unclear differences in behavior, harming transparency [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Providing only one deep interaction path (e.g., “you must click here, then filter there, then change tabs”) and calling it “discoverable.”
- **Why it fails:** Users who can’t or don’t follow that exact sequence are blocked from the same information/state because there is no second process to locate it [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Adding an alternative path that reaches a different end state (similar-looking but not equivalent).
- **Why it fails:** The rule requires more than one way to reach the same information/state, not merely another route to different content [@w3c_understanding_multiple_2].

## How to Check <!-- role: check -->

- **Visual Sign:** Key information appears “buried” behind a single chain of steps (filters → view change → page change) with no parallel route.
- **The Test:** Pick an important chart state (e.g., a particular filtered view) and attempt to reach it in at least two distinct ways (e.g., alternate navigation route, parallel UI control, or search-driven access). If only one process exists, the guideline is broken [@w3c_understanding_multiple_2] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a parallel control or navigation mechanism that reaches the same chart state (e.g., an additional UI control that leads to the same view/state) [@elavskyHowAccessibleMy2022].
- **Best Fix:** Redesign the information architecture so users can locate the same content through multiple ways such as navigation plus search or other parallel locating mechanisms, ensuring they converge on equivalent states [@w3c_understanding_multiple_2] [@elavskyHowAccessibleMy2022].
