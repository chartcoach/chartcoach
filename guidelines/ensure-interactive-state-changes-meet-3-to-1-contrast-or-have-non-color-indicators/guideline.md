---
id: ensure-interactive-state-changes-meet-3-to-1-contrast-or-have-non-color-indicators
title: Ensure interactive state changes reach 3:1 contrast against the previous state
  (or add a non-color indicator)
bibliography: references.bib
description: Make hover, focus, and selection states clearly perceivable by meeting
  a 3:1 contrast change from the prior state or adding a redundant non-color cue.
labels:
- chart:interactive
- task:navigate
- visual:color
- impact:accessibility
- data:any
- audience:general
- a11y:operable
- a11y:perceivable
---

## Interactive state changes must be clearly distinguishable <!-- role: advice -->

When an interactive element changes state (hover, focus, selection), ensure the new state has at least 3:1 contrast against the previous state, or provide a clearly perceivable non-color indicator of the state change. Prefer using both a color change and a non-color cue redundantly.

## Why state-change contrast affects operability <!-- role: reason -->

If state changes are hard to perceive, users cannot reliably discover what is interactive or confirm what they have focused or selected, which blocks navigation and control even when input methods like keyboard are available.

**Mechanism:** A distinct state-change signal lets users detect focus and selection transitions, supporting discoverability and confirmation of control state during interaction.

**Evidence:** User-interface components and graphical objects require at least 3:1 contrast against adjacent colors to remain distinguishable, supporting low-vision access to interactive affordances and states [@w3c_understanding_non_text_2]. Implementations that add explicit focus handling and semantic interaction affordances support accessible keyboard and screen reader operation of interactive chart elements [@github_visa_chart]. Chart auditing heuristics treat state-change clarity as a key intersection of perceivability and operability in visualization accessibility evaluation [@elavskyHowAccessibleMy2022].

**Notes:** Contrast change is evaluated between the element’s prior and new states when color is the primary state signal.

## When to apply this to interactive charts and controls <!-- role: context -->

- **User Goal:** Detect what can be interacted with and confirm focus/selection changes.
- **Task:** Operate interactive chart features such as highlighting, filtering, selecting, or navigating marks and controls.
- **Data:** Any data type where interaction changes the displayed state of marks or controls.
- **Chart Setting:** Interactive visualizations with hover, focus, active, selected, or pressed states on marks, legend items, buttons, or other controls.
- **Audience:** General audiences, including people with low vision and people navigating by keyboard or assistive technologies.
- **Success Criterion:** State changes are consistently perceivable and support reliable interaction without relying on color alone.

## When you can skip the 3:1 state-change contrast requirement <!-- role: exceptions -->

**Break it when:** The state change is not communicated by color difference because a clear additional indicator is provided (for example, a stroke thickness change of at least 2px, a dash pattern, or an added marker). **Why:** The non-color indicator carries the state-change signal, so state perception does not depend on color contrast alone [@elavskyHowAccessibleMy2022].

## Tradeoffs of stronger state-change indicators <!-- role: costs -->

**Sacrifice:** Additional visual complexity and potential visual clutter from redundant cues. **Risk:** Overemphasized state styling can distract from the data marks or overwhelm dense views. **Mitigation:** Keep the non-color indicator consistent and limited to interaction states rather than the default view.

## Common ways interactive state changes fail <!-- role: mistakes -->

- **Mistake:** Indicating hover/focus/selection only by subtle opacity, saturation, or hue shifts that are hard to see. **Why it fails:** Users may not perceive the state transition, reducing discoverability and confirmation of interaction [@elavskyHowAccessibleMy2022].
- **Mistake:** Relying on color-only state changes without any redundant cue. **Why it fails:** Users who cannot reliably perceive the color difference may miss the interaction state entirely [@elavskyHowAccessibleMy2022].

## How to quickly check interactive state-change visibility <!-- role: check -->

**Failure Sign:** Hover, focus, or selection appears unchanged or only subtly different from the default state. **Quick Check:** Compare the element’s default and interactive state colors and verify the difference is clearly visible without relying on fine color discrimination. **Stronger Test:** Measure contrast between the element’s prior and new states and confirm it is at least 3:1, or verify a non-color indicator is present and clearly perceivable [@w3c_understanding_non_text_2; @elavskyHowAccessibleMy2022].

## Ways to fix low-contrast interactive state changes <!-- role: fix -->

- Increase the state-change contrast so the interactive state differs from the previous state by at least 3:1 [@w3c_understanding_non_text_2].
- Add a redundant non-color state indicator such as a stroke thickness increase of at least 2px, a dash pattern, or an added marker [@elavskyHowAccessibleMy2022].
- Ensure keyboard focus styling applies the same state-change visibility treatment used for pointer hover, so state changes are perceivable during keyboard navigation [@elavskyHowAccessibleMy2022; @github_visa_chart].
- Implement explicit focus and interaction access handling so interactive chart elements expose clear interactive semantics and consistent state feedback across input methods [@github_visa_chart].
