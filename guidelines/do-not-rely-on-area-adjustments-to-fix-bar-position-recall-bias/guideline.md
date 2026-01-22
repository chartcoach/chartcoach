---
id: do-not-rely-on-area-adjustments-to-fix-bar-position-recall-bias
title: Do Not Rely on Area Adjustments to Fix Bar Position Recall Bias
bibliography: references.bib
description: Changing bar area (while holding or changing width) does not remove the
  aspect-ratio-driven bias in recalled bar-top position.
labels:
- chart:bar
- task:recall
- visual:position
- visual:area
- impact:accuracy
- data:quantitative
- audience:novice
- cognitive:memory
---

## Treat aspect ratio, not area, as the driver of recall bias <!-- role: advice -->

Do not expect changes to bar area alone (for example, making marks larger or smaller) to eliminate systematic over- or underestimation in recalled bar heights. Address the bar’s aspect ratio or the reliance on memory instead.

## Why area changes fail to remove the bias <!-- role: reason -->

In bar charts, area covaries with height and width, but the observed signed error in recalled bar-top position is tied to mark aspect ratio rather than to mark area. When area was allowed to vary across aspect ratios, the same pattern of overestimation for wider shapes and underestimation for taller shapes persisted.

**Mechanism:** The bias arises from memory reconstruction influenced by shape (aspect ratio) and attraction toward a square-like prototype, which is not corrected by making bars larger or smaller.

**Evidence:** When bar widths were held constant to create variable areas across aspect ratios, the direction and pattern of signed error remained: wide conditions were overestimated, tall conditions underestimated, with little change attributable to area condition [@cejaTruthSquareAspect2021a]. Modeling showed area condition did not significantly predict signed error, while aspect ratio did [@cejaTruthSquareAspect2021a].

**Notes:** Area may affect salience or attention in other contexts, but in these experiments it did not explain the systematic direction of position recall bias.

## When this applies <!-- role: context -->

- **User Goal:** Accurately remember and report bar values.
- **Task:** Reproduce a bar’s height after the bar is no longer visible.
- **Data:** Quantitative values encoded as bar-top position.
- **Chart Setting:** Any bar-like mark where designers consider changing size/area to “improve accuracy.”
- **Audience:** Any audience performing delayed value judgments.
- **Success Criterion:** Reduced signed error (bias), not only reduced variability.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The design change is aimed at reducing random error (variance) rather than systematic directional bias. **Why:** The evidence isolates area as not explaining the directional bias pattern, but does not rule out other effects of size on variability in different tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Focusing on aspect ratio or simultaneous visibility can constrain layout more than simple resizing. **Risk:** Designers may spend effort tuning mark size without addressing the underlying bias source. **Mitigation:** Evaluate changes using signed error (directional bias), not only subjective readability.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Enlarging bars (increasing area) to “make the height easier to remember” while keeping elongated shapes. **Why it fails:** The systematic bias persists when area varies; aspect ratio remains the key predictor of bias [@cejaTruthSquareAspect2021a].
- **Mistake:** Assuming wide-vs-tall distortions are caused by area differences between marks. **Why it fails:** Signed error was not significantly predicted by area condition in the tested design, but was predicted by aspect ratio [@cejaTruthSquareAspect2021a].

## Quick tests <!-- role: check -->

**Failure Sign:** After resizing bars, users still overestimate wide bars and underestimate tall bars in delayed recall. **Quick Check:** Compare signed error across aspect ratios before and after an area-only change. **Stronger Test:** Fit a simple analysis (or pilot study) that separates aspect ratio from area and check whether signed error tracks aspect ratio rather than area [@cejaTruthSquareAspect2021a].

## What to do instead <!-- role: fix -->

- Change bar aspect ratios (or the layout that creates them) rather than only changing bar area.
- Keep the relevant bars simultaneously visible during value matching so judgments rely less on memory.
- Reduce the need for cross-view recall by enabling within-view comparisons.
- Validate fixes using signed error by aspect ratio to confirm the directional bias is reduced.
