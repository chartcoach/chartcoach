---
id: verify-text-background-contrast-before-placing-labels-on-color
title: Verify Text Contrast on Colored Backgrounds
bibliography: references.bib
description: Check contrast when placing text on colored fills so annotations remain
  readable at intended sizes.
labels:
- chart:map
- task:annotate
- visual:color
- impact:accessibility
- data:any
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

Before placing text on colored areas, check that text and background color have sufficient contrast for the intended text size, and change colors if they don’t.

## The Logic <!-- role: reason -->

Low contrast makes labels unreadable; contrast checking ties readability to specific text sizes, preventing hidden annotation failures in maps and charts [@muth_colorguide_2018].

- **The Principle:** Contrast-dependent legibility
- **The Evidence:** [@muth_colorguide_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Read labels/annotations placed on fills (e.g., choropleths, highlighted bars).
- **Data Type:** Any chart/map using filled areas with overlaid text.
- **Audience:** General audiences, including low-vision readers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You can place labels outside colored areas with leader lines or direct labeling.
- **Reason:** If text is not on color, contrast constraints between text and fill are no longer the limiting factor [@muth_colorguide_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer palette choices; you may need to adjust brand colors or highlight hues.
- **The Risk:** Changing colors to increase contrast can alter the intended mood or emphasis [@muth_colorguide_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Putting saturated text on saturated backgrounds (e.g., red on blue) because it “feels vivid.”
- **Why it fails:** High saturation does not guarantee contrast; readability can still fail the contrast check [@muth_colorguide_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels look crisp at one size but become hard to read when scaled down or viewed quickly.
- **The Test:** Run a contrast check for the exact foreground/background pair and verify it passes for your planned font sizes [@muth_colorguide_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch label text to black/white (whichever improves contrast) and slightly adjust the background color.
- **Best Fix:** Redesign the palette and annotation strategy together: choose fills that maintain contrast or move labels off the colored areas [@muth_colorguide_2018].
