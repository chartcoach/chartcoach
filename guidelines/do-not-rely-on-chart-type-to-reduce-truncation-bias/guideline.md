---
id: do-not-rely-on-chart-type-to-reduce-truncation-bias
title: Do not rely on switching between bar and line charts to reduce y-axis truncation
  bias
bibliography: references.bib
description: Bar and line charts showed similar increases in perceived severity under
  y-axis truncation.
labels:
- chart:bar
- chart:line
- task:judge
- visual:scale
- impact:clarity
- data:quantitative
- audience:novice
- complexity:beginner
---

## Chart type does not neutralize truncation inflation <!-- role: advice -->

If you truncate the y-axis, assume that both bar and line charts will inflate perceived effect size in similar ways. Choose bar versus line for other reasons than “avoiding truncation bias.”

## Why changing chart type doesn’t remove the bias <!-- role: reason -->

The perceptual driver is the displayed y-range relative to the data range; both bars (height) and lines (slope/position) become more visually extreme when the y-range is narrowed.

**Mechanism:** Truncation increases the apparent visual change, and viewers map that stronger visual change to higher subjective severity regardless of whether the marks are rectangles or a connected line.

**Evidence:** In a within-subject experiment varying truncation level, perceived severity increased with truncation, while visualization type (bar vs line) had no significant effect and showed similar response patterns across truncation levels [@correllTruncatingYAxisThreat2020a].

**Notes:** Small framing differences from asking “trend” versus “values” questions were minor compared to the truncation effect.

## When this matters <!-- role: context -->

- **User Goal:** Communicate how big a difference/trend is.
- **Task:** Qualitative judgment of severity/importance or “how quickly values are changing.”
- **Data:** A small set of points (2–3) with modest changes.
- **Chart Setting:** Static reports, dashboards, or media graphics where chart type may be swapped late in production.
- **Audience:** Mixed audiences, including viewers who may not compute differences numerically.
- **Success Criterion:** Choice of bar vs line should not be used as a substitute for managing the impact of axis scale.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You are changing chart type for reasons unrelated to truncation (e.g., emphasizing continuity vs discreteness) and you will keep the same y-axis range across versions. **Why:** The guidance is specifically about not expecting chart type to fix truncation-driven severity inflation [@correllTruncatingYAxisThreat2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose a convenient “rule of thumb” that line charts are inherently safer with non-zero baselines. **Risk:** You may mistakenly approve a truncated line chart thinking it is perceptually neutral compared to a truncated bar chart [@correllTruncatingYAxisThreat2020a]. **Mitigation:** Evaluate truncation effects directly (e.g., via alternative y-axis starts) instead of using chart-type heuristics.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Replacing a truncated bar chart with a truncated line chart to “make it honest.” **Why it fails:** Perceived severity inflation persisted similarly for line charts under truncation [@correllTruncatingYAxisThreat2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** Stakeholders argue about honesty based on chart type while the y-axis range remains truncated. **Quick Check:** Hold the y-axis start/range constant and swap bar ↔ line; if the severity impression remains similar, chart type is not the controlling factor. **Stronger Test:** Re-run the same chart type with different y-axis starts and compare the magnitude of judgment shifts; truncation should dominate [@correllTruncatingYAxisThreat2020a].

## What to do instead <!-- role: fix -->

- Decide bar versus line based on intended data metaphor and task (values versus continuity), not as a truncation safeguard.
- Manage perceived effect size by explicitly choosing and reviewing the y-axis start/range, regardless of chart type.
- If chart type must change, keep y-axis range consistent across versions to avoid introducing an unintentional severity shift.
- Document the intended interpretation of magnitude so reviewers focus on scale choices rather than chart-type folklore [@correllTruncatingYAxisThreat2020a].
