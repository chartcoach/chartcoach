---
id: use-chart-height-at-least-80px-for-0-100-value-comparisons
title: "Use chart height of at least 80 px for accurate comparisons on a 0\u2013100\
  \ scale"
bibliography: references.bib
description: "Charts 40 px tall produced significantly higher error; accuracy plateaued\
  \ at and above 80 px for a 0\u2013100 range."
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- custom:responsive-design
---

## Make charts at least 80 pixels tall when viewers must compare values on a 0–100 scale <!-- role: advice -->

For value comparisons on a 0–100 axis, avoid chart heights as small as 40 pixels and target 80 pixels or more. Expect limited accuracy gains from increasing height beyond 80 pixels for that scale.

## Why very small heights increase error while larger heights plateau <!-- role: reason -->

When vertical resolution is too low relative to the data scale, small pixel differences represent large numeric differences, making positional decoding noisy; once pixel and data resolutions roughly align, additional height yields diminishing returns.

**Mechanism:** Increased pixel resolution improves discriminability of vertical differences up to a saturation point.

**Evidence:** In crowdsourced comparison tasks, 40-pixel-tall charts produced significantly more error than taller charts, while no significant accuracy differences were found among 80, 160, and 320 pixels for a 0–100 range, indicating a plateau beyond ~80 pixels [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** This result was observed across both bar and line chart conditions in the tested design.

## When this applies <!-- role: context -->

- **User Goal:** Compare two marked values and estimate their numeric difference.
- **Task:** Quantitative difference judgment from a plotted scale.
- **Data:** Values mapped to a 0–100 (or similarly bounded) vertical range.
- **Chart Setting:** Web or screen-based charts where height is a design choice.
- **Audience:** General audiences on heterogeneous displays.
- **Success Criterion:** Lower absolute error in value difference estimates.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is purely for showing a qualitative pattern and exact comparisons are not needed. **Why:** The measured benefit is specifically about comparison accuracy.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Taller charts consume more vertical space and can reduce information density. **Risk:** Applying an 80-pixel minimum to every sparkline-like element can bloat layouts unnecessarily. **Mitigation:** Reserve the minimum height for charts used for value comparisons, not for decorative summaries.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Compressing charts to ~40 pixels tall while still asking users to estimate differences. **Why it fails:** Error rises significantly at that height for the tested 0–100 scale.

## Quick tests <!-- role: check -->

**Failure Sign:** Users struggle to distinguish nearby values or give widely varying difference estimates. **Quick Check:** Shrink the chart to 40 pixels and note whether the comparison becomes noticeably harder; if so, restore height. **Stronger Test:** Collect a small sample of difference estimates at 40 vs 80 pixels and compare absolute error.

## What to do instead <!-- role: fix -->

- Reduce the numeric range (rescale) if a small height is unavoidable.
- Add direct labels for the compared values or their difference.
- Use interaction to reveal exact values on demand.
- Split the chart into small multiples with adequate height per panel rather than squeezing one panel too small.
