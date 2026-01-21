---
id: ensure-pointer-targets-are-at-least-24px-or-provide-alternatives
title: "Ensure Pointer Targets Are at Least 24\xD724px or Provide Equivalent Alternatives"
bibliography: references.bib
description: "Make every pointer-activated control at least 24\xD724px, or provide\
  \ an alternative interaction method when marks cannot meet that size."
labels:
- chart:scatter
- chart:interactive
- task:select
- task:filter
- visual:position
- visual:size
- impact:accessibility
- audience:general
- disability:motor
- source:chartability
---

## The Rule <!-- role: advice -->

Make every interactive element that users activate with mouse/touch at least **24×24 CSS pixels**; if the interactive target is a data-scaled mark that cannot meet this size, provide an **alternative way** to select/activate the same information or task without precise pointing [@elavskyHowAccessibleMy2022] [@w3c_understanding_target].

## The Logic <!-- role: reason -->

Small pointer targets demand high precision, which creates operability barriers for people with limited dexterity; a minimum target size (or an equivalent alternative control/spacing) reduces targeting errors and makes interactions more reliable [@w3c_understanding_target]. Chartability highlights this as particularly hard in visualization because marks are often sized by data, so equivalent non-precise interaction paths are necessary when size cannot be increased [@elavskyHowAccessibleMy2022].

- **The Principle:** Reduce precision demands for pointer input by meeting minimum target size or providing equivalent operable alternatives.
- **The Evidence:** WCAG 2.2 Target Size (Minimum) guidance specifies **24×24 CSS pixels** (or equivalent) for pointer-activated targets [@w3c_understanding_target], and Chartability synthesizes this requirement into visualization auditing guidance [@elavskyHowAccessibleMy2022].

## Where to Apply <!-- role: context -->

This advice is designed for interactive visualizations where users must click/tap marks or controls.

- **User Goal:** Selecting, activating, filtering, or otherwise operating chart elements via pointer input.
- **Data Type:** Mark-based views where mark size may encode data (e.g., dense scatterplots or other scaled marks).
- **Audience:** Any audience, especially people who experience motor-access barriers when precise pointing is required [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The interactive target is inherently data-scaled and increasing its size would change the meaning of the visualization.
- **Reason:** Enlarging the mark would compromise the visual encoding; instead of resizing, provide alternative selection/activation mechanisms as Chartability recommends [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Larger targets, added alternative controls (e.g., labels/tables/search/navigation), or added UI may increase layout complexity and take space away from the visual display [@elavskyHowAccessibleMy2022].
- **The Risk:** If alternatives are poorly integrated, users may face parallel interaction paths that are inconsistent or confusing across the experience [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying on invisible pointer-expansion techniques (e.g., overlay hit regions such as Voronoi-style target expansion) as the primary solution.
- **Why it fails:** Chartability argues these approaches can still impose significant operability barriers for people with motor impairments because they may still require precise or unintuitive targeting and do not replace robust alternative interaction paths [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Clickable/tappable marks or controls appear tiny (e.g., small points in a scatterplot) and require careful aiming to activate.
- **The Test:** Identify every pointer-activated target and verify it meets **24×24 CSS pixels**, or confirm there is an alternative method to perform the same action without precise pointer targeting [@w3c_understanding_target] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase the interactive target size to meet **24×24px** where possible (e.g., enlarge buttons/handles or increase spacing so the effective target area meets the minimum) [@w3c_understanding_target].
- **Best Fix:** When marks cannot be resized because they encode data, add alternative means to complete the same task (e.g., sufficiently large text labels, accompanying data tables or search functions, alternative navigation/input such as keyboard or other non-precise input, or zoom/filter features) as recommended by Chartability [@elavskyHowAccessibleMy2022].
