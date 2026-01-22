---
id: provide-standard-ui-alternatives-for-complex-chart-actions
title: Provide standard UI alternatives for complex chart actions
bibliography: references.bib
description: When a chart uses custom gestures or complex interactions (e.g., brushing,
  zooming, filtering), provide an equivalent standard UI alternative that works with
  keyboard, screen reader, and touch.
labels:
- chart:interactive
- task:filter
- task:zoom
- task:select
- impact:accessibility
- audience:screen-reader
- audience:keyboard-only
- complexity:advanced
- wcag:2.4.5
- wcag:2.5.1
- wcag:2.5.4
---

## Provide an alternative control for every complex interaction <!-- role: advice -->

For any special chart action such as brushing, zooming, filtering, or gesture-based input, provide a standard UI alternative that can be used with a keyboard, screen reader, and touch device. Ensure the alternative is clearly discoverable and usable without performing the original complex action.

## Multiple-ways access prevents interaction lockout <!-- role: reason -->

Complex or custom interactions can exclude people who cannot perform particular gestures, who rely on keyboard interfaces, or who use assistive technologies that do not expose bespoke chart controls reliably. Providing standard alternatives preserves access to the same underlying function through more than one operational pathway, reducing dependence on a single input method and making the experience operable across diverse interaction constraints.

**Mechanism:** Alternate, standard controls (such as conventional UI components or non-gesture pathways) let users reach the same chart state changes without needing fine motor control, motion gestures, or pointer-only interactions.

**Evidence:** Providing multiple ways to locate and operate functionality reduces reliance on a single navigation or interaction method and improves access for people with disabilities [@w3c_understanding_multiple]. Alternatives to pointer gestures and motion actuation are required so users can complete actions without complex gestures or device motion [@elavskyHowAccessibleMy2022].

**Notes:** The alternative does not need to be a 1-to-1 translation of the interaction; it can be a different pathway that achieves the same end state or selection outcome [@elavskyHowAccessibleMy2022].

## Contexts that trigger the need for alternatives <!-- role: context -->

- **User Goal:** Perform chart operations (select, filter, zoom, pan, or explore subsets) and reach specific data items or views.
- **Task:** Interactive exploration that changes chart state via custom controls or gestures.
- **Data:** Any dataset where users must interact to access subsets, details, or comparisons (especially when interaction is required to reveal information).
- **Chart Setting:** Web or app charts with bespoke interactions (brushing, lasso, drag-to-zoom, hover-dependent controls, gesture-only actions, motion-triggered actions).
- **Audience:** Users who operate via keyboard, screen reader, touch-only, or who cannot perform complex pointer gestures or motion actuation.
- **Success Criterion:** All key actions are achievable without the original complex interaction, using at least one standard, discoverable alternative control.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart has no special actions and no custom or complex controls (no brushing/zooming/filtering/gesturing). **Why:** There is no complex interaction to provide an alternative for [@elavskyHowAccessibleMy2022].

## Costs and tradeoffs <!-- role: costs -->

**Sacrifice:** Additional UI elements or pathways can add design and implementation complexity. **Risk:** Poorly designed alternatives can confuse users or create duplicate controls that diverge in behavior. **Mitigation:** Keep alternatives functionally equivalent in outcome and ensure they are clearly labeled and consistently supported across input methods [@elavskyHowAccessibleMy2022].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Offering only mouse-based brushing/hover/drag interactions with no other way to perform the action. **Why it fails:** Users who cannot use pointer gestures or who rely on keyboard/assistive technology cannot complete the task [@elavskyHowAccessibleMy2022].
- **Mistake:** Adding a “keyboard version” that requires exhaustive tabbing through every mark to replicate a pointer interaction. **Why it fails:** This can be an impractically high-effort substitute rather than a usable alternative path to the same outcome [@elavskyHowAccessibleMy2022].
- **Mistake:** Using motion actuation (device tilt/shake) to trigger a chart action without a non-motion control. **Why it fails:** Users who cannot or do not use motion inputs lose access to that function [@elavskyHowAccessibleMy2022].

## Quick checks for operable alternatives <!-- role: check -->

**Failure Sign:** An interaction (filter, zoom, selection, reveal) can only be performed via dragging, lassoing, hovering, gesturing, or device motion. **Quick Check:** Try to complete every chart action using only a keyboard and then using touch-only interaction; if any action is blocked, the chart fails this guideline [@elavskyHowAccessibleMy2022]. **Stronger Test:** Verify that every special action has a clearly discoverable standard control path (not just an implicit gesture) and that the outcome matches the original interaction’s result [@w3c_understanding_multiple; @elavskyHowAccessibleMy2022].

## Practical remediations <!-- role: fix -->

- Add a standard UI control that performs the same action as the gesture (e.g., explicit filter controls, zoom buttons, or a non-gesture selection mechanism) and ensure it works with keyboard, screen reader, and touch [@elavskyHowAccessibleMy2022].
- Provide a search-based or direct-selection pathway that lets users jump to items or subsets without spatial gestures, while producing the same selection or filtered state [@elavskyHowAccessibleMy2022].
- Expose key actions through conventional, focusable controls with clear labels so users can discover and operate them without relying on pointer gestures or motion actuation [@elavskyHowAccessibleMy2022].
- If the interaction is essential but cannot be made operable across modalities, provide an alternate representation or workflow that supports the same task outcome without the complex interaction [@elavskyHowAccessibleMy2022].
