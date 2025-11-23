---
id: sort-small-multiples-meaningfully
title: Sort Panels by Data Metrics
bibliography: references.bib
description: Sort small multiple panels by meaningful metrics (start value, change,
  etc.) rather than alphabetically.
labels:
- chart:small-multiples
- visual:order
- task:rank
- impact:readability
---

## The Rule <!-- role: advice -->
Sort your panels by a data-driven metric—such as start value, end value, range, or percentage change—rather than alphabetically. Explicitly state the sorting logic in the chart description.

## The Logic <!-- role: reason -->
*   **The Principle:** Narrative Navigation.
*   **The Evidence:** Sorting helps answer specific questions immediately (e.g., "Which value was highest at the end?"). According to [@muth_small_multiple_line_charts_2024], distinct sorting helps navigate the data and tells a story, whereas alphabetical sorting often has "no obvious logic" regarding the data trends.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying top performers, biggest growers, or steepest decliners.
*   **Data Type:** Categorical data over time.
*   **Audience:** Readers looking for insights, not just a specific category lookup.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The specific lookup of a category (e.g., "How is *my* country doing?") is the primary use case, and there are many categories (e.g., 50 US states).
*   **Reason:** Alphabetical sorting is the only efficient way to find a specific item in a large set.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It becomes harder to find a specific category by name if the list is long.
*   **The Risk:** If the sort order isn't stated, the arrangement may seem random.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Default alphabetical sorting.
*   **Why it fails:** It creates a random visual pattern that buries the most interesting data points (highest/lowest) in the middle of the grid.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the top-left panel "Afghanistan" just because it starts with A?
*   **The Test:** Can you immediately identify the category with the highest value? If not, resort.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Sort by the highest value at the most recent date.
*   **Best Fix:** Choose a sort order that matches the chart's headline (e.g., if the headline is "Prices rose fastest in the South," sort by % change).
