---
id: present-quantities-in-multiple-representations-to-support-representational-fluency
title: Present key quantities in multiple representations to support representational
  fluency
bibliography: references.bib
description: Use more than one format (e.g., percent and frequency, text and graphic)
  so users can recognize equivalence and reduce format-driven errors.
labels:
- chart:general
- task:compare
- visual:annotation
- impact:comprehension
- data:probabilistic
- audience:novice
- domain:health
---

## Show the same quantity in more than one format <!-- role: advice -->

Present important probabilities or measurements in multiple equivalent representations (for example, frequencies and percentages, or text and a graphic). Ensure the representations clearly refer to the same underlying quantity.

## Why multiple representations reduce format-driven misunderstanding <!-- role: reason -->

People vary in their ability to translate between representations of the same quantity, and unfamiliar representations can disrupt recognition even when the underlying value is understood. Multiple formats can reduce dependence on any single representational convention and improve interpretation for a broader audience.

**Mechanism:** Redundancy across representations helps users map a number to meaning by offering alternative cognitive entry points and by making equivalence explicit.

**Evidence:** Difficulty translating between representations (representational fluency) contributes to differing decisions across number formats and challenges using tabular displays even when device readouts are understood; presenting information in multiple formats can help compensate for poor representational fluency [@anckerRethinkingHealthNumeracy2007].

**Notes:** The goal is not duplication for its own sake, but making equivalence obvious.

## When multiple representations are especially needed <!-- role: context -->

- **User Goal:** Understand or compare probabilities, risks, or measured values.
- **Task:** Translate, compare magnitudes, or apply thresholds to numbers.
- **Data:** Probabilities, percentages, ratios, lab values, blood pressure/glucose logs.
- **Chart Setting:** Decision aids, portals, telehealth dashboards, printed instructions, device-to-screen transitions.
- **Audience:** Mixed numeracy and mixed familiarity with tables/graphs.
- **Success Criterion:** Users correctly recognize and use the same value across formats and contexts.

## When not to add multiple representations <!-- role: exceptions -->

**Break it when:** Space or cognitive load limits mean a second representation would crowd out essential explanatory text or labeling. **Why:** Overloading the display can create new navigation and attention problems that negate the benefit.

## Tradeoffs of multiple representations <!-- role: costs -->

**Sacrifice:** More screen/print space and design time. **Risk:** Inconsistencies or rounding differences across representations can reduce trust. **Mitigation:** Use consistent rounding rules and visually bind the paired representations.

## Common failure modes with multiple representations <!-- role: mistakes -->

- **Mistake:** Showing two formats without explicitly tying them together (e.g., percent on one side, frequency elsewhere). **Why it fails:** Users may not realize they are equivalent and may treat them as different facts.
- **Mistake:** Mixing representations that imply different denominators without clarifying the base (e.g., “per 1000” vs “1 in N”). **Why it fails:** Users can miscompare magnitudes when denominators change.

## Quick tests for representational fluency support <!-- role: check -->

**Failure Sign:** Users interpret the same risk differently when shown as “10%” versus “10 in 100.” **Quick Check:** Ask users to point to where the display shows “the same number in another way.” **Stronger Test:** A/B test single-format versus dual-format displays for accuracy in comparison tasks.

## What to do instead when dual-format is too costly <!-- role: fix -->

- Add a short equivalence annotation (e.g., “10% means 10 out of 100 people”) adjacent to the primary number.
- Replace secondary numeric format with a small visual representation that encodes the same denominator clearly.
- Use tailoring to show only the most relevant quantitative facts while reserving space for a second representation of those facts.
- Provide an interactive toggle between formats so users can switch representations without crowding the display.
