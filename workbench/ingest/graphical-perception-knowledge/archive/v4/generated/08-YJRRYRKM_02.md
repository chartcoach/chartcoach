---
id: index-data-for-performance-comparison
title: "Index time-series data to a common baseline to compare performance"

tags:
  - impact:perceptual
  - impact:ethical
  - impact:performance
  - chart:line
  - task:compare
  - task:rank
  - task:trend
  - data:temporal
  - data:quantitative

sources:
  - type: research
    ref: "Aigner et al., 2011"
    url: "https://doi.org/10.1111/j.1467-8659.2010.01845.x"
    note: "The study found that indexing led to significantly higher task correctness (fewer errors) for trend and percentage comparison tasks compared to both linear-juxtaposed and log-superimposed plots. It was also subjectively preferred by participants."

examples:
  - type: bad
    description: "Plotting two stock prices on a linear scale makes it hard to compare their performance. The higher-priced stock (MSFT) dominates the chart, while the lower-priced stock's (AAPL) volatility is hard to see. It's unclear which had better percentage growth."
    url: /images/index-data-linear.png
  - type: good
    description: "By indexing both stocks to 100 on the start date, the chart now clearly shows percentage change. It's immediately obvious that AAPL (blue) had far greater percentage growth over the period, a fact hidden in the original chart."
    url: /images/index-data-indexed.png
---

## Guidance

To compare the relative performance of multiple time series over a period, normalize them by indexing to a common baseline. This typically involves setting the value of all series to 100 on the start date and plotting subsequent values as a percentage of that start.

## Why

Indexing transforms absolute values into a single, intuitive scale: percentage change from a starting point. This removes the misleading visual effects of different starting values, allowing for a fair "apples-to-apples" comparison of growth or decline. Studies show this method significantly reduces errors in comparison tasks because it directly visualizes relative performance.

## When it applies

- When the goal is to answer questions like, "Which of these investments performed best since the beginning of the year?" or "How has our user growth compared to competitors since our launch?"
- When comparing time series that have very different absolute value ranges (e.g., a stock priced at $10 vs. one priced at $500).

## Exceptions

- When the absolute values or the magnitude of difference between the series are important to show. Indexing completely hides this information.
- When there is no meaningful or logical starting point to use as a common baseline for all series.
- When the chosen start date is an unrepresentative outlier (e.g., a market crash), which could distort the entire narrative.

## Trade-offs

- **Clarity vs. Magnitude:** Indexing provides excellent clarity for relative performance but completely obscures the original absolute values. A stock that grew 100% from $1 to $2 will look identical to a stock that grew 100% from $500 to $1000.
- **Framing:** The choice of the index date is a critical analytical decision that can dramatically change the story the chart tells.

## Signs of Trouble

- **Scale Dominance:** On a non-indexed line chart, the series with the highest absolute value appears to be the "biggest" or "most important," even if it had the lowest percentage growth.
- **False Conclusions:** A viewer mistakenly concludes that the line with the highest absolute value is the "best performer," when another series actually had a higher percentage return.
- **Dual-Axis Deception:** The chart uses two different y-axes to force two differently-scaled lines to overlap, creating arbitrary and misleading intersection points. This is a common but highly deceptive practice that indexing solves.

## How to Improve

- **Quick Fix:** If you cannot re-calculate the data, switch to a log scale. This acts as a rough proxy for comparing relative change, though it is less intuitive than a properly indexed chart.

- **Moderate Improvement:** In your data preparation step, create a new "indexed" column for each time series. Choose a start date, and for each series, divide every subsequent value by the value on that start date and multiply by 100. Plot these new indexed values instead of the original ones.

- **Comprehensive Approach:** Create an interactive chart where the user can dynamically select the index date. This adds a powerful layer of analysis, makes the chart's framing more transparent, and allows for richer exploration. Always clearly label the y-axis (e.g., "Indexed Value, Jan 1, 2024 = 100") to ensure correct interpretation.
