---
id: use-diverging-color-scales-only-with-a-meaningful-midpoint-or-to-emphasize-deviations
title: Use a diverging color scale only when a meaningful midpoint or deviation-from-baseline
  is central
bibliography: references.bib
description: Choose diverging palettes when values meaningfully split around a middle
  point or when your story depends on highlighting both low and high extremes.
labels:
- chart:map
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Use diverging color scales only with a meaningful midpoint or deviation focus <!-- role: advice -->

Use a diverging color scale only when your data has a meaningful middle value or when you want readers to focus on how values deviate to both sides of a baseline. Make the midpoint explicit in the legend and surrounding text.

## Diverging scales communicate “above vs. below” and sharpen differences near the center <!-- role: reason -->

Diverging palettes visually encode a split around a center, so readers interpret colors as “below the midpoint” versus “above the midpoint” rather than simply “less to more.” Because each side uses its own gradient, the same color range is spread over a smaller numeric interval on each side of the midpoint, making differences (especially near the center) appear more distinct.

**Mechanism:** A midpoint anchors interpretation (two-directional change), and halving the numeric range per gradient increases apparent contrast for midrange differences.

**Evidence:** Diverging scales are appropriate when there is a meaningful middle point such as zero, 50%, an average/median, a threshold, or a target, and they are also an editorial choice when you want to emphasize both low and high extremes rather than just the highs [@muth_diverging_vs_sequential_2021]. Diverging scales can reveal more differences than sequential scales because one gradient covers only half the numeric range, making midrange differences more pronounced [@muth_diverging_vs_sequential_2021].

**Notes:** A midpoint can be “agreed” rather than inherent (e.g., what counts as “normal”), but it must be defensible and clearly communicated.

## Applies when your quantitative values naturally split around a center <!-- role: context -->

- **User Goal:** Understand which areas/items are below vs. above a baseline and how far they deviate.
- **Task:** Compare magnitudes on both sides of a reference point; spot low and high extremes simultaneously.
- **Data:** Quantitative data with an interpretable midpoint (e.g., zero change, 50/50 split, average/median, threshold, target).
- **Chart Setting:** Choropleth maps, heatmaps, or any view where color carries the primary quantitative encoding and small differences matter.
- **Audience:** Mixed literacy audiences who may need explicit cues about what the midpoint and ends mean.
- **Success Criterion:** Readers correctly identify which values are below/above the midpoint and perceive meaningful differences across the range.

## Do not use diverging scales when there is no defensible midpoint <!-- role: exceptions -->

**Break it when:** The values run from low to high without a meaningful center (e.g., “GDP per capita” with no baseline). **Why:** The two-sided encoding implies an “above vs. below” story that the data does not support and can confuse interpretation [@muth_diverging_vs_sequential_2021].

## Diverging scales trade intuitive reading for two-sided emphasis <!-- role: costs -->

**Sacrifice:** You lose the “darker = more” intuition that often works without a legend. **Risk:** Readers may misread which hue corresponds to “high” versus “low,” or infer “good/bad” meaning incorrectly if not clarified [@muth_diverging_vs_sequential_2021]. **Mitigation:** The midpoint and both ends must be clearly labeled in the legend and reinforced by text or annotations.

## Common ways diverging scales get misused <!-- role: mistakes -->

- **Mistake:** Using a diverging scale for strictly unipolar quantities (only “less to more”). **Why it fails:** It suggests a central reference and two-directional meaning that readers will look for but won’t find [@muth_diverging_vs_sequential_2021].
- **Mistake:** Omitting or under-labeling the legend with a diverging palette. **Why it fails:** Diverging colors are not inherently intuitive; readers can’t reliably infer which side is low or high without explicit cues [@muth_diverging_vs_sequential_2021].

## Quick tests for whether diverging is justified <!-- role: check -->

**Failure Sign:** People ask “Which color is high?” or “What does the middle mean?” **Quick Check:** State the midpoint in one phrase (e.g., “0% change,” “50%,” “target”)—if you can’t, diverging is likely unjustified [@muth_diverging_vs_sequential_2021]. **Stronger Test:** Ask a colleague to identify one below-midpoint and one above-midpoint region without reading the legend; if they cannot, your midpoint/legend communication is insufficient [@muth_diverging_vs_sequential_2021].

## What to do instead when diverging is not appropriate or not clear enough <!-- role: fix -->

- Use a sequential color scale when the story is primarily about “more vs. less” without a midpoint [@muth_diverging_vs_sequential_2021].
- If you keep a diverging scale, label the midpoint and both extremes clearly in the legend and reinforce the meaning with title text or annotations [@muth_diverging_vs_sequential_2021].
- If the editorial goal is only to highlight the highest values, switch to a sequential scale that concentrates attention on the top end [@muth_diverging_vs_sequential_2021].
- If the editorial goal is to highlight both low and high extremes, keep diverging but ensure the baseline is explicit and defensible (e.g., threshold or target) [@muth_diverging_vs_sequential_2021].
