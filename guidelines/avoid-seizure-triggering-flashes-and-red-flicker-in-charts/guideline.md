---
id: avoid-seizure-triggering-flashes-and-red-flicker-in-charts
title: Avoid seizure-triggering flashes and red flicker in charts
bibliography: references.bib
description: "Ensure charts\u2014static or interactive\u2014do not include flashing\
  \ or red-flashing sequences that can trigger seizures."
labels:
- chart:any
- task:consume
- visual:animation
- impact:accessibility
- data:any
- audience:all
- a11y:seizure-risk
---

## Avoid seizure-triggering flashes and red flicker in charts <!-- role: advice -->

Design the chart so it does not flash in a way that creates seizure risk, including avoiding red flashes and avoiding animation with red or large areas of red. Validate the rendered output (including interactions) for flash thresholds before release.

## Seizure safety depends on temporal flashing patterns, including red flashes <!-- role: reason -->

Seizure risk can arise from the temporal behavior of visual output, where rapid flashing (including red flashes) or certain flashing patterns can be hazardous; interactive visualizations can also produce risky sequences during use.

**Mechanism:** Limiting flash frequency and avoiding red-flash patterns reduces exposure to flashing sequences that may trigger seizures.

**Evidence:** Content should not contain flashes that exceed seizure-related thresholds, including red flashes, to reduce risk for people with photosensitive epilepsy [@w3c_understanding_three; @elavskyHowAccessibleMy2022]. Video and multimedia output can be analyzed to detect flashes and red-flash patterns using dedicated analysis tooling [@umd_photosensitive_epilepsy; @elavskyHowAccessibleMy2022].

**Notes:** Interaction can create sequences that are not present in the initial static view, so the evaluation must include active states and interaction paths [@elavskyHowAccessibleMy2022].

## Where seizure-risk checks apply in visualization <!-- role: context -->

- **User Goal:** Consume information from a chart without being exposed to harmful flashing content.
- **Task:** View, navigate, or interact with a visualization over time (including hover, selection, filtering, playback, or transitions).
- **Data:** Any data, since the risk is driven by rendering behavior rather than data type.
- **Chart Setting:** Static charts that include flashing elements or interactive/animated charts that can generate rapid flicker or red-flash sequences during interaction.
- **Audience:** General audiences, including people with photosensitive epilepsy and people who may be unaware of their sensitivity.
- **Success Criterion:** The chart’s rendered output stays below seizure-risk thresholds for flashes (including red flashes) in both static and interactive use.

## When not to follow it <!-- role: exceptions -->

Break it when the visualization contains no flashing behavior and no interaction or animation that can generate flashing sequences. Why: without temporal flashing output, this specific seizure-risk constraint is not triggered.

## Tradeoffs of avoiding red flashes and flicker <!-- role: costs -->

**Sacrifice:** You may lose some attention-grabbing motion effects or high-salience red animation patterns. **Risk:** Over-removing motion or red emphasis can reduce visual prominence of key states. **Mitigation:** Preserve emphasis through non-flashing changes (e.g., stable contrast or annotation) rather than temporal flashing patterns [@elavskyHowAccessibleMy2022].

## Common ways seizure risk slips in <!-- role: mistakes -->

- **Mistake:** Adding animated transitions or interactive highlights that rapidly flicker during hover/selection. **Why it fails:** Interaction can generate rapid flashing sequences that create seizure risk even if the initial view seems safe [@elavskyHowAccessibleMy2022].
- **Mistake:** Using red flashing or animating with red over a significant portion of the display. **Why it fails:** Red flashes and large-area red animation are specifically called out as seizure risk patterns [@w3c_understanding_three; @elavskyHowAccessibleMy2022].

## Quick checks for flash and red-flash risk <!-- role: check -->

**Failure Sign:** The chart contains rapid flicker, repeated flashing, or red flashing during animation or interaction. **Quick Check:** Trigger all interactive states and animations you ship and watch for any repeated flashing sequences, especially involving red or large red areas [@elavskyHowAccessibleMy2022]. **Stronger Test:** Record the chart’s behavior as video (including interactions) and analyze it with a photosensitive epilepsy analysis tool to detect flash and red-flash patterns [@umd_photosensitive_epilepsy; @elavskyHowAccessibleMy2022].

## Practical mitigations to remove seizure risk <!-- role: fix -->

- Remove or redesign any effect that produces repeated flashing, including hover/selection states that flicker under rapid pointer movement.
- Avoid red flashing and avoid animating with red or having a significant portion of the display area use red during animation or state changes.
- Replace flashing-based emphasis with stable, non-flashing alternatives such as persistent annotation or non-temporal visual changes that do not create flicker patterns.
- Validate the final rendered output (including interactive sequences) with seizure-risk analysis tooling and remediate any detected flash or red-flash failures [@umd_photosensitive_epilepsy].
