---
id: use-icon-array-natural-frequency-displays-to-support-low-numeracy
title: Use natural-frequency icon arrays to support decisions for low numeracy or
  graph literacy audiences
bibliography: references.bib
description: Icon arrays can make probabilities interpretable as perceptual counts,
  improving decisions for low-literacy audiences.
labels:
- chart:icon-array
- task:compare
- visual:counting
- impact:accessibility
- data:probability
- audience:novice
- audience:low-literacy
---

## Prefer visual natural frequencies for communicating probabilistic medical risks to non-experts <!-- role: advice -->

When communicating probabilities to audiences with low numeracy or low graph literacy, present them as natural frequencies using icon arrays. Ensure the visual structure makes it easy to compare parts-to-whole without requiring calculation.

## Icon arrays enable perceptual comparison instead of computation <!-- role: reason -->

Probabilities are often unintuitive in numeric form; representing them as natural frequencies supports direct perceptual comparison and reduces the need for working-memory-heavy arithmetic. This can allow more accurate decisions even when viewers lack relevant quantitative skills.

**Mechanism:** The display turns an abstract proportion into a visible count (“X out of Y”), enabling Type 1-like perceptual inference and reducing reliance on Type 2 computation.

**Evidence:** Natural-frequency visualizations such as icon arrays improve risk comprehension for individuals with lower numeracy and related literacy measures in medical decision contexts [@padillaDecisionMakingVisualizations2018].

**Notes:** Benefits depend on the icon array being interpretable as a denominator-stable whole rather than as isolated salient differences.

## When this applies <!-- role: context -->

- **User Goal:** Understand and compare medical risks, side effects, or treatment benefits.
- **Task:** Compare probabilities across options; judge risk reduction.
- **Data:** Binary outcomes with probabilistic rates (e.g., event happens/does not happen).
- **Chart Setting:** Patient education materials, consent discussions, public health communication.
- **Audience:** Low numeracy, low graph literacy, or low health literacy audiences.
- **Success Criterion:** Improved risk comprehension and better-aligned choices.

## Exceptions <!-- role: exceptions -->

**Break it when:** The probabilities are extremely small and the required denominator would make the icon array unwieldy at the available resolution. **Why:** The display becomes too dense to count/compare perceptually.

## Costs <!-- role: costs -->

**Sacrifice:** Space and flexibility for multi-outcome or continuous distributions. **Risk:** Poor denominator choices can reintroduce denominator neglect or make comparisons misleading. **Mitigation:** Keep denominators consistent across options within a decision.

## Mistakes <!-- role: mistakes -->

- **Mistake:** Changing denominators between options (e.g., 1 in 100 vs 1 in 1000) within a single comparison. **Why it fails:** Viewers cannot compare visually without normalization.
- **Mistake:** Making the “affected” icons too visually dominant without preserving the visible whole. **Why it fails:** It encourages foreground-based judgments instead of rate-based judgments.

## Check <!-- role: check -->

**Failure Sign:** Users can restate the highlighted count but not the “out of” denominator. **Quick Check:** Ask users to explain the probability as “out of how many”; if they cannot, the natural frequency is not clear. **Stronger Test:** Compare comprehension across literacy levels; the design should reduce gaps between high- and low-numeracy users.

## Fix <!-- role: fix -->

- Use a consistent, explicitly visible denominator in the icon array for all options being compared.
- Add concise labels that bind the numerator to the denominator adjacent to the array.
- If the denominator must be large, switch to a scaled representation that still preserves a clear whole-per-part mapping.
- Reduce competing visual salience so viewers attend to the part-to-whole structure rather than to decorative elements.
