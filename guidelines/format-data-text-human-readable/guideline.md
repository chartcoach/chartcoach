---
id: format-data-text-human-readable
title: Format Data Values for Human and Screen Reader Readability
bibliography: references.bib
description: Ensure text and numbers are formatted to be understandable visually (e.g.,
  '6.5b') and parsed correctly for screen readers (e.g., 'six point five billion').
labels:
- impact:accessibility
- impact:cognitive-load
- visual:text
- visual:axis
- data:numerical
- audience:screen-reader-users
---

## The Rule <!-- role: advice -->

Format all textual information—including data labels, axes, annotations, legends, and tables—into content that is immediately understandable (human-readable). Create specific versions of this text that can be comfortably read and parsed by screen readers (e.g., convert "6.5b" visually to "six point five billion" aurally).

## The Logic <!-- role: reason -->

This rule is based on the **Assistive** principle of Chartability, which requires interfaces to be intelligent and multi-sensory to reduce the cognitive and functional labor required of the user [@elavsky_how_2022]. Raw data values (like 6500000000) require significant mental effort to parse.
*   **The Principle:** Cognitive Load Reduction (Assistive).
*   **The Evidence:** Properly formatting text reduces barriers for people with cognitive disabilities and those using screen readers by defining jargon, idioms, and acronyms [@w3c_understanding_unusual]. Axis labels specifically often lack intelligent solutions to parse states into usable formats, representing a "low-hanging fruit" for accessibility improvements [@elavsky_how_2022].

## Where to Apply <!-- role: context -->

This advice applies to any text-heavy element within a data visualization.
*   **User Goal:** Reading specific values without performing mental math or counting zeros.
*   **Data Type:** Large integers, timestamps, abbreviations, acronyms, or technical jargon.
*   **Audience:** Users with cognitive disabilities and users relying on screen readers.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** The user task requires retrieving the exact, raw integer (e.g., financial auditing or scientific precision).
*   **Reason:** Summarized formats (like "6.5b") obscure precise values. However, even in this case, the screen reader announcement should be formatted to be pronounceable rather than a digit-by-digit readout if possible.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Implementing dual-formatting (one string for visual space, one string for aural announcement) requires additional development effort and more complex code logic.
*   **The Risk:** Aggressive abbreviation for visual readability may reduce precision or introduce ambiguity if not clearly defined.

## Common Mistakes <!-- role: mistakes -->

*   **The Visual-Only Fix:** Formatting a number as "6.5b" for both the visual label and the screen reader.
*   **Why it fails:** A screen reader may announce "six point five bee," which is ambiguous or confusing compared to "six point five billion."
*   **The Raw Dump:** Displaying raw database values (e.g., `2021-01-01T00:00:00`) directly on axes.
*   **Why it fails:** It forces the user to parse the format manually to find the relevant information (e.g., just the year).

## How to Check <!-- role: check -->

*   **Visual Sign:** Look for long strings of numbers (e.g., 1000000) or unformatted dates on axes and tooltips.
*   **The Test:** Inspect the element using a screen reader or an accessibility auditing tool. Does the voice output sound like natural language (e.g., "one million"), or is it reading characters/digits individually?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Apply standard number and date formatters (e.g., adding commas to thousands, shortening dates) to the visible text.
*   **Best Fix:** Programmatically generate two versions of the text: a concise version for visual display (e.g., "6.5b") and a fully expanded, spoken-word version for the accessible name/label (e.g., "six point five billion") [@elavsky_how_2022].
