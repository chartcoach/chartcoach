---
id: express-parameter-uncertainty-with-probability-distributions-or-fractiles
title: Express Decision-Relevant Uncertainty Quantitatively
bibliography: references.bib
description: Use probability distributions or clearly stated fractiles for uncertain
  parameters when supporting choices among fixed options.
labels:
- task:estimate
- impact:clarity
- impact:decision-support
- data:quantitative
- audience:general
- uncertainty:probability
- domain:science-communication
---

## The Rule <!-- role: advice -->

When a numeric uncertainty matters to a decision, communicate it as a probability distribution over plausible values or as a clearly specified extreme fractile (e.g., 5th/95th).

## The Logic <!-- role: reason -->

Probability distributions are a standard representation of uncertainty for decision making; for some decisions, a single fractile can be sufficient, while others benefit from the full distribution. Explicit quantification reduces reliance on guessing and improvised interpretations [@fischhoffCommunicatingScientificUncertainty2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Evaluating expected outcomes and risks under uncertainty (climate sensitivity, treatment effects, investment returns).
- **Data Type:** Continuous parameters and model outputs.
- **Audience:** Decision makers comparing alternatives under uncertainty.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Experts can only provide conditional distributions without a probability for the conditioning event.
- **Reason:** Some uncertainties may be beyond current knowledge; reporting conditional cases can better prepare decision makers for surprises than forcing a single combined distribution [@fischhoffCommunicatingScientificUncertainty2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More effort to elicit, justify, and explain quantitative uncertainty.
- **The Risk:** Users may focus on a single number and ignore the distribution’s shape unless guided [@fischhoffCommunicatingScientificUncertainty2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using only vague verbal quantifiers (“likely,” “rare,” “good evidence”).
- **Why it fails:** Verbal uncertainty is interpreted inconsistently, especially by audiences unfamiliar with experts’ conventions [@fischhoffCommunicatingScientificUncertainty2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Different users report different meanings for the same uncertainty phrase.
- **The Test:** Ask users to translate your uncertainty statement into a numeric range; wide variation indicates a need for explicit quantification [@fischhoffCommunicatingScientificUncertainty2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a numeric range with an explicit probability level (e.g., “90% between Y and Z”).
- **Best Fix:** Provide a distribution (or a small set of key fractiles) plus a brief note on what sources of uncertainty it includes [@fischhoffCommunicatingScientificUncertainty2014].
