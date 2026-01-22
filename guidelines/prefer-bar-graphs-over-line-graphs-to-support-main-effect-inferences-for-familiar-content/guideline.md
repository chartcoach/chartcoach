---
id: prefer-bar-graphs-over-line-graphs-to-support-main-effect-inferences-for-familiar-content
title: Prefer bar graphs over line graphs to support main-effect inferences (especially
  for familiar content)
bibliography: references.bib
description: Bar graphs increase spontaneous main-effect inference reporting compared
  to line graphs when viewers have familiar expectations.
labels:
- chart:bar
- chart:line
- task:infer
- task:summarize
- impact:comprehension
- data:multivariate
- audience:expert
- audience:novice
- complexity:medium
---

## Use bar graphs to encourage main-effect takeaways when content is familiar <!-- role: advice -->

Use bar graphs rather than line graphs when you want viewers to spontaneously report main effects (averaged relationships that ignore the third variable), particularly when the topic is familiar enough that viewers have expectations about the outcome.

## Why bar-grouping helps viewers compute and report aggregates <!-- role: reason -->

Main effects in multivariate displays often require mentally averaging or otherwise collapsing across one variable; formats that visually group relevant comparisons can reduce the cognitive work needed to form those summaries and make them more likely to be reported.

**Mechanism:** Bar graphs support chunking and comparison by grouped bars, which can reduce working-memory demands for mentally collapsing across the third variable during open-ended interpretation.

**Evidence:** Viewers were more likely to make main-effect inferences with bar graphs than with line graphs, but this advantage appeared for familiar content rather than unfamiliar content [@shahBarLineGraph2011]. Overall, viewers generated far more main-effect inferences for familiar than unfamiliar graphs, indicating that expectations interact with whether main effects are reported at all [@shahBarLineGraph2011].

**Notes:** The findings are about spontaneous description of “most important information,” not forced-choice accuracy.

## When this applies: communicating averaged effects in multivariate results <!-- role: context -->

- **User Goal:** Walk away with the averaged difference across x or across z (a main effect) rather than a detailed interaction narrative.
- **Task:** Open-ended summary or executive interpretation of a three-variable graph.
- **Data:** Medium-complexity multivariate data (e.g., 3×3) where main effects require collapsing across the third variable.
- **Chart Setting:** Static report or slide where you cannot rely on interactive filtering to show collapsed views.
- **Audience:** Readers likely to have prior expectations because variable names/content are familiar.
- **Success Criterion:** Readers mention the intended main effect unprompted in short summaries.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary communication goal is an interaction pattern rather than an averaged effect. **Why:** Bar graphs reduce the dominance of x–y interaction descriptions compared to line graphs, which may weaken interaction-first messaging [@shahBarLineGraph2011].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce salience of trend/interaction patterns that line graphs make visually prominent. **Risk:** Readers may focus on discrete category differences and under-attend to continuous change across x. **Mitigation:** Align the format choice with the single most important takeaway you want in open-ended reading.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Expecting a line graph of three-variable data to naturally produce main-effect summaries in open-ended reading. **Why it fails:** Viewers more often describe interaction patterns in line graphs and are less likely to report main effects than with bar graphs, especially when content is familiar [@shahBarLineGraph2011].

## Quick tests <!-- role: check -->

**Failure Sign:** Reader summaries describe interactions or line separations but omit the averaged relationship you intended. **Quick Check:** Ask readers for a 2–4 sentence “main point” and check whether a main effect is mentioned. **Stronger Test:** Compare bar vs line variants in a small pilot and code main-effect inference frequency using the paper’s main-effect categories (x–y main effect or z–y main effect) [@shahBarLineGraph2011].

## What to do instead <!-- role: fix -->

- Use a line graph if interaction/trend descriptions are the intended primary message.
- Provide an explicit written main-effect statement adjacent to the chart when you must use a line graph.
- Split the display so the main effect is shown in a separate view that already collapses across the third variable.
