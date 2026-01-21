---
id: do-not-assume-numeric-reading-prevents-truncation-severity-bias
title: Do Not Assume Numeric Reading Prevents Truncation Severity Bias
bibliography: references.bib
description: Even when viewers estimate values, y-axis truncation still increases
  perceived severity.
labels:
- chart:bar
- task:estimate
- task:judge
- visual:axis
- impact:integrity
- data:quantitative
- audience:general
- source:correll-bertini-franconeri-2020
---

## The Rule <!-- role: advice -->

Do not assume that forcing attention to numeric values (e.g., asking users to read off values) will eliminate the perceived-severity inflation caused by y-axis truncation.

## The Logic <!-- role: reason -->

Perceived severity appears to be a visual judgment that persists even when participants attend to and can report numeric values; value-reading does not cancel the visual magnification from truncation.

- **The Principle:** Qualitative severity judgments are not corrected by numeric decoding.
- **The Evidence:** In Experiment 3, participants first estimated the first/last values, yet perceived severity still differed significantly across truncation levels [@correllTruncatingYAxisThreat2020a].

## Where to Apply <!-- role: context -->

- **User Goal:** Both (a) reading values and (b) judging how important the change is.
- **Data Type:** Bar-chart displays with truncated y-axes.
- **Audience:** Viewers who may be capable of value reading but still rely on visual impression for “how big” [@correllTruncatingYAxisThreat2020a].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your only objective is accurate trend direction or approximate slope, not severity impression.
- **Reason:** Experiment 3 found no significant differences across truncation levels in slope-estimation error (Eslope) [@correllTruncatingYAxisThreat2020a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional tasks/labels can increase effort without removing bias.
- **The Risk:** You may overestimate how much numerical literacy protects viewers from visual framing effects [@correllTruncatingYAxisThreat2020a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more numbers (or prompting value read-off) as the main mitigation for truncation.
- **Why it fails:** Severity inflation remained, indicating the effect is not primarily due to misreading values [@correllTruncatingYAxisThreat2020a].

## How to Check <!-- role: check -->

- **Visual Sign:** People can state the values but still describe the change as “extreme.”
- **The Test:** Collect both a value-readout and a severity rating in review; if severity rises with truncation while numeric accuracy stays similar, truncation is shaping impression [@correllTruncatingYAxisThreat2020a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the axis range to reduce visual magnification (less truncation).
- **Best Fix:** Decide on an axis range that makes the *meaningful* effect-size scale visually apparent, recognizing that numeric attention alone won’t neutralize severity framing [@correllTruncatingYAxisThreat2020a].
