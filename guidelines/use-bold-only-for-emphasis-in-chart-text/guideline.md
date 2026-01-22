---
id: use-bold-only-for-emphasis-in-chart-text
title: Use bold type only for titles or selective emphasis in chart annotations
bibliography: references.bib
description: Keep most chart text in regular or medium weight and reserve bold for
  hierarchy and emphasis.
labels:
- chart:generic
- task:focus
- visual:typography
- impact:hierarchy
- data:generic
- audience:general
- scope:font-weight
---

## Reserve bold for hierarchy, not for all text <!-- role: advice -->

Set most chart and table text in regular (or medium) weight, and use bold only for titles or to emphasize a small number of words or key values.

## Overuse of bold reduces readability and flattens hierarchy <!-- role: reason -->

Bold weight increases visual salience, so it should encode importance; when too much text is bold, the hierarchy collapses and longer text blocks become harder to read comfortably.

**Mechanism:** Weight contrast creates an attention signal; limiting bold preserves a clear “most important vs. supporting” structure and avoids making paragraphs feel heavy.

**Evidence:** Regular/medium weights are recommended as easiest to read for descriptions, notes, and annotations, with bold positioned as a tool for titles and sparse emphasis [@muth_fonts_2022].

**Notes:** Weight naming differs across type systems, including numeric weights where regular is commonly 400 and bold 700 [@muth_fonts_2022].

## Apply whenever you have multiple text roles in the same graphic <!-- role: context -->

- **User Goal:** Understand what to read first and what is supporting detail.
- **Task:** Scan titles, annotations, callouts, tooltips, and table highlights.
- **Data:** Any.
- **Chart Setting:** Annotated charts, dashboards, tables with highlighted values.
- **Audience:** General audiences; readers on small screens.
- **Success Criterion:** Clear, consistent hierarchy with easy-to-read longer text.

## Use stronger weights more broadly only in very short, display-like text <!-- role: exceptions -->

**Break it when:** The visualization contains only a few very short text elements (e.g., a headline-only graphic) and you intentionally want a forceful, attention-grabbing tone. **Why:** The readability penalty primarily shows up in longer text blocks and dense label sets [@muth_fonts_2022].

## Emphasis options shrink when bold is restricted <!-- role: costs -->

**Sacrifice:** You may need other hierarchy tools (size, spacing, color) instead of relying on bold everywhere. **Risk:** Under-emphasizing key takeaways can make the chart feel flat. **Mitigation:** Use bold sparingly but consistently for the same semantic role (e.g., only the key number) [@muth_fonts_2022].

## Don’t bold paragraphs to “make them readable” <!-- role: mistakes -->

- **Mistake:** Setting descriptions, notes, or many labels in bold by default. **Why it fails:** It makes the text block heavier and reduces the contrast needed to signal what is truly important [@muth_fonts_2022].

## Audit hierarchy by squinting and by role consistency <!-- role: check -->

**Failure Sign:** Everything looks equally loud, or the description competes with the title. **Quick Check:** Squint at the chart and see whether only the intended elements stand out. **Stronger Test:** List your text roles (title, axis labels, annotation, note) and verify each role uses a consistent weight system across the graphic [@muth_fonts_2022].

## Shift hierarchy to size, spacing, and selective bolding <!-- role: fix -->

- Change annotation and note text to regular or medium weight.
- Bold only the one or two words or numbers that carry the takeaway.
- Increase title size rather than bolding all surrounding text.
- Use color contrast carefully to separate supporting text from primary labels without resorting to bold everywhere [@muth_fonts_2022].
