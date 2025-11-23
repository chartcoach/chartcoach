---
id: reinforce-time-intervals
title: Explicitly Label the Time Interval
bibliography: references.bib
description: Repeatedly state the duration over which a risk occurs, as visuals often
  obscure time and lead to magnitude bias.
labels:
- visual:text-labels
- data:temporal
- impact:accuracy
- task:risk-assessment
---

## The Rule <!-- role: advice -->
Clearly and repeatedly describe the time interval (e.g., "over 5 years," "lifetime risk") associated with any risk statistic or graphic.

## The Logic <!-- role: reason -->
Patients tend to focus on the magnitude of the ratio (the "gist") and ignore the time element entirely. A high number over a lifetime may feel riskier than a low number over a short period, even if the annual risk is lower. Visuals like pictographs typically do not represent time spatially.
*   **The Principle:** Denominator Neglect (Temporal).
*   **The Evidence:** People perceive treatments as more effective when shown in a 15-year survival curve vs. a 5-year curve because they ignore the time axis and look at the curve's shape/area [@fagerlin_helping_2011].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the urgency or accumulation of a risk.
*   **Data Type:** Survival curves, risk probabilities, incidence rates.
*   **Audience:** Any patient reviewing risk data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None.
*   **Reason:** Inattention to time is a "robust phenomenon," and time should always be clarified [@fagerlin_helping_2011].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Redundancy. You may need to repeat "over 10 years" in titles, subtitles, and legends.
*   **The Risk:** Visual clutter from repetitive text.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on a survival curve's X-axis label.
*   **Why it fails:** Patients may look at the height of the curve or the number of icons in a pictograph and ignore the axis or legend entirely [@fagerlin_helping_2011].

## How to Check <!-- role: check -->
*   **Visual Sign:** A pictograph illustrating "Risk of Cancer" with no large text stating the duration (e.g., "10-Year Risk").
*   **The Test:** Cover the axis or legend. Does the chart imply immediate risk? If so, the time interval is not prominent enough.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add the time duration to the chart title.
*   **Best Fix:** Present the same risk at different time intervals side-by-side (e.g., 5-year risk vs 10-year risk) to force attention to the accumulation of risk over time [@fagerlin_helping_2011].
