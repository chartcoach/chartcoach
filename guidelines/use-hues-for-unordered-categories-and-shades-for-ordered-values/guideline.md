---
id: use-hues-for-unordered-categories-and-shades-for-ordered-values
title: Use hues for unordered categories, and use shades for ordered values
bibliography: references.bib
description: 'Match color encoding to data order: use distinct hues for categories
  without inherent order and a sequential/diverging scale for ordered values.'
labels:
- chart:general
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:basic
---

## Use hues for unordered categories, and shades for ordered values <!-- role: advice -->

Use different hues to encode categories that don’t have an inherent order, and use a quantitative color scale (shades/gradient) to encode values that do. Treat ordered non-numeric categories (like Likert responses or sizes) as ordered data and color them with a quantitative scale.

## Why order should determine hue vs. shade <!-- role: reason -->

Color implies structure: distinct hues are read as “different kinds,” while a light-to-dark scale is read as “more vs. less.” Aligning the palette type with whether the underlying values can be ranked reduces misinterpretation and makes the intended grouping or ordering easier to perceive.

**Mechanism:** Hue variation primarily signals categorical separation, while lightness (and sequential/diverging ramps) signals magnitude or rank; using the wrong kind makes viewers search for order where none exists, or miss order that is present.

**Evidence:** Choosing hues for unordered categories and quantitative scales for ordered values is presented as the default rule for most visualization situations, including ordered text categories like Likert scales and clothing sizes, to align color semantics with data semantics [@muth_quantitative_vs_qualitative_2021].

**Notes:** This guideline is about whether values are inherently rankable, not about whether they are expressed as numbers vs. words.

## When this applies: deciding between qualitative and quantitative palettes <!-- role: context -->

- **User Goal:** Help readers correctly interpret whether colored items are different kinds or different levels.
- **Task:** Categorize items or judge ordering/ranking from color.
- **Data:** Nominal categories (no rank) versus ordinal/continuous values (rankable).
- **Chart Setting:** Any chart type where color encodes groups or values (bars, lines, maps, treemaps, scatters).
- **Audience:** General audiences, including readers who will infer meaning from familiar color conventions.
- **Success Criterion:** Viewers can identify categories or order without inventing unintended hierarchy.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You need to prioritize distinguishing many entangled series (for tracking individual lines) over emphasizing rank/order. **Why:** Distinct hues can make individual series easier to follow even if an ordered shading scheme would better communicate ranking [@muth_quantitative_vs_qualitative_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Using shades for ordered data can make individual categories harder to tell apart when many items are present. **Risk:** Using hues for ordered data can cause readers to miss the order, because hue-encoded categories are not expected to be ranked. **Mitigation:** Decide explicitly whether the primary goal is “follow identity” or “see order” before choosing the palette type [@muth_quantitative_vs_qualitative_2021].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a qualitative palette for ordered values (including ordered text categories like Likert responses). **Why it fails:** It hides the inherent order and encourages “different kinds” interpretation instead of “more/less” [@muth_quantitative_vs_qualitative_2021].
- **Mistake:** Using a sequential ramp for nominal categories with no explanation. **Why it fails:** Readers often rationalize shades as meaning higher/lower or more/less important, even when the assignment is arbitrary [@muth_quantitative_vs_qualitative_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask what the light-to-dark differences “mean,” or they infer rank/importance you didn’t intend. **Quick Check:** Ask “Can these values be sorted meaningfully?”—if yes, prefer shades; if no, prefer hues. **Stronger Test:** Show the chart briefly to a colleague and ask them to explain what color means; if they describe an order you didn’t encode, the palette type is mismatched [@muth_quantitative_vs_qualitative_2021].

## What to do instead <!-- role: fix -->

- Use a qualitative palette (distinct hues) for nominal categories like industries or countries when no ordering is meaningful [@muth_quantitative_vs_qualitative_2021].
- Use a sequential scale for magnitude or rank, and use a diverging scale only when you are communicating deviation around a meaningful midpoint [@muth_quantitative_vs_qualitative_2021].
- If you must prioritize tracking many identities, switch to distinct hues and reinforce order with direct labeling or consistent ordering elsewhere in the layout [@muth_quantitative_vs_qualitative_2021].
- If neither palette makes the chart readable, change the chart form to reduce reliance on color for the main message (for example, fewer series, faceting, or highlighting) [@muth_quantitative_vs_qualitative_2021].
