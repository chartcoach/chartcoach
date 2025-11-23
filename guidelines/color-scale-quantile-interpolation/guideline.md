---
id: color-scale-quantile-interpolation
title: Use Quantile Interpolation to Reveal Patterns in Skewed Data
bibliography: references.bib
description: Use quantile scales to ensure every color appears equally, revealing
  patterns in data with outliers.
labels:
- chart:map
- chart:choropleth
- visual:color
- impact:contrast
- data:skewed
- task:rank
---

## The Rule <!-- role: advice -->
Use quantile interpolation (such as quartiles, quintiles, or deciles) when your data contains strong outliers and you want to ensure every color in your scale is used equally across the map.

## The Logic <!-- role: reason -->
Quantiles divide the data into segments containing an equal number of values. For example, a quintile scale ensures 20% of regions get the lightest color and 20% get the darkest. As explained by [@muth_interpolation_2022], this ensures the darkest color gets "as much showtime" as the lightest, maximizing contrast and revealing geographical patterns that linear scales hide. It shifts the visualization from showing absolute magnitude to showing relative rank (e.g., "the top 20%").

## Where to Apply <!-- role: context -->
*   **User Goal:** To see regional differences and patterns that are otherwise hidden by outliers.
*   **Data Type:** Highly skewed distributions (e.g., income, unemployment) where a few high values stretch the scale.
*   **Audience:** Readers looking for relative comparisons (high vs. low regions) rather than precise mathematical distances.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the magnitude of difference matters more than the rank.
*   **Reason:** Quantiles can mislead readers into thinking differences are stark where they are not. It might color two regions with very similar values (e.g., 3.8% and 9.9%) as vastly different because they fall into different "buckets," or conversely, color very different values (e.g., 9.9% and 23.5%) effectively the same [@muth_interpolation_2022].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You sacrifice truthfulness regarding magnitude.
*   **The Risk:** Readers may believe there is a massive "drama" or difference between regions that are actually statistically close, or fail to appreciate how extreme an outlier actually is.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding more and more cuts (e.g., using Deciles instead of Quintiles) just to make the map look dramatic.
*   **Why it fails:** This increases contrast artificially, making the map look "busy" and implying stark differences everywhere, even in areas where the data is relatively flat.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do adjacent regions with very similar numbers have drastically different colors?
*   **The Test:** Check the legend or color key. If the range for the darkest color is huge (e.g., 10% to 23%) while the range for the middle color is tiny (e.g., 4% to 4.2%), the visual hierarchy might be distorting the data.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the number of quantiles (e.g., move from deciles to quartiles) to smooth out minor differences.
*   **Best Fix:** Switch to "Natural Breaks" (Jenks) or a custom interpolation to find a compromise between equal representation and true data clustering.
