---
id: use-tables-for-precise-lookup
title: "Use tables for precise value lookup"

tags:
  - impact:perceptual
  - impact:performance
  - chart:bar # Note: A table is technically not a chart, but it's compared with them.
  - task:lookup
  - data:quantitative
  - data:categorical
  - audience:general
  - medium:static

evidence:
  strength: medium
  summary: "In a crowdsourced study (n=180), Saket et al. (2019) found that for retrieving a specific value, tables were among the fastest and most accurate visualizations. Critically, tables were overwhelmingly preferred by users for this task, rated significantly higher than bar charts, pie charts, scatterplots, and line charts (p<0.05)."

sources:
  - type: research
    ref: Saket et al., 2019
    url: https://doi.org/10.1109/TVCG.2018.2829750
    note: "For 'Retrieve Value' tasks, tables were significantly faster than scatterplots and line charts and had high accuracy. User preference for tables was significantly higher than all other chart types (p<0.05, η²=0.73)."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This meta-analysis highlights that different charts support different tasks, and the findings from Saket et al. underscore the specific strength of tables for lookup tasks."
    role: supporting

---

## Guidance

When users need to find and report a precise, exact numerical value, use a table.

## Why

While graphical charts are excellent for showing patterns, trends, and comparisons, they often require the viewer to estimate values from positions, lengths, or angles. A table, by contrast, presents the exact numerical data directly. This eliminates estimation and reduces cognitive load when the task is simply to look up a specific value. Empirical research confirms that for this task, users not only perform well with tables but also strongly prefer them over graphical charts.

### Core Principle

Match the tool to the task's required precision. For tasks requiring pattern detection, use graphical charts. For tasks requiring exact value retrieval, use a table to present the data directly.

## When it applies

- The user's primary goal is to find a specific number (e.g., "What were the sales in Q3?").
- Exactness is more important than the overall pattern.
- As a supplement to a graphical chart, allowing users to see the high-level pattern and then look up the underlying precise numbers.

## Exceptions

- For very large datasets, a full table can be overwhelming. In this case, an interactive chart that reveals precise values on hover or click is a better solution.
- If the goal is to compare the lookup value to other values, a sorted bar chart might be more effective, as it provides both the value (via a label) and its relative rank.

## Trade-offs

- **Pattern Obscurity:** Tables are very poor at revealing trends, clusters, or correlations. A user looking at a table of numbers will have great difficulty seeing the "shape" of the data.
- **Scalability:** Large tables become dense and difficult to scan, increasing the time it takes to find a specific row.

## Signs of Trouble

- **Graph Labels Overload:** Your chart is covered in so many data labels that it becomes unreadable. This is a sign that your users' primary need is lookup, and a table might be more appropriate.
- **User Complaints:** Users say "I can't see the exact number" or "I have to guess" when looking at a bar or line chart.
- **Redundant Questions:** After showing a graphical chart, you are frequently asked, "But what's the actual number for...?"

## How to Improve

- **Quick Fix: Add a Table as an Appendix.** Keep your primary visualization for showing the pattern, but include a small table below or nearby with the source data. This provides the best of both worlds.

- **Moderate Approach: Use an Interactive Table.** If the medium allows, use an interactive table that supports sorting and filtering. This empowers users to quickly find the values they care about, even in a larger dataset.

- **Comprehensive Approach: Integrate Lookup into a Chart.** In an interactive context, use a graphical chart (like a bar or line chart) as the primary view, but provide lookup-on-demand. For example, show the exact value in a tooltip when the user hovers over a data point. This balances a clean visual with access to precision when needed.