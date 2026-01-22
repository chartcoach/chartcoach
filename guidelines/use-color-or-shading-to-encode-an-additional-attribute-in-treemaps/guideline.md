---
id: use-color-or-shading-to-encode-an-additional-attribute-in-treemaps
title: Use color or shading to encode a secondary attribute inside treemap rectangles
bibliography: references.bib
description: Apply distinct colors or gray shading within treemap regions to represent
  categorical or ordinal attributes beyond size.
labels:
- chart:treemap
- task:categorize
- visual:color
- impact:clarity
- data:hierarchical
- audience:expert
- encoding:color
---

## Encode a second attribute with color or shading in treemaps <!-- role: advice -->

Assign colors (or gray shading) to treemap rectangles to represent an additional attribute such as file type, owner, frequency of use, or age. If adjacent regions share the same color, add a visible boundary to preserve separability.

## Why color supports attribute scanning in dense treemaps <!-- role: reason -->

Treemaps can contain thousands of small regions, so a secondary channel is needed to distinguish categories or statuses beyond area. Color enables rapid grouping and filtering by attribute while area continues to communicate magnitude.

**Mechanism:** Color provides a parallel perceptual grouping cue that helps viewers segment the “checkerboard” of rectangles into meaningful subsets without changing the area-based magnitude encoding.

**Evidence:** Different colors (or gray shading) are described as necessary for visual clarity in treemap regions and can encode attributes such as file type, ownership, frequency of use, or age; boundaries may be needed when adjacent areas share the same color [@shneidermanTreeVisualizationTreemaps1992].

**Notes:** Users may need control over parameter choices and color-to-attribute mapping because needs vary by application.

## When color/shading encoding applies <!-- role: context -->

- **User Goal:** Understand composition by category/status while also seeing magnitude.
- **Task:** Identify clusters of types (for example, file formats) and spot large items within a category.
- **Data:** Hierarchical data with a weight plus an additional categorical or ordered attribute.
- **Chart Setting:** Dense treemap where many rectangles would otherwise blend together.
- **Audience:** Users who need to scan quickly and perform follow-up actions (inspect, delete, mark).
- **Success Criterion:** Categories are visually separable without interfering with size judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The attribute has too many distinct values to map to distinguishable colors. **Why:** The display becomes visually noisy and categories can no longer be reliably discriminated.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Increased design and configuration effort to choose and manage color mappings. **Risk:** Adjacent same-colored regions can visually merge, hiding boundaries. **Mitigation:** Draw boundary lines when same-colored adjacency occurs.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using color without a stable legend or user-controlled mapping. **Why it fails:** Users cannot interpret what colors mean across sessions or tasks.
- **Mistake:** Allowing same-color adjacency without boundaries. **Why it fails:** Regions appear as a single merged block, undermining item-level identification.

## Quick tests <!-- role: check -->

**Failure Sign:** Users cannot tell where one rectangle ends and the next begins in same-colored regions. **Quick Check:** Visually scan for merged blocks and verify boundaries are still perceivable at typical zoom. **Stronger Test:** Ask users to find the largest item of a given category; failures indicate color grouping or boundary problems.

## What to do instead <!-- role: fix -->

- Add explicit boundary lines between adjacent rectangles when their fill colors match.
- Reduce attribute granularity by grouping values into a smaller set of meaningful categories.
- Provide a control panel to let users remap colors to the attributes relevant to their current task.
- Use interaction (hover details) to disambiguate items when color cannot carry the full attribute set.
