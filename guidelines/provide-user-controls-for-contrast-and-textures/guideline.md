---
id: provide-user-controls-for-contrast-and-textures
title: Provide user controls to adjust contrast and toggle textures
bibliography: references.bib
description: Let users increase contrast and turn chart textures on or off without
  the visualization overriding system or browser accessibility settings.
labels:
- chart:any
- task:read
- visual:color
- impact:accessibility
- data:any
- audience:disabled
- principle:flexible
- control:contrast
- control:texture
---

## Adjustable contrast and optional textures <!-- role: advice -->

Provide a way for users to adjust contrast and to toggle chart textures on or off. Do not block, override, or break user-agent contrast adjustments, and adapt the chart when those settings change.

## Why contrast/texture controls support flexible access needs <!-- role: reason -->

A single visual styling choice can create barriers for different users in different contexts, so allowing users to alter contrast and texture reduces the chance that the chart’s readability depends on one fixed presentation. When textures are forced on, visual complexity can increase and make rapid visual discrimination harder, so giving users a texture toggle helps users avoid that cost when it hurts them more than it helps.

**Mechanism:** User-controlled styling lets people match the visualization’s appearance to their own perceptual and cognitive needs, while respecting user-agent settings ensures that accessibility preferences applied elsewhere still work in the chart.

**Evidence:** Flexibility-based accessibility heuristics for data visualizations include respecting user-agent settings and providing presentation controls as part of robust access across contexts [@elavskyHowAccessibleMy2022]. Texture density and pattern adjustments can materially change how well color-plus-texture encodings work for readers (including under color-vision constraints), motivating user-adjustable texture parameters rather than a fixed default [@misc{observablehq_experimental_colour}].

**Notes:** This guideline addresses conflicting access needs: textures may help some users distinguish categories, but the added visual complexity can be a barrier for others [@elavskyHowAccessibleMy2022].

## When adjustable contrast and texture toggles are needed <!-- role: context -->

- **User Goal:** Read and distinguish encoded values/categories reliably under their own preferred visual settings.
- **Task:** Identify categories/series and compare marks without being blocked by styling.
- **Data:** Any data where color or fill styling contributes to distinguishing marks (especially categorical encodings).
- **Chart Setting:** Charts that use fills, strokes, patterns/textures, or theme styling; especially when embedded in environments affected by browser/operating-system contrast settings.
- **Audience:** Mixed audiences with varying access needs, including people who rely on high-contrast settings or who find textures visually overwhelming.
- **Success Criterion:** Users can make the chart legible by changing contrast and can enable/disable textures without losing access to the information.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization is a fixed, non-interactive static artifact where no user controls or user-agent settings can be detected or applied. **Why:** There is no mechanism available to provide toggles or respond to user-agent preference changes [@elavskyHowAccessibleMy2022].

## Tradeoffs of adding contrast/texture controls <!-- role: costs -->

**Sacrifice:** Additional implementation effort and interface complexity. **Risk:** Adding toggles can introduce inconsistent styling states that are not tested or documented. **Mitigation:** Keep the control surface minimal and ensure each mode preserves the same underlying data encoding [@elavskyHowAccessibleMy2022].

## Common ways this fails in practice <!-- role: mistakes -->

- **Mistake:** Shipping textures permanently enabled (or permanently disabled) with no user option. **Why it fails:** A fixed texture decision can either add visual complexity that becomes a barrier or remove a distinguishing cue that some users need [@elavskyHowAccessibleMy2022].
- **Mistake:** Forcing a custom theme that ignores or overrides user-agent contrast adjustments. **Why it fails:** Users lose the accessibility settings they depend on elsewhere, and the chart may not adapt when those settings change [@elavskyHowAccessibleMy2022].

## How to quickly check for failures <!-- role: check -->

**Failure Sign:** Users cannot make the chart legible when contrast is too low, and textures cannot be turned off when they feel visually noisy. **Quick Check:** Look for any exposed control to increase contrast and to toggle textures, and confirm the chart does not disable user-agent contrast adjustments [@elavskyHowAccessibleMy2022]. **Stronger Test:** Change contrast settings in the user agent and verify the chart adapts without losing category/value distinguishability, then vary texture settings (on/off or density) and confirm the encoding remains interpretable [@misc{observablehq_experimental_colour}; @elavskyHowAccessibleMy2022].

## What to do instead <!-- role: fix -->

- Provide a contrast control (or theme switch) that increases contrast without changing the meaning of encodings.
- Provide a user-facing toggle to enable or disable textures on mark fills.
- Ensure user-agent contrast adjustments are not overridden, and re-render or restyle the chart when those settings change.
- If textures are used for differentiation, allow adjusting texture density/pattern so users can reduce visual complexity while keeping distinctions [@misc{observablehq_experimental_colour}].
