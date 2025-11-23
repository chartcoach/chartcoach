---
id: use-fuzziness-value-location-for-uncertainty
title: Encode Uncertainty Using Fuzziness, Location, or Value
bibliography: references.bib
description: Use fuzziness, location, or color value to represent ordinal uncertainty,
  as these are empirically the most intuitive visual variables.
labels:
- visual:texture
- visual:color
- visual:position
- data:uncertainty
- impact:intuitiveness
- task:rank
---

## The Rule <!-- role: advice -->
When representing ordinal levels of uncertainty on point symbols, prioritize the visual variables of **Fuzziness** (clarity/blur), **Location** (splitting/offsetting), or **Color Value** (lightness). Ensure the encoding follows these specific mappings:
*   **Fuzziness:** More fuzzy = Less certain.
*   **Location:** Further from center/split = Less certain.
*   **Value:** Lighter = Less certain.

## The Logic <!-- role: reason -->
Empirical testing of symbol intuitiveness indicates that users perceive these three variables as the most logical for representing uncertainty. In Experiment 1, these three variables consistently received mean intuitiveness rankings over 5.0 (on a 7-point scale), with fuzziness and location having a mode of 7 (logical) [@maceachren_visual_2012]. These variables possess a natural perceptual order that aligns with the concept of deteriorating data quality.

## Where to Apply <!-- role: context -->
*   **User Goal:** When the user needs to intuitively grasp that specific data points are less reliable than others without extensive training.
*   **Data Type:** Discrete entity uncertainty (point symbols) reported at the ordinal level (e.g., High, Medium, Low certainty).
*   **Audience:** General audiences or users who rely on intuitive "semantically resonant" cues rather than memorized legends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When high precision reading of the uncertainty value is required.
*   **Reason:** Variables like fuzziness (blur) interfere with the resolution of the symbol, making it difficult to define boundaries or exact values compared to geometric variables like size.

## The Price <!-- role: costs -->
*   **The Sacrifice:** **Location** (splitting) and **Fuzziness** alter the shape and footprint of the symbol, which may clutter dense maps or obscure the precise centroid of the data point.
*   **The Risk:** **Value** (lightness) might be confused with data density or other value-encoded attributes if the map is multivariate.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using **Color Saturation** to encode uncertainty.
*   **Why it fails:** Despite being commonly recommended in literature, empirical results showed saturation received low intuitiveness rankings (<4.0), making it "unacceptable" for intuitive visualization without a legend [@maceachren_visual_2012].
*   **The Wrong Fix:** Using **Shape** or **Orientation**.
*   **Why it fails:** These variables lack an inherent order that maps naturally to "more" or "less" certainty.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the "Uncertain" symbol. Does it look "faded," "blurry," or "broken" compared to the "Certain" symbol?
*   **The Test:** Ask a user which symbol is "Certain" without showing the legend. If they cannot guess correctly, the visual variable is not intuitive.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If using color, switch from varying Saturation (vividness) to varying Value (lightness/darkness), making uncertain points lighter.
*   **Best Fix:** Apply a Gaussian blur (Fuzziness) to uncertain elements, as this was the highest-rated variable for intuitiveness.
