---
id: annotate-trends-with-outliers
title: "Explicitly annotate trends when outlier impact is critical"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:logos
  - impact:ethical
  - chart:scatter
  - chart:line
  - task:trend
  - task:correlation
  - data:quantitative
  - visual:position
  - audience:general
  - medium:static
  - medium:interactive

evidence:
  strength: medium
  summary: "Correll & Heer (2017, n=48) found that viewers' 'regression by eye' is robust to outliers, meaning they naturally down-weight them. Their visual estimates were significantly closer to a robust trend line (ignoring outliers) than to a standard Ordinary Least Squares (OLS) trend line, which is sensitive to outliers (p < 0.001)."

sources:
  - type: research
    ref: Correll & Heer, 2017
    url: https://doi.org/10.1145/3025453.3025922
    note: "Experiment 3 (n=48) showed that human visual trend estimation is less sensitive to outliers than OLS regression. As the number of outliers increased, the gap between the viewer's estimate and the OLS line grew significantly, while the gap to the robust line remained small."
    role: primary
  - type: research
    ref: Zeng & Battle, 2023
    url: https://doi.org/10.1145/3544548.3581349
    note: "This review synthesizes perception research, highlighting the importance of understanding how human perception can diverge from formal statistical models, as demonstrated in the Correll & Heer (2017) study on outliers."
    role: related

examples:
  - type: bad
    description: "A scatter plot of house prices vs. square footage includes a few multi-million dollar mansions (outliers). No trend line is shown. An analyst, using a standard OLS regression, concludes there's a steep trend, but a general viewer, visually ignoring the mansions, perceives a much flatter trend, leading to a disconnect."
  - type: good
    description: "The same scatter plot explicitly shows the OLS regression line, with an annotation that reads 'Trend including all properties.' This forces the viewer to see the statistical impact of the outliers, even if their intuition would otherwise ignore them."
---

## Guidance

When visualizing data with extreme outliers, explicitly draw the intended statistical trend line if you want the audience to understand the outliers' full impact.

## Why

Humans are natural "robust" estimators. When performing "regression by eye," people intuitively down-weight or ignore extreme outliers, estimating a trend that reflects the main cluster of data. This visual estimation can diverge significantly from formal statistical models like Ordinary Least Squares (OLS) regression, which are highly sensitive to outliers. If the goal is to communicate the result of such a model, you cannot rely on the viewer's unaided perception; you must show them the line.

### Core Principle

Visual intuition often prioritizes the central tendency of the majority, differing from formal statistical models that may give disproportionate weight to extreme values. Do not assume viewers "see" the same trend that your software calculates.

## When it applies

- In any bivariate visualization (like a scatter plot or line chart) containing one or more extreme outliers.
- When the analytical conclusion or story you are telling is based on a formal statistical model (like OLS) that is influenced by those outliers.
- When there is a risk of miscommunication if the audience and the analyst perceive two different trends from the same data.

## Exceptions

- When the goal is specifically to leverage the audience's robust visual estimation to find a trend that *ignores* the outliers. In this exploratory context, *not* showing the calculated trend line allows the viewer's natural perception to function as a robust filter.
- When the data has been pre-filtered to remove outliers, or a robust regression model (that also down-weights outliers) is being used and visualized.

## Trade-offs

- **Flexibility vs. Specificity:** Relying on "regression by eye" is flexible but less precise and can lead to interpretations that don't match formal analysis. Adding an explicit trend line is precise but anchors the viewer to one specific statistical model, potentially hiding other valid interpretations.
- **Simplicity vs. Completeness:** An unannotated chart is cleaner but may be misleading. Adding trend lines and explanations adds visual complexity but increases clarity and honesty about the data's properties.

## Signs of Trouble

- **Divergent Models:** Does the trend line you would intuitively draw by hand look very different from the one calculated by your software's default regression tool? This is a huge red flag.
- **Analyst-Audience Disconnect:** In presentations, do stakeholders consistently question your trend analysis, saying "it doesn't look like that to me"? This suggests their visual estimation is diverging from your formal model.
- **The "Weird Points":** If your first reaction to seeing the data is "what are those weird points way over there?", it's a sign you have outliers that will likely cause this perceptual divergence.

## How to Improve

- **Quick Fix: Acknowledge the Outliers.** Add a simple text annotation pointing to the outliers and explaining their potential effect. For example: "Note: These three high-value points pull the overall trend upwards."

- **Moderate Approach: Show the Formal Trend Line.** Overlay the calculated OLS trend line on the chart. Label it clearly (e.g., "OLS Trend") so viewers know it's a formal model that includes the influence of all data points.

- **Comprehensive Approach: Show Both Trends.** For maximum clarity, visualize two trend lines: 1) a "robust" trend that ignores outliers, and 2) the "standard" OLS trend that includes them. Use distinct styles (e.g., solid vs. dashed) and clear labels. Add an annotation explaining *why* they differ, educating the viewer about the outliers' impact.
