---
id: limit-categorical-palettes-to-seven-colors-or-restructure-the-view
title: Limit categorical palettes to seven colors, or restructure the chart
bibliography: references.bib
description: Avoid overloading readers with too many category colors; regroup categories
  or change chart type.
labels:
- chart:bar
- task:compare
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## Keep categorical color counts small enough to scan <!-- role: advice -->

If a chart needs more than seven distinct category colors, regroup categories or choose another chart type so readers do not have to rely on the color key constantly.

## Why too many colors slow comprehension <!-- role: reason -->

As the number of category colors increases, readers must repeatedly map colors to labels through the legend, which makes scanning and comparison slower and more error-prone.

**Mechanism:** Many distinct hues exceed quick visual discrimination in a single view, pushing readers into legend lookups instead of direct recognition.

**Evidence:** When more than seven colors are used in a chart, it becomes harder to read quickly and readers need to consult the color key more often, so regrouping or switching chart type is recommended [@muth_colors_2018].

**Notes:** The issue is not aesthetics; it is the interaction cost of decoding many categories through a legend.

## When this applies to category encoding <!-- role: context -->

- **User Goal:** Identify, compare, or talk about multiple categories accurately.
- **Task:** Match marks to category labels; compare categories across the view.
- **Data:** Categorical series with high cardinality.
- **Chart Setting:** Any chart using distinct hues to represent categories with a legend.
- **Audience:** Readers who need quick comprehension without careful legend decoding.
- **Success Criterion:** Most categories are identifiable without repeated legend checks.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is explicitly a keyed reference where frequent legend use is acceptable. **Why:** The reading mode is lookup-based rather than scan-based, so repeated legend checks are less of a failure [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Grouping can reduce category detail. **Risk:** Changing chart type can make it harder to keep a familiar format. **Mitigation:** Preserve detail via grouping plus a clear “Other” category or a separate supporting view.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding more and more distinct colors to “fit” all categories into one legend. **Why it fails:** The chart becomes slow to read because readers must consult the legend repeatedly [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** You cannot name a category from its color without looking at the legend. **Quick Check:** Try to identify five random categories in under ten seconds without using the legend. **Stronger Test:** Ask a first-time reader to answer a category comparison question while you observe legend back-and-forth.

## What to do instead <!-- role: fix -->

- Group small categories into an “Other” bucket and keep the palette limited.
- Switch to a chart type that labels categories directly instead of relying on color.
- Split into small multiples so each panel uses fewer categories/colors.
- Use color only to highlight a few key categories and render the rest in neutral tones.
