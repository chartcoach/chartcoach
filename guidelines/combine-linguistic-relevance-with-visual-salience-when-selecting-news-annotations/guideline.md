---
id: combine-linguistic-relevance-with-visual-salience-when-selecting-news-annotations
title: Combine linguistic relevance with visual salience when selecting news annotations
bibliography: references.bib
description: Balance topical relevance to the input article with visually salient
  data moments when choosing which events to annotate.
labels:
- chart:line
- task:select
- visual:annotation
- impact:relevance
- data:temporal
- audience:general
- domain:news
- complexity:advanced
---

## Select annotations by balancing relevance to the article and salience in the chart <!-- role: advice -->

When automatically choosing which events to annotate on a news-driven time series, rank candidate annotations using both linguistic relevance to the input article and visual (data-driven) salience in the plotted series.

## Relevance and salience optimize different user judgments <!-- role: reason -->

Topical relevance helps ensure annotations match the reader’s current information need, while salience helps ensure annotations align with chart moments that attract attention and feel explanatory of the visible pattern.

**Mechanism:** Relevance reduces topic drift (annotations that are “about the company” but not about the story), while salience increases perceived explanatory power by attaching text to peaks, troughs, and sharp changes.

**Evidence:** In a user rating study of generated stock visualizations, salience-driven selection was rated higher for explaining trends than relevance-only or random selection, and relevance-driven selection was rated higher for relevance than random selection [@hullmanContextifierAutomaticGeneration2013]. Combining relevance and salience improved over random selection but showed a tradeoff versus optimizing either dimension alone [@hullmanContextifierAutomaticGeneration2013].

**Notes:** The paper’s combined approach also included an article-volume feature, but the primary demonstrated gains were from relevance and salience.

## Applies when generating annotated stock or company timelines from a context article <!-- role: context -->

- **User Goal:** Understand a company-focused news article in the context of historical performance and related events.
- **Task:** Choose a small set of annotations that feel both relevant and explanatory.
- **Data:** Time series values (e.g., price, volume) plus a time-indexed corpus of candidate articles/snippets.
- **Chart Setting:** Limited annotation budget (e.g., a handful of callouts) and embedded reading context.
- **Audience:** Readers with limited time; moderate domain knowledge.
- **Success Criterion:** Annotations are judged relevant to the article and helpful for explaining visible changes.

## When not to balance relevance and salience <!-- role: exceptions -->

**Break it when:** The user’s goal is explicitly single-objective (only topical background, or only explaining the plotted movements). **Why:** Multi-objective ranking can dilute performance on the one dimension that matters most to that user.

## Tradeoffs of a balanced ranking strategy <!-- role: costs -->

**Sacrifice:** Optimality on any single dimension, since the selection becomes a compromise. **Risk:** The result can feel “somewhat relevant” and “somewhat explanatory” rather than clearly excelling at either. **Mitigation:** Treat weights as configurable for different use cases.

## Common failure modes in combined selection <!-- role: mistakes -->

**Mistake:** Overweighting one feature so heavily that the other effectively never affects selection. **Why it fails:** The system collapses to a single-feature strategy and loses the intended balance.

## Quick tests for balance quality <!-- role: check -->

**Failure Sign:** Annotations cluster only around extreme chart movements or only around the article’s topic vocabulary, but not both. **Quick Check:** For each annotation, ask two questions—“Is this about the input article?” and “Is it located at a visually notable moment?”; many “no” answers indicate imbalance. **Stronger Test:** Collect separate user ratings for relevance and explanatory power and verify neither collapses toward random baselines.

## What to do instead <!-- role: fix -->

- Generate two candidate sets (relevance-first and salience-first) and merge them to guarantee coverage of both goals.
- Reduce the number of annotations and require each to exceed minimum thresholds on both relevance and salience.
- Provide an interface control to shift weighting between relevance and salience depending on the reader’s intent.
