---
id: do-not-expect-wedge-legends-to-change-performance-vs-square-in-bivariate-maps
title: Treat wedge and square bivariate legends as equivalent for performance in basic
  lookup and choice tasks
bibliography: references.bib
description: Do not rely on wedge-shaped bivariate legends to improve accuracy or
  decision behavior relative to square legends.
labels:
- chart:heatmap
- task:identify
- visual:legend
- impact:clarity
- data:quantitative
- audience:general
- uncertainty:explicit
- legend:shape
---

## Choose wedge vs. square legends for communication needs, not expected accuracy gains <!-- role: advice -->

Choose a wedge-shaped or square bivariate legend based on how you want to communicate the mapping, but do not expect legend shape alone to reliably change accuracy or decision outcomes. Use other design levers (such as superposition and discretization) for performance-critical improvements.

## Why legend shape has limited effect on decoding and decisions <!-- role: reason -->

Legend shape changes the geometry of the key but does not necessarily reduce the core perceptual and cognitive demands of reading bivariate color encodings. As a result, performance differences may be dominated by other factors (e.g., juxtaposition vs. superposition, discrete vs. continuous).

**Mechanism:** The main difficulty lies in decoding bivariate color and integrating value with uncertainty; reshaping the legend does not materially simplify that decoding in the tested tasks.

**Evidence:** In the identification experiment, legend shape (wedge vs. square) showed no significant effect on accuracy among superimposed discrete bivariate charts [@correllValueSuppressingUncertaintyPalettes2018]. In the prediction experiment, legend shape likewise showed no significant effect on either uncertainty or value of selections [@correllValueSuppressingUncertaintyPalettes2018].

**Notes:** Legend shape can still affect conceptual communication even if it does not change measured task performance.

## When this “equivalence” assumption applies <!-- role: context -->

- **User Goal:** Decode a bivariate legend to interpret value and uncertainty.
- **Task:** Basic identification/lookups or simple placement choices using the legend.
- **Data:** Bivariate value + uncertainty encoded in color with discrete bins.
- **Chart Setting:** Bivariate map with a visible legend; limited training.
- **Audience:** General audiences.
- **Success Criterion:** Accuracy and decision distributions are not expected to change due to legend shape alone.

## When legend shape might matter more <!-- role: exceptions -->

**Break it when:** The legend must communicate a conceptual emphasis (e.g., explicitly signaling that high-uncertainty regions collapse). **Why:** Even without measured performance differences, the legend’s form can signal intent and may affect interpretation in unmeasured ways.

## Tradeoffs of focusing on legend shape <!-- role: costs -->

**Sacrifice:** Time spent tuning legend geometry may distract from higher-impact fixes. **Risk:** Designers may assume a wedge legend implicitly delivers VSUP-like caution without changing the underlying mapping. **Mitigation:** Validate with a task-focused check rather than relying on legend form.

## Common legend-shape misconceptions <!-- role: mistakes -->

- **Mistake:** Switching to a wedge legend to “fix” poor bivariate decoding. **Why it fails:** Legend shape alone did not produce significant accuracy improvements in the tested identification task.
- **Mistake:** Assuming a wedge legend will meaningfully change risk behavior. **Why it fails:** Decision behavior differences were driven by VSUP vs. standard quantization, not by legend shape.

## Quick checks for legend adequacy <!-- role: check -->

**Failure Sign:** Users still misread bivariate colors or ignore uncertainty even though the legend is wedge-shaped. **Quick Check:** Swap wedge and square legends while keeping the palette constant; if interpretation does not change, focus elsewhere. **Stronger Test:** Test superposition/discretization/quantization choices before iterating on legend geometry.

## What to do instead of changing legend shape <!-- role: fix -->

- Switch from juxtaposed to superimposed encoding when users must fuse value and uncertainty.
- Replace continuous bivariate color with discrete bins to reduce estimation error.
- Use Value-Suppressing Uncertainty Palette (VSUP) quantization when you want to discourage decisions based on high uncertainty.
- Add brief task-specific instruction text clarifying how uncertainty should affect interpretation when decision stakes are high.
