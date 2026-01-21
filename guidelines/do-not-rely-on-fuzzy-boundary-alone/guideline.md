---
id: do-not-rely-on-fuzzy-boundary-alone
title: Do Not Rely on Fuzzy Boundaries Alone to Communicate Uncertainty
bibliography: references.bib
description: Softening the cone edge changes what users talk about but may not reliably
  change their distance-based damage judgments.
labels:
- chart:map
- task:assess-risk
- visual:blur
- impact:robustness
- data:spatiotemporal
- audience:novice
- domain:hurricane
---

## The Rule <!-- role: advice -->

Do not assume that switching from a hard-edged cone to a fuzzy-edged cone will, by itself, fix non-expert misinterpretations of hurricane forecast uncertainty.

## The Logic <!-- role: reason -->

In the study, fuzzy-cone displays led participants to mention “depth of color” more, but fuzzy boundaries did not produce strong, consistent improvements in the main distance-based damage judgment patterns relative to the standard cone-centerline visualization [@ruginskiNonexpertInterpretationsHurricane2016].

- **The Principle:** Aesthetic uncertainty cues can be overridden by stronger structural cues (shape/center emphasis)
- **The Evidence:** [@ruginskiNonexpertInterpretationsHurricane2016]

## Where to Apply <!-- role: context -->

- **User Goal:** Interpret uncertainty correctly (not as impact footprint or storm size).
- **Data Type:** Cone-like forecast regions where designers consider adding “fuzziness” to signal uncertainty.
- **Audience:** Non-experts under minimal instruction/legend conditions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your evaluation shows fuzziness measurably improves the specific misunderstanding you care about in your audience.
- **Reason:** The paper’s result is about limited standalone benefit; local testing may differ.

## The Price <!-- role: costs -->

- **The Sacrifice:** Fuzzy edges can introduce ambiguity about what is “inside vs outside.”
- **The Risk:** Users may substitute new heuristics (e.g., darkness = intensity) that are not intended [@ruginskiNonexpertInterpretationsHurricane2016].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding fuzziness while leaving other misleading cues intact (widening cone, dominant centerline).
- **Why it fails:** Users continue to rely on the dominant structural cues; the paper found only limited shifts attributable to fuzziness alone [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users talk about color darkness rather than uncertainty, or their damage ratings still rise at later timepoints because the “cone looks bigger.”
- **The Test:** Compare judgments across timepoints; if later-time damage increases persist similarly to the hard-edged cone, fuzziness is not solving the core problem [@ruginskiNonexpertInterpretationsHurricane2016].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Pair fuzziness with a representation that better communicates multiple possible outcomes (rather than a single expanding region).
- **Best Fix:** Use an ensemble depiction (or similarly distribution-forward design) to reduce size/intensity misreadings and encourage uncertainty-aware reasoning [@ruginskiNonexpertInterpretationsHurricane2016].
