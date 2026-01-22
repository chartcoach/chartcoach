---
id: use-indented-trees-for-interactive-finding-and-label-scanning-not-for-compact-overview
title: Use indented trees for interactive finding and label scanning, not for compact
  multiscale overviews
bibliography: references.bib
description: Choose indented tree layouts when users must navigate to specific nodes
  and read labels, despite vertical space costs.
labels:
- chart:tree
- task:navigate
- visual:position
- impact:findability
- data:hierarchical
- audience:general
- complexity:foundational
---

## Use indented trees when label reading and targeted search dominate <!-- role: advice -->

Use an indented tree layout when users need efficient interactive exploration to find specific nodes and rapidly scan node labels.

## Indentation supports navigation but wastes space <!-- role: reason -->

Indentation aligns labels and reveals containment via horizontal offsets, which helps scanning and targeted expansion, but it consumes substantial vertical space and is weaker for simultaneous multiscale inference.

**Mechanism:** Progressive disclosure (expand/collapse) reduces visible complexity for search tasks, while aligned text supports label scanning.

**Evidence:** Indented trees allow efficient interactive exploration to find a specific node and enable rapid scanning of node labels, but they require excessive vertical space and do not facilitate multiscale inferences [@heerTourVisualizationZoo2010].

**Notes:** Adjacent columns can carry extra attributes (for example, file size) alongside the hierarchy.

## Context: Navigating hierarchies by name <!-- role: context -->

- **User Goal:** Locate a specific item within a hierarchy and understand its path.
- **Task:** Browse, expand/collapse, scan labels, and inspect adjacent attributes.
- **Data:** Hierarchical structures with meaningful node names.
- **Chart Setting:** UI with interaction (expand/collapse), often list-like navigation panels.
- **Audience:** General audiences accustomed to file-browser patterns.
- **Success Criterion:** Users can find nodes quickly and read labels reliably.

## Exceptions: When overview and compactness are required <!-- role: exceptions -->

**Break it when:** Users need dense multiscale comparison across the whole hierarchy at once. **Why:** Indented trees do not facilitate multiscale inference and consume excessive vertical space [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Space efficiency and whole-structure overview. **Risk:** Deep trees require extensive scrolling, causing users to lose context. **Mitigation:** Use collapsible sections and persistent breadcrumbs to maintain orientation.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using an indented tree as the primary view for comparing sizes or structure across many branches simultaneously. **Why it fails:** The layout is not designed for multiscale inference and wastes vertical space [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users scroll extensively and still cannot compare branches or remember where they are. **Quick Check:** Count how many screens of scrolling are needed to reach common targets; excessive scrolling suggests a mismatch. **Stronger Test:** Time “find node X” tasks and compare against a space-filling hierarchy view for the same data.

## Fix: What to do instead <!-- role: fix -->

- Use a treemap or adjacency diagram when size comparison across the hierarchy is central.
- Use a node-link tree when structure readability (parent/child relationships) matters more than space filling.
- Provide a search box and breadcrumb trail to reduce navigation cost.
- Offer an overview+detail pattern: a space-filling overview paired with an indented navigation panel.
