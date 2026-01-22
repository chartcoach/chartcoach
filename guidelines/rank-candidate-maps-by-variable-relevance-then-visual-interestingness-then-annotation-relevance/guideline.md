---
id: rank-candidate-maps-by-variable-relevance-then-visual-interestingness-then-annotation-relevance
title: Rank candidate maps by variable relevance, then visual interestingness, while
  meeting an annotation relevance threshold
bibliography: references.bib
description: Select the final map by prioritizing topic-variable match and spatial
  pattern saliency, subject to annotation quality.
labels:
- chart:map
- task:rank
- visual:layout
- impact:usefulness
- data:geospatial
- audience:novice
- pipeline:ranking
---

## Choose the final map by relevance-first ranking with an annotation threshold <!-- role: advice -->

Rank generated visualizations by highest variable-to-article relevance, then prefer higher visual interestingness among those, and select the top result that stays above an annotation relevance threshold.

## Why relevance-first ranking improves perceived usefulness <!-- role: reason -->

A visually striking map that is off-topic is not useful in a news context; relevance to the article’s content is the primary constraint. Within relevant candidates, emphasizing visually interesting spatial distributions can increase engagement and perceived quality, while enforcing an annotation relevance threshold prevents low-quality callouts from dominating.

**Mechanism:** Constraining by semantic relevance prevents mismatch, and secondary ranking by spatial pattern salience increases the chance the displayed map exhibits interpretable regionalization.

**Evidence:** The ranker uses PMI for variable relevance, cosine similarity for annotation relevance, and Moran’s I for visual interestingness, prioritizing variable match then interestingness while requiring annotation relevance; user ratings were higher when both cosine-similarity-based annotation selection and Moran’s-I-based saliency were included than when either was removed [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** The ordering reflects observed importance of relevance over saliency in the evaluation.

## When relevance-first ranking applies <!-- role: context -->

- **User Goal:** Quickly understand an article with a supporting map that feels on-topic and informative.
- **Task:** Select one visualization from multiple generated candidates.
- **Data:** Many possible variables and many possible map renderings per article.
- **Chart Setting:** Automated pipeline producing N candidate annotated maps.
- **Audience:** General readers; sensitive to irrelevant visuals and misleading context.
- **Success Criterion:** Higher perceived map usefulness, relevance, and interestingness.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The product goal is exploratory discovery rather than article accompaniment. **Why:** Relevance-first ranking can suppress novel but tangentially related views that may be desirable in exploration.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Potentially reduces diversity of shown maps by repeatedly choosing the most topically aligned variables. **Risk:** If PMI is noisy, relevance-first ranking can lock onto the wrong variable and still optimize saliency. **Mitigation:** Keep multiple high-PMI candidates and apply sanity checks before final selection.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Ranking primarily by visual “interestingness” without enforcing topical relevance. **Why it fails:** Users can receive visually salient but irrelevant maps that do not help explain the article.

## Quick tests <!-- role: check -->

**Failure Sign:** The chosen map is visually striking but users rate it as not relevant to the story. **Quick Check:** Confirm the selected variable is among the top PMI-ranked variables for the article. **Stronger Test:** Compare user ratings for relevance and overall usefulness across different ranking orders.

## What to do instead <!-- role: fix -->

- Filter to a small set of top PMI variables before applying any saliency-based ranking.
- Enforce a minimum annotation relevance threshold before considering a candidate eligible.
- If annotation relevance cannot be met, remove additive annotations and show a simpler map variant.
