---
id: prefer-contiguous-non-contiguous-cartograms-for-location
title: "Prefer contiguous or non-contiguous cartograms for location tasks"
tags:
  - impact:perceptual
  - impact:performance
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.contiguous
  - chart:map.cartogram.non-contiguous
  - chart:map.cartogram.rectangular
  - chart:map.cartogram.dorling
  - task:lookup
  - data:spatial
  - data:quantitative
  - visual:position
  - visual:area
  - audience:general
  - medium:static
  - access:cognitive-load-risk
evidence:
  strength: medium
  summary: "A 2018 study with 33 participants found that contiguous and non-contiguous cartograms led to significantly faster and more accurate performance on location tasks compared to rectangular and Dorling cartograms."
sources:
  - type: research
    ref: "Nusrat, Alam, and Kobourov, 2018"
    url: "https://doi.org/10.1109/TVCG.2016.2642109"
    note: "Compared four cartogram types on a 'locate' task. Found contiguous and non-contiguous types had significantly lower error rates and completion times than rectangular cartograms."
    role: primary
---
## Guidance

For tasks that require users to find or identify specific geographic regions on a cartogram (a "locate" task), prefer contiguous or non-contiguous cartogram types over rectangular or Dorling cartograms.

## Why

Contiguous and non-contiguous cartograms do a better job of preserving the relative positions of regions from the original map. This makes it easier for viewers to mentally map a known location to its new position on the distorted cartogram. The source study found statistically significant differences in both completion time and error rates for this task, with rectangular cartograms performing the worst.

### Core Principle

Minimize the cognitive distance between a user's mental model of a map and the visualized representation. Preserving relative locations, even if distorted, aids in this mapping.

## When it applies

-   When the primary goal for the user is to look up a specific region (e.g., "Find Texas on this population cartogram").
-   When working with a general audience that may rely on relative geography for orientation.

## Exceptions

-   If preserving exact adjacency (topology) in a schematic way is the absolute highest priority, a rectangular cartogram might be considered. However, be aware this comes at a significant performance cost for location tasks.

## Trade-offs

-   **Contiguous cartograms** achieve this by distorting the original shapes of regions.
-   **Non-contiguous cartograms** sacrifice all adjacency information, which can make the map feel fragmented and prevent users from understanding neighborhood relationships.

## Signs of Trouble

-   **Slow Lookup:** Users take a long time to find a specific region you ask them to locate.
-   **Frequent Misidentification:** Users frequently misidentify regions on the cartogram.
-   **Wrong Tool for the Job:** You are using a rectangular or Dorling cartogram, and the primary task for the user is looking up specific regions.

## How to Improve

-   **Quick Fix: Add Labels and a Reference.** Add clear labels to all regions, especially if you must use a poorly-suited cartogram type. Providing a small, undistorted reference map alongside the cartogram also helps, as was done in the study.
-   **Moderate Redesign:** If using a rectangular cartogram, switch to a Dorling cartogram. Performance is still poor for location tasks but was found to be slightly better than rectangular.
-   **Comprehensive Redesign:** Re-render the cartogram using a contiguous (e.g., diffusion-based) or non-contiguous algorithm. This directly addresses the perceptual issue by better preserving relative positions.
