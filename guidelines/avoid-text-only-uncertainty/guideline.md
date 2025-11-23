---
id: avoid-text-only-uncertainty
title: Visualize Distributions Instead of Textual Intervals
bibliography: references.bib
description: Textual probability summaries are brittle and fail to support consistent
  decision-making compared to visual distributions.
labels:
- visual:text
- task:risk-assessment
- impact:inconsistency
- data:probability
- audience:general-public
---

## The Rule <!-- role: advice -->
Avoid relying solely on textual prediction intervals (e.g., "85% chance," "High chance," or "Minutes 5–10") to communicate uncertainty for decision-making.

## The Logic <!-- role: reason -->
Textual displays compress the distribution into a single threshold that may not align with the user's personal utility function (risk tolerance). Users cannot adapt their decisions to different cost/benefit scenarios because the "shape" of the risk is hidden.
*   **The Principle:** Loss of Expressiveness / Inflexibility.
*   **The Evidence:** Textual displays (Text85, Text99) yielded inconsistent decision quality. Performance was sensitive to the specific probability level chosen; for example, the "85% chance" text condition resulted in poor performance with little learning over time compared to visual plots [@fernandes_uncertainty_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Making decisions where the cost of error varies (e.g., missing a bus to a casual lunch vs. missing a bus to a job interview).
*   **Data Type:** Uncertainty quantification.
*   **Audience:** Users who need to calibrate their own safety margins.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Voice-only interfaces or extremely low-resolution displays (e.g., smartwatches) where graphical plots are impossible.
*   **Reason:** Text is better than *no* uncertainty information, but it is the least effective of the uncertainty modalities tested [@fernandes_uncertainty_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Moving from text to graphics requires more screen pixels.
*   **The Risk:** Providing a full distribution (via graphics) requires the user to interpret more data points than a single number.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Changing the percentage (e.g., switching from 85% to 99%).
*   **Why it fails:** The study showed that decision quality fluctuates unpredictably based on the specific interval chosen. There is no single "correct" text interval that works for all risk profiles [@fernandes_uncertainty_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the uncertainty conveyed purely by a sentence or a number range (e.g., "5 - 9 min")?
*   **The Test:** Ask, "If the cost of being late doubles, does this display give me enough information to change my departure time intelligently?" If the display is just a static interval, the answer is likely no.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Accompany the text with a simple sparkline or probability density icon.
*   **Best Fix:** Replace the text summary with a **quantile dotplot** or **CDF** to expose the full probability distribution [@fernandes_uncertainty_2018].
