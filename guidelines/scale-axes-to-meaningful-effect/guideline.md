---
id: scale-axes-to-meaningful-effect
title: Scale Axes to Meaningful Effect Sizes
bibliography: references.bib
description: Determine the y-axis range based on practical significance, not just
  data range or dogmatic rules.
labels:
- chart:bar
- chart:line
- visual:scale
- impact:context
- task:communicate
---

## The Rule <!-- role: advice -->
Set your y-axis range based on the meaningful effect sizes of your specific domain, rather than automatically fitting the data or strictly adhering to a zero-baseline dogma.

## The Logic <!-- role: reason -->
Since all truncation exaggerates perception and no visual styling completely removes this bias, the "truthfulness" of a chart depends on whether the visual magnitude matches the practical importance of the change. The designer must take responsibility for defining what constitutes a "big" change.
*   **The Principle:** Proportionality of Intent. The visual impact should scale with the real-world impact.
*   **The Evidence:** [@correll_truncating_2020] concludes that there is no "domain-agnostic ground truth" for how severe an effect ought to look. Therefore, "designers must take into account the range and magnitude of effect sizes they wish to communicate."

## Where to Apply <!-- role: context -->
*   **User Goal:** Making decisions based on data variations (e.g., stock prices vs. global temperature).
*   **Data Type:** Data where small variations can have vastly different implications (e.g., a 1-degree body temperature rise is significant; a 1-degree oven temperature rise is not).
*   **Audience:** Users relying on the chart for actionable insight.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Exploratory Data Analysis (EDA).
*   **Reason:** When you don't yet know what effect sizes are meaningful, "zoom to fit" is a necessary default to see the shape of the data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires domain knowledge. You cannot automate this purely based on min/max values.
*   **The Risk:** If you misjudge what is "meaningful," you may inadvertently hide a crisis (by under-truncating) or create panic over noise (by over-truncating).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Always starting at zero (hiding real changes) or always zooming to fit (exaggerating noise).
*   **Why it fails:** Both extremes abdicate the designer's responsibility to match the visual signal to the data's context [@correll_truncating_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the graph look flat when the situation is urgent? Does the graph look spiked when the situation is stable?
*   **The Test:** Ask a domain expert: "Does this curve *feel* like the severity of the situation?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually set the axis range to encompass the "safe" or "expected" operating range of the metric, rather than just the data points.
*   **Best Fix:** Annotate the chart to explicitly state why the range was chosen (e.g., "Axis scaled to show critical deviation threshold").
