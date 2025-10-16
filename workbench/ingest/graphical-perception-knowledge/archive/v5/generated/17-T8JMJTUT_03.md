---
id: prefer-contiguous-cartograms-for-area-comparison
title: "Prefer contiguous cartograms for comparing or ranking region values"
tags:
  - impact:perceptual
  - impact:performance
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.contiguous
  - task:compare
  - task:rank
  - data:spatial
  - data:quantitative
  - visual:area
  - visual:shape
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "In a 2018 study, contiguous cartograms consistently resulted in the lowest error rates for tasks requiring users to compare the size of regions or find the region with the top value ('compare' and 'find top-k' tasks)."
sources:
  - type: research
    ref: "Nusrat, Alam, and Kobourov, 2018"
    url: "https://doi.org/10.1109/TVCG.2016.2642109"
    note: "For three tasks related to value comparison ('compare', 'find top-k', 'detect change'), contiguous cartograms had the lowest error rates, with the difference being statistically significant compared to rectangular cartograms."
    role: primary
---
## Guidance

For tasks that require users to compare the statistical values of regions or rank them, prefer using contiguous cartograms.

## Why

While human perception of area is known to be less accurate than length, this study found that within cartograms, the irregular, familiar shapes of contiguous cartograms may provide better perceptual cues for size judgment than simple circles (Dorling) or rectangles with potentially misleading aspect ratios. Across three different tasks testing value comparison, contiguous cartograms consistently yielded the lowest error rates.

## When it applies

-   When the user's primary goal is to judge relative magnitudes, such as "Which state is bigger, Texas or California?" or "Find the state with the second-highest population."

## Exceptions

-   The study noted that for simple comparisons where the area ratio was large, Dorling cartograms also performed well, suggesting they are a viable alternative for non-complex comparisons.
-   If perfect statistical accuracy is required, Dorling or non-contiguous cartograms are better, as they can be scaled with zero cartographic error, whereas contiguous algorithms introduce some error.

## Trade-offs

-   Contiguous cartograms distort the original shapes of regions, which can make them harder to recognize without labels.
-   The algorithms for creating contiguous cartograms introduce some statistical inaccuracy (cartographic error), meaning the visualized area may not perfectly match the data value.

## Signs of Trouble

-   **Comparison Errors:** Users struggle to determine which of two regions is larger on your cartogram.
-   **Rectangular Confusion:** You are using a rectangular cartogram for comparison tasks, a type which showed significantly higher error rates in the study.

## How to Improve

-   **Quick Fix: Add Data Labels.** Add tooltips or direct labels that show the exact data value. This provides an escape hatch, allowing users to compare numbers directly instead of relying solely on area perception.
-   **Moderate Redesign:** If using a rectangular cartogram, switch to a Dorling cartogram, which performed better for comparison tasks.
-   **Comprehensive Redesign:** Switch to a contiguous cartogram to minimize user error for comparison and ranking tasks, as it was the best-performing type in the study.
