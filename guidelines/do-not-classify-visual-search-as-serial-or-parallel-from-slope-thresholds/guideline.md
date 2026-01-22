---
id: do-not-classify-visual-search-as-serial-or-parallel-from-slope-thresholds
title: "Avoid classifying visual search as \u201Cserial\u201D or \u201Cparallel\u201D\
  \ from a slope threshold alone"
bibliography: references.bib
description: Search slopes form a unimodal distribution with overlapping task classes,
  so a single cutoff cannot reliably label mechanisms.
labels:
- chart:scatter
- task:classify
- visual:position
- impact:validity
- data:quantitative
- audience:expert
- domain:psychophysics
- metric:rt-set-size-slope
---

## Reject slope-threshold labels for search mechanism <!-- role: advice -->

Do not label a visual search as “parallel” or “serial” just because the reaction time (RT) × set size slope falls below or above a fixed cutoff (such as 10 ms/item). Treat slope as a continuous performance measure rather than a categorical diagnostic.

## Unimodal slopes and overlapping task distributions <!-- role: reason -->

When a metric’s empirical distribution is unimodal and task families overlap heavily on that metric, any attempt to impose a binary partition from a single cutoff will create systematic misclassification. In visual search, slope magnitude varies continuously across many stimulus/task types, so the same slope value can arise from different task classes and cannot uniquely identify an underlying mechanism.

**Mechanism:** A threshold assumes separable clusters (e.g., “parallel” vs. “serial”) in slope space; a unimodal, overlapping distribution means the mapping from slope to process label is many-to-one.

**Evidence:** Across roughly 2,500 sessions (about 1 million trials), the distribution of target-present and target-absent slopes was unimodal, with no bimodality even under finer binning and even when restricting to subsets of task types, undermining data-driven “serial vs. parallel” divisions by slope alone [@wolfeWhatCan11998]. Feature, conjunction, and spatial-configuration tasks had different mean slopes but substantially overlapping slope distributions, so slope values could not uniquely determine task class [@wolfeWhatCan11998].

**Notes:** This does not imply tasks are indistinguishable; it implies slope alone is not a reliable classifier.

## When slope-based classification is being attempted <!-- role: context -->

- **User Goal:** Infer a qualitative search “mode” (e.g., serial vs. parallel) from performance data.
- **Task:** Categorize a search task using RT × set size slope magnitude.
- **Data:** Target-present and/or target-absent RTs across multiple set sizes; slopes computed per condition/session.
- **Chart Setting:** Scatterplots or histograms of slopes; comparisons across task conditions.
- **Audience:** Researchers interpreting visual search outcomes from small-N experiments.
- **Success Criterion:** Avoid false mechanistic conclusions driven by arbitrary cutoffs.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The goal is purely descriptive binning for convenience (not mechanistic inference) and the bins are explicitly presented as arbitrary. **Why:** The harm is specifically in treating a cutoff as evidence about underlying search mechanisms.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose a simple one-number decision rule for labeling tasks. **Risk:** Results may feel less interpretable because you must report gradients and uncertainty rather than a binary label. **Mitigation:** Use multiple complementary diagnostics (e.g., slopes plus other derived measures) to support any categorization.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Declaring “parallel search” because mean slope is “near zero” or below a traditional cutoff (e.g., 10 ms/item). **Why it fails:** The empirical slope distribution is unimodal and task distributions overlap, so “small” slopes are not a unique signature of a distinct mode [@wolfeWhatCan11998].
- **Mistake:** Declaring “serial self-terminating search” because slopes look “linear” and “large.” **Why it fails:** Many tasks populate the same slope range, and additional diagnostics (like target-absent behavior) systematically depart from simple serial predictions [@wolfeWhatCan11998].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Your conclusion depends on a single ms/item cutoff and would flip if the cutoff moved slightly. **Quick Check:** Ask whether tasks from different stimulus families could plausibly yield the same slope value in your dataset. **Stronger Test:** Compare the full slope distributions (not just means) across task categories or conditions to see if they actually separate.

## Fix: What to do instead <!-- role: fix -->

- Quantify and report the full distribution of slopes (e.g., histogram or density) rather than relying on a binary label.
- Compare slope distributions across task classes to show overlap and uncertainty in categorization.
- Treat slope as one dimension of evidence and avoid mapping it directly to “serial/parallel” without additional diagnostics.
- If categorization is required, build it from multiple metrics rather than a single slope cutoff.
