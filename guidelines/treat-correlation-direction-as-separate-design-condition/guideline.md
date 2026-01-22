---
id: treat-correlation-direction-as-separate-design-condition
title: Treat positive and negative correlation as separate visualization conditions
  when choosing a chart
bibliography: references.bib
description: Many charts change perceptual performance depending on correlation sign,
  so evaluate and choose separately for positive vs negative correlations.
labels:
- chart:parallel-coordinates
- task:choose
- visual:orientation
- impact:accuracy
- data:quantitative
- audience:practitioner
- concept:asymmetry
---

## Evaluate and select charts separately for positive versus negative correlations <!-- role: advice -->

Choose a visualization for correlation only after checking its performance for the correlation direction you expect (positive or negative), because the same chart can be much more precise for one sign than the other.

## Why correlation sign can change perceptual precision for the same chart <!-- role: reason -->

Many visualization forms produce different visual structures for positive versus negative correlations even when the magnitude |r| is the same. If the salient visual features differ by sign, viewers’ discrimination thresholds (JNDs) can also differ, requiring separate performance assessments.

**Mechanism:** When the sign flips, the chart’s geometry and overlap patterns can change, which changes the perceptual cues viewers use to judge “more correlated,” altering JND.

**Evidence:** The paper finds striking sign asymmetries across visualization types, including parallel coordinates where negatively correlated data significantly outperformed positively correlated data, while scatterplots showed no significant difference between positive and negative performance [@harrisonRankingVisualizationsCorrelation2014a]. The paper concludes that many visualizations may require two Weber models—one per sign—to be described completely [@harrisonRankingVisualizationsCorrelation2014a].

**Notes:** Some visualization×direction pairs were excluded due to unreliable JNDs, reinforcing that sign can be a gating factor for whether correlation is perceivable at all.

## When to separate positive and negative correlation in design decisions <!-- role: context -->

- **User Goal:** Communicate correlation strength reliably.
- **Task:** Compare correlations or detect differences in correlation.
- **Data:** Bivariate quantitative data where correlation sign is meaningful and may vary across subsets.
- **Chart Setting:** Static charts or dashboards where readers may compare multiple correlated relationships.
- **Audience:** Mixed literacy audiences where reliance on strong perceptual cues matters.
- **Success Criterion:** Low JND for the expected sign; no chance-boundary behavior for that sign.

## When this separation is less necessary <!-- role: exceptions -->

**Break it when:** You are using a visualization that shows symmetric JND performance across signs in your validated setting. **Why:** A single model or evaluation may be sufficient when sign does not change discrimination precision.

## Tradeoffs of treating sign as a separate condition <!-- role: costs -->

**Sacrifice:** More evaluation effort, because each chart may need separate assessment (or separate fitted models) for positive and negative correlations. **Risk:** Overcomplicating selection when your data rarely includes one sign. **Mitigation:** Limit sign-specific evaluation to the sign(s) present in your target data.

## Common mistakes around correlation sign <!-- role: mistakes -->

- **Mistake:** Assuming that performance for |r| generalizes across signs for any chart. **Why it fails:** The paper shows large sign-dependent differences for several chart types.
- **Mistake:** Using a chart that performed well for negative correlations to present mostly positive correlations (or vice versa). **Why it fails:** The discriminability threshold can be substantially worse after the sign flip.

## Quick checks for sign sensitivity <!-- role: check -->

**Failure Sign:** A chart looks visually “structured” for one sign but visually “noisy” or ambiguous for the other at the same |r|. **Quick Check:** Compare predicted JND (or measured JND) for the chart under positive and negative conditions at your target |r|. **Stronger Test:** Run a small forced-choice staircase for both signs on representative correlation levels and compare resulting JNDs.

## What to do instead when sign sensitivity is a problem <!-- role: fix -->

- Use a visualization form (or a sign-specific variant) that has low JND for the sign you need to communicate.
- Maintain separate sign-specific chart choices within the same product if users will encounter both signs.
- Re-encode or reorder within a visualization family when feasible so that the more perceptible sign structure is emphasized for the relationships users will compare.
- If a sign condition yields chance-level perception, switch to a different visualization form for that sign.
