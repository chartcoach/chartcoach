---
id: do-not-rely-on-perceptual-distance-models-alone-to-predict-colormap-performance
title: Do not rely on perceptual distance models alone to predict colormap performance
bibliography: references.bib
description: Perceptual color spaces and color-name models only weakly predict user
  accuracy and speed in triplet similarity judgments, so validate with task-based
  testing.
labels:
- chart:heatmap
- task:evaluate
- visual:color
- impact:trust
- data:quantitative
- audience:designer
- complexity:advanced
---

## Validate colormap choices with task-based tests instead of trusting color-distance metrics alone <!-- role: advice -->

Do not assume that uniform distances in a perceptual color space will translate into uniform user performance on comparison tasks. Validate candidate colormaps with task-based checks that resemble the comparisons users will actually make.

## Predictive models explain little variance in observed performance <!-- role: reason -->

Perceptual color models are calibrated on pairwise discrimination and can miss contextual and task-driven effects; adding categorical (name-based) measures helps but still leaves most performance unexplained.

**Mechanism:** Triplet judgments depend on comparing differences between two perceived distances (not just detecting a difference), and contextual factors (like background and categorical boundaries) can dominate over nominal color-space distances.

**Evidence:** Models based on CIELAB (CIELAB) and CAM02-UCS (Uniform Color Space) distances and a color-name distance measure improved when combined, but still explained only a small fraction of observed error variance (about 10%) and a limited fraction of response-time variance (about 24%) [@liuSomewhereRainbowEmpirical2018a]. The models also did a poor job ranking colormaps by observed error, indicating limited usefulness for selecting among palettes without empirical validation [@liuSomewhereRainbowEmpirical2018a].

**Notes:** The studied task included a visible legend; model fit might differ without legends, but the demonstrated limitation holds for the tested decision context.

## Context <!-- role: context -->

- **User Goal:** Choose or generate a colormap that supports accurate judgments.
- **Task:** Predicting comparison accuracy/speed from computed palette metrics.
- **Data:** Continuous quantitative encodings using color.
- **Chart Setting:** Designs where color is used for similarity judgments with legends.
- **Audience:** Visualization designers, tool builders, and library maintainers.
- **Success Criterion:** Palette choice that reliably supports user judgments, not just good metric scores.

## Exceptions <!-- role: exceptions -->

**Break it when:** You only need a rough first-pass filter among many candidate palettes before running user tests. **Why:** Metrics can still be useful for narrowing options even if they are not reliable selectors by themselves.

## Costs <!-- role: costs -->

**Sacrifice:** Running task-based validation takes time and participants. **Risk:** Overfitting evaluation to one micro-task could miss other real usage patterns. **Mitigation:** Align the validation task with the intended user decisions (e.g., similarity judgments vs threshold detection).

## Mistakes <!-- role: mistakes -->

- **Mistake:** Selecting a palette solely because it is “perceptually uniform” by a distance metric. **Why it fails:** The study showed that distance metrics (even combined with naming) weakly predicted actual errors and response times.
- **Mistake:** Treating a single numeric score (e.g., average distance) as a proxy for performance everywhere on the scale. **Why it fails:** Localized failures (e.g., dark regions, midpoint boundaries) can dominate error.

## Check <!-- role: check -->

**Failure Sign:** A palette scores well on computed metrics but users still make clustered errors in certain regions of the scale. **Quick Check:** Probe performance on small-span triplets at multiple reference locations, including extremes and boundary regions. **Stronger Test:** Run a short within-subjects study with triplet judgments over spans and reference points similar to expected usage.

## Fix <!-- role: fix -->

- Run a small pilot with representative “which is closer” comparisons across the scale before standardizing a colormap.
- Stratify evaluation by scale location (low/mid/high) and by comparison span to detect localized failures.
- Include the actual background and viewing context (e.g., white UI) in the test stimuli.
- If you must use metrics, combine perceptual distance measures with color-name distance measures as a screening heuristic, then validate empirically.
