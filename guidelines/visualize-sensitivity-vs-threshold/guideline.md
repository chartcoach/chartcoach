---
id: visualize-sensitivity-vs-threshold
title: Separate Scientific Sensitivity from Decision Thresholds
bibliography: references.bib
description: When visualizing binary decision aids, explicitly distinguish between
  the quality of the evidence (sensitivity) and the value judgments determining the
  action (threshold).
labels:
- chart:roc-curve
- task:decision-support
- impact:clarity
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->
When communicating evidence used for binary decisions (e.g., treat/don't treat, evacuate/stay), visualize the scientific discrimination ability ($d'$) separately from the decision threshold ($\beta$). Use Receiver Operating Characteristic (ROC) curves or similar displays to show the trade-off between hits and false alarms.

## The Logic <!-- role: reason -->
*   **The Principle:** Signal Detection Theory.
*   **The Evidence:** According to [@fischhoff_communicating_2014], decision-making involves two distinct parameters: how well experts can discriminate states of the world (sensitivity or $d'$) and the trade-offs made among possible outcomes (the decision rule or $\beta$). If these are conflated in a single recommendation, decision-makers cannot distinguish between weak science and a cautious decision policy.

## Where to Apply <!-- role: context -->
*   **User Goal:** Evaluating whether to act on a warning or diagnostic result (e.g., medical diagnoses, storm evacuations, financial sell signals).
*   **Data Type:** Binary classification data or probabilistic forecasts triggered by a threshold.
*   **Audience:** Decision-makers who must weigh the risks of false positives against false negatives.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience lacks the statistical literacy to interpret ROC curves or trade-off plots.
*   **Reason:** While accurate, the separation of $d'$ and $\beta$ requires abstract thinking. In these cases, simpler categorical advice may be necessary, though it risks obscuring the value judgments involved [@fischhoff_communicating_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. A simple "Do X" command is easier to process than a probability curve showing trade-offs.
*   **The Risk:** Decision-makers might distrust the science if a recommendation proves wrong (e.g., a "false alarm"), not realizing the error was due to a cautious safety threshold rather than bad data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** presenting only the final recommendation or a single accuracy metric.
*   **Why it fails:** It hides the "fiduciary responsibility" or value judgments inherent in setting the threshold (e.g., tolerating many false alarms to avoid missing a single catastrophe).

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the display only show the final decision (Yes/No)?
*   **The Test:** Can the user determine if a "missed" event was caused by poor data quality or a high threshold for action?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Annotate recommendations with the specific trade-off made (e.g., "We recommend evacuation to minimize loss of life, accepting a 20% chance this is a false alarm").
*   **Best Fix:** Provide an interactive ROC plot or trade-off table allowing the user to see how changing the decision threshold impacts the ratio of hits to false alarms.
