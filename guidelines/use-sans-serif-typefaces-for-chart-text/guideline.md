---
id: use-sans-serif-typefaces-for-chart-text
title: Use a sans-serif typeface for chart and table text by default
bibliography: references.bib
description: Default to a normal-width sans-serif typeface to keep chart and table
  text easy to scan and read.
labels:
- chart:generic
- task:read
- visual:typography
- impact:clarity
- data:generic
- audience:general
- scope:typography
---

## Prefer sans-serif for labels, ticks, and table text <!-- role: advice -->

Use a sans-serif typeface for most chart and table text (axis ticks, labels, tooltips, notes) unless you have a specific reason to use a serif.

## Sans-serif supports fast scanning of short chart text <!-- role: reason -->

In charts and tables, readers typically scan short fragments and many numbers rather than reading long passages, so a clean, familiar sans-serif reduces visual complexity and supports quick recognition of labels and values.

**Mechanism:** Familiar, low-ornament letterforms and consistent stroke patterns make small UI-like text (ticks, labels, tooltips) easier to skim across many items.

**Evidence:** Sans-serif is presented as the common, readability-first default for web-based data visualizations, with serif framed as the less common choice that is mainly useful when deliberately aiming for a traditional or “classy” feel [@muth_fonts_2022].

**Notes:** Serifs can still work in data visualization, especially for titles, but sans-serif is the safest default when unsure [@muth_fonts_2022].

## Use when the graphic is read as an interface, not a paragraph <!-- role: context -->

- **User Goal:** Read values and categories quickly without friction.
- **Task:** Scan axis ticks, legend labels, tooltip fields, table cells, and short annotations.
- **Data:** Any mix, especially numeric-heavy displays.
- **Chart Setting:** Web or screen-first charts; dense layouts with many small text elements.
- **Audience:** General audiences who expect common UI typography.
- **Success Criterion:** Fast, low-effort readability across many small text items.

## Use serif only when you need a deliberate traditional tone or brand match <!-- role: exceptions -->

- **Break it when:** A serif typeface is central to the publication’s identity and you need the visualization to match that voice (often in titles). **Why:** Visual consistency and intentional tone can outweigh the default convention if readability remains acceptable [@muth_fonts_2022].
- **Break it when:** You intentionally want a more traditional, serious, or literary feel for the entire visualization and can keep text legible. **Why:** Serif styling can differentiate the work and signal a specific tone [@muth_fonts_2022].

## Trade off distinctiveness for a safer default <!-- role: costs -->

**Sacrifice:** A common sans-serif choice can feel generic and make the visualization less distinctive. **Risk:** Over-relying on the default can miss opportunities to align with a strong brand or editorial tone. **Mitigation:** Use brand type selectively (often in titles) while keeping the bulk of small text in a highly legible face [@muth_fonts_2022].

## Don’t pick decorative categories just because they look “unique” <!-- role: mistakes -->

- **Mistake:** Using script, handwritten, slab, or monospace styles as a default for chart labels. **Why it fails:** These categories are uncommon in data visualization and can reduce scan-ability or add an unintended vibe that competes with the data [@muth_fonts_2022].

## Check readability by scanning, not reading <!-- role: check -->

**Failure Sign:** You have to slow down to decipher tick labels, legend items, or table values. **Quick Check:** Shrink the chart to the smallest expected viewing size and see whether labels remain instantly recognizable. **Stronger Test:** Ask someone unfamiliar with the chart to read out a few values and categories quickly without zooming [@muth_fonts_2022].

## Improve legibility without changing the whole design language <!-- role: fix -->

- Switch labels, ticks, tooltips, and table cells to a normal-width sans-serif family used for UI text.
- Keep a serif only for the headline if you need a traditional or editorial tone.
- Replace decorative faces with a neutral sans-serif and use size/weight/color for hierarchy instead.
- If you must use a distinctive face, limit it to large display text where legibility is less fragile [@muth_fonts_2022].
