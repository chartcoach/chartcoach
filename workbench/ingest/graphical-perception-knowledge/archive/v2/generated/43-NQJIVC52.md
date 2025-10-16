---
id: channel-ranks-are-contextual
title: "Recognize that visual channel rankings depend on task complexity"

impact:
  - perceptual
  - cognitive
  - logos
  - performance
tags:
  - visual-channel
  - ranking
  - task-complexity
  - working-memory
  - comparison
  - bar-chart
  - line-chart
  - heatmap
  - bubble-chart
  - position
  - length
  - area
  - angle

sources:
  - type: research
    ref: McColeman et al., 2022
    url: https://doi.org/10.1109/TVCG.2021.3114684
    note: "Challenges the classic ranking of visual channels, showing that task complexity and the number of data points fundamentally alter channel effectiveness."

examples:
  - type: bad
    description: "A designer chooses a bubble chart (area) over a bar chart (position) for a comparison of 8 products, arguing that area is a valid quantitative channel. While true, they fail to consider that as the number of items to compare increases, the cognitive load makes accurate area judgments extremely difficult compared to position judgments."
  - type: good
    description: "When showing a comparison of 2-3 key statistics, a designer uses a misaligned bar chart (length). When the comparison grows to 10 statistics, they switch to a standard bar chart (position on a common axis), correctly identifying that position is more robust to the increased cognitive load of remembering and comparing more items."
---

<!--
  FRONTMATTER GUIDE:

  id: Use a short, descriptive slug in lowercase-with-dashes format
      Example: "avoid-pie-charts" or "start-axis-at-zero"

  title: Write as an imperative command or clear instruction
         Examples: "Start bar chart axes at zero"
                  "Use position over color for quantitative comparisons"
                  "Avoid rainbow color schemes for ordered data"

  impact: Select all that apply from this list:
    - perceptual: How visual information is perceived/decoded (accuracy, speed, discriminability)
    - cognitive: Memory load, attention, mental effort, comprehension complexity
    - accessibility: Screen readers, colorblindness, motor/cognitive disabilities, assistive tech
    - inclusion: Cultural sensitivity, diverse audiences, avoiding bias, universal design
    - logos: Logic, clarity, data integrity, reasoning (appeal to rational understanding)
    - pathos: Emotional impact, engagement, storytelling (appeal to feelings and narrative)
    - ethos: Credibility, trust, professionalism, authority (appeal to trustworthiness)
    - ethical: Truthfulness, avoiding deception, transparency, fairness in representation
    - aesthetic: Visual appeal, style, design quality, brand consistency
    - performance: Rendering speed, file size, scalability, technical efficiency

  tags: Free-form keywords for categorization. Consider including:
    - Chart types: bar-chart, line-chart, scatterplot, pie-chart, heatmap, etc.
    - Tasks: comparison, correlation, distribution, composition, trend
    - Visual channels: color, position, size, shape, texture
    - Data types: categorical, quantitative, temporal, spatial
    - Audience: general-public, expert, colorblind-users
    - Domain-specific terms if relevant

  sources: List of references that support this guideline (optional - omit if none)
    Each source is an object with:
    - type: One of "research" (peer-reviewed), "standard" (WCAG, ISO), "practitioner" (style guides), "personal" (team rules)
    - ref: Short citation (e.g., "Cleveland & McGill, 1984" or "WCAG 2.1")
    - url: Full URL or DOI link (optional but preferred)
    - note: Additional context about what this source supports (optional)

    Examples:
      - type: research
        ref: Cleveland & McGill, 1984
        url: https://doi.org/10.2307/2288400
      - type: standard
        ref: WCAG 2.1 Success Criterion 1.4.3
        url: https://www.w3.org/TR/WCAG21/#contrast-minimum
      - type: practitioner
        ref: Financial Times Visual Vocabulary
        url: https://ft.com/vocabulary
      - type: personal
        ref: Internal design system v2.1
        note: Established Q2 2024

  tools: List of tools/resources to implement, validate, or learn about this guideline (optional - omit if none)
    Each tool is an object with:
    - type: One of "implement" (helps apply), "validate" (checks compliance), "learn" (educational)
    - name: Tool or resource name
    - url: Link to the tool/resource
    - description: Brief description of what it does

    Examples:
      - type: implement
        name: Colorgorical
        url: http://vrl.cs.brown.edu/color
        description: Generate categorical color palettes
      - type: validate
        name: Viz Palette
        url: https://projects.susielu.com/viz-palette
        description: Check color accessibility for colorblind users
      - type: learn
        name: Data Viz Color Guide
        url: https://blog.datawrapper.de/colors/
        description: Comprehensive guide to using color in data visualization

  examples: List of illustrative examples showing the guideline in action (optional - omit if none)
    Each example is an object with:
    - type: One of "good" (follows guideline) or "bad" (violates guideline)
    - description: What to notice or what makes this example relevant (required)
    - url: Link to image, interactive example, or article (optional)

    Note: URLs can point to:
      - Image files (.png, .jpg, .svg, etc.) - either local paths or external URLs
      - Interactive visualizations
      - Articles or blog posts discussing the example
      - Any web resource that illustrates the point

    Each example should have either:
      - Just a description (text-only reference)
      - description + url (with link to resource)

    Examples:
      - type: good
        description: FiveThirtyEight's 2020 election forecast uses position to show probabilities
        url: https://projects.fivethirtyeight.com/2020-election-forecast/
      - type: bad
        description: Pie chart with 12 slices makes comparison nearly impossible
        url: /examples/bad-pie-12-slices.png
      - type: good
        description: Chart uses colorblind-safe palette from Okabe-Ito color scheme
-->

## Guidance

Don't blindly follow a single, static ranking of visual channels (e.g., "position is always better than length"). The effectiveness of a channel changes dramatically based on the task's complexity, especially the number of data points your audience needs to compare.

## Why

Classic channel rankings are often based on simple tasks, like judging the ratio between only two marks. However, real-world visualizations often require comparing and remembering many values at once. Research shows that as the number of data points increases, our visual working memory becomes a bottleneck. This cognitive load can completely change which channel is most effective. The number of marks in a chart can have a greater impact on perceptual accuracy than the choice of visual channel itself.

## When it applies

- When a chart displays more than two or three values that need to be compared.
- When a task requires a user to remember values, even for a moment (e.g., to compare values that are not side-by-side).
- When designing for tasks beyond simple value lookup, such as understanding trends, distributions, or finding anomalies.

## Exceptions

- For very simple, direct perceptual tasks involving only two marks (e.g., "what is the ratio of bar A to bar B?"), the classic rankings (Position > Length > Angle > Area) are often a reliable starting point.

## Trade-offs

- **Clarity vs. Nuance:** A channel that is robust for many data points (like position in a bar chart) might hide certain perceptual biases. For example, using `angle` to encode just two values may lead to less overall bias than using a bar chart, but it becomes much less effective as more values are added.
- **Precision vs. Bias:** The most *precise* channel (most consistent responses) may not be the least *biased* (closest to the true value). For example, `area` can be surprisingly precise but is often more biased than other channels. You may need to decide which is more important for your goal.

## Evaluate

- [ ] The choice of visual channel is justified solely by a single, universal ranking without considering the number of items being compared.
- [ ] The chart requires users to remember and compare more than 4-5 values encoded with a channel that performs poorly under memory load (e.g., area, line position).

## Repair

1. **Reduce cognitive load first.** If possible, filter the data to show fewer items or break a complex chart into several simpler ones (like small multiples). This is often the most impactful fix.
2. **Choose a channel that is more robust to complexity.** If comparing many values is essential, use channels that perform better under memory load. For example, `position` on a common baseline (bar charts) is generally more robust than `area` (bubble charts) or `angle` when more than a few marks are involved.
3. **Re-evaluate your goal.** If the task is to compare two specific values, use a channel that is optimal for that simple comparison. If the task is to understand a distribution of many values, the channel choice will be different. Match the channel to the *specific* task and complexity.