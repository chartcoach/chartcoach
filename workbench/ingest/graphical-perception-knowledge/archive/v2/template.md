---
id: short-slug
title: "Imperative, directional instruction"

impact:
  - perceptual
  - cognitive
  - accessibility
  - inclusion
  - logos
  - pathos
  - ethos
  - ethical
  - aesthetic
  - performance
tags:
  - keyword
  - chart-type
  - task
  - audience
  - domain

sources:
  - type: research
    ref: Cleveland & McGill, 1984
    url: https://doi.org/10.2307/2288400
    note: "Optional note about what this source specifically supports"
  - type: standard
    ref: WCAG 2.1
    url: https://www.w3.org/TR/WCAG21/
  - type: practitioner
    ref: DataViz Society Best Practices
    url: https://www.datavizsociety.org/best-practices
  - type: personal
    ref: Team colorblind-safe palette preference
    note: Adopted by design team in 2023 for all internal dashboards

tools:
  - type: implement
    name: Tool Name
    url: https://example.com
    description: Brief description of what it does
  - type: validate
    name: Tool Name
    url: https://example.com
    description: Brief description of what it checks
  - type: learn
    name: Resource Name
    url: https://example.com
    description: Brief description of what it teaches

examples:
  - type: good
    description: Brief description of what makes this a good example
    url: https://example.com/chart-or-image.png
  - type: bad
    description: Brief description of what's wrong and why it's problematic
    url: https://example.com/chart-or-image.png
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

<!--
  The core actionable rule or recommendation.
  This should be a clear, imperative statement of what to do or avoid.
  Examples: "Use position rather than color for quantitative comparisons"
           "Avoid truncating the y-axis for bar charts showing magnitude"
           "Sort categorical data by value when order is not meaningful"
-->

A rule, preference, or suggestion—describe the recommended action, best practice, or stylistic preference.

## Why

<!--
  The reasoning, evidence, or intent behind the guidance.
  Explain WHY this guidance matters. This can reference:
  - Perceptual principles (how humans perceive visual information)
  - Cognitive limitations (working memory, attention)
  - Task performance (accuracy, speed of interpretation)
  - Accessibility concerns (colorblindness, screen readers)
  - Communication goals (clarity, persuasion)
  Keep it concise but substantive—2-4 sentences typically.
-->

Short explanation of reasoning, evidence, or intent. Can be perceptual, rhetorical, practical, or personal.

## When it applies

<!--
  Contexts, cues, or situations where this guidance is relevant.
  List specific, observable conditions that indicate this guideline applies.
  Be concrete: mention chart types, data characteristics, tasks, or audience needs.
  Examples: "When comparing quantitative values across categories"
           "For time series with multiple overlapping lines"
           "When the audience includes colorblind users"
-->

- Observable cues, chart types, data, audience, or context where this is relevant.

## Exceptions

<!--
  Legitimate reasons to bend or ignore the guidance.
  Not every guideline applies universally. List circumstances where:
  - Breaking the rule is acceptable or even preferable
  - Other constraints take priority (branding, space, audience)
  - The context makes the guidance irrelevant
  If there are no known exceptions, you can omit this section or state "None known."
-->

- Legitimate reasons to bend or ignore the guidance.

## Trade-offs

<!--
  What you might sacrifice or what conflicts may arise.
  Acknowledge costs or tensions when applying this guidance:
  - Visual properties you give up (e.g., aesthetics for clarity)
  - Other guidelines that might conflict
  - Practical constraints (time, tooling, flexibility)
  If there are no significant trade-offs, you can omit this section.
-->

- What you might sacrifice or what conflicts may arise.

## Evaluate

<!--
  How to recognize when the guidance is violated.
  Provide concrete, checkable signals that indicate the guideline is not being followed.
  Use checkbox format for clarity. Make checks specific and observable.
  Examples: "[ ] Y-axis starts at a value other than zero"
           "[ ] More than 7 colors used for categorical distinction"
           "[ ] Legend requires back-and-forth eye movement to decode"
-->

- [ ] Signal A: What to look for.
- [ ] Signal B: Another tangible cue.

## Repair

<!--
  Steps to fix or improve when the guidance is violated.
  Provide actionable steps in priority order:
  1. Quick wins with high impact
  2. More thorough improvements
  3. Alternative approaches if the guideline can't be fully satisfied
  Be specific about HOW to make the change, not just WHAT to change.
-->

1. Smallest fix with biggest impact.
2. Follow-up refinement.
3. Fallback/alternative.
