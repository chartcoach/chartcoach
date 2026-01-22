---
id: define-technical-terms-and-test-interpretation-before-using-uncertainty-words
title: Define technical forecast terms and user-test their interpretation
bibliography: references.bib
description: Prevent misunderstanding by defining key terms (like event definitions)
  and empirically testing comprehension.
labels:
- chart:annotation
- task:interpret
- visual:text
- impact:clarity
- data:uncertainty
- audience:public
- domain:science-communication
---

## Define the event and the terms before expressing uncertainty <!-- role: advice -->

Before you communicate an uncertainty statement, define the outcome/event and any technical term used to describe it in audience-meaningful language. Validate comprehension with user testing and replace jargon-like everyday words that have expert-only meanings.

## Why shared definitions are prerequisite to uncertainty communication <!-- role: reason -->

Uncertainty statements only work if sender and receiver share the same referents for outcomes and categories. Common words used in specialized ways and vague category boundaries cause users to form the wrong mental model of what probabilities or labels apply to, undermining decision-making.

**Mechanism:** Clear, tested definitions align the audience’s interpretation with the model’s inputs/outputs, reducing semantic error before numeric uncertainty is even considered.

**Evidence:** People misinterpret probability-of-precipitation forecasts when they do not know the operational definition of “precipitation,” showing that seemingly simple terms can mislead without shared meaning [@fischhoffCommunicatingScientificUncertainty2014]. Clarity of terminology is treated as an empirical question best answered by user testing, and familiar rephrasings may be needed when expert terms fail to communicate [@fischhoffCommunicatingScientificUncertainty2014].

**Notes:** Terminology failures can also arise when institutional labels change (e.g., category downgrades) while the underlying hazard remains severe.

## When terminology defines what the uncertainty refers to <!-- role: context -->

- **User Goal:** Interpret an uncertainty statement and apply it to a real-world decision.
- **Task:** Map a probability/label to an expected condition or event.
- **Data:** Forecasts, warnings, screening results, risk categories, model outputs with thresholds.
- **Chart Setting:** Public-facing advisories, legends, tooltips, FAQs, reports with probability language.
- **Audience:** Non-experts; mixed numeracy; may assume everyday meanings of words.
- **Success Criterion:** Users can correctly paraphrase the defined event and what the uncertainty statement is about.

## When not to prioritize term definition first <!-- role: exceptions -->

**Break it when:** The communication is purely internal among specialists who already share operational definitions. **Why:** The primary risk (semantic mismatch) is reduced in expert-to-expert contexts.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional space and time for definitions and testing. **Risk:** Over-defining can feel patronizing or clutter the main message. **Mitigation:** Put definitions in lightweight, skimmable elements (glossary, hover, short parenthetical) validated with users.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using common words in technical ways without stating the operational definition. **Why it fails:** Users apply everyday meanings and misinterpret the uncertainty statement [@fischhoffCommunicatingScientificUncertainty2014].
- **Mistake:** Assuming a label downgrade implies reduced danger without explaining category criteria. **Why it fails:** Users may infer the hazard changed when only the classification changed [@fischhoffCommunicatingScientificUncertainty2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Users disagree about what the forecast term refers to (location, threshold, timeframe).\
**Quick Check:** Ask a typical user to define the key term in one sentence; failure indicates misalignment.\
**Stronger Test:** Run a comprehension test where users classify scenarios as “counts as the event” vs “does not.”

## What to do instead <!-- role: fix -->

- Add an explicit operational definition of the event (threshold, location, timeframe) next to the uncertainty statement.
- Replace expert shorthand with audience-language equivalents where feasible.
- Provide one concrete example and one non-example of what the term includes.
- User-test paraphrase accuracy and revise until most users restate the intended meaning.
