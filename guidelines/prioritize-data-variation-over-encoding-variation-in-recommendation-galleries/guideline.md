---
id: prioritize-data-variation-over-encoding-variation-in-recommendation-galleries
title: Prioritize data variation over encoding variation in recommendation galleries
bibliography: references.bib
description: Show many different variable sets and transformations first, and defer
  alternative encodings of the same data unless requested.
labels:
- chart:gallery
- task:explore
- visual:layout
- impact:coverage
- data:tabular
- audience:novice
- system:mixed-initiative
---

## Prefer data variation in the default gallery view <!-- role: advice -->

Show different variable subsets and transformations as the primary way to vary recommendations, and avoid filling the gallery with multiple encodings of the same data unless the user asks to drill down.

## Data-first variation increases breadth without overwhelming the gallery <!-- role: reason -->

A gallery has limited attention and space, so showing many near-duplicate encodings can crowd out opportunities to see different parts of the dataset. Prioritizing data variation helps analysts scan broadly, discover relationships they would not think to specify, and reduce premature fixation on a single question.

**Mechanism:** More distinct variable combinations increase the chance of encountering informative structure early, while limiting redundant design variants reduces cognitive load when scanning.

**Evidence:** In a controlled comparison, recommendation browsing led to substantially greater exposure to unique variable sets and more interaction with unique variable sets than manual specification, indicating improved coverage during early exploration [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** This rule concerns the default gallery; design variation can still be valuable when explicitly requested.

## When you are generating and presenting many recommendations at once <!-- role: context -->

- **User Goal:** Build an initial understanding of an unfamiliar dataset and identify promising follow-up questions.
- **Task:** Broad exploratory analysis and scanning for patterns across many variables.
- **Data:** Multivariate tabular data with enough fields that manual enumeration is tedious.
- **Chart Setting:** A multi-view gallery of recommended charts with limited screen real estate.
- **Audience:** Analysts who may not have a clear question yet or lack visualization design expertise.
- **Success Criterion:** High coverage of variables/transformations with low effort and low overwhelm.

## When not to default to data variation first <!-- role: exceptions -->

**Break it when:** The user is refining a specific view to answer a targeted question and needs to compare encoding choices for the same data. **Why:** Encoding variants become the relevant search space once the data subset is fixed [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of a data-variation-first gallery <!-- role: costs -->

**Sacrifice:** You show fewer alternative encodings that might be better for a specific analytic judgment. **Risk:** Users may miss an encoding that improves readability for the selected data. **Mitigation:** Provide a deliberate “expand” affordance that reveals encoding alternatives on demand [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common ways this goes wrong in galleries <!-- role: mistakes -->

**Mistake:** Showing many charts that differ only by swapping color/shape/size for the same variables. **Why it fails:** The gallery becomes visually repetitive and reduces exposure to other variables and transformations [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Fast checks before shipping the gallery defaults <!-- role: check -->

**Failure Sign:** A user scrolling sees many charts that share the same variable capsules with only minor aesthetic differences. **Quick Check:** Count unique variable sets among the first screenful of recommendations; if most repeats are the same set, the gallery is design-heavy. **Stronger Test:** Compare unique variable-set exposure and interaction counts between your gallery and a manual-spec tool in a timed exploration task [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Alternatives when you need more depth on one data slice <!-- role: fix -->

- Add an explicit “expand” mode that shows multiple encodings for the currently selected variable set.
- Cluster recommendations by underlying data table and show only the top-ranked exemplar per cluster in the main gallery.
- Provide a bookmark mechanism so users can save a promising data slice before switching attention to other variables.
- Offer lightweight in-place refinements (for example, transpose, sort, linear/log) without spawning many near-duplicate thumbnails [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
