---
id: use-article-volume-peaks-to-suggest-high-newsworthiness-periods-for-annotation
title: Use article-volume peaks to suggest high-newsworthiness periods for annotation
bibliography: references.bib
description: Treat spikes in the count of related articles over time as candidates
  for important events worth annotating.
labels:
- chart:line
- task:detect
- visual:annotation
- impact:coverage
- data:temporal
- audience:general
- domain:news
- complexity:advanced
---

## Identify candidate annotation periods using peaks in related-article volume <!-- role: advice -->

When selecting events to annotate on a company time series, use peaks in the count of related articles over time to propose time windows likely to correspond to highly newsworthy events.

## Volume can act as a proxy for event importance <!-- role: reason -->

High publishing volume around a company often indicates heightened attention and potentially consequential events, which supports comprehensiveness by reducing the chance that major story periods are omitted.

**Mechanism:** Aggregated article counts can surface periods of concentrated reporting even when individual stories are not lexically similar to the input article.

**Evidence:** The system design uses weekly article-volume counts to capture times when highly newsworthy events likely occurred, and feature comparisons found volume rankings were largely uncorrelated with relevance rankings while being more correlated with salience rankings [@hullmanContextifierAutomaticGeneration2013].

**Notes:** The evaluation did not directly test a volume-only condition for user-rated quality.

## Applies when building contextual timelines from a news corpus <!-- role: context -->

- **User Goal:** Get a more comprehensive picture of what mattered historically for the entity in the article.
- **Task:** Surface major event periods without reading the whole archive.
- **Data:** A time-indexed corpus with enough density to compute meaningful volume fluctuations.
- **Chart Setting:** A timeline where annotations represent selected weeks or dates.
- **Audience:** Readers who may not know which events were historically important.
- **Success Criterion:** The timeline includes major high-attention periods that a relevance-only strategy could miss.

## When not to use article volume as a candidate signal <!-- role: exceptions -->

**Break it when:** The corpus has uneven coverage, syndication artifacts, or systematic bursts unrelated to real-world importance. **Why:** Volume spikes may reflect publishing mechanics rather than meaningful events.

## Tradeoffs of volume-based candidate selection <!-- role: costs -->

**Sacrifice:** Topical coherence with the input article, since high-volume periods may be off-topic. **Risk:** Users may see annotations that feel irrelevant to their current reading goal. **Mitigation:** Use volume as a candidate generator rather than the sole ranking criterion.

## Common failure modes with volume signals <!-- role: mistakes -->

**Mistake:** Selecting annotations primarily from the single highest-volume period regardless of the input article topic. **Why it fails:** The visualization stops being context-for-this-article and becomes generic “biggest news” summarization.

## Quick tests for volume usefulness <!-- role: check -->

**Failure Sign:** Many selected annotations are about unrelated company topics even though the input article is specific. **Quick Check:** Compare selected periods against known major events; if volume misses them or over-selects minor bursts, the signal is unreliable. **Stronger Test:** Have reviewers judge whether each volume-selected annotation period was “newsworthy for the company” independent of the input article.

## What to do instead <!-- role: fix -->

- Use volume only to ensure at least one annotation comes from a high-attention period, then fill remaining slots by relevance and salience.
- Normalize or de-duplicate the corpus to reduce syndication-driven spikes before computing volume.
- Prefer representative-article selection within a high-volume week rather than showing multiple similar headlines.
