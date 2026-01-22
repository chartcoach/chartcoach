---
id: start-bar-chart-y-axes-at-zero-to-preserve-length-judgments
title: Start bar-chart y-axes at zero to avoid exaggerating differences
bibliography: references.bib
description: Bar heights are read as lengths from the baseline, so non-zero y-axes
  visually inflate small differences.
labels:
- chart:bar
- task:compare
- visual:position
- impact:trust
- data:quantitative
- audience:general
- risk:exaggeration
---

## Use a zero baseline for bars so height matches magnitude <!-- role: advice -->

For bar charts, set the quantitative axis baseline to zero so bar length encodes magnitude honestly. Do not truncate the bar baseline to “zoom in” on small differences.

## Why truncated baselines bias bar comparisons <!-- role: reason -->

People interpret bar values by visually measuring the distance from the baseline to the bar end. If the baseline is not zero, the visual ratio between bars no longer matches the data ratio, so small numeric differences can look like large proportional changes even when axis labels are present.

**Mechanism:** Pre-attentive “gist” reading emphasizes shape and relative lengths, while reading axis labels requires deliberate attention that many viewers do not apply.

**Evidence:** Non-zero baselines in common charts cause small differences to appear much larger than they are, and viewers often draw conclusions from the visual ratio rather than from carefully reading axis labels [@szafirGoodBadBiased2018]. Distortion techniques like truncating axes have been empirically associated with deceptive interpretation effects in common settings [@szafirGoodBadBiased2018].

**Notes:** This guideline is specific to bars and other “length from baseline” encodings.

## When this applies <!-- role: context -->

- **User Goal:** Compare magnitudes across categories and judge proportional differences.
- **Task:** Rank, compare, and estimate gaps between groups.
- **Data:** Non-negative quantitative values mapped to bar height/length.
- **Chart Setting:** Static charts in reports, slides, news, or dashboards.
- **Audience:** General audiences who may not read axis labels carefully.
- **Success Criterion:** Visual differences reflect true numeric differences and do not amplify effects.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart type is a line chart where the analytic focus is fine-grained variation rather than absolute magnitude. **Why:** Some argue truncated axes can make small variations easier to see when magnitude is not the question being asked [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Small differences may become harder to see when the full zero-based range is shown. **Risk:** Viewers may miss practically important but numerically small changes. **Mitigation:** Use additional encodings or computed change metrics rather than truncating the baseline.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Truncating the bar axis and assuming axis labels prevent misinterpretation. **Why it fails:** Viewers often rely on the immediate visual ratio, not on careful label reading, so the bias remains [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** Bars look like “twice as big” while the numeric difference is only a few percentage points. **Quick Check:** Verify the quantitative axis includes zero and that the baseline is visible. **Stronger Test:** Ask a viewer to estimate the percent difference from the picture alone; large overestimates indicate baseline distortion.

## What to do instead <!-- role: fix -->

- Keep the bar baseline at zero and show the full scale needed for honest magnitude comparison.
- If the real question is change, compute and plot change relative to a baseline instead of truncating axes.
- Use annotations to call out small but important differences without altering the baseline.
- Switch to a chart that better matches the question (for example, plot growth rate rather than raw totals).
