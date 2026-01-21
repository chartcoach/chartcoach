---
id: avoid-seizure-triggering-flashes-and-red-animation
title: Avoid Seizure-Triggering Flashes and Red Animation
bibliography: references.bib
description: Ensure charts never exceed seizure-risk flash thresholds and avoid red
  flashing or red-heavy animation, validating with a tool like PEAT.
labels:
- chart:interactive
- task:explore
- visual:animation
- impact:accessibility
- data:multivariate
- audience:general
- risk:seizure
- source:chartability
---

## The Rule <!-- role: advice -->

Do not create charts (static or interactive) that flash above seizure-risk thresholds, and avoid red flashes; avoid animating with red or having a significant portion of the display area be red during animation. Validate the result with a seizure-risk assessment tool such as PEAT.

## The Logic <!-- role: reason -->

Flashing content and red flashes can trigger seizures for people with photosensitive epilepsy, so visuals must stay below defined flash thresholds and avoid red-flash conditions. This guideline is captured as a critical “Perceivable” heuristic in Chartability to reduce seizure risk in data visualizations [@elavskyHowAccessibleMy2022].

- **The Principle:** Prevent seizure-inducing visual stimuli by controlling flash frequency and red-flash conditions.
- **The Evidence:** WCAG guidance specifies avoiding flashes that exceed three per second and avoiding red flashes that can trigger seizures [@w3c_understanding_three]. PEAT exists to analyze media for flashes/patterns that may trigger seizures, including red flashes and rapid flicker [@umd_photosensitive_epilepsy].

## Where to Apply <!-- role: context -->

This advice is designed for charts that can present rapid visual change.

- **User Goal:** Viewing or interacting with a chart without health risk from visual flicker.
- **Data Type:** Any (especially when interaction or animation changes the display over time).
- **Audience:** Broad/public audiences, including users with photosensitive epilepsy.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None stated in the cited sources.
- **Reason:** The cited guidance is framed as a safety constraint (“must not pose a seizure risk”) rather than an optional tradeoff [@elavskyHowAccessibleMy2022] [@w3c_understanding_three].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced ability to use flashing, rapid flicker, or red-heavy animated effects as attention-grabbing emphasis.
- **The Risk:** If you rely on these effects for salience, removing them may require redesigning how emphasis is communicated [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming only “video” needs seizure checks and skipping checks for interactive visualization states.
- **Why it fails:** Interactive data experiences can produce seizure-inducing sequences through built-in interaction/animation patterns, so both static and active states must be considered [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Keeping animations but allowing red flashing or red-dominant animated regions.
- **Why it fails:** The guideline explicitly warns to avoid red flashes and to avoid animating with red or having a significant portion of the display area use red during animation [@elavskyHowAccessibleMy2022] [@w3c_understanding_three].

## How to Check <!-- role: check -->

- **Visual Sign:** Noticeable flicker/rapid flashing during animation or interaction, especially involving red flashes or large red areas.
- **The Test:** Export/record the chart’s animation and key interactive states and analyze the media with PEAT to detect red flashes and rapid flicker; confirm results meet seizure-safety thresholds described in WCAG guidance [@umd_photosensitive_epilepsy] [@w3c_understanding_three] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove or disable the flashing/rapid-flicker behavior (including red flashing) in animations and interactive transitions.
- **Best Fix:** Redesign the interaction/animation so state changes do not create flash patterns (including red-flash conditions), then re-validate with PEAT across the full set of interactive states [@umd_photosensitive_epilepsy] [@elavskyHowAccessibleMy2022].
