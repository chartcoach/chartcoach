---
id: use-color-in-small-multiple-line-charts-to-encode-meaning-not-identity
title: Use color in small multiple line charts to encode groups or highlights, not
  line identity
bibliography: references.bib
description: Because panels and titles identify lines, reserve color for categorization
  or emphasis.
labels:
- chart:line
- task:highlight
- visual:color
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Use color in small multiple line charts to encode groups or highlights, not line identity <!-- role: advice -->

Use color in small multiple line charts to communicate grouping or emphasis rather than to help readers tell lines apart. Rely on the panel separation and panel titles for identity, and apply color only when it makes a point.

## Small multiples remove the need for a legend-driven color key <!-- role: reason -->

In a standard multi-line chart, color is often required just to distinguish series and connect them to a legend. In small multiples, each line already has its own panel and title, freeing color to carry meaning like grouping by trend direction or highlighting selected categories.

**Mechanism:** When identity is provided by layout and labeling, color can be reassigned from “lookup” to “signal,” increasing interpretability.

**Evidence:** In small multiple line charts, different colors are not necessary to distinguish lines because each line has its own panel and panel title; color can instead be used to categorize lines or highlight certain panels [@muth_small_multiple_line_charts_2024].

**Notes:** This is especially useful when you want readers to see clusters like upward vs. downward trends.

## When panel structure already identifies series <!-- role: context -->

- **User Goal:** Notice groups, patterns, or highlighted categories quickly.
- **Task:** Categorize panels (e.g., up vs. down trends) or draw attention to selected panels.
- **Data:** Multiple categories with one time series per panel.
- **Chart Setting:** Small multiples with clear panel titles; legend is unnecessary or undesirable.
- **Audience:** Readers scanning quickly, including those who may struggle with legend lookups.
- **Success Criterion:** Color encodes a message (grouping/emphasis) rather than being decorative.

## When identity color is still necessary <!-- role: exceptions -->

**Break it when:** Panel titles are missing or insufficient to identify each series. **Why:** Without reliable labeling, readers may need color cues to keep track of what they’re looking at [@muth_small_multiple_line_charts_2024].

## Tradeoffs of using color for meaning <!-- role: costs -->

**Sacrifice:** You may have fewer distinct colors available for other encodings. **Risk:** If the meaning of colors is not clear, readers may search for a legend or misinterpret emphasis. **Mitigation:** Apply color sparingly and consistently so the intention is obvious [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assigning a different bright color to every panel by default. **Why it fails:** Color stops carrying meaning and can make the set feel noisy without adding clarity [@muth_small_multiple_line_charts_2024].
- **Mistake:** Using color both for identity and for emphasis at the same time. **Why it fails:** Readers can’t tell whether color differences mean different categories or special importance [@muth_small_multiple_line_charts_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers ask what the colors mean or look for a legend even though each panel is titled. **Quick Check:** Turn all lines gray; if the chart still works, reintroduce color only where it adds a specific message. **Stronger Test:** Ask a reader what the colored panels have in common; if they can’t answer, color isn’t encoding meaning [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Use a single neutral line color when color does not encode a message.
- Apply one highlight color to draw attention to selected panels or categories.
- Use a small set of colors to group panels by trend direction or another meaningful grouping.
- If identity is unclear, improve panel titles rather than relying on many distinct colors [@muth_small_multiple_line_charts_2024].
