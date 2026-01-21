---
id: prioritize-additive-annotations-for-news-context
title: Prioritize Additive Annotations to Provide External Context
bibliography: references.bib
description: Use annotations primarily to add external background, related events,
  or perspectives that contextualize the chart for the accompanying news story.
labels:
- chart:line
- task:contextualize
- visual:annotation
- impact:comprehension
- data:temporal
- audience:general
- domain:journalism
---

## The Rule <!-- role: advice -->

Prioritize additive annotations that bring in external, relevant information (e.g., related events) when annotating news visualizations.

## The Logic <!-- role: reason -->

Additive annotations provide “background or perspective” beyond what the plotted data alone shows, which is especially valuable in news settings where readers need context quickly rather than deep analytic interpretation.

- **The Principle:** Additive context improves narrative comprehension by connecting data to external events.
- **The Evidence:** A qualitative analysis of 136 professional news visualizations found additive annotations were more prevalent than observational annotations (73.5% vs. 49.3%), motivating Contextifier’s focus on additive context [@hullmanContextifierAutomaticGeneration2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Get historical/background context while reading a news article (e.g., “what else happened around these changes?”).
- **Data Type:** Time-indexed series that can be connected to dated external content (e.g., stock prices, traded volume).
- **Audience:** News readers and non-specialists who need fast orientation.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The purpose is analytical explanation of the data itself (e.g., highlighting extremes, comparisons, anomalies).
- **Reason:** Observational annotations may better support direct interpretation of the chart features than external context [@hullmanContextifierAutomaticGeneration2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less emphasis on explaining internal chart structure (peaks/valleys/trends) if you over-invest in external context.
- **The Risk:** Annotations can become a “news list” that distracts from the data rather than supporting interpretation [@hullmanContextifierAutomaticGeneration2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many external callouts without regard to what is visually happening in the chart.
- **Why it fails:** It ignores the need to tie annotations to salient chart features and can reduce coherence/engagement [@hullmanContextifierAutomaticGeneration2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Annotations read like unrelated headlines and don’t map to meaningful moments in the plotted series.
- **The Test:** Ask: “If I remove the line, do the annotations still seem equally valid?” If yes, they may be insufficiently chart-coupled.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to a small set of the most context-relevant events for the shown period.
- **Best Fix:** Combine additive selection with a saliency-aware step so external events are anchored to visually important moments [@hullmanContextifierAutomaticGeneration2013].
