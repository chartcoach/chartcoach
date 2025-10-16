---
id: broken-axis-glyphs-dont-mitigate-exaggeration
title: "Don't Rely on Broken Axis Glyphs to Mitigate Perceptual Exaggeration"
tags:
  - impact:perceptual
  - impact:ethical
  - chart:bar
  - task:compare
  - task:trend
  - data:quantitative
  - visual:shape
  - audience:general
  - medium:static
evidence:
  strength: medium
  summary: "In a crowd-sourced experiment (n=32), Correll et al. (2020) found no significant difference in the perceived severity of trends between standard truncated bar charts and truncated bar charts with explicit 'broken axis' visual cues. The perceptual exaggeration caused by truncation persisted despite the visual warning."
sources:
  - type: research
    ref: Correll, Bertini, & Franconeri, 2020
    url: https://doi.org/10.1145/3313831.3376222
    note: "Experiment 2 (n=32) directly tested standard truncated bar charts against variants with broken axes and gradient fills, finding 'no significant difference between perceived severity among visualization designs' (p=0.05, but post-hoc tests were not significant)."
    role: primary
examples:
  - type: bad
    description: "A chart uses a small wavy line on the y-axis to indicate a break, but the bars are still dramatically different in height, leading the viewer to overestimate the difference between them. The designer assumes the glyph has 'fixed' the problem."
---
## Guidance

Do not assume that adding a "broken axis" symbol (like a wavy line, gap, or gradient) will prevent viewers from perceiving the exaggerated effect size of a truncated y-axis.

## Why

The perceptual bias from a truncated axis is powerful and stems from the direct visual magnification of the data marks (e.g., the bars' heights). A small, symbolic glyph is not strong enough to override this dominant visual effect. Viewers' judgments of severity appear to be driven by the magnified visual differences, even when they are made aware of the truncation.

### Core Principle

Strong, direct perceptual effects (like relative size and position) tend to dominate weaker, symbolic cues (like a break glyph).

## When it applies

- When you have truncated the y-axis of a bar chart (or other chart using length/position) and are considering adding a visual indicator to signal the break.
- When evaluating a chart that uses a broken axis glyph.

## Exceptions

- While a broken axis glyph does not fix the perceptual bias, it can still serve as an important signal of transparency and an ethical disclosure that the axis does not start at zero. Use it for disclosure, not as a perceptual fix.

## Trade-offs

- Adding the glyph takes minimal effort and signals transparency, but it can create a false sense of security that you have "fixed" the potential for misinterpretation. The primary trade-off is mistaking a symbolic disclosure for a perceptual solution.

## Signs of Trouble

- **False Security:** You've used a broken axis glyph and assume the chart is now "honest" or that the exaggeration effect has been neutralized.
- **Unchanged Perception:** Despite the glyph, users still describe the changes in the data using strong, dramatic language that reflects the visual exaggeration.

## How to Improve

- **Quick approach:** Keep the glyph for transparency, but add a clear annotation in the title or caption explaining the truncation and its purpose, e.g., "Note: Y-axis starts at $50M to show monthly variation."
- **Moderate approach:** Instead of just a glyph, choose a design that makes the context more explicit. For example, a "panel chart" (as in the paper's Fig 4e) shows both the truncated view and a full-range view in a separate panel.
- **Comprehensive approach:** Re-evaluate if a single static, truncated chart is the right choice. Consider an interactive chart that allows users to toggle between a zero-baseline and a truncated view, giving them full control and context.
