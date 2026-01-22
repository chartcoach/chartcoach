---
id: use-treemaps-to-compare-node-sizes-in-hierarchies-with-rectangular-space-filling
title: Use treemaps to compare node sizes in hierarchies with rectangular space-filling
bibliography: references.bib
description: Subdivide a rectangle into nested rectangles so area represents node
  size and enclosure communicates hierarchy.
labels:
- chart:treemap
- task:part-to-whole
- visual:area
- impact:space-efficiency
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Use treemaps for space-efficient hierarchy size comparison <!-- role: advice -->

Use a treemap to visualize a hierarchy when comparing node sizes quickly is important and screen space is limited.

## Enclosure plus area makes size patterns pop at multiple scales <!-- role: reason -->

Treemaps use containment to show hierarchy and area to show size, enabling rapid macro observations of large groups and micro inspection of smaller elements within the same view.

**Mechanism:** Recursive subdivision creates a space-filling display where relative area supports quick judgments of dominance and distribution across branches.

**Evidence:** Treemaps are enclosure diagrams that recursively subdivide area into rectangles, quickly revealing node sizes; squarified treemaps use approximately square rectangles that offer better readability and size estimation than naive slice-and-dice subdivision [@heerTourVisualizationZoo2010].

**Notes:** Padding or saturation can emphasize enclosure boundaries.

## Context: Weighted hierarchies under space constraints <!-- role: context -->

- **User Goal:** Identify largest contributors and understand distribution across hierarchy.
- **Task:** Compare sizes across nodes and branches.
- **Data:** Hierarchical data with a quantitative size metric.
- **Chart Setting:** Dashboards or reports where compactness matters.
- **Audience:** General audiences if labeling strategy is clear.
- **Success Criterion:** Viewers can reliably pick dominant nodes/branches and compare sizes.

## Exceptions: When structure paths must be traced explicitly <!-- role: exceptions -->

**Break it when:** Understanding explicit parent–child link paths is more important than size comparison. **Why:** Enclosure emphasizes size and grouping more than link structure readability [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some structural clarity and label readability for small rectangles. **Risk:** Very small nodes become effectively invisible. **Mitigation:** Allow zooming into branches or provide search/hover details.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a naive slice-and-dice treemap when many rectangles become long and thin. **Why it fails:** Thin shapes reduce readability and make size estimation harder than more square-like rectangles [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Many rectangles are too thin to label or compare. **Quick Check:** If a large fraction of leaf rectangles have extreme aspect ratios, the layout is likely harming readability. **Stronger Test:** Ask viewers to compare two similarly sized nodes; frequent disagreement suggests poor size estimation.

## Fix: What to do instead <!-- role: fix -->

- Use a squarified treemap layout to improve rectangle aspect ratios.
- Add padding or boundary emphasis to clarify enclosure.
- Provide interaction to zoom into a subtree and reveal small nodes.
- Use a circle-packing layout if emphasizing the hierarchy’s “shape” is more important than space efficiency.
