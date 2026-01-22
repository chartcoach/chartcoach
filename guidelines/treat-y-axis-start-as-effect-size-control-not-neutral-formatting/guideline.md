---
id: treat-y-axis-start-as-effect-size-control-not-neutral-formatting
title: Treat y-axis start selection as a control for perceived effect size (not neutral
  formatting)
bibliography: references.bib
description: Changing the y-axis start systematically shifts how severe viewers judge
  the same underlying differences to be.
labels:
- chart:bar
- chart:line
- task:judge
- visual:scale
- impact:trust
- data:quantitative
- audience:novice
- complexity:intermediate
---

## Y-axis start is an effect-size dial <!-- role: advice -->

Choose the y-axis start intentionally because it will change how severe the same differences look. Do not assume that switching chart type or adding obvious truncation cues will neutralize this shift.

## Why y-axis start changes judgments <!-- role: reason -->

Changing the y-axis start changes the visual spread of values (bar heights or line slopes), which alters subjective judgments of how large or important the differences are even when the numbers are the same.

**Mechanism:** Truncation increases the apparent magnitude of change by expanding the displayed range around the data, so viewers experience a stronger visual “effect size” and rate the change as more severe.

**Evidence:** Perceived severity increased monotonically as the y-axis start moved upward (0% → 25% → 50%) in repeated-measures crowd experiments using the same underlying data patterns [@correllTruncatingYAxisThreat2020a]. This inflation held across bar charts and line charts, and persisted even when designs explicitly signaled truncation (broken-axis and gradient/continuation designs) [@correllTruncatingYAxisThreat2020a].

**Notes:** The bias observed is primarily qualitative (how big the change feels), not simply a failure to read values.

## When this matters <!-- role: context -->

- **User Goal:** Judge how severe, meaningful, or important a difference/trend is.
- **Task:** Provide a subjective severity/importance rating of change between endpoints.
- **Data:** Quantitative values with relatively small differences (e.g., 12.5%–25% endpoint change) shown over 2–3 points.
- **Chart Setting:** Static charts where readers rely on the visual impression of magnitude.
- **Audience:** General audiences with mixed graphical literacy, including people who may still be influenced even if they notice truncation.
- **Success Criterion:** Severity judgments should reflect the intended interpretation of magnitude, not an arbitrary axis start.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your communication goal explicitly requires amplifying small but meaningful differences by narrowing the displayed y-range. **Why:** The point of the graphic is to make subtle variation visually salient, and truncation is a direct lever for doing so [@correllTruncatingYAxisThreat2020a].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You give up the convenience of treating axis defaults as a stylistic choice and must justify scale choices per message. **Risk:** Unintentional exaggeration or downplaying can occur because the same data will be judged differently under different y-axis starts [@correllTruncatingYAxisThreat2020a]. **Mitigation:** Make scale choice part of the message definition (what magnitude should look “small” vs “large”) rather than a last-step formatting decision.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming “line charts are safe” while only bar charts are distorted by truncation. **Why it fails:** Severity inflation from truncation was not meaningfully different between bar and line charts in the experiments [@correllTruncatingYAxisThreat2020a].
- **Mistake:** Assuming an obvious truncation cue (e.g., broken axis) eliminates the perceptual inflation. **Why it fails:** Designs that clearly indicated truncation did not reliably reduce perceived severity relative to standard truncated bars [@correllTruncatingYAxisThreat2020a].

## Quick tests <!-- role: check -->

**Failure Sign:** The same dataset appears “barely changing” in one version and “dramatically changing” in another solely due to y-axis start. **Quick Check:** Re-render the chart with at least two y-axis starts (including a less-truncated baseline) and see whether the qualitative takeaway about severity flips. **Stronger Test:** Ask a small sample of viewers to rate severity across the alternate axis starts; large shifts indicate the y-axis is acting as an effect-size control [@correllTruncatingYAxisThreat2020a].

## What to do instead <!-- role: fix -->

- Render and compare at least two candidate y-axis starts during design review to quantify how much the intended message depends on truncation.
- Align the chosen y-axis range to the magnitude of effects you intend to communicate as “meaningful” versus “minor,” rather than defaulting to 0 or defaulting to tight bounds.
- If severity inflation is undesirable, broaden the y-axis range until subjective severity no longer depends strongly on small changes in y-axis start.
- If severity amplification is desirable, explicitly document that intent so viewers and reviewers understand the rhetorical choice is intentional rather than accidental [@correllTruncatingYAxisThreat2020a].
