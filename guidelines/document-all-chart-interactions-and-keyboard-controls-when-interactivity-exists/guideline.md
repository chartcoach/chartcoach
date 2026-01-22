---
id: document-all-chart-interactions-and-keyboard-controls-when-interactivity-exists
title: Document all chart interactions and keyboard controls when any interactivity
  exists
bibliography: references.bib
description: If a visualization is interactive, provide visible cues and clear instructions
  for how to use every interaction with mouse, keyboard, and assistive technologies.
labels:
- chart:interactive
- task:explore
- visual:interaction
- impact:accessibility
- data:any
- audience:general
- principle:operable
- critical:true
---

## Provide visible interaction cues and instructions for every chart interaction <!-- role: advice -->

If a visualization includes any interactive behavior, provide visible instructions that explain what is interactive and how to operate it with both mouse and keyboard. Place the instructions where users can find them without guessing.

## Why documented controls make interactions operable <!-- role: reason -->

Interactive visualizations are operable only when users can discover available actions and successfully execute them with their available input methods. Making interaction instructions explicit removes the need to infer hidden behaviors and reduces interaction errors, especially when users cannot rely on mouse-only conventions or visual trial-and-error.

**Mechanism:** Clear labels and instructions turn implicit, experience-dependent interactions into explicit, learnable controls that can be discovered and executed through multiple input modalities.

**Evidence:** Interactive controls need labels or instructions so users can understand required actions and operate interfaces correctly, with particular benefit for users with cognitive disabilities [@w3c_understanding_labels; @elavskyHowAccessibleMy2022]. Providing explicit keyboard instructions for interactive charts supports keyboard and screen reader users in navigating and operating dashboard interactions [@sf_covid19_data; @elavskyHowAccessibleMy2022].

**Notes:** Instructions should cover both what the interaction does and how to trigger it with different input devices.

## Situations that trigger the need for interaction instructions <!-- role: context -->

- **User Goal:** Understand the data and use the provided interactions to filter, navigate, or reveal details.
- **Task:** Explore, drill down, filter, or select data marks or controls.
- **Data:** Any dataset shown through interactive marks, filters, or linked views.
- **Chart Setting:** Any chart, dashboard, or data interface that supports hover, click/tap, selection, zoom/pan, filtering, brushing, or cross-highlighting.
- **Audience:** Mixed audiences including keyboard-only users and screen reader users.
- **Success Criterion:** Users can discover interactive capabilities and complete the same interactions using keyboard-only operation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is fully static and contains no interactive capabilities or controls. **Why:** There are no interactions to document.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional on-screen space and authoring time for instruction text. **Risk:** Overly long instructions can distract from the visualization’s main message. **Mitigation:** Keep instructions succinct while still covering mouse and keyboard operation.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Relying on “intuitive” interaction without any visible cue or instruction. **Why it fails:** It assumes users can discover interactions through mouse exploration or visual conventions that may not be available to many users [@elavskyHowAccessibleMy2022].
- **Mistake:** Documenting mouse actions only (for example “hover to see details”) while omitting keyboard operation. **Why it fails:** It leaves keyboard and assistive-technology users unable to access the same interactive functionality [@sf_covid19_data; @elavskyHowAccessibleMy2022].

## Quick tests to detect missing interaction instructions <!-- role: check -->

**Failure Sign:** The chart responds to hover/click/selection, but there is no visible text explaining what is interactive or how to use it. **Quick Check:** Scan the chart and surrounding UI for a short “How to interact” description that mentions both mouse and keyboard controls. **Stronger Test:** Attempt to operate every interactive feature using only the keyboard and verify the necessary keystrokes are discoverable from visible instructions [@sf_covid19_data].

## Practical remediations when instructions are missing <!-- role: fix -->

- Add a concise “How to interact” block that lists the chart’s interactive features and the keyboard keys needed to operate them.
- Add visible cues near the chart (such as a help link, hint text, or inline prompt) that indicates interactivity exists and where to learn controls.
- Ensure interaction instructions cover all supported inputs (mouse hover/click and keyboard navigation/activation) rather than only one input method.
- If an interaction is too complex to explain clearly, replace it with simpler, explicit controls whose operation can be labeled or instructed.
