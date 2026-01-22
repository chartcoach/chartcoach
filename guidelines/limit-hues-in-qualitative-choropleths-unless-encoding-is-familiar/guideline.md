---
id: limit-hues-in-qualitative-choropleths-unless-encoding-is-familiar
title: Limit qualitative choropleths to a few hues unless the category-to-color mapping
  is already familiar
bibliography: references.bib
description: Too many category colors overload memory; keep qualitative maps to a
  small set unless readers already know the encoding.
labels:
- chart:choropleth
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:foundational
---

## Use only a few distinct hues for qualitative choropleths unless readers already know the colors <!-- role: advice -->

Keep qualitative (categorical) choropleths to as few colors as possible so readers can remember what each color means. Use more hues only when the audience already recognizes the category-to-color encoding.

## Category colors compete with working memory <!-- role: reason -->

Qualitative palettes require viewers to memorize arbitrary color-category pairings. As the number of hues increases, readers must consult the legend more often, slowing comprehension and increasing errors; familiar encodings reduce that burden.

**Mechanism:** Legend lookups increase when color meanings are not easily retained; limiting hues reduces cognitive load.

**Evidence:** Using fewer colors in qualitative schemes is recommended because more colors make it harder for readers to remember meanings; three colors are suggested as a low-friction choice, with more allowed when the encoding is already known (e.g., political party colors) [@muth_choroplethmaps_2018].

**Notes:** Qualitative colors should not resemble sequential/diverging scales when the data is unordered.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Identify which category each region belongs to.
- **Task:** Classify regions into groups without implying order.
- **Data:** Nominal categories with no intrinsic ranking.
- **Chart Setting:** Map with a legend that readers will consult to decode categories.
- **Audience:** General readers unfamiliar with bespoke color-category mappings.
- **Success Criterion:** Readers can correctly name a region’s category with minimal legend checking.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The audience already knows the color encoding (e.g., party colors in election maps). **Why:** Familiarity reduces the need to repeatedly consult the legend [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Fewer hues may require collapsing categories or changing the framing of the story. **Risk:** Too few hues can hide meaningful distinctions if categories are genuinely important. **Mitigation:** Use tooltips to provide the category name so color is not the only carrier.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using many qualitative hues for unfamiliar categories. **Why it fails:** Readers can’t retain the mapping and must constantly decode the legend [@muth_choroplethmaps_2018].
- **Mistake:** Choosing qualitative hues that look like a gradient. **Why it fails:** It implies an order that the categories do not have [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers keep returning to the legend to interpret the map. **Quick Check:** Hide the legend and ask someone to recall what each color means; if they can’t, there are too many colors. **Stronger Test:** Ask users to classify five random regions; frequent legend checks indicate overload.

## What to do instead <!-- role: fix -->

- Reduce the number of categories or group them into a smaller set of meaningful classes.
- Use tooltips to show the category name so color decoding is optional.
- Use labels for key regions when categories must be unambiguous.
- Switch to a non-map view if the primary task is category comparison rather than geography.
