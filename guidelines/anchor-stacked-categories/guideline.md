---
id: anchor-stacked-categories
title: Anchor the Most Important Category to the Baseline
bibliography: references.bib
description: In stacked bar charts, the bottom segment is perceived significantly
  more accurately than upper segments.
labels:
- chart:stacked-bar
- visual:position
- visual:length
- task:sort
- impact:accuracy
---

## The Rule <!-- role: advice -->
Place the most critical data category at the bottom of a stacked bar chart.

## The Logic <!-- role: reason -->
The bottom segment of a stacked bar chart is perceived as a **position** encoding (aligned to the X-axis), whereas upper segments are perceived as **length** encodings (unaligned start points).
*   **The Evidence:** According to experimental results in [@heer_crowdsourcing_2010] and [@zeng_review_2023], the bottom segment (E-2) performs statistically significantly better in accuracy tasks than the top segment (E-4).
*   **The Mechanism:** Position on a common scale (E-2) is a top-tier encoding, while unaligned length (E-4) is a second-tier encoding.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing specific sub-categories across multiple groups.
*   **Data Type:** Nominal data nested within quantitative stacks.
*   **Audience:** Users needing to compare specific segments, not just the total bar height.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data has a natural ordinal structure (e.g., "Low, Medium, High") that dictates a specific vertical order.
*   **Reason:** Breaking the natural logic of the data to optimize for perception might confuse the user about the data's meaning.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Secondary categories (those stacked on top) will be harder to compare accurately.
*   **The Risk:** Users may misinterpret the size differences of the upper segments due to the lack of a common baseline.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Sorting the stack order alphabetically or randomly.
*   **Why it fails:** This often pushes the most relevant variable to the middle or top (E-4), degrading the user's ability to sort or compare it accurately.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the category you want users to focus on. Is it touching the axis line?
*   **The Test:** Try to compare the size of the "floating" blocks across bars. Is it difficult? (It should be).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reorder the stack so the primary category is at the bottom (E-2).
*   **Best Fix:** Unstack the chart and use small multiples or a grouped bar chart (E-1) to give every category a common baseline.
