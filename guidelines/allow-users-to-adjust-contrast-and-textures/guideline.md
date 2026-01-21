---
id: allow-users-to-adjust-contrast-and-textures
title: Let Users Adjust Contrast and Textures
bibliography: references.bib
description: Provide user controls to increase/decrease contrast and toggle chart
  textures without overriding user-agent accessibility settings.
labels:
- chart:any
- task:explore
- visual:color
- impact:accessibility
- data:any
- audience:disabled
- principle:flexible
- source:chartability
---

## The Rule <!-- role: advice -->

Provide a way for users to adjust chart contrast and to toggle chart textures on/off, and do not interfere with or override user-agent contrast adjustments; the chart must adapt to the new settings.

## The Logic <!-- role: reason -->

Adjustable contrast and optional textures preserve user agency over perceivability and operability in the presence of diverse accessibility needs, especially when user-agent settings change; this aligns with Chartability’s Flexible principle (Perceivable/Operable yet Robust) that requires respecting settings from browsers/OS/apps and supporting presentation/operation control [@elavskyHowAccessibleMy2022]. Because textures can add visual complexity and can become barriers when enabled by default, users must be able to enable or disable textures based on preference [@elavskyHowAccessibleMy2022]. Texture density/pattern can also be tuned as part of this adjustability to better support accessibility outcomes in practice [@observablehq_experimental_colour].

## Where to Apply <!-- role: context -->

This advice is designed for situations where presentation settings materially affect understanding.

- **User Goal:** Reading and interpreting encoded values/categories when default styling is not perceivable or is visually overwhelming.
- **Data Type:** Any chart where color/contrast and fill patterns/textures carry meaning (especially categorical encoding via color + texture).
- **Audience:** Users who rely on user-agent contrast adjustments or who have differing preferences for texture use (some need redundancy; others find texture overwhelming) [@elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization does not use textures at all and does not expose any styling controls.
- **Reason:** The “toggle textures” part is non-applicable when no textures exist as a feature; however, the rule about not overriding user-agent contrast adjustments still applies [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional UI/engineering effort to expose controls and maintain multiple visual states.
- **The Risk:** If implemented inconsistently, users may end up with confusing or mismatched encodings when switching contrast/texture settings [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Turning textures on by default “for accessibility” without a way to disable them.
- **Why it fails:** Default textures can introduce visual complexity that creates barriers and can undermine pre-attentive reading; different users have conflicting needs, so textures must be user-controllable [@elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Hard-coding contrast/palette choices that override or ignore user-agent contrast changes.
- **Why it fails:** It removes user agency and breaks robustness when system/browser settings change; the chart must adapt to those settings [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart’s contrast and texture styling stays fixed even after the user changes contrast settings, or textures are unavoidable once enabled.
- **The Test:** Change user-agent/system contrast settings and verify the chart adapts; then verify there is an explicit way to toggle chart textures and that enabling/disabling textures produces a usable result [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a visible, user-facing toggle to turn textures on/off and ensure chart styling does not block user-agent contrast adjustments [@elavskyHowAccessibleMy2022].
- **Best Fix:** Provide a small set of user controls for contrast and texture (including texture density/pattern options) and ensure the chart updates correctly when user-agent contrast adjustments change, maintaining legible encodings across states [@elavskyHowAccessibleMy2022; @observablehq_experimental_colour].
