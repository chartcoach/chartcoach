---
id: ensure-pointer-targets-are-at-least-24px-or-provide-alternative-selection
title: "Ensure pointer-targetable interactive marks are at least 24\xD724 CSS px or\
  \ provide an alternative selection method"
bibliography: references.bib
description: "Make pointer-activated interactive elements large enough to hit (24\xD7\
  24 CSS px minimum) or offer another way to perform the same action when marks are\
  \ smaller due to data encoding."
labels:
- chart:scatter
- chart:map
- chart:interactive
- task:select
- task:filter
- visual:position
- visual:size
- impact:accessibility
- audience:general
- modality:pointer
- modality:touch
- disability:motor
- complexity:advanced
---

## Pointer targets must be 24×24 CSS px or have an equivalent alternative <!-- role: advice -->

Make any interactive element that is activated by mouse or touch at least 24×24 CSS pixels, or provide another way to complete the same interaction when the mark is smaller due to data-driven sizing. If mark size encodes a variable (for example, small points in a scatterplot), do not require precise pointer hits as the only way to select, activate, or access the represented information.

## Why small pointer targets block interaction in data visualizations <!-- role: reason -->

Small pointer targets create operability barriers because users must perform precise cursor or touch movements to reach the intended control, and this becomes infeasible for many people with limited dexterity or motor impairments. In data visualization, this risk is amplified when marks are intentionally small because size and spatial position often encode data values, so accessibility must be achieved through alternative, equivalent interaction pathways rather than by forcing precision on the primary view [@elavskyHowAccessibleMy2022].

**Mechanism:** Increasing target size (or providing an equivalent non-precision alternative) reduces the motor control and accuracy needed to trigger the intended action, making interaction more error-tolerant and feasible under pointer input constraints.

**Evidence:** A minimum target size of 24×24 CSS pixels (or an equivalent alternative such as spacing or another control) is required to ensure pointer-activated controls are large enough for users with limited dexterity [@w3c_understanding_target]. Complex interactive data stories can depend heavily on pointer interaction, illustrating how requiring precise pointer hits can become a primary access barrier if equivalent alternatives are not provided [@fivethirtyeight_how_house; @elavskyHowAccessibleMy2022].

**Notes:** Techniques that expand hit areas without changing the visible mark can still leave significant operability barriers for people with motor impairments in dense visualizations, so equivalent alternative selection methods remain important [@elavskyHowAccessibleMy2022].

## When you must enforce minimum target size or add alternative selection <!-- role: context -->

- **User Goal:** Select or activate a specific data mark (or a control embedded in a chart) to reveal details, filter, highlight, or navigate.
- **Task:** Point-and-click (or tap) selection of marks or controls; repeated selection in exploration workflows.
- **Data:** High-density plots, many small marks, or marks whose size is driven by a data variable (making some marks necessarily small).
- **Chart Setting:** Interactive visualizations where pointer input is supported (mouse, trackpad, touchscreen) and mark-level interaction exists.
- **Audience:** Broad public audiences including people with motor impairments or limited dexterity.
- **Success Criterion:** The same information and functionality can be reached without requiring precise pointer targeting of tiny marks.

## When not to follow the 24×24 px minimum literally <!-- role: exceptions -->

**Break it when:** Mark size must remain small because size encodes a data variable and enlarging the visible mark would change the meaning of the chart. **Why:** Forcing a visual size increase can distort the data encoding, so equivalent alternative selection/activation must be used instead [@elavskyHowAccessibleMy2022].

## Tradeoffs of larger targets and alternative controls <!-- role: costs -->

**Sacrifice:** Larger targets or extra controls can increase visual clutter and consume space, especially in dense charts. **Risk:** Adding alternate interaction pathways can introduce additional UI complexity that must be kept consistent with the primary interaction. **Mitigation:** Keep the alternative pathway functionally equivalent to the mark-level interaction so users can achieve the same outcome without precision pointer input [@elavskyHowAccessibleMy2022].

## Common ways teams fail this requirement <!-- role: mistakes -->

- **Mistake:** Treating tiny marks (such as small points) as pointer-clickable without any equivalent alternative interaction. **Why it fails:** Users who cannot precisely target the mark cannot access the information or task that the mark represents [@w3c_understanding_target; @elavskyHowAccessibleMy2022].
- **Mistake:** Relying only on expanded invisible hit regions (for example, overlay-based targeting) as the sole remedy in dense charts. **Why it fails:** This can still impose significant operability barriers for people with motor impairments and does not guarantee an accessible, error-tolerant interaction path [@elavskyHowAccessibleMy2022].

## How to quickly check pointer target size and operability <!-- role: check -->

**Failure Sign:** Users must precisely click or tap very small marks to get any response, and missed clicks are common. **Quick Check:** For a sample of interactive marks and controls, verify that the pointer target area is at least 24×24 CSS pixels, or confirm there is an alternative way to perform the same selection/activation without precise targeting [@w3c_understanding_target]. **Stronger Test:** Attempt the key interactions in a dense region of the chart and confirm the same outcomes can be achieved via an alternative selection method when marks are smaller than 24×24 due to encoding [@elavskyHowAccessibleMy2022].

## Fixes when marks are too small to target reliably <!-- role: fix -->

- Provide an alternative selection method that does not require precise pointer targeting of individual marks, such as an accompanying data table, search function, or another non-precision control that triggers the same actions [@elavskyHowAccessibleMy2022].
- Add text labels or other selectable UI elements that meet the minimum target size and map clearly to the underlying marks and actions [@elavskyHowAccessibleMy2022].
- Support alternative navigation and input paths (such as keyboard-based interaction) that allow users to reach and activate the same mark-level functionality without pointer precision [@elavskyHowAccessibleMy2022].
- Add interaction features that reduce precision demands in dense charts, such as zooming or filtering that makes intended targets easier to access without requiring exact hits on tiny marks [@elavskyHowAccessibleMy2022].
