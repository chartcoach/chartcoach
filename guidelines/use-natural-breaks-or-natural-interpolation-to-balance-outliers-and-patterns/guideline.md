---
id: use-natural-breaks-or-natural-interpolation-to-balance-outliers-and-patterns
title: Use natural interpolation to reflect clustering while keeping outliers visibly
  rare
bibliography: references.bib
description: Choose natural breaks (Jenks) for classed scales or natural interpolation
  for continuous scales when data clusters heavily but you still want outliers to
  stand out.
labels:
- chart:map-choropleth
- task:reveal-patterns
- visual:color
- impact:balance
- data:quantitative
- audience:general
- complexity:advanced
---

## Use natural interpolation when you need both pattern visibility and outlier honesty <!-- role: advice -->

Use natural breaks (Jenks) for classed color scales or natural interpolation for continuous scales when values cluster in some ranges and have sparse outliers in others. Prefer it when quantiles make outliers look too common and linear makes typical regions look too similar.

## Cluster-aware grouping allocates colors where values are dense <!-- role: reason -->

Natural methods form groups so values within a group are as close as possible, producing narrower bands where data is dense and wider bands where data is sparse. This tends to increase differentiation around the bulk of the distribution while still reserving the darkest colors for truly extreme values.

**Mechanism:** By aligning cut points with “gaps” in the value distribution, natural methods emphasize meaningful separations in the data rather than equal numeric distance or equal counts.

**Evidence:** Natural breaks grouped many closely packed county unemployment rates together while placing fewer, far-apart outliers into smaller groups, producing a map that showed regional differences around the middle while keeping the darkest shade limited to clear outliers [@muth_interpolation_2022]. For continuous scales, natural interpolation applies similar distribution-based cuts and then stretches values within those segments, producing a gradient that stays light longer but reaches darker tones earlier than linear/median in dense regions [@muth_interpolation_2022].

**Notes:** Natural methods can yield non-round thresholds, which can reduce legend readability even when the mapping is effective.

## When natural methods are the best match <!-- role: context -->

- **User Goal:** See geographic patterns among typical regions without pretending outliers are common.
- **Task:** Compare areas in a way that respects clustering and highlights meaningful separations.
- **Data:** Skewed distribution with dense clusters and sparse extremes.
- **Chart Setting:** Choropleth maps using either stepped (classed) colors or continuous gradients.
- **Audience:** Readers who need both an interpretable legend and a fair sense of rarity/extremeness.
- **Success Criterion:** Patterns among the majority are visible, and only a few regions take the most extreme colors when outliers are truly rare.

## When not to use natural methods <!-- role: exceptions -->

**Break it when:** You need thresholds that are simple, round, and easy to communicate without explanation. **Why:** Natural methods often produce cut points like 4.1 or 5.7 that can be harder to read and remember [@muth_interpolation_2022].

## Tradeoffs of natural interpolation <!-- role: costs -->

**Sacrifice:** Legend thresholds may be less “nice” and can feel arbitrary to some readers. **Risk:** Without clear legend presentation, readers may not understand why the cut points fall where they do. **Mitigation:** If you keep the natural grouping, adjust thresholds to more readable values while checking that the map’s overall message stays the same [@muth_interpolation_2022].

## Mistakes to avoid with natural methods <!-- role: mistakes -->

**Mistake:** Using natural breaks but leaving awkward legend thresholds unedited when readability is crucial. **Why it fails:** The map may be interpretable but the legend becomes a barrier to understanding [@muth_interpolation_2022].

## Quick checks for natural interpolation quality <!-- role: check -->

**Failure Sign:** The legend thresholds look overly precise and distract from interpretation, or the darkest colors spread too widely despite clear outliers. **Quick Check:** Verify that only a small number of regions receive the darkest shade when your histogram shows only a few extreme values. **Stronger Test:** Round cut points (slightly) and confirm that the geographic impression changes only minimally [@muth_interpolation_2022].

## What to do instead if natural is hard to read <!-- role: fix -->

- Use a custom classed interpolation that rounds natural-break thresholds to simpler numbers while preserving the same general grouping [@muth_interpolation_2022].
- Use quantiles if your primary goal is equal representation of colors and relative ranking rather than highlighting rarity [@muth_interpolation_2022].
- Use linear interpolation if communicating absolute numeric distance is more important than showing within-cluster variation [@muth_interpolation_2022].
- Add brief legend/annotation support that helps readers interpret why bands differ in width and what the thresholds mean [@muth_interpolation_2022].
