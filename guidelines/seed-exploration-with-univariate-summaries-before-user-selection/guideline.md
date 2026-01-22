---
id: seed-exploration-with-univariate-summaries-before-user-selection
title: Seed exploration with univariate summaries before user selection
bibliography: references.bib
description: Avoid empty or directionless starting states by showing an initial overview
  for every variable.
labels:
- chart:histogram
- chart:bar
- task:explore
- visual:overview
- impact:orientation
- data:mixed-types
- audience:novice
- system:recommendation
---

## Show one-variable summaries for all fields on load <!-- role: advice -->

When no variables are selected, populate the gallery with univariate summaries for each variable so users can quickly orient and start steering exploration.

## Overviews reduce empty starts and premature fixation <!-- role: reason -->

A blank canvas forces users to guess where to start and can cause early fixation on a small subset of fields. Univariate summaries provide immediate structure: distributions for quantitative fields and counts for categorical fields, enabling informed next clicks.

**Mechanism:** A complete one-field overview lowers the cost of “reading the schema” and turns variable selection into a recognition task rather than recall.

**Evidence:** The system design uses univariate summaries as the default gallery content to discourage empty-result states and to encourage broad initial examination of variables as part of early exploration [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** The summaries can be simple; the key is coverage across all variables.

## When users are just starting with unfamiliar data <!-- role: context -->

- **User Goal:** Understand what variables exist and what their basic distributions look like.
- **Task:** Orientation and deciding what to explore next.
- **Data:** A table with multiple variable types (nominal, ordinal, quantitative, temporal).
- **Chart Setting:** Recommendation gallery or browser that otherwise requires selections to produce views.
- **Audience:** Users who have not previously analyzed the dataset.
- **Success Criterion:** Users can pick next variables quickly without prior knowledge.

## When univariate-first is not the best default <!-- role: exceptions -->

**Break it when:** The user arrives with a known question and already knows which variables to analyze. **Why:** They may prefer immediately constructing targeted multivariate views rather than scanning every variable [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of showing all univariate views <!-- role: costs -->

**Sacrifice:** Initial screen space is consumed by many small charts. **Risk:** Users might treat the overview as exhaustive and not proceed to relationships. **Mitigation:** Make variable selection and “add one more variable” recommendations prominent so users naturally move from univariate to multivariate views [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common failure modes for overview-first starts <!-- role: mistakes -->

**Mistake:** Showing only the schema list with no visual summaries. **Why it fails:** Users must guess which fields are informative and may overlook important variables [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick tests for a good starting state <!-- role: check -->

**Failure Sign:** Users hesitate at the beginning and ask “what should I click?” **Quick Check:** With no selections, verify that every field has at least one visible summary view. **Stronger Test:** Run a timed “first 5 minutes” exploration and measure how quickly users begin interacting with multiple variables [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if the overview feels too dense <!-- role: fix -->

- Show exactly one default univariate chart per variable and defer variants (sorting, scale, bin count) to interactions.
- Provide a predictable ordering of the summaries (for example, grouped by data type) to support scanning.
- Allow users to exclude variables from future suggestions to focus after initial orientation [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
