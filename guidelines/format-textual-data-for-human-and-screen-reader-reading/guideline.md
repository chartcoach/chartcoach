---
id: format-textual-data-for-human-and-screen-reader-reading
title: Format all textual data values into human-readable and screen-reader-friendly
  forms
bibliography: references.bib
description: Present numbers, units, and terms in readable formats for sighted readers
  and in comfortably parsable phrases for screen readers.
labels:
- chart:any
- task:read
- visual:text
- impact:accessibility
- data:any
- audience:all
- disability:cognitive
- disability:blindness
- assistive:screen-reader
---

## Human-readable text formatting for data labels and accessibility text <!-- role: advice -->

Format every textual data value shown in labels, axes, annotations, legends, and tables into a human-readable form and provide an equivalent screen-reader-friendly phrasing for accessibility text. Avoid raw or unusually formatted values that are hard to parse (for example long ungrouped numbers) by either sighted readers or screen readers.

## Reduced cognitive and parsing labor through readable value formats <!-- role: reason -->

When textual values are presented in compact, familiar formats, readers can interpret chart text quickly without doing mental decoding, and screen readers can announce the same content without forcing listeners to infer structure from dense digit strings or unfamiliar terms. This reduces the functional labor of reading chart text and supports understanding for people with cognitive disabilities as well as people relying on text-to-speech.

**Mechanism:** Human-readable formatting reduces cognitive load for decoding numbers and terms, while screen-reader-friendly phrasing improves auditory parsing by turning dense or unfamiliar text into language that can be comfortably heard and understood.

**Evidence:** Unusual words and unfamiliar phrasing create understanding barriers unless definitions or explanations are provided, supporting the need to transform hard-to-parse textual content into understandable forms for diverse readers and assistive technology users [@misc{w3c_understanding_unusual}]. A synthesized accessibility heuristic set for data visualizations includes the requirement that textual data be human-readable and comfortably parsable by screen readers to reduce user labor in data interfaces [@elavskyHowAccessibleMy2022].

**Notes:** This applies to all textual chart elements, including axis tick labels where automated formatting support is often missing in authoring tools [@elavskyHowAccessibleMy2022].

## Where human-readable data text matters in visualization interfaces <!-- role: context -->

- **User Goal:** Read and interpret chart text (values, ranges, categories, and takeaways) without extra decoding effort.
- **Task:** Identify magnitudes, compare values, and understand annotations or labels conveyed through text.
- **Data:** Numeric values (especially large magnitudes), abbreviations, jargon, acronyms, or unusually formatted strings.
- **Chart Setting:** Any chart that renders text in axes, labels, legends, tables, or annotation callouts, including interfaces that expose values via accessibility labels or alternative text.
- **Audience:** Mixed audiences including people with cognitive disabilities and screen reader users.
- **Success Criterion:** Text can be understood visually and announced by a screen reader without requiring the user to translate dense formats or unfamiliar terms.

## When you might not follow the exact formatting pattern <!-- role: exceptions -->

**Break it when:** The exact raw value format is itself the object of interpretation and changing it would alter meaning. **Why:** Transforming the representation could remove important precision or encoding needed for the user’s intended reading of that specific textual artifact.

## Tradeoffs of making text more readable <!-- role: costs -->

**Sacrifice:** Some precision or compactness may be lost when converting raw values into rounded, abbreviated, or explanatory formats. **Risk:** Over-formatting can obscure exact values or introduce ambiguity if users need the original representation. **Mitigation:** Keep a path to the exact underlying value in accompanying text channels while still presenting a readable primary form.

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Displaying long raw numbers (for example, ungrouped digit strings) directly in axes, labels, or tables. **Why it fails:** Readers must perform extra decoding and screen readers may announce the value in a way that is slow or hard to understand [@elavskyHowAccessibleMy2022].
- **Mistake:** Leaving jargon, acronyms, or unusual terms unexplained in chart text or accessibility text. **Why it fails:** Unfamiliar wording creates comprehension barriers, especially for people with cognitive disabilities and for screen reader users who cannot easily infer meaning from context [@misc{w3c_understanding_unusual}].

## Fast ways to detect unreadable chart text <!-- role: check -->

**Failure Sign:** Axis ticks, labels, or accessibility text contain dense digit strings, unexplained acronyms, or unusually formatted words that are hard to read aloud. **Quick Check:** Read every textual value in the chart out loud; if it sounds cumbersome or ambiguous, it is likely not screen-reader-friendly. **Stronger Test:** Use a screen reader to navigate the chart’s available text alternatives and confirm values are announced as comfortably understandable phrases rather than long, difficult-to-parse strings [@elavskyHowAccessibleMy2022].

## Practical fixes for unreadable textual data values <!-- role: fix -->

- Format large magnitudes into compact, conventional human-readable forms in visible text while preserving meaning.
- Provide screen-reader-friendly phrasings for the same values in accessibility labels and alternative text so they can be comfortably announced [@elavskyHowAccessibleMy2022].
- Expand or define unusual words, jargon, idioms, and acronyms in nearby text or provided explanations so the terminology is understandable [@misc{w3c_understanding_unusual}].
- Ensure the formatted text is applied consistently across axes, labels, annotations, legends, and tables so users do not have to relearn parsing rules within the same visualization [@elavskyHowAccessibleMy2022].
