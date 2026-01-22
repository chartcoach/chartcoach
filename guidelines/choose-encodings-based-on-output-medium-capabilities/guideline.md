---
id: choose-encodings-based-on-output-medium-capabilities
title: "Choose encodings based on the output medium\u2019s available channels"
bibliography: references.bib
description: Select different encodings when color or other channels are unavailable
  so that all relations remain expressible and readable.
labels:
- chart:general
- task:select
- visual:color
- impact:accessibility
- data:multivariate
- audience:general
- concept:media-sensitivity
---

## Adapt encoding choices to available channels like color versus monochrome <!-- role: advice -->

Choose encodings that match the output medium’s available channels, and switch to alternative designs when a required encoding (such as color) is unavailable.

## Why medium constraints change what designs are feasible and effective <!-- role: reason -->

The availability of channels such as color affects which primitive encodings can be used and which compositions are possible. Removing a channel can force backtracking to different encodings or even different overall chart structures to keep the presentation expressible and effective.

**Mechanism:** Channel availability constrains the set of expressive encodings and the compatibility of compositions; removing a channel can eliminate otherwise valid mark compositions.

**Evidence:** When color is available, an integrated scatter plot can encode multiple relations using position and color, but on monochrome output the system rejects certain retinal encodings (for example, saturation with many levels) and may fall back to aligned bar charts to remain expressible and readable [@mackinlayAutomatingDesignGraphical1986b]. The selection process explicitly treats medium capabilities as constraints that change which encodings and compositions succeed [@mackinlayAutomatingDesignGraphical1986b].

**Notes:** Medium sensitivity is not just cosmetic; it changes the feasible design space.

## When this applies <!-- role: context -->

- **User Goal:** Present the same underlying relations across different devices or media.
- **Task:** Preserve meaning and readability under channel constraints.
- **Data:** Multiple relations that may rely on retinal encodings.
- **Chart Setting:** Color displays, monochrome printers, or environments with restricted rendering capabilities.
- **Audience:** Readers who may receive the graphic in different media.
- **Success Criterion:** The chosen design remains expressive and legible in the target medium.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The output medium constraint is unknown or variable at view time. **Why:** You cannot reliably commit to a channel-dependent encoding without knowing whether the channel exists [@mackinlayAutomatingDesignGraphical1986b].

## Tradeoffs <!-- role: costs -->

**Sacrifice:** Medium-robust designs can be less compact or less integrated than designs that exploit all channels. **Risk:** Fallback designs (such as aligned views) can make global patterns harder to perceive. **Mitigation:** Reserve high-integration designs for media where the necessary channels are guaranteed.

## Common mistakes <!-- role: mistakes -->

**Mistake:** Designing a chart that depends on color encoding and then rendering it in monochrome without redesign. **Why it fails:** The intended distinctions collapse, forcing a different design to maintain expressiveness and effectiveness [@mackinlayAutomatingDesignGraphical1986b].

## Quick tests <!-- role: check -->

**Failure Sign:** In monochrome, categories that were distinct in color become indistinguishable or require too many gray levels to separate. **Quick Check:** View a grayscale version and verify that each encoded relation remains distinguishable. **Stronger Test:** For each relation, list which channel encodes it and confirm the channel exists and supports the needed number of distinct values.

## What to do instead <!-- role: fix -->

- Replace color encodings with positional encodings or separate aligned views when color is unavailable.
- Avoid encodings that require many distinct grayscale steps for ordinal variables in monochrome settings.
- Change the composition strategy (for example, from mark composition to single-axis composition) when channel conflicts arise.
- Provide separate designs optimized for color and monochrome outputs when the same design cannot serve both.
