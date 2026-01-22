---
id: visually-distinguish-user-selected-fields-from-system-suggested-fields-in-each-chart
title: Visually distinguish user-selected fields from system-suggested fields in each
  chart
bibliography: references.bib
description: Mark which variables the user chose and which were added by the system
  to preserve control and attribution.
labels:
- chart:gallery
- task:browse
- visual:annotation
- impact:orientation
- data:tabular
- audience:novice
- system:mixed-initiative
---

## Label selected and suggested variables with distinct visual treatments <!-- role: advice -->

In each recommended chart, display variable labels that clearly differentiate user-selected variables from system-suggested variables using consistent, easily recognized styling.

## Clear attribution supports trust and comprehension in mixed-initiative systems <!-- role: reason -->

When recommendations include elements the user did not explicitly request, users need to know what the system contributed to interpret the result and decide the next step. Distinguishing selected versus suggested fields helps users maintain agency while benefiting from automation.

**Mechanism:** Visual attribution reduces ambiguity about the source of a chart’s content and prevents misattributing added variables to user intent.

**Evidence:** The interface differentiates selected-variable capsules from suggested-variable capsules using different visual styles within each view to help users stay oriented while browsing recommendations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Consistent styling across the gallery helps users learn the meaning quickly.

## When the system can add variables beyond user input <!-- role: context -->

- **User Goal:** Browse recommendations while understanding what was requested versus suggested.
- **Task:** Interpreting and steering recommended charts.
- **Data:** A dataset where recommendations routinely introduce additional fields.
- **Chart Setting:** Multi-view gallery with field capsules or similar labels per chart.
- **Audience:** Users who may be unfamiliar with the data and the system’s behavior.
- **Success Criterion:** Users can correctly identify which fields they selected without effort.

## When this distinction is unnecessary <!-- role: exceptions -->

**Break it when:** The system never adds variables and only displays charts built strictly from user input. **Why:** There is no attribution ambiguity to resolve [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of explicit attribution styling <!-- role: costs -->

**Sacrifice:** Additional visual elements can add slight clutter in small thumbnails. **Risk:** Overly subtle styling may be missed; overly strong styling may distract from the chart. **Mitigation:** Use a small but consistent difference that is legible at thumbnail size [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes in mixed-initiative labeling <!-- role: mistakes -->

**Mistake:** Using identical styling for selected and suggested variables in chart labels. **Why it fails:** Users cannot tell what the system added and may misunderstand why a view appears [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for attribution clarity <!-- role: check -->

**Failure Sign:** Users believe they selected a variable that was actually suggested. **Quick Check:** In any view with a suggested variable, verify the suggested label is visually distinct from selected labels. **Stronger Test:** Ask users to point out which fields they selected for a given recommended chart; errors indicate insufficient distinction [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users still miss the distinction <!-- role: fix -->

- Add a section-level separation between exact-match and suggestion views so attribution is reinforced by layout.
- Include a short header summary that states whether a section contains only selected variables or includes added variables.
- Provide a control to exclude suggested variables so users can validate that the system is adding fields intentionally [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
