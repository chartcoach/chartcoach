---
id: use-rectangular-cartograms-with-caution
title: "Use rectangular cartograms with caution due to negative user perception"

tags:
  - impact:aesthetic
  - impact:pathos
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.rectangular
  - audience:general

evidence:
  strength: medium
  summary: "A 2018 study (n=33) on subjective preferences found that rectangular cartograms were rated as the least helpful, least elegant, and least innovative type. In a follow-up choice, 0 out of 33 participants chose to continue working with them, whereas contiguous (17) and Dorling (15) cartograms were highly preferred."

sources:
  - type: research
    ref: "Nusrat, Alam, & Kobourov, 2018"
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "The subjective preference and attitude study (Figs. 4 & 5) showed rectangular cartograms were consistently rated lowest on positive attributes like 'helpful,' 'elegant,' 'innovative,' and 'easy to understand.' They were the only type no user chose for subsequent tasks."
    role: primary

---

## Guidance

Use **rectangular cartograms** with caution, especially for general audiences, as they are often perceived negatively and are strongly disliked compared to other cartogram types.

## Why

While rectangular cartograms can effectively preserve geographic topology in a schematic way, their severe shape distortion and rigid, grid-like appearance are viewed by users as unaesthetic, unhelpful, and difficult to understand. In a study of user attitudes, they were rated as the least preferable cartogram type across nearly every positive attribute. This negative perception can cause viewers to disengage from the visualization or distrust the presentation.

### Core Principle

A visualization's effectiveness depends not only on its perceptual accuracy but also on its ability to engage the viewer and be seen as appealing and trustworthy. A chart that is disliked is a chart that may not be read.

## When it applies

- When creating visualizations for a general audience where engagement, visual appeal, and positive reception are important.
- When choosing a default cartogram type for a broad set of use cases.

## Exceptions

- In highly specialized, expert contexts where the primary and sole goal is to present a schematic of adjacencies, and aesthetic appeal is irrelevant (e.g., some abstract network or system diagrams that happen to be geographically based).

## Trade-offs

- By avoiding rectangular cartograms, you may sacrifice a method that can create a perfectly-tiled, schematic layout that preserves topology.

## Signs of Trouble

- **Negative Feedback:** Viewers describe the chart as "ugly," "confusing," "boring," or "drab."
- **Disengagement:** Viewers quickly lose interest or express a desire not to use the chart.
- **Poor Ratings:** When asked, users give the visualization low ratings on subjective measures like "helpfulness" or "elegance."

## How to Improve

- **Moderate Redesign: Switch to a Contiguous Cartogram.** If preserving topology is important, a contiguous cartogram is a much more popular and favorably perceived alternative that still maintains adjacencies.

- **Comprehensive Redesign: Use a Dorling Cartogram.** If a schematic, abstract representation is acceptable and showing broad patterns is the goal, a Dorling (circle) cartogram is a better choice. It performed well on summary tasks and was highly rated by users for being "elegant" and "innovative."
