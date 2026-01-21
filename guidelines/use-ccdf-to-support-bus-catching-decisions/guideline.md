---
id: use-ccdf-to-support-bus-catching-decisions
title: Use a Complementary CDF to Communicate Chance of Catching the Bus
bibliography: references.bib
description: Use a (complementary) cumulative distribution plot when you want users
  to reason about the chance the bus arrives at or after a chosen time.
labels:
- chart:cdf
- task:estimate-probability
- visual:position
- impact:decision-quality
- data:temporal
- audience:novice
- domain:transit
---

## The Rule <!-- role: advice -->

Use a complementary CDF (CCDF) to show uncertainty when the key question is “If I arrive at time T, what’s my chance of still catching the bus?”

## The Logic <!-- role: reason -->

A CCDF directly encodes “probability of arriving at or later than T,” aligning with the natural decision framing in bus catching. In the incentivized decision study, CDF-style displays performed nearly as well as the top-performing dotplot condition and outperformed several other representations [@fernandesUncertaintyDisplaysUsing2018].

- **The Principle:** Match the uncertainty encoding to the decision query (probability-of-not-missed).
- **The Evidence:** CDF/CCDF conditions converged on high mean performance and low variance similar to dotplots [@fernandesUncertaintyDisplaysUsing2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Choose a departure/arrival time threshold based on acceptable miss probability.
- **Data Type:** Predictive distribution over a time-of-arrival variable.
- **Audience:** Non-expert users making quick, in-the-moment choices.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users primarily need to understand density/most-likely timing rather than threshold probabilities.
- **Reason:** A CDF emphasizes cumulative probability rather than the “shape” of the distribution; another encoding may better foreground the mode/peak (the paper compares multiple encodings for differing affordances) [@fernandesUncertaintyDisplaysUsing2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate depiction of “where the distribution is concentrated” than density-style shapes.
- **The Risk:** Users unfamiliar with cumulative encodings may require some exposure/learning, though the experiment showed learning over trials [@fernandesUncertaintyDisplaysUsing2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing a standard CDF without considering the bus-catching question.
- **Why it fails:** The paper selected CCDF specifically because it better corresponds to “chance I still catch it if I delay,” i.e., a survival-style probability [@fernandesUncertaintyDisplaysUsing2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users interpret higher values as “bus is more likely to arrive earlier” rather than “more likely to arrive later/after T.”
- **The Test:** Ask a quick comprehension question: “If you arrive at 10 minutes, is your chance of catching the bus higher or lower than if you arrive at 5?” The curve should make the direction unambiguous.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Flip/relabel the axis so it clearly communicates “chance bus arrives after time T.”
- **Best Fix:** Use an explicit CCDF design (probability of arrival at/after) consistent with the decision framing tested in the paper [@fernandesUncertaintyDisplaysUsing2018].
