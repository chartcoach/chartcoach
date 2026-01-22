---
id: rank-correlation-charts-by-jnd-weber-model
title: Rank correlation visualizations by predicted JND from a fitted Weber model
bibliography: references.bib
description: Use Weber-law JND models to quantitatively compare and rank correlation
  visualizations for a target correlation range.
labels:
- chart:scatter
- task:rank
- visual:position
- impact:accuracy
- data:quantitative
- audience:practitioner
- method:weber-law
---

## Rank by Weber-law JND predictions for your correlation range <!-- role: advice -->

Rank candidate visualizations by the just-noticeable difference (JND) predicted by their Weber model over the correlation values you need to communicate. Prefer the visualization (and correlation-direction variant) with the lowest predicted JND in that range.

## Why Weber-model JND ranking predicts correlation-judgment precision <!-- role: reason -->

Correlation judgment precision can be summarized as the smallest change in correlation that viewers can reliably detect (the JND). When a visualization’s JND varies linearly with adjusted correlation (a Weber-law relationship), that fitted line becomes a compact, predictive way to compare “how precise” different visualization designs are for correlation discrimination.

**Mechanism:** Lower JND means viewers can discriminate smaller differences in correlation, so comparisons and rankings of correlations become perceptually easier and more reliable.

**Evidence:** Across nine common visualization forms, correlation-discrimination precision followed Weber’s law (JND as a linear function of adjusted correlation), enabling prediction at untested correlation values and direct ranking by model output [@harrisonRankingVisualizationsCorrelation2014a]. The paper demonstrates producing per‑r rankings (including predicted r values) and an overall ranking by averaging performance across correlations using the fitted Weber models [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** The paper’s ranking treats positive and negative correlations as separate conditions because many charts show strong direction asymmetries.

## When Weber-model ranking applies <!-- role: context -->

- **User Goal:** Choose the most perceptually precise chart to communicate strength of correlation.
- **Task:** Discriminate which of two datasets is more correlated (precision), possibly across multiple r values.
- **Data:** Two quantitative variables with correlations in a known range (the paper tested |r| from about 0.3 to 0.8, and predicts beyond via the model).
- **Chart Setting:** Static side-by-side comparisons or workflows where viewers must judge correlation differences.
- **Audience:** General audiences (crowdsourced participants) or mixed statistical backgrounds.
- **Success Criterion:** Smaller detectable differences in correlation (lower JND) for the correlation range that matters.

## When not to use this ranking approach <!-- role: exceptions -->

- **Break it when:** Your goal is “accuracy of numeric estimation” of r rather than discrimination (precision). **Why:** The modeled outcome here is JND-based discrimination, not direct numeric readout.
- **Break it when:** A visualization×correlation-direction pair yields unreliable JNDs (many results at the method’s chance boundary). **Why:** The model fit and ranking become unstable when viewers cannot reliably perceive correlation in that condition.

## Tradeoffs of Weber-model ranking <!-- role: costs -->

**Sacrifice:** You need experimental measurements (or an existing model) to fit Weber parameters before ranking. **Risk:** Rankings can differ by correlation value (model lines can cross), so a single global “best” can be misleading if your r range is narrow. **Mitigation:** Rank within the correlation interval you care about, not only by an overall average.

## Common mistakes when ranking correlation charts <!-- role: mistakes -->

- **Mistake:** Treating “positive” and “negative” correlations as equivalent for a given chart. **Why it fails:** Many visualization forms show strong asymmetry between positive and negative correlation perception, requiring separate models.
- **Mistake:** Picking a chart based on a single representative r (for example, mid-range only). **Why it fails:** The paper shows rank order can change across correlation values due to different model slopes/intercepts.

## Quick checks for whether your ranking is trustworthy <!-- role: check -->

**Failure Sign:** Viewers’ discrimination performance looks like guessing for a chart (many JNDs near the chance boundary). **Quick Check:** Verify the selected visualization×direction has a stable fitted line (high linear fit) and predicted JNDs well below the chance boundary across your r range. **Stronger Test:** Run a small staircase/JND pilot for your exact chart settings and correlation range, then refit and rerank.

## What to do instead if Weber-model ranking is not usable <!-- role: fix -->

- Fit separate Weber models for positive and negative correlations and rank them independently for your use case.
- Restrict the candidate set to visualization×direction pairs with reliable JND measurements (well below the chance boundary) before ranking.
- If your target correlations fall outside the reliably measured region, collect additional JND measurements in that region and refit the model.
- If the task is numeric estimation rather than discrimination, evaluate with an accuracy-focused method instead of JND ranking.
