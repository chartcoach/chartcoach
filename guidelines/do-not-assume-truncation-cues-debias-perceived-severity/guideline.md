---
id: do-not-assume-truncation-cues-debias-perceived-severity
title: Do not assume broken-axis or gradient-continuation cues reduce truncation-driven
  severity inflation
bibliography: references.bib
description: Even explicit visual cues for truncation did not reliably reduce perceived
  severity compared to standard truncated bars.
labels:
- chart:bar
- task:judge
- visual:annotation
- visual:scale
- impact:trust
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Truncation cues do not reliably reduce perceived severity <!-- role: advice -->

When you must truncate a bar chart’s y-axis, do not expect a broken-axis mark or a gradient/continuation treatment to reduce perceived effect size. Treat these cues as disclosure, not as debiasing.

## Why disclosure cues don’t remove the perceptual effect <!-- role: reason -->

Viewers’ severity judgments are driven by the magnified visual differences created by a narrowed y-range, and that visual impression can persist even when the truncation is made explicit.

**Mechanism:** Attention to a truncation indicator does not necessarily override the fast, visual inference of magnitude from bar height differences within the displayed range.

**Evidence:** In experiments comparing standard truncated bars to broken-axis bars and gradient/continuation bars, perceived severity did not significantly differ among these designs for truncated conditions, while truncation level still increased perceived severity [@correllTruncatingYAxisThreat2020a].

**Notes:** Making truncation “obvious” did not function as a reliable corrective for subjective judgments.

## When this matters <!-- role: context -->

- **User Goal:** Interpret how big a difference is, not merely detect that truncation occurred.
- **Task:** Rate severity/importance of change from the chart’s visual impression.
- **Data:** Values with modest differences where truncation is tempting to improve visibility.
- **Chart Setting:** Static bar charts where designers add break marks or gradients to signal non-zero baselines.
- **Audience:** Viewers who may notice truncation yet still be influenced by the amplified visual slope/height differences.
- **Success Criterion:** The chart should not unintentionally overstate (or understate) the subjective magnitude of change.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your only requirement is to disclose that truncation occurred, not to control severity judgments. **Why:** Cues can support transparency even if they do not reduce severity inflation [@correllTruncatingYAxisThreat2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional visual complexity may be added without improving judgment calibration. **Risk:** Designers may feel “protected” from misleading effects after adding a break cue, even though subjective severity remains inflated [@correllTruncatingYAxisThreat2020a]. **Mitigation:** Separate disclosure goals (“signal truncation”) from judgment goals (“avoid exaggeration”) in review criteria.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Adding a broken-axis symbol and assuming the exaggeration problem is solved. **Why it fails:** Perceived severity remained similar to standard truncated bar charts in the tested designs [@correllTruncatingYAxisThreat2020a].
- **Mistake:** Using a gradient/continuation fill to imply omitted range and assuming it will dampen severity judgments. **Why it fails:** The tested gradient design did not reliably reduce perceived severity relative to standard truncated bars [@correllTruncatingYAxisThreat2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Reviewers accept a truncated chart because “it has a break/gradient, so it’s fine,” while the takeaway remains dramatically stronger than a less-truncated view. **Quick Check:** Compare perceived-severity judgments (informally, with a few readers) between the truncated chart with cues and a less-truncated version; if the cue version still reads as much more severe, the cue is not debiasing. **Stronger Test:** Pilot-test severity ratings across designs with the same data and truncation level to confirm cues do not materially change subjective magnitude [@correllTruncatingYAxisThreat2020a].

## What to do instead <!-- role: fix -->

- Use truncation cues primarily as transparency features, and separately manage the y-axis range to control severity inflation.
- Provide an alternate view with a broader y-axis range when the magnitude interpretation is consequential.
- Reconsider whether truncation is necessary by checking whether the message depends on the inflated severity impression.
- If truncation is kept, explicitly align the chosen y-axis range with the intended “meaningful effect size” you want viewers to perceive [@correllTruncatingYAxisThreat2020a].
