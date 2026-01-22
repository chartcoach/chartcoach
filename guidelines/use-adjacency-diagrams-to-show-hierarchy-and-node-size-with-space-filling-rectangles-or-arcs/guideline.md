---
id: use-adjacency-diagrams-to-show-hierarchy-and-node-size-with-space-filling-rectangles-or-arcs
title: Use adjacency diagrams to show hierarchy and node size with space-filling rectangles
  or arcs
bibliography: references.bib
description: "Represent parent\u2013child relationships with adjacent bars or arcs\
  \ so length can encode node size in a compact layout."
labels:
- chart:adjacency-diagram
- task:part-to-whole
- visual:length
- impact:space-efficiency
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Use space-filling adjacency to encode hierarchy and size simultaneously <!-- role: advice -->

Use an adjacency diagram (such as an icicle or sunburst layout) when you need a space-filling hierarchy view where node size can be read from bar or arc length.

## Space filling enables an additional quantitative encoding <!-- role: reason -->

Replacing link lines with adjacent areas preserves hierarchical structure while enabling length to encode a numeric attribute, which is difficult to show in standard node-link trees without clutter.

**Mechanism:** Adjacency conveys parent–child containment through placement, freeing visual channels (like length) for quantitative attributes.

**Evidence:** Adjacency diagrams are space-filling variants of node-link diagrams where nodes are solid areas and placement reveals hierarchy; because nodes are space-filling, length can encode node size, revealing an additional dimension that is difficult to show in a node-link diagram [@heerTourVisualizationZoo2010].

**Notes:** Icicle and sunburst layouts are related via Cartesian vs polar coordinates.

## Context: Hierarchies with meaningful node weights <!-- role: context -->

- **User Goal:** Understand hierarchical structure and relative sizes of nodes.
- **Task:** Compare node sizes and locate large branches.
- **Data:** Tree-structured hierarchy with a quantitative value per node (size, counts, bytes).
- **Chart Setting:** Static or interactive; space constraints favor compactness.
- **Audience:** General audiences if labeling is handled carefully.
- **Success Criterion:** Viewers can identify large nodes/branches and understand nesting.

## Exceptions: When label readability is the primary need <!-- role: exceptions -->

**Break it when:** Accurate reading of many node labels is more important than size comparison. **Why:** Space-filling layouts can reduce label space and make scanning harder than indented trees [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Label legibility for small nodes. **Risk:** Thin segments become hard to select or interpret. **Mitigation:** Use interaction to reveal labels/details on demand.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Expecting viewers to compare many tiny leaf nodes by length when the layout produces very thin segments. **Why it fails:** Extremely small marks undermine both label and size decoding in space-filling layouts [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Many nodes cannot be labeled or selected without ambiguity. **Quick Check:** Count the proportion of nodes whose label is truncated or missing at default view; a high proportion suggests a mismatch. **Stronger Test:** Ask viewers to find the largest node in a subtree; frequent errors indicate insufficient discriminability.

## Fix: What to do instead <!-- role: fix -->

- Aggregate or prune low-importance leaves to increase mark sizes.
- Add interaction to zoom into a branch or show tooltips for small nodes.
- Use a treemap when rectangular area comparisons are preferred over adjacency structure.
- Use an indented tree when label scanning and targeted navigation are the main tasks.
