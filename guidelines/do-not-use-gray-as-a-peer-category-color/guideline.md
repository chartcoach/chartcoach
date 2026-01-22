---
id: do-not-use-gray-as-a-peer-category-color
title: Avoid using gray as a normal category color when categories are equally important
bibliography: references.bib
description: "Reserve gray for de-emphasis so readers don\u2019t misinterpret a full-strength\
  \ category as secondary."
labels:
- chart:general
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:foundational
---

## Reserve gray for deemphasis, not for peer categories <!-- role: advice -->

Do not color an equally important category in gray while other equally important categories are in vivid hues. Use gray only when you intend that item to be read as less important or background context.

## Readers interpret gray as “secondary” because it signals reduced importance <!-- role: reason -->

Many readers have learned the convention that gray indicates “other,” “unknown,” or low priority, so using gray for a peer category silently changes the meaning of the category encoding.

**Mechanism:** Gray reduces saturation and salience, so it communicates a weaker status than nearby colored categories.

**Evidence:** Gray is treated as special in common data visualization conventions and is typically used for least-important categories (for example “miscellaneous,” “others,” “no data,” “no answer,” or “don’t know”), so using it as a peer category color creates misleading hierarchy [@muth_emphasize_color_2023].

**Notes:** If you “run out of colors,” that is a palette constraint problem, not a reason to assign gray to an equally important category [@muth_emphasize_color_2023].

## When gray-as-deemphasis matters most <!-- role: context -->

- **User Goal:** Correctly interpret category importance and grouping from color.
- **Task:** Compare multiple categories that should be treated as peers.
- **Data:** Categorical data with several important groups.
- **Chart Setting:** Legends or color keys where viewers infer meaning from color prominence.
- **Audience:** Broad audiences accustomed to gray-as-secondary conventions.
- **Success Criterion:** No category appears unintentionally “less important” due to color choice.

## When to break this rule <!-- role: exceptions -->

**Break it when:** A category truly is intended to be treated as “other/unknown/no response” or otherwise secondary. **Why:** In that case, gray communicates the intended lower priority and reduces distraction [@muth_emphasize_color_2023].

## Tradeoffs of avoiding gray as a peer color <!-- role: costs -->

**Sacrifice:** You may need a larger palette or a different chart structure to keep categories distinguishable. **Risk:** For many categories, adding more hues can increase visual complexity. **Mitigation:** Consider simplifying categories or changing the display so fewer distinct hues are required [@muth_emphasize_color_2023].

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Assigning gray to one of many key categories just because the palette is limited. **Why it fails:** Readers interpret that category as less important or as “other,” distorting the message [@muth_emphasize_color_2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers assume the gray category is less important, missing, or “other.” **Quick Check:** Ask a reader what gray means in the chart; if they infer lower importance and that is not intended, the encoding is wrong. **Stronger Test:** Temporarily recolor the gray category to a normal hue; if the chart’s perceived meaning changes substantially, gray was carrying unintended semantics [@muth_emphasize_color_2023].

## What to do instead <!-- role: fix -->

- Introduce additional non-gray hues so all peer categories have comparable visual weight.
- Group low-importance categories into an explicit “Other” bucket and color only that bucket gray.
- Reduce the number of categories shown at once so the palette is sufficient without gray.
- Switch to a design that relies more on direct labeling and less on many distinct category colors [@muth_emphasize_color_2023].
