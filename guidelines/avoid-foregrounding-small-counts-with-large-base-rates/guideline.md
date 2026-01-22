---
id: avoid-foregrounding-small-counts-with-large-base-rates
title: Avoid foregrounding small icon differences when a large base rate determines
  meaning
bibliography: references.bib
description: Do not let visually salient small counts dominate judgments when the
  base rate makes differences negligible.
labels:
- chart:icon-array
- task:compare
- visual:foreground
- impact:accuracy
- data:probability
- audience:novice
- bias:foreground-effect
---

## Keep base rates visually integrated with the focal counts <!-- role: advice -->

When communicating risk or frequency, visually integrate the base rate with the displayed counts so viewers cannot ignore it. Do not present a large base rate only as background text while the focal differences are shown as salient icons.

## Foreground salience can trigger base-rate neglect in decisions <!-- role: reason -->

If a display makes a small set of icons highly noticeable while the base rate is minimally visible, viewers may rely on a “foreground effect,” judging magnitude from the salient count rather than from the true rate relative to the population size. This produces decisions that diverge from what the underlying probabilities warrant.

**Mechanism:** Bottom-up attention prioritizes the visually depicted icons, while the base rate (if relegated to text) is less likely to be encoded and used in the decision.

**Evidence:** When small icon differences were shown prominently but the large base rate was not visually integrated, decisions such as willingness-to-pay were substantially inflated relative to text-only presentations, consistent with a foreground-driven heuristic [@padillaDecisionMakingVisualizations2018].

**Notes:** The risk is highest when the absolute difference is visually easy to count but practically negligible after scaling by the base rate.

## When this issue occurs <!-- role: context -->

- **User Goal:** Decide between options based on risk reduction or expected harm.
- **Task:** Compare two treatments/products by their risk outcomes.
- **Data:** Very small probabilities with very large denominators (large populations).
- **Chart Setting:** Static risk communication graphics (health, safety, product risk).
- **Audience:** General public or non-experts.
- **Success Criterion:** Decisions reflect the true difference in rates, not the raw icon count.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The base rate is constant across all options and is already visually encoded in a shared denominator that viewers can see and compare. **Why:** The key comparison may legitimately be the difference in numerators when denominators are explicitly common and visible.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** More space or complexity to encode the denominator visually. **Risk:** Overly dense displays can overwhelm viewers if not carefully scaled. **Mitigation:** Use a consistent denominator and a clear visual grouping so the scale remains legible.

## Common mistakes <!-- role: mistakes -->

- **Mistake:** Putting the base rate as a single line of text while using icons for outcomes. **Why it fails:** Viewers attend to the icons and underuse the text base rate.
- **Mistake:** Using different implicit denominators across options. **Why it fails:** Viewers cannot reliably normalize, increasing reliance on salient counts.

## Quick checks <!-- role: check -->

**Failure Sign:** Viewers talk about “twice as many icons” while ignoring the population size. **Quick Check:** Remove the base-rate text and see if the graphic still seems interpretable; if it does, the base rate is not integrated enough. **Stronger Test:** Ask a short question that requires using the denominator (e.g., “out of how many?”) and see if accuracy collapses.

## Fixes <!-- role: fix -->

- Encode the denominator visually (e.g., consistent total set) so the base rate is part of what viewers see, not just what they read.
- Keep denominators identical across options and make that common scale visually explicit.
- Add a brief annotation that binds the numerator to the denominator (e.g., “X out of Y” placed adjacent to the marks).
- If the practical difference is negligible, explicitly state that equivalence as a takeaway alongside the visualization.
