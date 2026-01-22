---
id: match-choropleth-color-scheme-to-data-sequential-diverging-qualitative
title: 'Match choropleth color schemes to the data: sequential for magnitude, diverging
  for meaningful midpoints, qualitative for categories'
bibliography: references.bib
description: Choose sequential, diverging, or qualitative palettes based on whether
  your values are ordered, signed around a center, or categorical.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- data:geospatial
- data:quantitative
- audience:general
- accessibility:colorblind
---

## Choose sequential, diverging, or qualitative palettes based on whether the data is ordered, centered, or categorical <!-- role: advice -->

Use a sequential palette for ordered magnitude (low-to-high), a diverging palette when both extremes matter around a center value, and a qualitative palette for categories. Ensure the chosen palette is colorblind-friendly.

## Palette type sets the viewer’s expectations about meaning <!-- role: reason -->

Color schemes signal structure: sequential palettes imply increasing magnitude, diverging palettes imply departure in two directions from a central reference, and qualitative palettes imply distinct groups without order. If the palette type contradicts the data’s structure, viewers infer patterns (trend, polarity, or order) that are not actually present.

**Mechanism:** Viewers use hue and lightness cues to infer ordering or categorical separation; the palette encodes not just values but also the conceptual model of the data.

**Evidence:** Three map color scheme types are recommended—sequential, diverging, and qualitative/categorical—with guidance to pick sequential to emphasize high values and diverging to emphasize both extremes; qualitative schemes are recommended for unordered categories [@muth_choroplethmaps_2018]. Colorblind-friendly colors are recommended for any scheme [@muth_choroplethmaps_2018].

**Notes:** The palette choice is part of the message: it determines which values draw attention.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Interpret what higher/lower colors mean across regions.
- **Task:** Compare regions by ordered magnitude, signed difference, or category membership.
- **Data:** Ordered numeric values; signed values around a center; or nominal categories.
- **Chart Setting:** Choropleth with legend; static or interactive.
- **Audience:** Broad audiences including readers with color-vision deficiencies.
- **Success Criterion:** The palette communicates the correct data structure without implying false order or polarity.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Readers already have a widely recognized category-to-color convention (e.g., political party colors) that must be maintained even if it uses multiple hues. **Why:** Familiar encoding can reduce lookup effort and confusion for known categories [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Strict palette matching can limit stylistic freedom or branding colors. **Risk:** Forcing a diverging palette without a meaningful center can invent a “good/bad” split. **Mitigation:** Make the center value explicit in the legend when diverging is used.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using a qualitative multi-hue palette for ordered numeric data. **Why it fails:** It weakens the perception of ranking and can imply arbitrary groups [@muth_choroplethmaps_2018].
- **Mistake:** Using a sequential palette for data where both extremes should stand out around a center. **Why it fails:** It emphasizes only one end of the range and hides the other extreme [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers disagree on whether the colors imply order, polarity, or categories. **Quick Check:** Ask “is there a meaningful midpoint that separates two directions?”—if yes, diverging; if no and values are ordered, sequential; if unordered, qualitative. **Stronger Test:** Show only the legend to a colleague and ask what structure they infer; it should match your data structure.

## What to do instead <!-- role: fix -->

- Switch to a sequential palette when the data is a single ordered magnitude (e.g., rates).
- Switch to a diverging palette when deviations around a center value are the story (e.g., difference between two sides).
- Switch to a qualitative palette when values are categories without order.
- Replace the palette with a colorblind-friendly alternative while preserving the same scheme type.
