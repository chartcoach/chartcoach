---
id: encode-hierarchies-with-contained-cells-to-show-part-whole-within-clusters
title: "Encode cluster hierarchies with contained cell areas to show part\u2013whole\
  \ composition within causes or risks"
bibliography: references.bib
description: Use a hierarchical, cell-contained layout to reveal how sub-causes or
  sub-risks compose higher-level clusters.
labels:
- task:understand
- task:compare
- visual:area
- visual:containment
- impact:clarity
- data:hierarchical
- audience:expert
- complexity:advanced
- domain:health
---

## Use hierarchical cell containment to show what makes up a cluster <!-- role: advice -->

When users must understand what sub-items contribute to a cause or risk cluster and in what proportion, represent the cluster as a hierarchy of contained cells where cell area encodes contribution.

## Why containment + area expresses part–whole within hierarchy <!-- role: reason -->

A containment-based hierarchical layout lets users perceive both membership (which sub-items belong to a cluster) and part–whole composition (relative contribution) within the same structure.

**Mechanism:** Hierarchical containment externalizes structure, and area-based cells provide a direct visual cue for proportional contribution of sub-items within their parent.

**Evidence:** For temporal mortality exploration, hierarchical cluster composition was represented using a blended [Token–Cell–Hierarchy] structure to convey both the hierarchical structure and the proportion of items within each cluster, enabling inspection of composition changes over time (e.g., tuberculosis vs HIV/AIDS within a cluster) [@olaSimpleChartsDesign2016].

**Notes:** Labeling can be minimized in dense views and exposed through interaction when needed.

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Understand which specific causes (or risks) dominate within a higher-level cluster.
- **Task:** Part–whole comparison within a hierarchy; detect composition shifts across time or regions.
- **Data:** Hierarchical categories with quantitative contributions at the leaf level.
- **Chart Setting:** Interactive analytics where clusters can be expanded/collapsed.
- **Audience:** Users comfortable with clustered health taxonomies.
- **Success Criterion:** Users can name dominant sub-items and see composition change without leaving the view.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users only need the cluster total and not its internal composition. **Why:** Exposing hierarchy adds detail and visual complexity without supporting the required decision [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Small sub-items can become hard to label or select when contributions are tiny. **Risk:** Users may miss low-prevalence sub-items. **Mitigation:** Support reveal-on-demand for labels and allow expansion of a selected cluster.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Showing only cluster totals (or only leaf items) when users need both structure and composition. **Why it fails:** The user cannot connect the cluster-level signal to its constituent drivers [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “what’s inside this cluster?” after seeing the visualization. **Quick Check:** Verify that a user can identify both the parent cluster and its top contributing sub-item without switching views. **Stronger Test:** Ask users to compare composition between two times or regions within the same cluster.

## What to do instead <!-- role: fix -->

- Add a contained hierarchical subview that can be opened for the selected cluster.
- Use size (area) to encode contribution and keep membership boundaries visually explicit.
- Provide interaction to expand small cells and reveal labels on demand.
- If proportion is not essential, switch to a simpler ranked list of sub-items within the selected cluster.
