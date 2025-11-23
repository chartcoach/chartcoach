---
id: expect-truncation-bias-in-lines
title: Anticipate Exaggeration Across All Chart Types
bibliography: references.bib
description: Truncating the y-axis inflates perceived effect size in line charts just
  as severely as in bar charts.
labels:
- chart:line
- chart:bar
- visual:scale
- impact:bias
- audience:general
---

## The Rule <!-- role: advice -->
Do not assume that switching from a bar chart to a line chart mitigates the exaggerated perception of change caused by a truncated y-axis; expect both chart types to inflate perceived effect sizes equally.

## The Logic <!-- role: reason -->
While data visualization theory often distinguishes between bar charts (length encoding) and line charts (position encoding) regarding the permissibility of non-zero baselines, empirical evidence shows that human perception does not make this distinction regarding effect size.
*   **The Evidence:** In a series of experiments, [@correll_truncating_2020] found "no significant effect of visualization design on perceived effect size" when the axis was truncated. Whether the data was shown as bars or lines, cutting the axis consistently increased the subjectively perceived severity of the trend.

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating the magnitude of change or difference between values.
*   **Data Type:** Quantitative data where the variations are small relative to the absolute values (small dynamic range).
*   **Audience:** Any audience relying on the visual shape of the graph to make quick judgments about significance.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** None regarding the *anticipation* of bias.
*   **Reason:** While you may still choose to use a line chart for other reasons (e.g., continuity), you should never break this rule's core warning: do not believe the line chart protects the viewer from exaggeration.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use "chart type" as a defense against accusations of misleading data.
*   **The Risk:** By truncating a line chart axis, you are making the trend appear just as "threatening" or "severe" as a truncated bar chart, potentially overstating the practical significance of minor fluctuations.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Converting a truncated bar chart to a truncated line chart to make it "honest."
*   **Why it fails:** Although line charts do not require a zero baseline for *encoding* validity, the *perceived* exaggeration of the trend remains identical to the bar chart [@correll_truncating_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** A line chart where the y-axis does not start at zero.
*   **The Test:** Ask yourself: "If this were a bar chart, would I consider this zoom-level misleading?" If yes, the line chart is likely conveying the same exaggerated severity.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Set the y-axis to start at zero to ground the visual magnitude.
*   **Best Fix:** Evaluate the "meaningful effect size" of the domain. If the small change is truly critical, the truncation is justified by the analytic intent; if the change is trivial, expand the axis range to minimize the slope.
