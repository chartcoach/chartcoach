---
id: make-chart-state-shareable-and-reproducible
title: Make Chart State Easy to Share and Reproduce
bibliography: references.bib
description: Ensure any customized visualization view created through interaction
  can be recreated and shared easily (e.g., via a single link, file, or saved state).
labels:
- chart:interactive
- task:explore
- task:share
- visual:interaction
- impact:accessibility
- impact:usability
- audience:analyst
- complexity:advanced
- principle:compromising
- source:community-practices
---

## The Rule <!-- role: advice -->

Provide a simple way to share and reproduce the current chart state whenever users can create a customized view through analysis or interaction (e.g., one link, file, or saved state).

## The Logic <!-- role: reason -->

Failing to preserve and transmit the exact interaction state forces people to reconstruct complex analysis steps, shifting the access burden onto collaborators and increasing cognitive effort; replacing state sharing with screenshots also removes “proof in the system” and introduces new accessibility risks that must be remediated. Chartability frames this as a Compromising issue (Understandable yet Robust) about transparent, tolerant information flows for different access needs [@elavskyHowAccessibleMy2022].

- **The Principle:** Reduce cognitive labor by preserving analysis context in a reproducible state.
- **The Evidence:** URL-encoded map parameters demonstrate how sharing a single link can recreate an exact view for another person [@moz_everything_you]; dashboard/report sharing mechanisms show how collaborators can access the same interactive artifact/state rather than a static capture [@key2consulting_how_share].

## Where to Apply <!-- role: context -->

This advice is designed for interactive or exploratory data experiences where users can branch, drill down, filter, or otherwise reach a personalized view.

- **User Goal:** Share a specific discovered view so others can see exactly what the sharer sees (and continue from there).
- **Data Type:** Any data used in dashboards/apps with customizable interaction state (filters, selections, narrative branches).
- **Audience:** Analysts and collaborators who need to communicate findings and reproduce analysis states reliably.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization has no interaction or cannot produce a customized view beyond the initial default.
- **Reason:** There is no state to preserve or reproduce beyond the static baseline [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional engineering and product effort to persist, serialize, and restore state.
- **The Risk:** Poorly implemented state saving/sharing can be fragile or incomplete, undermining trust in whether two viewers truly see the same state.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Tell users to take a screenshot of the chart.
- **Why it fails:** It shifts cognitive and accessibility labor onto others, loses interactive “proof in the system,” and creates a new accessibility remediation burden for the image [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** A user can filter/drill into a unique view but can only communicate it by describing steps or sharing a screenshot.
- **The Test:** Create a non-default view (via a realistic sequence of interactions), then attempt to share it; confirm a second person can open what you shared and see the same view/state without manual reconstruction [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit “share” or “save view” output that captures the current state as a single artifact (one link or one file) [@elavskyHowAccessibleMy2022].
- **Best Fix:** Encode all necessary parameters so the state is reproducible and transferable in a single shareable representation, analogous to shareable parameterized map URLs that recreate an exact view for another user [@moz_everything_you], and support collaboration-oriented sharing flows used for interactive reports [@key2consulting_how_share].
