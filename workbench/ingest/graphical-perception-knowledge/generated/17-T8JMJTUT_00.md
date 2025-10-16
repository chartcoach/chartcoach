---
id: use-topology-preserving-cartograms-for-adjacency
title: "Use topology-preserving cartograms when showing adjacency"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - task:lookup
  - data:spatial
  - medium:static
  - medium:interactive
  - access:cognitive-load-risk

evidence:
  strength: medium
  summary: "A 2018 study (n=33) found that cartograms preserving topology (contiguous and rectangular) had significantly lower error rates for adjacency-finding tasks (11% and 5%, respectively) compared to types that do not (non-contiguous at 48.5% and Dorling at 24.2%), with p<0.001."

sources:
  - type: research
    ref: "Nusrat, Alam, & Kobourov, 2018"
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Experiment H4 tested finding neighbors. Contiguous and rectangular cartograms, which preserve topology, vastly outperformed non-contiguous and Dorling cartograms in accuracy (p<0.001), even when a reference map was provided."
    role: primary

---

## Guidance

When viewers need to understand which geographic regions are neighbors, use cartogram types that preserve topology, such as **contiguous** or **rectangular** cartograms. Avoid non-contiguous and Dorling (circle) cartograms for this task.

## Why

Contiguous and rectangular cartograms are constructed to maintain the adjacency relationships of the original map, making it possible to see which regions border each other. In contrast, non-contiguous and Dorling cartograms break these connections, making it perceptually impossible to determine neighbors without memorizing the original map. Experiments show this leads to extremely high error rates for adjacency tasks, even when a reference map is provided.

### Core Principle

The visual structure of a map should support its primary tasks. If understanding spatial relationships like adjacency is key, the visualization must encode those relationships.

## When it applies

- When a primary task for the viewer is to identify which states, countries, or regions border one another.
- When creating static cartograms where interactive aids (like hover effects) are not available.

## Exceptions

- When adjacency is not a relevant task for the viewer. If the goal is purely to compare values (task:compare), preserve shapes (task:lookup), or see an overall summary (task:summary-mean), other cartogram types may be more effective.

## Trade-offs

- **Shape Distortion:** To preserve topology, contiguous cartograms must distort geographic shapes, which can hinder recognition. Rectangular cartograms distort shapes even more severely.
- **Aesthetics:** Rectangular cartograms are often perceived as unaesthetic and are generally disliked by viewers.

## Signs of Trouble

- **Neighbor Confusion:** Viewers are unable to tell which regions are neighbors simply by looking at the cartogram.
- **High Error Rates:** When tested, users make frequent mistakes (over 20% error rate) on tasks that require identifying adjacent regions.

## How to Improve

- **Quick Fix: Add Interaction.** If you must use a Dorling or non-contiguous cartogram, add an interactive feature where hovering over a region highlights all of its neighbors on the cartogram or on a linked reference map.

- **Moderate Redesign: Switch to a Contiguous Cartogram.** This preserves topology while being more aesthetically pleasing and better for comparison tasks than a rectangular cartogram.

- **Comprehensive Redesign: Re-evaluate Chart Choice.** If adjacency is critical, confirm that a cartogram is the right choice. A standard choropleth map paired with a bar chart might communicate the data values and the geography more clearly, albeit separately.
