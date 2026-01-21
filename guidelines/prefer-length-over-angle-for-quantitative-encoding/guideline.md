---
id: prefer-length-over-angle-for-quantitative-encoding
title: Prefer Length Over Angle for Quantitative Encoding
bibliography: references.bib
description: When position is not available, use length rather than angle to encode
  quantitative values.
labels:
- task:compare
- visual:length
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general
- complexity:foundational
---

## The Rule <!-- role: advice -->

If you cannot encode a quantitative value with position, encode it with length rather than angle.

## The Logic <!-- role: reason -->

In the theoretical effectiveness ordering, quantitative encodings rank length above angle. This guideline is drawn from the ranked effectiveness knowledge in [@mackinlayAutomatingDesignGraphical1986a] and collated as actionable recommendation knowledge in [@zengReviewCollationGraphical2023].

- **The Principle:** Effectiveness ranking for quantitative perceptual tasks
- **The Evidence:** [@mackinlayAutomatingDesignGraphical1986a], collated in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** More accurate magnitude comparison when position cannot be used
- **Data Type:** Quantitative values requiring single-channel encoding
- **Audience:** General audiences

## When to Break It <!-- role: exceptions -->

- **Scenario:** Length cannot be represented due to strict mark or layout constraints, but angle is feasible.
- **Reason:** The rule assumes both encodings are feasible choices; feasibility can dominate ranking.

## The Price <!-- role: costs -->

- **The Sacrifice:** Length encodings may require more space or specific mark choices (e.g., bars).
- **The Risk:** Poorly implemented length encodings (e.g., cramped layout) can still harm readability even if the channel ranks higher.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing an angle encoding by default when a simple length encoding is possible.
- **Why it fails:** It uses a lower-ranked perceptual task for quantitative decoding.

## How to Check <!-- role: check -->

- **Visual Sign:** Quantitative values are communicated primarily by wedge/sector angles while a comparable length-based encoding is possible.
- **The Test:** Ask: “Could this value be read as a bar/extent instead of a slice angle?” If yes, length should usually win.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert angle marks into length marks (e.g., replace angle comparisons with bar lengths).
- **Best Fix:** Reallocate the quantitative variable to position; if not possible, use length as the next choice.
