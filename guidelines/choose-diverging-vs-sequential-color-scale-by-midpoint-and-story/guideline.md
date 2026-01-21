---
id: choose-diverging-vs-sequential-color-scale-by-midpoint-and-story
title: Choose Diverging or Sequential Color Scales Based on Midpoint and Story
bibliography: references.bib
description: Use diverging scales for meaningful midpoints or to highlight extremes
  and subtle differences; use sequential scales for more intuitive low-to-high reading.
labels:
- chart:choropleth
- task:encode-magnitude
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use a **diverging** color scale when your data has a **meaningful middle point** or when you want to **emphasize both low and high extremes**; use a **sequential** color scale when you want the most **intuitive low-to-high reading** and your story mainly emphasizes the high end. [@muth_diverging_vs_sequential_2021]

## The Logic <!-- role: reason -->

Diverging scales split the value range around a midpoint, so each side of the scale covers a smaller numeric span; that makes differences near each extreme more visually pronounced, and it editorially centers the story on “below vs above” a reference value. Sequential scales map the full range in one direction, which many readers can interpret as “lighter = lower, darker = higher” even without consulting a legend. [@muth_diverging_vs_sequential_2021]

- **The Principle:** Midpoint-based encoding vs. one-direction magnitude encoding
- **The Evidence:** [@muth_diverging_vs_sequential_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See whether values are **below vs above** a reference (and how far), or focus on **both extremes** rather than only the maximums. [@muth_diverging_vs_sequential_2021]
- **Data Type:** Quantitative data where a midpoint can be defined (e.g., **zero**, **50%**, **average/median**, a **threshold**, or a **target**). [@muth_diverging_vs_sequential_2021]
- **Audience:** Especially useful when readers need help spotting **differences** across a range (e.g., maps/heatmaps where subtle differences matter), but plan for legend-reading. [@muth_diverging_vs_sequential_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is **no defensible midpoint** (or choosing one would be arbitrary).\
  **Reason:** A diverging scale implies “two sides” around a center; if that center isn’t meaningful, the color structure suggests a story you don’t actually have. [@muth_diverging_vs_sequential_2021]
- **Scenario:** You expect the chart to be understood **without a color key** (e.g., quick-glance contexts).\
  **Reason:** Diverging scales are less intuitive; readers can’t reliably infer which hue means “high” vs “low” without a legend or strong cues. [@muth_diverging_vs_sequential_2021]
- **Scenario:** Your story is primarily about the **highest values** (not the lows).\
  **Reason:** Sequential scales more directly support “where are the biggest values?” without splitting attention across two extremes. [@muth_diverging_vs_sequential_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Diverging scales demand more **legend attention** and can slow comprehension. [@muth_diverging_vs_sequential_2021]
- **The Risk:** If hues are not chosen and explained carefully, readers may invert meaning (e.g., assume red means “more” when it actually means “less”). [@muth_diverging_vs_sequential_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a diverging scale without clearly defining and communicating the **midpoint** (or using one just because it “looks nice”).\
  **Why it fails:** The chart implies a central reference and two-sided interpretation that may not exist or may be unclear. [@muth_diverging_vs_sequential_2021]
- **The Wrong Fix:** Using a diverging scale but providing a **weak/unclear legend** (or expecting readers to infer direction).\
  **Why it fails:** Diverging hues aren’t inherently ordered; readers get lost about which side is high/low or good/bad. [@muth_diverging_vs_sequential_2021]
- **The Wrong Fix:** Using a sequential scale when the story is about **both very low and very high values**.\
  **Why it fails:** The low end can fade into the background because the narrative and visual emphasis skew toward the dark/high end. [@muth_diverging_vs_sequential_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers could plausibly read the chart “backwards” (unclear which hue is high/low), or the chart fails to draw attention to the low end when that’s part of the story. [@muth_diverging_vs_sequential_2021]
- **The Test:** Hide the legend briefly and ask: “Can someone correctly tell which colors mean high vs low?” If not, a diverging scale needs stronger cues—or a sequential scale may be more appropriate. [@muth_diverging_vs_sequential_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** If you use a diverging scale, **label the legend clearly** and make the extremes and midpoint explicit (e.g., show the midpoint value and what it represents). [@muth_diverging_vs_sequential_2021]
- **Best Fix:** Re-align the scale choice to the editorial goal:
  - Switch to **sequential** if the message is “higher values stand out” and you want intuitive reading.
  - Switch to **diverging** if the message is “below vs above a meaningful reference,” or you need to make differences near extremes more visible. [@muth_diverging_vs_sequential_2021]
