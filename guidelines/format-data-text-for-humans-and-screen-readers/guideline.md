---
id: format-data-text-for-humans-and-screen-readers
title: Format Data Text for Humans and Screen Readers
bibliography: references.bib
description: Format all numeric and textual data in labels and descriptions into human-readable
  forms, including screen-reader-friendly versions.
labels:
- chart:any
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:all
- source:chartability
---

## The Rule <!-- role: advice -->

Format all displayed data text (axes, data labels, annotations, tables, legends, and descriptions) into human-readable forms, and provide screen-reader-friendly phrasing for the same values.

## The Logic <!-- role: reason -->

Unusual, overly technical, or unformatted text (e.g., long raw numbers) increases interpretation effort and can be harder to parse via assistive technologies; providing understandable equivalents reduces user labor and supports comprehension [@elavskyHowAccessibleMy2022]. WCAG guidance emphasizes helping users understand unusual words by providing definitions or explanations, which aligns with ensuring chart text is presented in an understandable form rather than raw or jargon-like encodings [@w3c_understanding_unusual; @elavskyHowAccessibleMy2022].

- **The Principle:** Reduce cognitive and functional labor by making textual information understandable and parseable.
- **The Evidence:** [@w3c_understanding_unusual; @elavskyHowAccessibleMy2022]

## Where to Apply <!-- role: context -->

This advice is designed for moments when users must read values directly from text within a data visualization or its accessible alternatives [@elavskyHowAccessibleMy2022].

- **User Goal:** Understanding and interpreting values from chart text (e.g., reading axis ticks, labels, table entries, or annotation numbers).
- **Data Type:** Any data shown as text (especially large numbers or dense labeling).
- **Audience:** People with cognitive accessibility needs and people using screen readers or other assistive technologies [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must present the exact raw value as originally encoded (e.g., an identifier-like string where formatting would change meaning).
- **Reason:** Reformatting could alter the meaning or make the value ambiguous compared to the source representation.

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional authoring/engineering effort to create and maintain both a visual-friendly format and a screen-reader-friendly phrasing [@elavskyHowAccessibleMy2022].
- **The Risk:** Inconsistent formatting across axes/labels/descriptions can introduce confusion if different parts of the visualization describe the same value differently.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Leaving raw numeric strings everywhere (e.g., `6500000000`) and assuming users will mentally convert them.
- **Why it fails:** It increases cognitive load and can be difficult to read comfortably, especially when repeated across axes or labels [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Using a compact visual abbreviation (e.g., `6.5b`) but not providing a screen-reader-friendly equivalent.
- **Why it fails:** The value may not be read as intended by screen readers, reducing understandability and comfort in non-visual access paths [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** You see raw, dense, or unusual text in axes/labels/annotations/tables (e.g., long unseparated numerals) rather than a readable format [@elavskyHowAccessibleMy2022].
- **The Test:** Inspect every place text appears (axes, labels, annotations, tables, legends) and verify each value has (1) a visually understandable format and (2) a screen-reader-friendly phrasing for labels/alt text where applicable (e.g., ensure `6500000000` is presented as `6.5b` visually and as “six point five billion” for screen readers) [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reformat displayed values into a readable visual form (e.g., convert `6500000000` into `6.5b`) everywhere they appear in the chart text [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide parallel, screen-reader-friendly phrasing for the same values wherever they are used in screen reader labels and alternative text (e.g., “six point five billion”), while keeping the visible formatting optimized for human reading [@elavskyHowAccessibleMy2022].
