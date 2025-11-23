---
id: ensure-semantic-validity
title: Use Semantically Valid Elements for Interactive Components
bibliography: references.bib
description: Ensure chart elements use correct semantic roles (e.g., buttons for actions)
  to be programmatically determinable by assistive technologies.
labels:
- impact:accessibility
- impact:robustness
- task:audit
- visual:interaction
- source:chartability
---

## The Rule <!-- role: advice -->
Ensure all chart components are semantically valid according to modern standards; specifically, if an element functions like a button or control, it must be semantically defined as that specific element.

## The Logic <!-- role: reason -->
Assistive technologies rely on code structures to convey meaning. User interface components must have programmatically determinable names, roles, and states so that tools can identify what the control is, what it does, and its current state [@w3c_understanding_name]. Without valid semantics, a user cannot effectively operate the interface [@elavsky_how_2022].

*   **The Principle:** Robustness (POUR+CAF)
*   **The Evidence:** [@w3c_understanding_name], [@elavsky_how_2022]

## Where to Apply <!-- role: context -->
This applies to any data visualization or interface that includes interactive elements.

*   **User Goal:** Navigating or operating controls within a data interface.
*   **Data Type:** Interactive visualizations (web-based charts, dashboards).
*   **Audience:** Users of assistive technologies, particularly screen readers.

## When to Break It <!-- role: exceptions -->
There are strictly limited scenarios where semantic roles should be omitted.

*   **Scenario:** Purely decorative elements.
*   **Reason:** Elements that provide no information or functionality should not have semantic roles that confuse the accessibility tree.

## The Price <!-- role: costs -->
Implementing robust semantics requires effort beyond visual design.

*   **The Sacrifice:** Developers must understand and implement proper HTML semantics or ARIA roles rather than relying on generic container tags.
*   **The Risk:** Automated testing alone captures only a portion of errors; manual screen reader verification is required to ensure true robustness [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
Developers often rely on visual cues rather than code structure.

*   **The Wrong Fix:** Using a generic element (like a `div` or `span`) with a click handler without assigning it a `role="button"`.
*   **Why it fails:** The element functions as a button visually but reports itself as generic text to assistive technology, making it semantically invalid [@elavsky_how_2022].

## How to Check <!-- role: check -->
Validation requires a mix of automated scanning and manual verification.

*   **Visual Sign:** There is often no visual sign of semantic failure; the interface may look correct but fail for screen readers.
*   **The Test:** Run automated tools such as Axe-core or Accessibility Insights [@deque_axe_devtools]. Must also manually verify with a screen reader that the element announces its role correctly [@elavsky_how_2022].

## How to Fix <!-- role: fix -->
Correct the code to match the element's function.

*   **Quick Fix:** Replace generic tags with native HTML interactive elements (e.g., use `<button>` tags for buttons).
*   **Best Fix:** Ensure all custom controls expose programmatically determinable names, roles, and values to assistive technologies [@w3c_understanding_name].
