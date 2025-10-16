---
id: use-topology-preserving-cartograms-for-adjacency
title: "Use contiguous or rectangular cartograms to show geographic adjacencies"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.contiguous
  - chart:map.cartogram.rectangular
  - task:spatial-relationships
  - data:spatial
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "A 2018 study found that topology-preserving cartograms (contiguous and rectangular) led to significantly lower error rates (11% and 5%) on adjacency-finding tasks compared to non-preserving types like Dorling (24%) and non-contiguous (48%)."
sources:
  - type: research
    ref: "Nusrat, Alam, and Kobourov, 2018"
    url: "https://doi.org/10.1109/TVCG.2016.2642109"
    note: "For a 'find adjacency' task, a statistically significant difference in error rates was found, favoring cartogram types that preserve neighborhood connections."
    role: primary
---
## Guidance

When the user's task is to identify which geographic regions are neighbors, use a cartogram type that preserves topology, such as a contiguous or rectangular cartogram.

## Why

By definition, contiguous and topology-preserving rectangular cartograms ensure that regions that are adjacent in reality remain adjacent in the visualization. Non-contiguous and Dorling cartograms break these connections, making it perceptually difficult to determine neighbors. The study confirmed this, showing that even with a reference map, users made far more errors trying to identify neighbors on Dorling and non-contiguous cartograms.

### Core Principle

The visual structure of a chart should match the structure of the data relationships being communicated. If adjacency is a key relationship, it must be visually encoded.

## When it applies

-   When the user needs to answer questions about neighborhood relationships, such as "Which states border Nevada?".
-   When analyzing the spatial context of a region is important.

## Exceptions

-   None known. If the task is to find adjacencies, a topology-preserving cartogram is required. Other types are unsuitable for this specific task.

## Trade-offs

-   **Contiguous cartograms** must distort region shapes to maintain topology.
-   **Rectangular cartograms** heavily distort shape and relative position to create a schematic, grid-like layout. They also perform poorly on other tasks like comparison and summarization.

## Signs of Trouble

-   **Lost Neighbors:** Your visualization uses a Dorling (circles) or non-contiguous cartogram, and you expect users to understand which regions are neighbors.
-   **Topological Confusion:** Users are confused about the spatial relationships between regions in your cartogram.

## How to Improve

-   **Quick Fix: Add Interaction.** If you must use a Dorling or non-contiguous cartogram, add interaction (e.g., highlighting all neighbors on hover) to explicitly communicate the lost adjacency information.
-   **Comprehensive Redesign: Switch Chart Type.** If the primary task is to understand topology, switch to a contiguous or rectangular cartogram. Choose the contiguous type if preserving some sense of shape and location is important. Choose the rectangular type only if a highly schematic, abstract layout is the main goal.
