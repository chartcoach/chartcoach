---
id: limit-annotations-to-a-small-fixed-count
title: Limit Annotations to a Small Fixed Count
bibliography: references.bib
description: Constrain the number of annotations so the visualization remains readable
  and useful within brief news-reading sessions.
labels:
- chart:line
- task:annotate
- visual:layout
- impact:clarity
- data:temporal
- audience:general
- domain:journalism
---

## The Rule <!-- role: advice -->

Limit the visualization to a small number of annotations (e.g., five) so the chart stays legible and scannable.

## The Logic <!-- role: reason -->

News-reading is a short-duration task with strong spatial constraints; too many messages reduce coherence and increase confusion. Contextifier explicitly chooses a small set of weeks to annotate to satisfy concision and fit constraints for embedding in an article.

- **The Principle:** Annotation concision preserves readability and narrative coherence under space/time limits.
- **The Evidence:** Contextifier selects five weeks for annotations and notes that over-selecting (e.g., from high-volume weeks) can “detract from the coherency of the messages” and increase confusion [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Skim key contextual events without reading a full timeline of headlines.
- **Data Type:** Dense time series with many plausible event candidates.
- **Audience:** General news readers in embedded or small multiples layouts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is meant as an exploratory entry point for browsing many related items (more like a navigation interface than a summary).
- **Reason:** In that use case, higher annotation density may be intentional, though it changes the chart’s function [@hullmanContextifierAutomaticGeneration2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced comprehensiveness; important events might be omitted.
- **The Risk:** Over-summarization can bias interpretation toward only the selected moments.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding annotations wherever there is available whitespace.
- **Why it fails:** Layout-driven selection ignores relevance/salience and can produce arbitrary narratives.

## How to Check <!-- role: check -->

- **Visual Sign:** Labels overlap, require excessive leader lines, or prevent seeing the line.
- **The Test:** If you cannot read all labels without zooming or interaction, reduce annotation count.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to the top N annotation windows ranked by your selection criteria.
- **Best Fix:** Keep N small and provide details-on-demand (e.g., show snippets on hover and link out) so depth is available without clutter [@hullmanContextifierAutomaticGeneration2013].
