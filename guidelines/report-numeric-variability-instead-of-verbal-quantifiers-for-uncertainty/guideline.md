---
id: report-numeric-variability-instead-of-verbal-quantifiers-for-uncertainty
title: "Report numeric variability (\xB1 or intervals) instead of verbal uncertainty\
  \ qualifiers"
bibliography: references.bib
description: Use numeric expressions of variability to avoid wide interpretation ranges
  from vague verbal terms.
labels:
- chart:annotation
- task:interpret
- visual:text
- impact:clarity
- data:uncertainty
- audience:public
- domain:science-communication
---

## Express uncertainty with numbers rather than vague verbal qualifiers <!-- role: advice -->

When summarizing measurement variability or result uncertainty, use numeric formats such as ±X% or an explicit interval rather than qualitative phrases like “stable,” “rare,” or “good evidence.” Keep the numeric statement tied to a clearly defined outcome and time frame.

## Why numeric uncertainty reduces ambiguity in interpretation <!-- role: reason -->

Verbal quantifiers are interpreted inconsistently, especially by people unfamiliar with a field’s conventions, which makes audiences guess at magnitude. Numeric expressions constrain interpretation and reduce reliance on intuitive statistics that can be biased or insensitive to sample size and measurement quality.

**Mechanism:** Numeric bounds narrow the range of plausible meanings and let users compare magnitudes across outcomes and options without translating ambiguous adjectives.

**Evidence:** Verbal expressions of uncertainty communicate poorly and are widely misinterpreted, whereas explicit quantitative expressions (like intervals) are generally interpretable well enough to extract the main message [@fischhoffCommunicatingScientificUncertainty2014]. Decision makers otherwise must infer uncertainty using intuitive judgments that can be systematically biased, especially with poor data quality [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** Numeric expressions still require clear definitions of what is being quantified.

## When you are summarizing variability or uncertainty magnitude <!-- role: context -->

- **User Goal:** Understand how much confidence to place in a result and compare options.
- **Task:** Judge magnitude of uncertainty; decide whether differences matter.
- **Data:** Estimated effects, measurements, forecast probabilities, error rates, model outputs.
- **Chart Setting:** Reports, dashboards, side panels, evidence summaries, legends and footnotes.
- **Audience:** Mixed numeracy; may not share expert language conventions.
- **Success Criterion:** Users can correctly identify which result is more uncertain and by roughly how much.

## When not to use numeric expressions <!-- role: exceptions -->

**Break it when:** No defensible numeric bound can be provided even approximately (e.g., the uncertainty source is unknown and unbounded). **Why:** Numbers may falsely imply precision that the evidence cannot support [@fischhoffCommunicatingScientificUncertainty2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Added cognitive load for users who dislike numbers. **Risk:** Users may mistake a reported interval as the only uncertainty, ignoring omitted sources. **Mitigation:** Pair the number with a brief statement of what sources are included (and what is not).

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Replacing numbers with adjectives to “simplify” uncertainty. **Why it fails:** Audience interpretations vary widely and the message becomes non-comparable across contexts [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Giving a precise-looking number without clarifying what uncertainties were included. **Why it fails:** Users may overtrust the estimate and be surprised by later revisions [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Different readers map the same phrase (“rare,” “likely”) to very different probabilities.\
**Quick Check:** Remove adjectives and see whether the message still conveys magnitude via numbers alone.\
**Stronger Test:** Ask users to compare two uncertainty statements; they should choose the larger uncertainty reliably.

## What to do instead <!-- role: fix -->

- Replace verbal qualifiers with a numeric interval or ± expression tied to a defined outcome.
- Add a short label indicating what the interval represents (e.g., “expected range,” “uncertainty band”).
- Provide a plain-language paraphrase of the numeric range without adding new qualitative quantifiers.
- If uncertainty is not quantifiable, state what is unknown and why it cannot be bounded with current science.
