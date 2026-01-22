---
id: use-semantic-html-and-valid-roles-for-interactive-chart-controls
title: Implement interactive chart controls with semantic HTML and valid programmatic
  name/role/value
bibliography: references.bib
description: Ensure every interactive element in a visualization exposes a valid semantic
  role and programmatic name, state, and value so assistive technologies can interpret
  and operate it.
labels:
- chart:interactive
- task:navigate
- visual:interaction
- impact:accessibility
- data:any
- audience:all
- principle:robust
- disability:screen-reader
---

## Semantic validity for interactive chart elements <!-- role: advice -->

Implement every interactive element in the visualization using semantically correct document elements so its role, name, and value are programmatically determinable. If a component behaves like a button, it must be implemented and exposed as a button to assistive technologies. [@elavskyHowAccessibleMy2022]

## Why semantic validity enables assistive technology interoperability <!-- role: reason -->

Assistive technologies rely on the programmatic semantics of user interface components to identify what each component is, what it does, and what its current state is; semantically invalid controls can be present visually but opaque or misleading to assistive technology users. When semantics are valid, automated auditing tools can detect many violations early, but the experience still must be verified in assistive technology because tooling is incomplete and interaction behavior can diverge from static code signals. [@elavskyHowAccessibleMy2022]

**Mechanism:** Correct semantics expose consistent role and state information, allowing assistive technologies to announce and operate interactive components reliably.

**Evidence:** User interface components must have programmatically determinable name, role, and value, including states for custom controls, so assistive technologies can identify and interact with them. [@w3c_understanding_name] Automated accessibility testing tools can flag semantic and ARIA-related issues but are an initial screen rather than a complete verification of real assistive technology behavior. [@deque_axe_devtools; @elavskyHowAccessibleMy2022]

**Notes:** Passing automated checks is not sufficient if a screen reader cannot perceive the control’s role/state changes during interaction. [@elavskyHowAccessibleMy2022]

## When to apply semantic validation in visualizations <!-- role: context -->

- **User Goal:** Understand and operate the visualization’s controls and read their current states using assistive technologies.
- **Task:** Navigate, select, filter, toggle, or otherwise interact with chart elements and UI controls.
- **Data:** Any dataset; applicability is driven by interaction rather than data type.
- **Chart Setting:** Web-based or document-based visualizations with custom marks, overlays, tooltips, filters, legends, or bespoke interaction patterns.
- **Audience:** Users who rely on assistive technologies and those auditing for accessibility compliance and usability.
- **Success Criterion:** Every interactive component has correct role semantics and exposes programmatic name/role/value such that assistive technologies can interpret and operate it consistently. [@w3c_understanding_name; @elavskyHowAccessibleMy2022]

## When not to follow it <!-- role: exceptions -->

**Break it when:** There are no interactive components and no UI elements that function as controls. **Why:** The guideline targets mismatches between behavior and control semantics, which do not occur without interactive functionality. [@elavskyHowAccessibleMy2022]

## Tradeoffs and risks of strict semantic enforcement <!-- role: costs -->

**Sacrifice:** Additional implementation effort when building bespoke interactions rather than using native controls.\
**Risk:** Over-reliance on automated tools can create false confidence if behavior is not verified with assistive technologies. [@elavskyHowAccessibleMy2022]\
**Mitigation:** Treat automated scans as initial screening and confirm behavior with assistive technology testing. [@elavskyHowAccessibleMy2022]

## Common semantic anti-patterns in interactive charts <!-- role: mistakes -->

- **Mistake:** Implementing a control that behaves like a button but exposing it as a non-button element without an appropriate role. **Why it fails:** Assistive technologies may not announce it as an operable control or may announce the wrong role, preventing reliable operation and comprehension. [@w3c_understanding_name; @elavskyHowAccessibleMy2022]
- **Mistake:** Passing automated checks and stopping there. **Why it fails:** Tooling may miss issues that only appear in real assistive technology interaction flows and state announcements. [@deque_axe_devtools; @elavskyHowAccessibleMy2022]

## Quick tests for semantic invalidity <!-- role: check -->

**Failure Sign:** A screen reader announces an interactive component generically (or with an incorrect role) and does not announce state changes after interaction. [@elavskyHowAccessibleMy2022]\
**Quick Check:** Run an automated accessibility scan to detect semantic/ARIA issues and markup problems as an initial screen. [@deque_axe_devtools; @elavskyHowAccessibleMy2022]\
**Stronger Test:** Verify with a screen reader that each interactive element is announced with an appropriate role and that changes in state/value are announced during interaction. [@w3c_understanding_name; @elavskyHowAccessibleMy2022]

## Remediations for semantically invalid chart controls <!-- role: fix -->

- Implement controls using semantically appropriate elements so behavior matches role (for example, controls that act like buttons are exposed as buttons). [@w3c_understanding_name; @elavskyHowAccessibleMy2022]
- Ensure each interactive component exposes a programmatic name and any relevant state/value so assistive technologies can announce what it is and what changed. [@w3c_understanding_name; @elavskyHowAccessibleMy2022]
- Use automated accessibility testing tools to identify semantic invalidity early, then validate with assistive technology interaction testing before considering the issue resolved. [@deque_axe_devtools; @elavskyHowAccessibleMy2022]
- Validate the document markup to reduce semantic inconsistencies that can interfere with assistive technology interpretation. [@elavskyHowAccessibleMy2022]
