---
id: use-circle-packing-to-reveal-hierarchy-organically-when-some-wasted-space-is-acceptable
title: Use circle packing to reveal hierarchy organically when some wasted space is
  acceptable
bibliography: references.bib
description: Pack nested circles to show hierarchical containment with an organic
  look, trading space efficiency for structure visibility.
labels:
- chart:circle-packing
- task:overview
- visual:area
- impact:structure
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Choose circle packing when hierarchy shape matters more than tight space use <!-- role: advice -->

Use a circle-packing layout to show hierarchical containment when you want the hierarchy to be visually apparent and can tolerate unused space.

## Wasted space can make nesting easier to see <!-- role: reason -->

Compared to treemaps, circle packing uses space less efficiently, but the gaps and round boundaries can make hierarchical nesting more visually salient.

**Mechanism:** Containment of circles creates clear nested group boundaries, and relative circle areas support approximate size comparison.

**Evidence:** Circle-packing layouts have an organic appearance and, though they do not use space as efficiently as treemaps, their “wasted space” effectively reveals the hierarchy while still allowing node size comparison using area judgments [@heerTourVisualizationZoo2010].

**Notes:** Best used for overview rather than dense leaf-level labeling.

## Context: Hierarchy overview with aesthetic and nesting emphasis <!-- role: context -->

- **User Goal:** Understand hierarchical grouping and approximate relative sizes.
- **Task:** Identify major branches and see nesting relationships.
- **Data:** Hierarchical tree with node sizes.
- **Chart Setting:** Overview visuals where aesthetics and structure salience are valued.
- **Audience:** General audiences who benefit from obvious nesting cues.
- **Success Criterion:** Viewers can describe the major groups and their relative dominance.

## Exceptions: When space efficiency is critical <!-- role: exceptions -->

**Break it when:** You must show many leaves with minimal wasted space. **Why:** Circle packing uses space less efficiently than treemaps [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space efficiency and often label room at leaf nodes. **Risk:** Small circles become hard to compare and label. **Mitigation:** Use interaction for details on demand or switch to a treemap for dense displays.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Expecting precise size comparisons across many similarly sized small circles. **Why it fails:** Area judgments become difficult at small sizes and with many items [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Many nodes cannot be identified without interaction because circles are too small. **Quick Check:** If users cannot name or select a target leaf reliably, the layout is too dense. **Stronger Test:** Ask users to find the largest node within a branch; frequent misses suggest insufficient discriminability.

## Fix: What to do instead <!-- role: fix -->

- Switch to a treemap for higher space efficiency and denser leaf display.
- Enable zooming into selected branches to increase effective mark size.
- Aggregate small leaves into an “other” group to reduce clutter.
- Provide search and highlight to locate nodes without relying on labels.
