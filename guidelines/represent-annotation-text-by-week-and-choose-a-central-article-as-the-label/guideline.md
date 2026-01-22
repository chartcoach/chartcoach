---
id: represent-annotation-text-by-week-and-choose-a-central-article-as-the-label
title: Represent each selected time window with a central article as the annotation
  label
bibliography: references.bib
description: "When annotating by time windows (e.g., weeks), choose a representative\
  \ article that is central among that window\u2019s articles."
labels:
- chart:line
- task:summarize
- visual:text
- impact:coherence
- data:temporal
- audience:general
- domain:news
- complexity:advanced
---

## Use a representative (central) article to label each selected period <!-- role: advice -->

If annotations are selected at the granularity of a time window such as a week, choose one article that is most representative of that window’s related articles to serve as the displayed annotation text.

## Centrality improves coherence within a time window <!-- role: reason -->

Picking a central article helps the annotation summarize what that period was “about” rather than selecting an outlier headline, which supports the goal of concise but meaningful context.

**Mechanism:** Centrality within a similarity graph favors content that overlaps most with other reporting in that window, making the chosen label less idiosyncratic.

**Evidence:** The system selects five weeks and then chooses the representative article per week by building an article-similarity graph (using Kullback–Leibler divergence) and selecting the article with highest degree centrality, while controlling for relevance to the input article [@hullmanContextifierAutomaticGeneration2013].

**Notes:** This is designed to summarize notable events/issues in each selected week with a single label.

## Applies when annotations summarize clustered news in discrete time windows <!-- role: context -->

- **User Goal:** Skim what was happening in selected historical periods without reading many articles.
- **Task:** Summarize each chosen period with one concise label.
- **Data:** Multiple candidate articles per time window with computable text similarity.
- **Chart Setting:** Annotation budget is small; each annotation must carry high informational value.
- **Audience:** Readers scanning quickly; low tolerance for redundant labels.
- **Success Criterion:** Each period’s annotation reads like a reasonable summary of that period’s reporting.

## When not to use a single representative article label <!-- role: exceptions -->

**Break it when:** The time window contains two or more distinct storylines with low similarity. **Why:** Any single “central” article may misrepresent the diversity of events in that window.

## Tradeoffs of representative-article labeling <!-- role: costs -->

**Sacrifice:** Coverage of minority but potentially important sub-stories within the same window. **Risk:** Centrality can favor generic reporting over the most consequential development. **Mitigation:** Allow multiple annotations within a window only when topical clustering indicates multiple distinct themes.

## Common failure modes in representative labeling <!-- role: mistakes -->

**Mistake:** Displaying several headlines from the same week that are near-duplicates. **Why it fails:** It uses space without adding new context and reduces skim efficiency.

## Quick tests for representative-article fit <!-- role: check -->

**Failure Sign:** Multiple other articles in the window look “more like the week” than the chosen label. **Quick Check:** Sample a few articles from the same window; if most seem unrelated to the chosen label, the representative selection is failing. **Stronger Test:** Ask readers to judge whether the label “summarizes that week’s company news” after reading 2–3 sampled articles.

## What to do instead <!-- role: fix -->

- Split the window into smaller windows when the period is heterogeneous.
- Use two annotations for a window when there are clearly separate story clusters.
- Replace the headline label with a short synthesized snippet derived from the window’s common terms.
