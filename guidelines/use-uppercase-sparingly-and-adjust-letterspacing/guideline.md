---
id: use-uppercase-sparingly-and-adjust-letterspacing
title: Use uppercase sparingly in chart text, and add letter spacing if you do
bibliography: references.bib
description: Limit all-caps to short labels and compensate with tracking, size, and
  weight so it stays readable and balanced.
labels:
- chart:generic
- task:scan
- visual:typography
- impact:readability
- data:categorical
- audience:general
- scope:capitalization
---

## Limit uppercase to short, high-level labels and tune spacing <!-- role: advice -->

Use uppercase text only for a few short words (such as small headers or group labels), and increase letter spacing when you set text in all caps.

## All-caps reduces word-shape cues and changes layout needs <!-- role: reason -->

Uppercase removes the ascenders and descenders that help readers recognize word shapes, making text slower to read; it also expands text width, so spacing and size adjustments are needed to avoid dense, overlong labels.

**Mechanism:** Mixed-case text provides distinctive word silhouettes, while all-caps turns words into more uniform rectangles; added tracking and careful size/weight adjustments restore some readability and visual balance.

**Evidence:** Uppercase is described as harder to read and wider than sentence case, with recommended adjustments such as added letter spacing and compensating size/weight changes; uppercase is framed as best reserved for short UI-like labels (filters, headers, group labels, some axis labels, map region labels) [@muth_fonts_2022].

**Notes:** Uppercase can look tidy and distinct, which makes it useful for elements meant to stand apart—if used sparingly [@muth_fonts_2022].

## Apply to UI-like labels, group headers, and map region labels <!-- role: context -->

- **User Goal:** Identify structural groupings or UI controls quickly.
- **Task:** Scan short labels (filters, tooltip field names, small headers).
- **Data:** Often categorical labels and section headings.
- **Chart Setting:** Dashboards, tooltips, tables, and maps with region names.
- **Audience:** General audiences; skim readers.
- **Success Criterion:** Uppercase elements are easy to find but do not harm overall readability.

## Avoid uppercase for long phrases or dense axis labeling <!-- role: exceptions -->

- **Break it when:** The label text is long or numerous (e.g., many category labels). **Why:** The readability penalty and width expansion compound quickly, causing crowding and slower scanning [@muth_fonts_2022].
- **Break it when:** Precise reading of sentences is required (e.g., explanatory notes). **Why:** Mixed case supports faster, more comfortable reading for longer text [@muth_fonts_2022].

## Uppercase consumes space and can over-signal importance <!-- role: costs -->

**Sacrifice:** Uppercase typically requires more horizontal room, which can force smaller sizes or truncation. **Risk:** Too many all-caps elements make everything feel equally important and reduce hierarchy. **Mitigation:** Confine uppercase to one semantic role and keep the wording short [@muth_fonts_2022].

## Don’t convert lots of labels to caps to look “tidier” <!-- role: mistakes -->

- **Mistake:** Setting many axis labels or long annotations in uppercase without adjusting spacing. **Why it fails:** The text becomes wider and denser while also being harder to read, creating crowding and visual fatigue [@muth_fonts_2022].

## Confirm caps remain readable and not overly dense <!-- role: check -->

**Failure Sign:** Uppercase labels look cramped, dominate the chart, or force truncation/wrapping. **Quick Check:** Toggle between sentence case and uppercase and see whether uppercase still reads instantly. **Stronger Test:** If using uppercase, increase letter spacing and then compare the visual length and stroke presence against the original mixed-case label to ensure balance [@muth_fonts_2022].

## Prefer mixed case, or compensate caps with spacing and sizing <!-- role: fix -->

- Switch long labels back to sentence case.
- Add letter spacing (tracking) to uppercase text so it does not appear dense.
- Reduce uppercase font size slightly and increase weight if needed to maintain stroke presence while controlling width.
- Replace uppercase with other hierarchy signals (size, weight, color) when the text must stay long [@muth_fonts_2022].
