---
id: if-using-scattered-icon-arrays-include-a-settle-to-grouped-view
title: If You Start Scattered, Animate a Settle into Grouped Icons
bibliography: references.bib
description: Scattered icon arrays perform poorly for comparing risk magnitudes unless
  users are given a grouped view via a settle animation.
labels:
- chart:icon-array
- task:compare
- visual:motion
- impact:clarity
- data:probabilistic
- audience:general-public
- animation:settle
- domain:health-risk
- source:zikmund-fisher-2012
---

## The Rule <!-- role: advice -->

If you present risk with scattered icons, include a “settle” animation (or otherwise provide a grouped end-state) so users can see event icons in a contiguous block.

## The Logic <!-- role: reason -->

Scattering may cue randomness but makes magnitude harder to judge; letting icons settle into a grouped block restores countability and supports better comparisons than scattered-only designs.

- **The Principle:** Provide a stable grouped configuration for magnitude extraction
- **The Evidence:** Scattered displays generally produced poorer knowledge and ratings; scattered conditions improved when they included a settle-to-grouped view, whereas scattered-not-settled versions were among the worst performers [@zikmund-fisherAnimatedGraphicsComparing2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Understand “how many out of 100” and compare two options’ side-effect risks
- **Data Type:** Icon arrays where you are tempted to show randomness via dispersion
- **Audience:** General audiences who may not want to count dispersed icons

## When to Break It <!-- role: exceptions -->

- **Scenario:** The only intended message is “outcomes are random,” not “compare magnitudes precisely”
- **Reason:** Adding a grouped state shifts attention toward magnitude; if magnitude comparison is not a goal, the settle step may be unnecessary [@zikmund-fisherAnimatedGraphicsComparing2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra transition time and added visual complexity versus a single static grouped display
- **The Risk:** Even with settling, the animation does not outperform simply starting grouped, so you may add complexity without benefit [@zikmund-fisherAnimatedGraphicsComparing2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the display scattered the whole time to “look more realistic”
- **Why it fails:** Users struggle to assess magnitude and comparisons degrade in scattered-only presentations [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Event icons remain dispersed with no grouped summary view.
- **The Test:** Ask users which treatment has the higher risk; if accuracy is low, add a grouped end-state and retest against a static grouped baseline [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** After initial scatter, transition to a grouped arrangement and hold that final state.
- **Best Fix:** Skip the scatter entirely and show the static grouped icon array from the start for two-risk comparisons [@zikmund-fisherAnimatedGraphicsComparing2012].
