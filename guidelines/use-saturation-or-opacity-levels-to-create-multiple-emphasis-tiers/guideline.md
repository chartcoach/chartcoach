---
id: use-saturation-or-opacity-levels-to-create-multiple-emphasis-tiers
title: Use saturation and darkness to create clear tiers of importance
bibliography: references.bib
description: Create multiple levels of attention by varying saturation and lightness
  so readers see the most important elements first.
labels:
- chart:general
- task:prioritize
- visual:color
- impact:focus
- data:general
- audience:general
- complexity:intermediate
---

## Build an attention ladder using saturation and lightness differences <!-- role: advice -->

Use more saturated and darker colors for higher-priority elements, and less saturated or lighter colors for lower-priority ones to create multiple tiers of emphasis. Ensure each tier is visibly distinct so readers can tell “most important,” “next,” and “background” at a glance.

## Saturation and contrast govern what the eye lands on first <!-- role: reason -->

When several colored elements compete, readers tend to attend to the strongest contrast and most saturated marks first, and then move to less saturated or gray marks.

**Mechanism:** Increasing saturation and (on light backgrounds) darkness increases contrast against the background and surrounding elements, making those marks more attention-grabbing.

**Evidence:** A hierarchy can be created where the most saturated/dark colors receive attention first, followed by lighter/less saturated colors, and then by grays; highly saturated colors can attract attention even when they are lighter than dark neutrals [@muth_emphasize_color_2023].

**Notes:** Darkest does not always win if another element uses a much more saturated color, so treat saturation as a primary lever for attention, not only lightness [@muth_emphasize_color_2023].

## When tiered emphasis is the right tool <!-- role: context -->

- **User Goal:** Know what to read first without losing the ability to read secondary patterns.
- **Task:** Scan, then compare: primary first, secondary next, background last.
- **Data:** Multiple categories/series with more than one “important” group.
- **Chart Setting:** Static charts where you cannot rely on hover/selection to guide attention.
- **Audience:** Readers who may not spend long but should still take away the main ranking of importance.
- **Success Criterion:** Most readers look at the same primary element first and can still access secondary elements afterward.

## When not to use multiple tiers <!-- role: exceptions -->

**Break it when:** You cannot defend a meaningful priority order among categories. **Why:** Artificial tiers can bias interpretation toward an editorial ranking that the data or purpose does not support [@muth_emphasize_color_2023].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Some even-handedness; the design becomes more editorial. **Risk:** Over-tiering can make mid-tier elements feel like background noise. **Mitigation:** Keep the number of tiers small and make tier boundaries visually unambiguous [@muth_emphasize_color_2023].

## Common mistakes <!-- role: mistakes -->

**Mistake:** Using many different hues without controlling saturation/lightness to indicate priority. **Why it fails:** All categories appear equally loud, weakening the intended hierarchy [@muth_emphasize_color_2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers cannot tell which category is intended to be most important without reading the caption carefully. **Quick Check:** Convert the chart to grayscale; if the priority order becomes unclear, your emphasis relies on hue differences rather than tiered salience. **Stronger Test:** Ask readers to rank what seems most important based on the chart alone; compare their ranking to your intended tiers [@muth_emphasize_color_2023].

## What to do instead <!-- role: fix -->

- Reduce the number of emphasis tiers by merging mid-priority groups into one visual level.
- Use direct labeling and line/mark thickness in addition to color when tiers are hard to perceive.
- Gray out true background elements and reserve color variation only for the top tiers.
- Rewrite the chart framing (title/annotation) so fewer elements need to compete for top attention [@muth_emphasize_color_2023].
