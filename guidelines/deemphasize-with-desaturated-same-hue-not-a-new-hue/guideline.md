---
id: deemphasize-with-desaturated-same-hue-not-a-new-hue
title: De-emphasize with gray or a less saturated version of the same hue (not a new
  hue)
bibliography: references.bib
description: Use saturation changes to signal importance without implying a different
  category through hue changes.
labels:
- chart:general
- task:highlight
- visual:color
- impact:clarity
- data:categorical
- audience:general
- complexity:intermediate
---

## Keep hue constant when muting; change saturation instead <!-- role: advice -->

When you need to show multiple items as related but less important, keep them in the same hue as the emphasized item and reduce saturation (or use gray) to push them back. Do not introduce a different hue to indicate “less important.”

## Hue implies category boundaries, while saturation implies emphasis <!-- role: reason -->

A hue change is commonly read as a categorical distinction, so using a second hue for deemphasis can accidentally create a new group in the reader’s mind.

**Mechanism:** Hue differences are interpreted as “different kinds,” while saturation differences are interpreted as “more vs. less prominent” within the same kind.

**Evidence:** Using a different hue for unlabeled or secondary items can wrongly signal a categorical difference; using the same hue with reduced saturation better communicates that items belong together but are less emphasized [@muth_emphasize_color_2023].

**Notes:** The safe default for deemphasis is gray or desaturation because it reduces salience without introducing new categorical meaning [@muth_emphasize_color_2023].

## When constant-hue deemphasis applies <!-- role: context -->

- **User Goal:** Understand which items are primary while still seeing related context items as part of the same group.
- **Task:** Highlight a subset without creating an unintended new category.
- **Data:** Categorical or multi-series data where several series are conceptually the same kind.
- **Chart Setting:** Charts where color is the main grouping cue (legends, multi-series lines, scatter groups).
- **Audience:** Readers who rely on color to infer grouping at a glance.
- **Success Criterion:** Deemphasized items are clearly “the same kind, just less important.”

## When not to follow it <!-- role: exceptions -->

**Break it when:** You truly need to communicate a separate category (not just lower importance). **Why:** A new hue is a legitimate signal for categorical difference and should be reserved for that meaning [@muth_emphasize_color_2023].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** With many series, same-hue variations can be harder to distinguish from each other. **Risk:** If labels are sparse, readers may not be able to tell deemphasized series apart. **Mitigation:** Use direct labels or reduce the number of simultaneously shown series [@muth_emphasize_color_2023].

## Common mistakes <!-- role: mistakes -->

**Mistake:** Making secondary items a different hue (for example bright blue vs dark blue) to push them back. **Why it fails:** The hue shift suggests a different category instead of lower priority [@muth_emphasize_color_2023].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers describe two “groups” that you did not intend. **Quick Check:** Remove the legend and ask what groups exist; if hue creates unintended grouping, reconsider. **Stronger Test:** Recolor secondary items to a desaturated version of the highlight hue; if the perceived grouping becomes correct, the original hue split was misleading [@muth_emphasize_color_2023].

## What to do instead <!-- role: fix -->

- Recolor secondary items to the same hue as the primary item and reduce saturation.
- Use gray for the entire background group when only one or two items are meant to stand out.
- Add direct labels to the primary items so color can focus on emphasis rather than identification.
- Reduce the number of colored categories shown at once so hue can be reserved for true category differences [@muth_emphasize_color_2023].
