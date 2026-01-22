---
id: separate-exact-match-and-suggested-variable-views-into-distinct-gallery-sections
title: Separate exact-match views from views with added variables in distinct sections
bibliography: references.bib
description: Partition the gallery so users can distinguish charts that match their
  selection from charts that extend it.
labels:
- chart:gallery
- task:browse
- visual:layout
- impact:orientation
- data:tabular
- audience:novice
- system:faceted-browsing
---

## Partition the gallery into “selected only” and “selected plus suggested” sections <!-- role: advice -->

Show charts that use only user-selected variables in one section and charts that include additional recommended variables in another section.

## Clear sectioning reduces confusion about what the system changed <!-- role: reason -->

When a system introduces additional variables, users need to maintain a clear mental model of what they asked for versus what was suggested. Separating these cases supports trust and makes scanning more efficient because users can choose between refining their selection and discovering new fields.

**Mechanism:** Explicit structure provides a stable frame of reference that helps users attribute differences to user intent versus system suggestion.

**Evidence:** The interface design uses distinct “exact match” and “suggestion” sections to group views by whether they contain only selected variables or include additional recommended variables, supporting orientation during browsing [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Headers that describe each section’s contents help users interpret the grouping.

## When recommendations can include variables the user did not select <!-- role: context -->

- **User Goal:** Browse recommendations while staying in control of analysis direction.
- **Task:** Alternating between refining current variables and discovering new ones.
- **Data:** A dataset with enough fields that suggestions add non-selected variables.
- **Chart Setting:** A multi-view recommendation gallery with scrolling.
- **Audience:** Users who need to understand why a chart appeared.
- **Success Criterion:** Users can quickly tell whether a chart matches their selection or extends it.

## When sectioning may be unnecessary <!-- role: exceptions -->

**Break it when:** The system never introduces non-selected variables and only varies encodings or transformations of the selected set. **Why:** The distinction between match and suggestion does not exist, so sectioning adds clutter [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of splitting the gallery into sections <!-- role: costs -->

**Sacrifice:** Additional UI structure consumes vertical space and may reduce charts-per-screen. **Risk:** Users may ignore the suggestion section if it is visually deprioritized. **Mitigation:** Use clear labels and consistent ordering so both sections are easy to scan [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common mistakes in mixed-initiative galleries <!-- role: mistakes -->

**Mistake:** Mixing “selected only” and “selected plus extra variables” charts in one undifferentiated grid. **Why it fails:** Users cannot easily infer which views reflect their intent versus the system’s additions [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for section clarity <!-- role: check -->

**Failure Sign:** Users misinterpret an added variable as part of their selection. **Quick Check:** For any chart that contains a non-selected variable, verify it appears only in the suggestion section. **Stronger Test:** Ask users to classify charts as “selected only” vs “includes a suggestion” during a short browsing task [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users still feel lost <!-- role: fix -->

- Visually differentiate selected-variable labels from suggested-variable labels within each chart (for example, different border styles).
- Add section headers that summarize what varies within the section (variables, transformations).
- Provide controls in the schema panel to exclude variables from suggestions to reduce noise [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
