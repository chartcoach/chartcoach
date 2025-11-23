---
id: restrict-math-operations-by-scale
title: Restrict Mathematical Operations by Data Scale
bibliography: references.bib
description: Ensure analysis and visualization techniques align with the permissible
  logical operations for nominal, ordinal, interval, and ratio data.
labels:
- data:nominal
- data:ordinal
- data:quantitative
- task:analysis
- impact:accuracy
---

## The Rule <!-- role: advice -->
Do not apply advanced mathematical operations (like averaging or subtraction) to data scales that do not support them. Limit nominal data to equality checks, and limit ordinal data to ranking and equality.

## The Logic <!-- role: reason -->
Data variables have specific scales that dictate valid logical mathematical operations. Applying invalid operations leads to meaningless results (e.g., the "average" of a Zip Code).
*   **The Principle:** Stevens' Theory of Scales of Measurement.
*   **The Evidence:** According to the DVL-FW typology in [@borner_data_2019], nominal data only supports equality (`=`, `≠`). Ordinal data supports ranking (`<`, `>`) and median calculation but not arithmetic mean. Only interval and ratio data possess the properties required for addition, subtraction, and geometric means.

## Where to Apply <!-- role: context -->
This advice applies during the "Analyze" and "Visualize" steps of the framework.
*   **User Goal:** Summarizing or aggregating data.
*   **Data Type:** Any dataset containing mixed types (qualitative and quantitative).
*   **Audience:** Stakeholders requiring accurate statistical representation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Transforming scales for specific encoding needs.
*   **Reason:** As noted in [@borner_data_2019], quantitative data can be converted into qualitative data (e.g., using thresholds to convert interval data into ordinal bins), or ordinal rankings can be converted to yes/no categorical decisions for decision making.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use single summary statistics (like "Mean") for every column in a dataset.
*   **The Risk:** Attempting to force ordinal data into ratio-based visualizations (like bar charts implying precise differences) may misrepresent the distance between values, which is not equal in ordinal scales [@borner_data_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Calculating the arithmetic mean of ordinal data (e.g., Likert scales) or nominal codes.
*   **Why it fails:** Ordinal data assumes ranking but not measurable intervals; the distance between "Agree" and "Strongly Agree" is not mathematically defined or consistent [@borner_data_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** A bar chart or summary statistic showing decimal precision for categorical inputs (e.g., "Average Department ID is 4.5").
*   **The Test:** Check the data type against Figure 1 in [@borner_data_2019]. If the data is Nominal/Ordinal, ensure no `+`, `-`, `x`, or `÷` operations were used to derive the visual.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the aggregation method: Use "Mode" for nominal data and "Median" for ordinal data.
*   **Best Fix:** Re-classify the data variable in your analysis workflow to ensure the visualization tool respects the limits of the scale (e.g., treating Zip Codes as strings, not numbers).
