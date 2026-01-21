---
id: document-the-y-axis-range-in-sd-units-when-it-varies
title: Document the Y-Axis Range in SD Units When It Varies
bibliography: references.bib
description: If y-axis ranges differ across plots or omit error bars, state the y-axis
  span in SD units so readers can interpret magnitude consistently.
labels:
- chart:bar
- chart:line
- task:interpret
- visual:annotation
- impact:transparency
- impact:calibration
- data:continuous
- audience:novice
- custom:captioning
- source:wittGraphConstruction2019
---

## The Rule <!-- role: advice -->

When the y-axis range is chosen in SD units and may vary across plots (or when error bars are not shown), state the y-axis range in SD units in the figure caption [@wittGraphConstruction2019].

## The Logic <!-- role: reason -->

If SD-based scaling is the mechanism that aligns visual size with conceptual effect size, disclosing the SD span helps readers understand the intended calibration and supports consistent interpretation across figures [@wittGraphConstruction2019].

- **The Principle:** Transparency of scaling choices for calibrated interpretation
- **The Evidence:** The paper explicitly suggests indicating the axis range in SD units, especially when ranges vary across plots or error bars are omitted [@wittGraphConstruction2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Interpreting effect magnitude consistently across multiple figures.
- **Data Type:** Any SD-standardized context where the axis is centered on the mean and scaled by SD [@wittGraphConstruction2019].
- **Audience:** Readers comparing across panels/papers, especially when uncertainty is not visualized [@wittGraphConstruction2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The axis range is fixed and identical across all figures and clearly labeled in data units.
- **Reason:** The SD disclosure is less necessary if variability and ambiguity are minimal (the paper frames this as “could be useful,” particularly when it varies) [@wittGraphConstruction2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Slightly longer captions and added cognitive overhead for readers unfamiliar with SD units.
- **The Risk:** If computed SD differs across panels (by design), readers may misinterpret differences as substantive; the caption must be clear about the convention used [@wittGraphConstruction2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using SD-based scaling but not telling readers, leaving them to infer why charts look “zoomed” or “compressed.”
- **Why it fails:** It obscures the calibration intent and can reduce trust or comparability [@wittGraphConstruction2019].
- **The Wrong Fix:** Reporting only raw axis endpoints without the SD span.
- **Why it fails:** Readers cannot easily translate the visual range into standardized effect-size intuition [@wittGraphConstruction2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Multi-panel figures where each panel “feels” differently zoomed, with no explanation.
- **The Test:** Scan captions: if SD-based axis logic is used and not mentioned anywhere, add the SD span disclosure [@wittGraphConstruction2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a caption note such as “y-axis spans ~1.5 SD around the grand mean.”
- **Best Fix:** Standardize captions to report (a) the SD span used, and (b) whether the range was adjusted to include error bars or unusually large effects [@wittGraphConstruction2019].
