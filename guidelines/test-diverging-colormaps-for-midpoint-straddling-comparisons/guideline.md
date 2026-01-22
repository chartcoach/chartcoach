---
id: test-diverging-colormaps-for-midpoint-straddling-comparisons
title: Test diverging colormaps specifically for midpoint-straddling comparisons
bibliography: references.bib
description: Diverging colormaps can incur higher errors when comparisons cross the
  neutral midpoint, so validate those cases explicitly.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Validate diverging palettes on comparisons that cross the midpoint <!-- role: advice -->

When you use a diverging colormap, explicitly test judgments where the candidate values lie on opposite sides of the midpoint. Do not assume performance on each side separately guarantees correct cross-midpoint comparisons.

## Midpoint boundaries can trigger misgrouping and distance errors <!-- role: reason -->

A diverging palette concatenates two sequential ramps around a neutral center; comparisons that cross that center can be distorted by categorical grouping (chromatic vs neutral) or by hue-boundary effects.

**Mechanism:** Viewers may overweight hue similarity or saturation changes and underweight true scale distance when one option is near the neutral midpoint and the other is a saturated color on the opposite side.

**Evidence:** In the evaluated diverging blueorange colormap, performance matched single-hue behavior when all three stimuli stayed on one side, but error rates increased when comparisons straddled the central boundary (near the midpoint) [@liuSomewhereRainbowEmpirical2018a]. Example high-error triplets involved a nearer achromatic option versus a farther, similarly-hued saturated option, indicating a systematic failure mode at the midpoint boundary [@liuSomewhereRainbowEmpirical2018a].

**Notes:** This is about relative distance judgments, not simply identifying sign (above vs below midpoint).

## Context <!-- role: context -->

- **User Goal:** Compare “which is closer” to a reference value in signed or deviation-from-baseline data.
- **Task:** Similarity judgments that can involve values on both sides of a central reference.
- **Data:** Quantitative data with a meaningful midpoint used as a semantic divider.
- **Chart Setting:** Diverging legend with a neutral center; users compare across that center.
- **Audience:** General; may rely on perceptual grouping rather than legend reading.
- **Success Criterion:** Consistent accuracy for within-side and cross-midpoint comparisons.

## Exceptions <!-- role: exceptions -->

**Break it when:** Users only ever compare within the same side of the midpoint (e.g., only positive deviations are explored at once). **Why:** The midpoint-straddling failure mode is not exercised.

## Costs <!-- role: costs -->

**Sacrifice:** Additional evaluation time for a targeted set of midpoint-crossing cases. **Risk:** Focusing only on midpoint behavior might miss other localized issues (e.g., extremes). **Mitigation:** Sample tests across midpoint and at both ends of the scale.

## Mistakes <!-- role: mistakes -->

- **Mistake:** Evaluating a diverging palette by checking only monotonicity on each half. **Why it fails:** Cross-midpoint comparisons can be disproportionately error-prone even if each half behaves like a good sequential ramp.
- **Mistake:** Assuming the neutral midpoint is always perceptually “between” the two sides in a way that supports distance judgments. **Why it fails:** The experiment showed higher error when values straddled the midpoint.

## Quick tests <!-- role: check -->

**Failure Sign:** Users pick the option with the same hue family as the reference even when it is farther in value, especially near the midpoint. **Quick Check:** Create a few triplets where one option is just across the midpoint and the other is farther but shares hue characteristics, and see if errors spike. **Stronger Test:** Run a short triplet-judgment pilot stratified by whether triplets cross the midpoint.

## Fix <!-- role: fix -->

- Reduce reliance on cross-midpoint distance judgments by adding direct numeric labels or hover readouts near the midpoint.
- Adjust the palette design so the midpoint neighborhood does not create a strong chromatic-vs-neutral grouping cue.
- If the primary task is cross-midpoint comparison, consider alternative encodings that do not hinge on the midpoint hue boundary.
- Split the view into separate panels for each side of the midpoint when comparisons across sides are not essential.
