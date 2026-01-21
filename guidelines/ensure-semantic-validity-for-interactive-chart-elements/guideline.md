---
id: ensure-semantic-validity-for-interactive-chart-elements
title: Use Semantically Correct Elements for All Chart Interactions
bibliography: references.bib
description: Ensure every interactive or meaningful chart component exposes a valid
  programmatic name, role, and state so it works reliably with assistive technologies.
labels:
- chart:interactive
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:assistive-technology-users
- category:robust
- source:chartability
---

## The Rule <!-- role: advice -->

Implement chart UI using semantically valid elements so each component’s **name, role, and state/value** are programmatically determinable; do not make something behave like a button while exposing it as something else.

## The Logic <!-- role: reason -->

Semantically invalid structures prevent assistive technologies from reliably identifying what an interactive component is, what it does, and what state it is in, which breaks robust interoperability. Chartability explicitly flags “semantically invalid use of document elements” as a Robust accessibility failure and requires conformance to modern standards plus verification with a screen reader [@elavskyHowAccessibleMy2022].

- **The Principle:** Programmatic determinability of UI semantics (name, role, value)
- **The Evidence:** WCAG’s Name, Role, Value requirement [@w3c_understanding_name]

## Where to Apply <!-- role: context -->

Use this rule whenever your visualization includes interactive or stateful components.

- **User Goal:** Operating chart functionality (e.g., selecting, filtering, toggling, navigating) via assistive technology
- **Data Type:** Any (the issue is about UI semantics, not the dataset)
- **Audience:** People using assistive technologies (especially screen readers), plus auditors validating robustness [@elavskyHowAccessibleMy2022]

## When to Break It <!-- role: exceptions -->

- **Scenario:** There are no meaningful or interactive components (purely decorative visuals with no information or functionality to convey programmatically).
- **Reason:** If nothing conveys meaning or supports interaction, there may be no UI semantics to expose (though Chartability still expects screen reader verification for the overall experience) [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** More development effort to align behavior with correct semantics and to resolve automated validation findings.
- **The Risk:** Automated tools may report issues that require manual investigation, and you still must do a screen reader verification pass to confirm real behavior [@elavskyHowAccessibleMy2022] [@deque_axe_devtools].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying only on automated scans and assuming “no issues found” means the chart works with assistive tech.
- **Why it fails:** Chartability notes automated checks are only an initial step and may only “pass” once a screen reader test has verified the experience [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Creating custom controls that behave like buttons/toggles but are exposed with mismatched semantics (e.g., “looks/acts clickable” but is not semantically a button).
- **Why it fails:** Assistive technologies depend on correct programmatic name/role/state to announce and operate components consistently [@w3c_understanding_name].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart “works” with mouse/touch, but assistive technology output is ambiguous or misleading about what elements are and whether they are interactive.
- **The Test:** Run automated semantic/markup checks (e.g., axe DevTools) and then verify behavior with a screen reader, as required by Chartability [@deque_axe_devtools] [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace semantically incorrect interactive constructs with semantically correct ones so the exposed role matches the behavior (e.g., interactive control exposed as the correct kind of control), then re-run automated checks [@deque_axe_devtools] [@elavskyHowAccessibleMy2022].
- **Best Fix:** Ensure every interactive component exposes correct programmatic name, role, and state/value end-to-end (standards-valid semantics plus confirmation via screen reader testing) [@w3c_understanding_name] [@elavskyHowAccessibleMy2022].
