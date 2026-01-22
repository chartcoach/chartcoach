---
id: use-prediction-ellipse-geometry-as-a-correlation-cue-in-scatterplots
title: Use prediction-ellipse area or minor axis as a primary cue when viewers must
  judge scatterplot correlation
bibliography: references.bib
description: Prediction-ellipse geometry tracks correlation judgments and can serve
  as a perceptual proxy for correlation strength.
labels:
- chart:scatter
- task:rank
- visual:shape
- impact:accuracy
- data:quantitative
- audience:novice
- complexity:advanced
---

## Prediction-ellipse geometry should carry correlation meaning <!-- role: advice -->

When the task is judging correlation from scatterplots, ensure that the perceived area or minor-axis thickness of the point cloud (as captured by a prediction ellipse) provides a clear, consistent cue.

## Ellipse-based features are top predictors of judgments <!-- role: reason -->

Multiple feature families can explain correlation judgments, but prediction-ellipse geometry (area and minor axis) is among the strongest and most consistent predictors, making it a robust perceptual proxy for correlation strength.

**Mechanism:** A tighter relationship produces a visually thinner cloud orthogonal to the trend; ellipse area and minor axis summarize that tightness in a way viewers can perceive quickly.

**Evidence:** Models of forced-choice correlation judgments showed that the prediction ellipse area and the ellipse minor axis outperformed correlation-based predictors across multiple model-quality metrics, placing them among the top-performing features overall [@yangCorrelationJudgmentVisualization2019a]. These kinds of visual features supported building correlation-perception models with comparable precision to models that use correlation directly [@yangCorrelationJudgmentVisualization2019a].

**Notes:** The paper treats these ellipse properties as computable “visual features” that align with what viewers likely extract perceptually.

## When this applies: correlation judgments from point clouds <!-- role: context -->

- **User Goal:** Compare or rank the strength of linear association between two variables.
- **Task:** Forced-choice discrimination or ranking of correlation.
- **Data:** Approximately linear bivariate relationships shown as scatterplots.
- **Chart Setting:** Side-by-side comparison, repeated judgments, or small-multiple dashboards.
- **Audience:** Broad audiences, including those using quick “at a glance” judgments.
- **Success Criterion:** Judgments that track intended correlation differences with low variance.

## When not to follow it: non-elliptical or non-linear structures <!-- role: exceptions -->

**Break it when:** The data pattern is strongly non-linear or multi-modal such that an ellipse is a poor summary of the point cloud. **Why:** Ellipse geometry can misrepresent the structure that viewers should use for the task, weakening the proxy relationship [@yangCorrelationJudgmentVisualization2019a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Prioritizing ellipse-like tightness can reduce emphasis on other structures (clusters, heteroscedasticity). **Risk:** A design optimized for ellipse cues may bias viewers toward interpreting relationships as linear. **Mitigation:** Align the design and evaluation task to the intended inference (linear correlation vs. general association) [@yangCorrelationJudgmentVisualization2019a].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating all “shape” cues as equally useful for correlation judgment. **Why it fails:** Only a small subset of features (including ellipse area/minor axis) strongly aligned with judgments, while many candidates were weaker [@yangCorrelationJudgmentVisualization2019a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users report “it looks similarly correlated” across plots that differ in intended correlation. **Quick Check:** Visually inspect whether one cloud is clearly thinner (smaller minor-axis thickness) than the other. **Stronger Test:** Collect forced-choice judgments and verify accuracy is predictable from ellipse area/minor axis differences [@yangCorrelationJudgmentVisualization2019a].

## What to do instead when ellipse cues are misleading <!-- role: fix -->

- Reframe the task away from linear correlation if the data pattern is non-linear or multi-modal.
- Use a representation or interaction that helps viewers see dispersion around the trend rather than relying on a global cloud summary.
- Validate with a discrimination-threshold experiment to confirm the cue supports the intended judgment [@yangCorrelationJudgmentVisualization2019a].
