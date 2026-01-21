---
id: use-roc-framing-for-categorical-signal-messages
title: Use ROC Tradeoff Framing for Categorical Signal Messages
bibliography: references.bib
description: For yes/no warnings, summarize uncertainty as a tradeoff between misses
  and false alarms, not as a single vague statement.
labels:
- task:classify
- impact:decision-support
- data:categorical
- audience:general
- uncertainty:tradeoff
- domain:science-communication
---

## The Rule <!-- role: advice -->

When communicating a categorical warning (act vs don’t act), express uncertainty as the achievable tradeoff between hit rate and false-alarm rate (the “receiver operating” tradeoff), and state where the current threshold sits.

## The Logic <!-- role: reason -->

For threshold decisions, what matters is not only uncertainty but the tradeoff it forces between missed events and false alarms. Receiver operating framing captures that structure and helps users interpret performance without guessing the science’s discriminability or the chosen caution level [@fischhoffCommunicatingScientificUncertainty2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Acting at the right time under uncertainty.
- **Data Type:** Binary outcomes with imperfect detection (storms, tumors, emergency transfers).
- **Audience:** People evaluating or relying on warnings and alerts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is no definable “event” or no way to evaluate outcomes after the fact.
- **Reason:** ROC-style tradeoffs require clear definitions of events and outcomes; without them, the tradeoff cannot be grounded [@fischhoffCommunicatingScientificUncertainty2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More analytical work (or elicitation) to estimate tradeoffs; more explanation needed for unfamiliar audiences.
- **The Risk:** Poorly defined events (“what counts as a tumor/flood”) can make the tradeoff misleading [@fischhoffCommunicatingScientificUncertainty2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Reporting only “accuracy” or a single probability without the miss/false-alarm structure.
- **Why it fails:** Users cannot distinguish uncertain science from a cautious threshold, and can over- or under-trust the recommendation system [@fischhoffCommunicatingScientificUncertainty2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Users interpret false alarms as evidence that “experts don’t know anything.”
- **The Test:** Ask whether the message lets a user say what kind of error is being minimized (misses vs false alarms); if not, the tradeoff is not communicated [@fischhoffCommunicatingScientificUncertainty2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit “miss vs false alarm” language (even if qualitative) and specify the preference.
- **Best Fix:** Provide quantified rates (or ranges) of misses and false alarms tied to a clear event definition and the current threshold [@fischhoffCommunicatingScientificUncertainty2014].
