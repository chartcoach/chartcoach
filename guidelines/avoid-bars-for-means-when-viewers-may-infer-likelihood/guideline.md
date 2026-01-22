---
id: avoid-bars-for-means-when-viewers-may-infer-likelihood
title: Avoid bar charts to depict means when viewers may infer likelihood of values
bibliography: references.bib
description: Bars used for averages can make values visually 'inside the bar' seem
  more likely than equally distant values outside it.
labels:
- chart:bar
- task:infer
- visual:position
- impact:accuracy
- data:distribution
- audience:novice
- cognitive-bias:within-the-bar
---

## Prefer non-bar encodings for means in likelihood or distribution-interpretation contexts <!-- role: advice -->

Avoid using a bar whose edge represents a mean when readers are likely to judge how probable particular values are. Use an encoding that does not create an “inside the bar” region for the mean.

## Object boundaries make “inside the bar” feel like where the data live <!-- role: reason -->

A bar is perceived as a bounded visual object, and attention and interpretation tend to privilege regions inside an object over equally distant regions outside it. When a mean is depicted as the end of a bar that extends to an axis, viewers can misread the filled region as containing more plausible data values than the empty region beyond the bar, even when those values are equidistant from the mean.

**Mechanism:** The bar’s filled area behaves like a container in perception, shifting subjective likelihood toward values that would fall within the bar’s extent rather than treating equal deviations above and below the mean symmetrically.

**Evidence:** Viewers rated test values as more likely when they would fall within the bar than when they were equally distant from the mean but outside the bar, across multiple experiments and participant populations [@newmanBarGraphsDepicting2012]. The bias persisted with and without error bars, with bars rising from a lower axis or falling from an upper axis, and even when judgments were made while the graph remained visible [@newmanBarGraphsDepicting2012].

**Notes:** The effect occurred even when the compared test values had equally extreme numeric labels (e.g., +5 vs. −5 around a mean of zero), indicating it is not merely a preference for less extreme numbers [@newmanBarGraphsDepicting2012].

## When the reader might reason from a mean to “what values are likely” <!-- role: context -->

- **User Goal:** Judge whether a particular value is plausible given a displayed average.
- **Task:** Likelihood judgment or inference about a distribution from a mean.
- **Data:** A distribution summarized by a central tendency (e.g., mean) without showing the full distribution.
- **Chart Setting:** Static or interactive displays where the mean is drawn as a bar extending from a single axis.
- **Audience:** General audiences or analysts making quick judgments from summaries.
- **Success Criterion:** Readers treat equal deviations above and below the mean as equally plausible unless additional distribution information is provided.

## When not to avoid bar charts for means <!-- role: exceptions -->

**Break it when:** The quantity being shown is inherently asymmetric from a baseline (such as counts or other values that conceptually accumulate from zero). **Why:** The “within” region corresponds to meaningful magnitude-from-baseline rather than an implied region of likely observations around a mean [@newmanBarGraphsDepicting2012].

## Tradeoffs and risks of avoiding mean-as-bar encodings <!-- role: costs -->

**Sacrifice:** You may lose a familiar visual form that some audiences expect for quick magnitude comparisons. **Risk:** Switching encodings can reduce immediate comparability if the rest of the report is built around bars. **Mitigation:** Keep the comparison structure the same (same axes and categories) while changing only the mark used to represent the mean.

## Common failure modes that preserve the bias <!-- role: mistakes -->

**Mistake:** Adding error bars to a mean bar and assuming this prevents misinterpretation of where values are likely. **Why it fails:** The within-the-bar bias occurred even when bidirectional error bars were present [@newmanBarGraphsDepicting2012].

## Quick ways to detect the problem in your design <!-- role: check -->

**Failure Sign:** People talk as if values “in the bar” are more likely, or interpret the filled region as where observations reside. **Quick Check:** Ask a reviewer whether values equally far above and below the mean should be equally plausible; if they hesitate or favor the “inside the bar” side, the design is at risk. **Stronger Test:** Run a small between-subjects check where different people judge the plausibility of symmetric test values (one falling within the bar region, one outside); look for a systematic within-bar preference.

## What to do instead of a mean bar <!-- role: fix -->

- Depict the mean with a point-like mark positioned on the value axis rather than as the end of a filled bar.
- Show the distribution directly (or a representation of it) when the user task involves likelihood of particular values.
- If a bar must be used for layout consistency, remove the filled “container” implication by avoiding a single-origin bar whose interior can be read as a region of likely values.
- Add explicit text that the bar represents only the mean and does not indicate where individual observations are more likely to fall.
