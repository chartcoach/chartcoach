---
id: use-sankey-or-alluvial-diagrams-to-show-flows
title: Use Sankey or alluvial diagrams to show flows through a system
bibliography: references.bib
description: Flow diagrams show how quantities or categories move between stages or
  groups.
labels:
- chart:sankey
- task:flow
- visual:connection
- impact:clarity
- data:flow
- audience:mainstream
- complexity:intermediate
---

## Use flow diagrams for movement between categories or stages <!-- role: advice -->

Use a Sankey diagram or an alluvial diagram when you need to show how things move through a system or how people shift between categories. Choose the term and styling that best matches whether you emphasize flowing volume or category switching.

## Why flow diagrams fit transition stories <!-- role: reason -->

Flow charts encode transitions as connected bands, turning “from-to” changes into a continuous visual path.

**Mechanism:** Connections preserve origin and destination simultaneously, supporting tracing and comparison of pathways that tables or separate bars make harder to follow.

**Evidence:** Alluvial and Sankey diagrams are presented as common choices to visualize how people change opinions or how things move through a system, with an acknowledged overlap in usage and terminology [@muth_chart_types_guide_2025].

**Notes:** The precise distinction between “Sankey” and “alluvial” is not consistently agreed upon.

## Context <!-- role: context -->

- **User Goal:** Understand transitions (who/what goes where).
- **Task:** Trace major pathways; compare relative magnitudes of flows.
- **Data:** From-to relationships across stages, categories, or time.
- **Chart Setting:** Explanations of systems, switching, and allocation.
- **Audience:** Mainstream readers who can follow connected shapes.
- **Success Criterion:** Readers can identify dominant flows and key switches.

## Exceptions <!-- role: exceptions -->

**Break it when:** Your audience primarily needs simple totals by category without tracing transitions. **Why:** The connective complexity can add unnecessary cognitive load compared with simpler summaries.

## Costs <!-- role: costs -->

**Sacrifice:** Simplicity and ease of reading exact values. **Risk:** Too many small flows can create clutter and make tracing difficult. **Mitigation:** Treat flow count and fragmentation as readability constraints.

## Mistakes <!-- role: mistakes -->

**Mistake:** Using a flow diagram when the story is only “how much in each group,” not “how it moves between groups.” **Why it fails:** The added structure doesn’t support the main question and can distract.

## Check <!-- role: check -->

**Failure Sign:** Readers focus on total sizes and ignore the connections. **Quick Check:** Ask “Do I need to show origins and destinations together?” If not, don’t use a flow diagram. **Stronger Test:** Ask a reader to trace a major pathway from start to end; if they can’t, the diagram is too dense.

## Fix <!-- role: fix -->

- Use a bar chart to show totals by category when transitions are not central.
- Reduce the number of categories or merge tiny flows to reduce fragmentation.
- Highlight a small number of key pathways and de-emphasize the rest.
- Split the story into multiple views if you need both totals and transitions.
