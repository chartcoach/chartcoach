---
id: lower-data-ink-ratio-to-increase-visualization-memorability
title: Allow a lower data-ink ratio when memorability is more important than minimalism
bibliography: references.bib
description: Visualizations with lower data-ink ratios (more non-data ink) were more
  memorable in recognition-based tests.
labels:
- chart:any
- task:recall
- visual:annotation
- impact:memorability
- data:any
- audience:general
- custom:chartjunk
- evidence:experiment
---

## Use more non-data ink when optimizing for memorability <!-- role: advice -->

Allow a lower data-ink ratio by adding non-data visual elements if your priority is making the visualization memorable as an image.

## Why lower data-ink ratio can increase memorability <!-- role: reason -->

Additional non-data elements can create distinctive visual structure that supports recognition and reduces confusability with other visualizations.

**Mechanism:** Extra visual cues provide more features that can be encoded and later matched during recognition, improving sensitivity in repeat detection.

**Evidence:** Visualizations rated as having a “bad” data-ink ratio (more non-data ink) had higher memorability scores than those rated “good,” and intermediate ratings fell between them [@borkinWhatMakesVisualization2013a].

**Notes:** The data-ink ratio ratings were subjective categorical labels used for analysis in the memorability experiment.

## When to apply lower data-ink ratio <!-- role: context -->

- **User Goal:** Remember the visualization later as a visual artifact.
- **Task:** Recognize the visualization in a stream or set of many items.
- **Data:** Any; especially where standard chart forms look similar.
- **Chart Setting:** Static single-panel graphics; brief exposure.
- **Audience:** General audiences; attention competition.
- **Success Criterion:** Higher memorability score (higher hits with lower false alarms).

## When not to lower data-ink ratio <!-- role: exceptions -->

**Break it when:** You are optimizing for comprehension or analytic reading of the data values. **Why:** The experiment measures image memorability and does not show that added non-data ink improves understanding [@borkinWhatMakesVisualization2013a].

## Tradeoffs of lower data-ink ratio <!-- role: costs -->

**Sacrifice:** Minimalism and potentially perceived “cleanliness.”\
**Risk:** The memorable elements may be unrelated to the intended data message.\
**Mitigation:** Keep added non-data elements semantically aligned with the key takeaway.

## Common mistakes with data-ink ratio <!-- role: mistakes -->

- **Mistake:** Treating “chart junk improves memorability” as a blanket endorsement of decoration. **Why it fails:** The study separates memorability from comprehension and does not evaluate whether viewers remember the intended information [@borkinWhatMakesVisualization2013a].
- **Mistake:** Adding non-data ink that makes many charts look stylistically identical (template clutter). **Why it fails:** Similar-looking designs can increase confusion, which is penalized by false alarms in the memorability score [@borkinWhatMakesVisualization2013a].

## Quick checks for data-ink changes <!-- role: check -->

**Failure Sign:** Viewers recall the decorations but cannot identify the visualization’s subject at all.\
**Quick Check:** Remove the added non-data ink and compare whether the visualization becomes harder to recognize at a glance.\
**Stronger Test:** Test recognition (repeat detection) and message recall separately to ensure memorability is not purely decorative.

## What to do instead <!-- role: fix -->

- Add a small number of distinctive elements that directly support the narrative or topic of the data.
- Use a recognizable pictorial element, since pictograms showed a strong memorability effect in the study.
- Increase distinct colors to improve discriminability without relying only on non-data marks.
- Change the visualization type to a more distinctive form if the current chart is easily confusable.
