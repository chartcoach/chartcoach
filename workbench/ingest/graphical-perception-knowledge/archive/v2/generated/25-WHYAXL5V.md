---
id: use-orderable-channels-for-ordered-data
title: "Use perceptually ordered channels for ordered data"

impact:
  - perceptual
  - cognitive
  - logos
  - performance

tags:
  - visual-channel
  - ranking
  - comparison
  - find-extremum
  - trend
  - quantitative
  - ordinal
  - glyph
  - color
  - size
  - shape
  - texture

sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "This paper empirically tested the 'perceptual orderability' of visual channels and found that channels perceived as ordered (like value and size) improve performance on ranking and comparison tasks compared to non-ordered channels (like hue)."

examples:
  - type: good
    description: "A series of data points is encoded using size or lightness (value). It's easy to see the order and identify the largest/smallest elements at a glance."
  - type: bad
    description: "The same ordered series is encoded using different color hues (e.g., red, blue, green, yellow). It's impossible to know the inherent order without a legend, and comparing values is slow and difficult."
---

## Guidance

For data that has a natural order (like rankings, ratings, or quantities), encode it using visual channels that people intuitively perceive as ordered. Prioritize lightness, size, or countable texture/shape over channels like color hue or orientation.

## Why

Humans can quickly and accurately judge order and magnitude when looking at changes in **lightness** (e.g., from light gray to dark gray) or **size**. These channels are perceptually "ordered."

In contrast, channels like **color hue** (e.g., red, green, blue) or **orientation** are not inherently perceived as having a specific rank. Using them to encode ordered data forces viewers to constantly consult a legend, which increases cognitive load, slows down interpretation, and leads to more errors when trying to find the highest, lowest, or middle values.

## When it applies

- When displaying **ordinal** data (e.g., small, medium, large) or **quantitative** data (e.g., 0-100).
- When a key task is to **compare ranks**, identify **trends**, or find the **highest/lowest values** (find extremum).
- When designing **glyphs** for multivariate data where one of the attributes you are encoding has a natural order.

## Exceptions

- **Categorical Data:** When data has no inherent order (e.g., countries, product categories), using a non-ordered channel like color hue is perfectly appropriate and effective for distinguishing categories.
- **Literal Angles:** Orientation can be used effectively when it represents a literal direction (e.g., wind direction), not an abstract magnitude.
- **Obvious Extremes:** The choice of channel matters less when a sequence is perfectly ordered or completely random, as the pattern is obvious. The negative impact of a poor channel choice is strongest for data that is mostly, but not perfectly, ordered.

## Trade-offs

- **Aesthetics vs. Clarity:** A vibrant (but unordered) color hue palette might seem more visually engaging than a simple grayscale or size-based encoding, but it sacrifices perceptual accuracy and speed for the task of comparison.
- **Cognitive Load:** Even some ordered channels can be demanding. The study found that countable shapes (like stars with an increasing number of points) were accurate for ranking but slower to process than size or lightness, suggesting a higher cognitive cost.

## Evaluate

- [ ] An ordered or quantitative variable (e.g., low to high, 1 to 10) is represented by a qualitative color hue palette (e.g., red, blue, green).
- [ ] A ranked series is encoded using different shapes that have no intuitive order (e.g., a circle, a square, and a triangle to represent 1st, 2nd, and 3rd).
- [ ] Users struggle to identify the largest or smallest item in a series without carefully inspecting each element one by one.

## Repair

1. **Swap the channel.** Replace the non-ordered channel with an ordered one. The highest-impact change is to switch from a qualitative hue encoding to a sequential one (e.g., from light blue to dark blue) or a size-based encoding.
2. **Prioritize the best channels.** For showing order, prioritize **size** or **lightness (value)**, as they are the most effective and perceptually intuitive.
3. **Add redundancy.** If a non-ordered channel must be used (e.g., for branding), supplement it with a direct label or a more perceptually effective redundant encoding (e.g., using both size and color to represent the same value).