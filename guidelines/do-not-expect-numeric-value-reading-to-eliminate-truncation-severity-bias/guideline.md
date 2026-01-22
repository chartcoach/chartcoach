---
id: do-not-expect-numeric-value-reading-to-eliminate-truncation-severity-bias
title: Do not expect prompting numeric value reading to eliminate truncation-driven
  severity bias
bibliography: references.bib
description: Even when viewers estimate values, truncated axes still increase perceived
  severity.
labels:
- chart:bar
- task:estimate
- task:judge
- visual:scale
- impact:trust
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Numeric attention does not cancel subjective severity inflation <!-- role: advice -->

Do not assume that making viewers read or estimate exact values will remove the perceived-severity inflation caused by truncating the y-axis. Treat subjective severity as a visual judgment that can persist alongside correct numeric understanding.

## Why numeric tasks don’t fully override visual impression <!-- role: reason -->

People can attend to numeric labels and still experience the truncated display as showing a larger “visual effect,” so their qualitative severity ratings remain higher even when they can estimate the underlying trend reasonably well.

**Mechanism:** The visual amplification from truncation influences the intuitive sense of magnitude, which can operate independently from deliberate numeric decoding.

**Evidence:** When participants were required to estimate the first and last values numerically before rating severity, perceived severity still differed significantly across truncation levels, replicating the earlier inflation pattern [@correllTruncatingYAxisThreat2020a]. Trend (slope) estimation error did not significantly differ across truncation levels, indicating the severity shift is not explained solely by misreading the direction or size of change [@correllTruncatingYAxisThreat2020a].

**Notes:** Individual value estimation error increased in the 25% axis-start condition, suggesting some truncated scales can make value decoding harder even when severity inflation persists.

## When this matters <!-- role: context -->

- **User Goal:** Use a chart to judge whether a change is “big” or “small.”
- **Task:** Provide qualitative ratings of severity after (or alongside) numeric readout/estimation.
- **Data:** Percentage-like values (0–100%) where truncation levels such as 25% and 50% are plausible.
- **Chart Setting:** Interfaces that add tooltips, value labels, or quiz-like prompts to force attention to numbers.
- **Audience:** Viewers capable of reading axes but still susceptible to visual magnitude cues.
- **Success Criterion:** Avoid a situation where the chart’s “feel” overpowers the intended interpretation of magnitude.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary outcome is improving numeric read accuracy rather than calibrating qualitative severity. **Why:** Numeric prompting can still be valuable for reading values even if it does not remove the severity bias [@correllTruncatingYAxisThreat2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Added prompts, labels, or interaction steps can slow viewing without fixing the qualitative bias. **Risk:** Designers may falsely conclude the chart is “safe” because users can report numbers, while severity impressions remain inflated [@correllTruncatingYAxisThreat2020a]. **Mitigation:** Evaluate both numeric accuracy and qualitative takeaways separately during validation.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding data labels/tooltips and assuming truncation is no longer perceptually consequential. **Why it fails:** Severity ratings still increased with truncation even after numeric estimation tasks [@correllTruncatingYAxisThreat2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Users can state the values but still describe the change as much more dramatic in the truncated version than in a broader-scale version. **Quick Check:** Ask a few viewers for both (a) the numeric difference and (b) a severity rating across two y-axis starts; divergence indicates a persistent visual bias. **Stronger Test:** In a small study, require numeric estimation first and test whether severity ratings still vary with truncation; if they do, numeric prompting is not a debiasing strategy [@correllTruncatingYAxisThreat2020a].

## What to do instead <!-- role: fix -->

- Validate truncation choices using qualitative outcome measures (severity/importance judgments), not only numeric read accuracy.
- Provide a broader-scale alternative view when qualitative interpretation of magnitude is important.
- Choose y-axis range based on the magnitude you intend viewers to perceive as meaningful, rather than assuming numeric labels will calibrate perception.
- Avoid truncated starts that also make value decoding harder (e.g., starts that create awkward midpoints), especially when exact values matter [@correllTruncatingYAxisThreat2020a].
