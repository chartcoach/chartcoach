---
id: do-not-assume-keys-will-correct-visual-spatial-biases
title: Do not rely on legends alone to correct visual-spatial misinterpretations
bibliography: references.bib
description: Explanatory keys may not override automatic visual-spatial biases induced
  by an encoding.
labels:
- chart:general
- task:interpret
- visual:legend
- impact:accuracy
- data:uncertainty
- audience:novice
- bias:visual-spatial
---

## Build the correct interpretation into the encoding, not just into a legend <!-- role: advice -->

Design the visualization so the intended meaning is the most natural perceptual interpretation, even without reading a key. Use legends as reinforcement rather than as the primary mechanism for preventing misinterpretation.

## Some visual-spatial biases persist despite explicit explanation <!-- role: reason -->

Visual-spatial biases can arise early from the encoding itself and can be difficult to suppress through effortful reasoning. If viewers’ default schema or perceptual inference contradicts the legend, they may continue to use the default interpretation.

**Mechanism:** Automatic Type 1 interpretations (from salience, boundaries, and learned schemas) can dominate over explicit instructions, especially when the display invites a deterministic or categorical construal.

**Evidence:** For uncertainty shown with interval-like graphics, viewers can maintain incorrect “high/low” interpretations despite a key describing the intended uncertainty meaning [@padillaDecisionMakingVisualizations2018]. Misinterpretations of salient uncertainty summaries (e.g., bounded regions) persist and can be linked to the visual encoding rather than lack of access to explanatory text [@padillaDecisionMakingVisualizations2018].

**Notes:** This does not mean instructions never help; it means encoding-driven biases require encoding-level solutions.

## When this applies <!-- role: context -->

- **User Goal:** Correctly interpret what the graphic encodes (especially uncertainty).
- **Task:** Use the visualization to make a consequential decision (evacuate, allocate resources, choose treatment).
- **Data:** Uncertain or probabilistic quantities that are easy to misread deterministically.
- **Chart Setting:** Static visuals where viewers may not read legends carefully.
- **Audience:** Non-experts or time-pressured viewers.
- **Success Criterion:** Correct interpretation without requiring legend reading.

## Exceptions <!-- role: exceptions -->

**Break it when:** You have a trained, captive audience and can require legend use as part of a standardized workflow. **Why:** Procedural compliance can reduce reliance on default interpretation.

## Costs <!-- role: costs -->

**Sacrifice:** Encoding-level clarity may require more space or less compact summaries. **Risk:** Over-engineering for “legend-free” reading can reduce flexibility for expert use. **Mitigation:** Provide layered detail: an intuitive primary encoding plus a legend for precision.

## Mistakes <!-- role: mistakes -->

- **Mistake:** Adding more legend detail after misinterpretations are observed. **Why it fails:** The default perceptual inference can remain unchanged.
- **Mistake:** Using a visually strong but semantically ambiguous form and expecting text to disambiguate. **Why it fails:** Viewers may not consult text before deciding.

## Check <!-- role: check -->

**Failure Sign:** People answer incorrectly but cite the legend as “clear,” or they never mention it. **Quick Check:** Hide the legend and see if interpretations change drastically; if they do, the encoding is not self-evident. **Stronger Test:** Timed comprehension questions that limit deliberation reveal whether the encoding itself drives the right inference.

## Fix <!-- role: fix -->

- Redesign the encoding to better match the intended schema (e.g., distributional rather than bounded/deterministic cues).
- Move key explanatory text adjacent to the marks it describes rather than isolating it in a legend.
- Add an explicit statement of what not to infer (e.g., “not a boundary/size”) directly on the graphic.
- Provide a second representation that makes the intended concept perceptually obvious (e.g., samples/ensembles alongside a summary).
