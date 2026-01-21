---
id: avoid-connecting-items-when-users-must-estimate-number-of-parts
title: Avoid Connecting Items When Users Must Estimate Number of Parts
bibliography: references.bib
description: Connecting marks can reduce perceived number of underlying items, so
  avoid connections when numerosity judgments are important.
labels:
- chart:network
- task:summarize
- task:compare
- visual:connection
- impact:accuracy
- data:relational
- audience:general
---

## The Rule <!-- role: advice -->

If users must estimate how many items are present, avoid visually connecting items (e.g., with lines) in ways that merge parts into perceived wholes.

## The Logic <!-- role: reason -->

- **The Principle:** Perceived numerosity relies on segmented objects.
- **The Evidence:** The paper reports that grouping objects through visual connection can cause underestimation of the number of original parts, and warns visualization designers (e.g., network diagrams) accordingly [@szafirFourTypesEnsemble2016a].

## Where to Apply <!-- role: context -->

- **User Goal:** Judge counts of nodes/items or compare counts across groups.
- **Data Type:** Node-link diagrams, connected scatterplots, flow-like diagrams, or any display where edges visually fuse items.
- **Audience:** Any audience making quick numerosity judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When the relationship structure (edges) is the primary message and numerosity is secondary.
- **Reason:** Removing connections may destroy the relational information the visualization is meant to convey [@szafirFourTypesEnsemble2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may reduce readability of connectivity or path structure.
- **The Risk:** Viewers may misinterpret the graph’s topology if you minimize or de-emphasize edges too strongly [@szafirFourTypesEnsemble2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more edges to “clarify” structure while also asking users “How many nodes are there?”
- **Why it fails:** Stronger connection cues can further collapse segmentation and worsen undercounting [@szafirFourTypesEnsemble2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Users report fewer items than actually present, especially in dense connected regions.
- **The Test:** Show a version with edges removed; if perceived count increases markedly, connections are biasing numerosity [@szafirFourTypesEnsemble2016a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** De-emphasize edges (lighter stroke, fewer edges) when count tasks are required.
- **Best Fix:** Provide a separate unconnected view (or small multiple) specifically for numerosity, while keeping a connected view for relationship reading [@szafirFourTypesEnsemble2016a].
