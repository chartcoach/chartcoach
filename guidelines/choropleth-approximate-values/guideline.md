---
id: choropleth-approximate-values
title: Expect Only Approximate Values from Choropleth Maps
bibliography: references.bib
description: Treat Choropleth maps as tools for approximate value retrieval, not precise
  data reading.
labels:
- chart:choropleth
- chart:map
- task:retrieve-value
- visual:color
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not design Choropleth Maps (filled maps) if the user's primary task is retrieving precise numerical values. Design them for retrieving "Approximate Values" only.

## The Logic <!-- role: reason -->
Choropleth maps encode values through color saturation or hue, which are difficult for the human eye to map back to a precise number on a legend.
*   **The Principle:** **Visual Decoding Precision.** In the VLAT Test Blueprint, the task "Retrieve Value" for Choropleth Maps is explicitly marked with a caveat: "Only Approximate Value."
*   **The Evidence:** Table 1 in [@lee_vlat_2017] notes that for Choropleth Maps, users "only the approximately segmented range of each value is represented." Consequently, the associated task is listed as "Retrieve Value (Approximate Value)" in the item analysis (Table 2, Item 55).

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding geographic distribution or identifying regional hotspots.
*   **Data Type:** Quantitative data aggregated by geographic region.
*   **Audience:** Any audience.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Interactive Maps.
*   **Reason:** If the map supports hover-over tooltips that display the exact number, the visual limitation of the color encoding is mitigated.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision. Users can only say "Usage was high in this state," not "Usage was 45.2%."
*   **The Risk:** Users may confidently misinterpret a color shade if the legend gradient is not distinct enough.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a continuous color gradient without distinct steps.
*   **Why it fails:** It makes it nearly impossible to match a specific region's color to a precise point on the legend bar.
*   **The Wrong Fix:** expecting users to calculate differences between regions.
*   **Why it fails:** Subtracting "Dark Blue" from "Medium Blue" is cognitively impossible without the underlying numbers.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the legend. Is it a smooth gradient? Look at a region. Can you tell if the value is 50 or 55?
*   **The Test:** Ask a user to write down the exact value of a specific region. If they give a range (e.g., "between 10 and 20"), the map is working as intended. If you need them to write "15", the map has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use a stepped (binned) color scale rather than a continuous gradient to make matching easier.
*   **Best Fix:** Add labels with the actual numbers on top of the regions, or accompany the map with a sorted table.
