---
id: support-low-numeracy-with-natural-frequency-visuals
title: Use Natural-Frequency Visualizations to Support Low Numeracy
bibliography: references.bib
description: Represent probabilities as countable frequencies so users can make perceptual
  comparisons instead of calculations.
labels:
- chart:icon-array
- task:risk-compare
- visual:count
- impact:accessibility
- data:probability
- audience:low-numeracy
- mechanism:type-1
---

## The Rule <!-- role: advice -->

When communicating risks or probabilities to general audiences, visualize them as natural frequencies (e.g., “10 out of 100”) that can be compared perceptually.

## The Logic <!-- role: reason -->

The review highlights that probabilities are often unintuitive, and that visualizations can make them more interpretable by depicting them as natural frequencies, enabling perceptual comparison rather than mathematical computation—benefiting people with lower numeracy/graph literacy [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare treatment risks/benefits, understand chance of an outcome, compare options under risk
- **Data Type:** Probabilities, medical risks, proportions
- **Audience:** People with low numeracy, low graph literacy, or low health literacy

## When to Break It <!-- role: exceptions -->

- **Scenario:** Extremely small or extremely large denominators where frequency grids become unwieldy
- **Reason:** The display may become too dense to support perceptual comparison, undermining the intended benefit [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and scalability; icon arrays can be large
- **The Risk:** If poorly designed, the display may reintroduce salience problems (e.g., foreground effects) [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only the affected cases (numerator) without an equally visible total (denominator)
- **Why it fails:** Viewers can overweigh highlighted cases and ignore the base rate [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can quickly say “how many out of how many” by inspection.
- **The Test:** Ask users to compare two risks without calculation; if they can do it by counting/estimating visually, the rule is working [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a consistent denominator frame (same total icons) across options.
- **Best Fix:** Use a frequency-based visual encoding that supports direct perceptual comparison between outcomes and options [@padillaDecisionMakingVisualizations2018].
