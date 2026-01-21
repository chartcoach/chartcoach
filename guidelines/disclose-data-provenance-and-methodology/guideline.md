---
id: disclose-data-provenance-and-methodology
title: Cite Data Sources and Methodology Explicitly
bibliography: references.bib
description: Increase perceived transparency and trust by documenting sources, methods,
  exceptions, and corrections.
labels:
- task:explain
- impact:trust
- impact:clarity
- custom:rhetoric:provenance
- audience:novice
- audience:general-public
---

## The Rule <!-- role: advice -->

Cite your **data sources** and provide **methodology notes**, including exceptions, corrections, and key facts needed to interpret the data.

## The Logic <!-- role: reason -->

Provenance rhetoric signals transparency and trustworthiness; such signals cue journalistic/objectivity conventions and shape interpretation by strengthening credibility of the presentation.

- **The Principle:** Transparency cues trust and interpretive acceptance
- **The Evidence:** [@hullmanVisualizationRhetoricFraming2011a]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether to believe the story and how to interpret it
- **Data Type:** Any data that is summarized, aggregated, filtered, or otherwise edited
- **Audience:** Public-facing narrative visualization readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Confidential/internal data where source disclosure is prohibited
- **Reason:** You cannot reveal provenance without violating constraints; disclose as much as permissible.

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and attention (annotations compete with the story)
- **The Risk:** Overloading with methodological detail can reduce engagement.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Listing a vague source (“public data”) without variable definitions or edits
- **Why it fails:** Omissions in provenance can function rhetorically as hidden framing, undermining interpretability [@hullmanVisualizationRhetoricFraming2011a].

## How to Check <!-- role: check -->

- **Visual Sign:** Readers could not reconstruct what was included/excluded or how values were computed
- **The Test:** Ask: “Could a reader explain where the data came from and what transformations occurred?” If not, provenance is insufficient.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a “Source” line plus a short “Notes/Methods” link.
- **Best Fix:** Provide concise in-chart callouts for major data edits (aggregation, thresholds, exclusions) plus a linked methods page.
