---
id: connected-scatterplot-use-to-increase-initial-attention-in-thumbnail-views
title: Use connected scatterplots to attract initial attention in multi-chart thumbnail
  selection
bibliography: references.bib
description: When users choose what to view, connected scatterplots can be prioritized
  in early viewing compared to dual-axis line charts.
labels:
- chart:scatter
- task:select
- visual:shape
- impact:engagement
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Use connected scatterplots when you need a viewer to choose your chart first from a set <!-- role: advice -->

When presenting a mix of chart thumbnails where users can choose what to open, include connected scatterplots for paired time series to increase the chance of early inspection. Ensure the connected scatterplot thumbnail preserves the overall path shape.

## Novel, unusual shapes can bias initial inspection choices <!-- role: reason -->

In browsing scenarios, attention is allocated before comprehension, and visually distinctive forms can be preferentially selected for closer inspection. Connected scatterplots create unusual shapes (such as loops and sharp turns) that can stand out compared to more conventional dual-axis line charts.

**Mechanism:** Visual novelty and distinctive global shape increase salience during rapid selection, leading to earlier viewing.

**Evidence:** In a preferential viewing study with six thumbnails (three connected scatterplots and three dual-axis line charts), viewers spent a larger share of early viewing time on connected scatterplots (about 57% in the first half) and prioritized viewing them despite reporting higher difficulty for connected scatterplots [@harozConnectedScatterplotPresenting2016].

**Notes:** Total viewing time across formats did not differ reliably; the effect was about prioritization rather than sustained time.

## Situations where attention capture is the main objective <!-- role: context -->

- **User Goal:** Decide which visualization to open or read first.
- **Task:** Visual selection under time pressure or casual browsing.
- **Data:** Paired time series that can be shown as either connected scatterplots or dual-axis line charts.
- **Chart Setting:** Dashboards, news aggregators, article link previews, or filmstrip thumbnail selectors.
- **Audience:** Naive viewers who have not been taught the connected scatterplot convention.
- **Success Criterion:** Higher rate of first-clicks or earlier opens for the intended chart.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The audience must immediately and accurately extract correlation language or simple “together vs opposite” relationships without extra effort. **Why:** Connected scatterplots may not cue correlational interpretations as strongly as dual-axis line charts [@harozConnectedScatterplotPresenting2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some viewers may find connected scatterplots harder to understand on first encounter. **Risk:** Increased attention can come from confusion rather than comprehension, which can harm trust if the chart is not well-supported with cues. **Mitigation:** Pair attention-grabbing forms with clear labels and direction cues.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming attention capture implies comprehension. **Why it fails:** Viewers reported that the most difficult chart was always a connected scatterplot, especially “loopy” ones [@harozConnectedScatterplotPresenting2016].

## Quick tests for attention vs comprehension balance <!-- role: check -->

**Failure Sign:** Users click the chart quickly but abandon it or express confusion immediately. **Quick Check:** Run a hallway test where users pick which thumbnail to open and then explain what it shows. **Stronger Test:** Measure first-click rate and error rates for basic interpretation questions.

## What to do instead <!-- role: fix -->

- Use a dual-axis line chart when immediate interpretability is more important than initial selection.
- Provide a short on-chart cue about how to read the connected scatterplot when opened (for example, start/end labeling).
- If loops are the attention driver but also the confusion source, annotate only the key loop and simplify or segment the rest.
