---
id: avoid-boundaries-for-uncertainty
title: Use Gradients Instead of Boundaries for Uncertainty
bibliography: references.bib
description: Avoid hard borders when visualizing continuous uncertainty to prevent
  the 'containment heuristic'.
labels:
- data:uncertainty
- data:geospatial
- visual:opacity
- visual:blur
- psychology:bias
- chart:map
---

## The Rule <!-- role: advice -->
When visualizing continuous uncertainty (such as a storm path or a pollution cloud), use gradients, fading, or ensembles rather than solid circles or hard outlines.

## The Logic <!-- role: reason -->
Hard boundaries trigger a "containment heuristic"—a visual-spatial bias where users perceive everything inside the line as "homogeneous" (equally likely) and everything outside as "safe" (zero probability). [@padilla_decision_2018] describes this as a Type 1 heuristic: "Framing a picture is a way of saying that what is inside the picture has a different status from what is outside." This leads to deterministic construal errors, whereas gradients or fuzziness (visualizing the uncertainty directly) mitigate this bias.

*   **The Principle:** Visual-Spatial Biases (Containment Heuristic)
*   **The Evidence:** McKenzie et al. (2016), cited in [@padilla_decision_2018], found that users made better decisions about positional uncertainty with a Gaussian fade than with a bounded circle.

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing risk or likelihood of an event in a specific location.
*   **Data Type:** Continuous probabilistic data (weather forecasts, GPS error margins).
*   **Audience:** General public and non-experts who are prone to "deterministic construal."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Binary decision thresholds.
*   **Reason:** If the decision is strictly binary (e.g., "If probability > 50%, evacuate"), a hard line representing that specific threshold may be more effective than a gradient.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision in reading specific values. It is harder to say exactly where a gradient "ends."
*   **The Risk:** Users may complain that the visualization looks "blurry" or "unprofessional" compared to clean vector lines.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a disclaimer text saying "The cone represents 66% probability."
*   **Why it fails:** Visual-spatial biases (Type 1) are fast and automatic; they often override knowledge-driven corrections (Type 2), meaning users will still intuitively feel safe just outside the line.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there sharp lines separating "risk" from "no risk"?
*   **The Test:** Ask a user: " Is a point just inside the line significantly more dangerous than a point just outside the line?" If they say yes, the design is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Make the boundary semi-transparent or dashed to reduce the visual weight of the "container."
*   **Best Fix:** Use a "fuzzy" visual encoding like a gradient opacity or an ensemble display (showing many possible outcome paths) to represent the distribution.
