---
id: avoid-point-labeling-in-dense-scatter-plots-when-marks-must-remain-legible
title: Avoid Labeling Every Point in Dense Scatter Plots
bibliography: references.bib
description: Point labels can obscure mark positions and make identification difficult;
  use alternatives when item detail is required.
labels:
- chart:scatter
- task:identify
- visual:text
- impact:clarity
- data:multivariate
- audience:any
- problem:occlusion
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Do not label every point in a scatter plot when labels will overlap marks or make points hard to see.

## The Logic <!-- role: reason -->

Labels introduce visual occlusion and interfere with the perceptual task of judging position; they also make it difficult to find a specific label among many, reducing effectiveness even if the design is expressive.

- **The Principle:** Preserve positional readability; avoid occlusion by added annotation
- **The Evidence:** The paper’s labeled scatter plot example shows labels obscure points and make individual items hard to find [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** See overall relationship (pattern) while maintaining readable point positions
- **Data Type:** Many items (high mark density) with quantitative axes
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** Very small number of points (low density), where labels do not overlap or obscure marks.
- **Reason:** The failure mode described in the paper depends on occlusion and search difficulty from many labels [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** Users cannot directly read item identities from the plot.
- **The Risk:** If item identities are essential and you remove labels without an alternative, the display may not meet the task [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking font until labels “fit.”
- **Why it fails:** It may reduce overlap but increases search difficulty and can still obscure points; the plot becomes hard to read [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** Labels overlap each other or cover the marks; point positions become ambiguous.
- **The Test:** Look specifically at whether you can accurately judge point positions without mentally “ignoring” labels; if not, labeling is harming the encoding [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove most labels and keep only a few key annotations.
- **Best Fix:** Switch to an alternative design better for per-item lookup (e.g., aligned bar chart when item details must be readable) [@mackinlayAutomatingDesignGraphical1986b].
