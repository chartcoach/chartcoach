---
id: cartogram-for-adjacency
title: "Use contiguous or rectangular cartograms to identify adjacent regions"
tags:
  - impact:perceptual
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.contiguous
  - chart:map.cartogram.rectangular
  - task:composition
  - task:spatial-adjacency
  - data:spatial
  - data:topology
  - medium:static

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "For a 'find adjacency' task, contiguous and rectangular cartograms were significantly more accurate (error rates of 11% and 5%) than Dorling and non-contiguous cartograms (error rates of 24% and 48%)."

---

## Guidance

When the task requires identifying neighboring regions, use cartogram types that preserve the original map's topology, such as **contiguous** or **rectangular** cartograms.

## Why

By definition, contiguous and topology-preserving rectangular cartograms are constructed to ensure that regions that are neighbors on the original map remain neighbors in the cartogram. Conversely, Dorling and non-contiguous cartograms break these adjacencies, making it impossible to reliably determine neighbors from the visualization alone. Experiments show that contiguous and rectangular cartograms are significantly more accurate for this task, even when a reference map is provided.

## When it applies

- When analyzing spatial relationships, such as identifying which states border another state, is a key part of the analysis.
- When understanding geographic clustering or the spread of a phenomenon across borders is important.

## Exceptions

- None. If identifying adjacency is a required task, cartogram types that do not preserve topology are fundamentally unsuited for it. Proximity in Dorling or non-contiguous cartograms does not equal adjacency.

## Trade-offs

- To preserve adjacency, **contiguous cartograms** must distort shape, and **rectangular cartograms** distort shape even more severely. You sacrifice shape recognizability and perceptual accuracy in area judgments to gain topological accuracy.

## Signs of Trouble

- **"Are these touching?":** Users are confused about whether two nearby regions in a Dorling or non-contiguous cartogram are actually adjacent.
- **Proximity-as-Adjacency Error:** Users incorrectly identify neighbors based on visual proximity rather than true shared borders.
- **Inability to Analyze Spread:** Viewers cannot answer questions about regional clustering or the diffusion of a variable across borders because the connections are missing.

## How to Improve

- **Quick Fix (for non-topological types): Use Interaction.** If you must use a Dorling or non-contiguous cartogram, add an interaction (e.g., on hover) that highlights all true neighbors of a selected region, either on the cartogram itself or on a linked reference map.
- **Moderate Redesign: Switch Cartogram Type.** If you are using a Dorling or non-contiguous cartogram for a task requiring adjacency, switch to a **contiguous** or **rectangular** cartogram to ensure adjacencies are correctly represented.
