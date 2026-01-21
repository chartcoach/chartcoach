---
id: use-indented-trees-for-interactive-search-and-label-scanning
title: Use Indented Trees for Fast Label Scanning and Interactive Finding
bibliography: references.bib
description: Use indented trees when users need to efficiently scan labels and interactively
  expand to find specific nodes.
labels:
- chart:tree
- task:find
- visual:position
- impact:usability
- data:hierarchical
- audience:novice
- complexity:foundational
---

## The Rule <!-- role: advice -->

Use an indented tree layout when the task is to find a specific node through interactive exploration and label scanning.

## The Logic <!-- role: reason -->

Indented trees support efficient interactive expansion/collapse and rapid scanning of node labels; they also allow showing adjacent multivariate attributes (e.g., file size) alongside the hierarchy.

- **The Principle:** Prioritize navigability and label readability over compact structure depiction
- **The Evidence:** [@heerTourVisualizationZoo2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Locate a known item in a hierarchy (files, menus, package lists)
- **Data Type:** Hierarchies with meaningful labels
- **Audience:** General users performing lookup/navigation

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need multiscale inferences (simultaneous micro + macro structure understanding)
- **Reason:** Indented trees use excessive vertical space and do not facilitate multiscale inferences [@heerTourVisualizationZoo2010]

## The Price <!-- role: costs -->

- **The Sacrifice:** Screen space efficiency
- **The Risk:** Deep trees become long and require lots of scrolling

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using an indented tree to communicate overall hierarchy shape at a glance
- **Why it fails:** The layout is optimized for finding nodes, not summarizing structure [@heerTourVisualizationZoo2010]

## How to Check <!-- role: check -->

- **Visual Sign:** Users scroll extensively and still can’t infer high-level structure
- **The Test:** If users ask “what are the major branches?” rather than “where is X?”, you’re using the wrong layout [@heerTourVisualizationZoo2010]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add collapse/expand controls and show key attributes in aligned columns
- **Best Fix:** Provide an alternative overview (e.g., treemap/icicle) for macro structure while retaining indented tree for search [@heerTourVisualizationZoo2010]
