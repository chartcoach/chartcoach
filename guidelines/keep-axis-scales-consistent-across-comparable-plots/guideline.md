---
id: keep-axis-scales-consistent-across-comparable-plots
title: Keep axis scales consistent across comparable plots to avoid false crossings
  and shape distortions
bibliography: references.bib
description: Changing axis ranges across related charts changes perceived shape, creating
  misleading comparisons like artificial trend reversals.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:general
- risk:scale-distortion
---

## Use the same axis ranges when comparing the same variables across plots <!-- role: advice -->

When multiple plots show the same variables for comparison, map axes to the same data ranges across all plots. Do not renormalize each panel to its own min/max if viewers must compare shapes or levels across panels.

## Why inconsistent scales create misleading narratives <!-- role: reason -->

Viewers form an unconscious “gist” of a chart’s shape and relative relationships. If axis ranges change between plots, that gist changes even if the data pattern does not, producing apparent crossings or reversals that are artifacts of scale choices rather than real changes.

**Mechanism:** Shape-based perception is fast and automatic, while scale reading is slower and often skipped; inconsistent scaling therefore changes perceived structure more than it changes explicit numeric interpretation.

**Evidence:** Using different axis ranges for comparable plots can create salient but false features (such as apparent crossings) that reverse the story told by the data once scales are normalized consistently [@szafirGoodBadBiased2018]. Viewers frequently rely on perceived ratios and shapes at a glance rather than carefully reading axis labels, making scale manipulation especially biasing [@szafirGoodBadBiased2018].

**Notes:** The risk is highest when the narrative depends on whether one series overtakes another or whether trends diverge/converge.

## When this applies <!-- role: context -->

- **User Goal:** Compare trends, levels, or dominance across time, groups, or panels.
- **Task:** Detect crossings, compare slopes, judge which series is larger.
- **Data:** Repeated measures or comparable metrics shown in multiple panels or successive views.
- **Chart Setting:** Small multiples, dashboards with tabs, slide sequences.
- **Audience:** Readers scanning quickly or making decisions under time pressure.
- **Success Criterion:** Comparisons across views reflect data differences, not scale choices.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Each panel is explicitly intended to show within-panel variation only and cross-panel magnitude comparison is not a goal. **Why:** A shared scale can hide within-panel variation when ranges differ widely across panels [@szafirGoodBadBiased2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** A shared scale can compress panels with small ranges, reducing visible variation. **Risk:** Viewers may miss local fluctuations in low-variance panels. **Mitigation:** Pair a shared-scale view for cross-panel comparison with a separate view focused on within-panel detail.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Auto-scaling each panel to maximize plot area without indicating the change. **Why it fails:** It changes perceived shape and can create false comparative claims (like overtakes) [@szafirGoodBadBiased2018].

## Quick tests to catch problems <!-- role: check -->

**Failure Sign:** A “crossing” or reversal appears only when switching panels, not when plotting together. **Quick Check:** Confirm identical min/max axis values across comparable plots. **Stronger Test:** Recreate the comparison in a single shared-scale plot and see whether the key story feature persists.

## What to do instead <!-- role: fix -->

- Lock axis ranges across panels that are meant to be compared directly.
- If differing ranges are unavoidable, explicitly encode change-from-baseline rather than raw magnitude.
- Provide a superposed comparison view for a small number of series to validate cross-panel claims.
- Add clear scale indicators and annotations that prevent viewers from inferring comparisons the design cannot support.
