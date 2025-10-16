---
id: use-ordered-shape-cautiously
title: "Use Ordered Shape Encodings Cautiously Due to High Cognitive Load"
tags:
  - impact:cognitive
  - impact:perceptual
  - task:rank
  - task:find-extremum
  - data:quantitative
  - data:ordinal
  - visual:shape
  - access:cognitive-load-risk
  - chart:glyphs
  - chart:scatter
evidence:
  strength: medium
  summary: "Chung et al. (2016) found that while an ordered shape encoding (varying the number of spikes) was perceived as orderable, it was the slowest channel for judging order (Exp 1, n=110) and one of the slowest for finding min/max values (Exp 2, n=87), indicating high cognitive load."
sources:
  - type: research
    ref: Chung et al., 2016
    url: https://doi.org/10.1111/cgf.12889
    note: "The study showed that response times for shape were significantly higher than for value, size, or texture in both experiments. For example, in Experiment 1, shape was ~2.5 seconds slower on average than value. This suggests a 'counting' process that is cognitively expensive."
    role: primary
examples:
  - type: bad
    description: "Using a sequence of star shapes with an increasing number of points (e.g., 3 to 10) to show order. While technically ordered, a viewer must mentally count the points on each shape to determine its rank, which is slow and effortful."
---

## Guidance

Avoid using a sequence of varying **shapes** (e.g., triangle, square, pentagon) to encode a primary ordered variable, as it is slow for users to interpret.

## Why

While shapes can be designed to be ordered (e.g., by increasing the number of sides or points), decoding this information requires a slow, deliberate cognitive process, often involving mental counting. This makes tasks like ranking or finding extremes significantly slower compared to using more efficient channels like value (lightness) or size. You are essentially forcing the viewer to do extra mental work that another encoding could have done for them automatically.

### Core Principle

Minimize the cognitive work required to decode a visualization. Visual channels that can be processed quickly and pre-attentively are preferable to those that require slow, conscious effort.

## When it applies

This applies when you are considering using a set of systematically varying shapes to encode quantitative or ordinal data, and the speed of interpretation is a concern.

## Exceptions

- **Very Low Cardinality:** If the number of distinct steps is very small (e.g., 2 or 3 distinct shapes) and the task does not require speed, it may be acceptable.
- **Redundant Encoding:** It can be used as a secondary, redundant encoding to reinforce a faster primary channel (e.g., using both size and shape to encode a value). This can improve discriminability without relying on shape as the sole indicator of order.
- **Categorical Data:** Shape's primary strength is encoding unordered, categorical data, where it is highly effective. This guideline applies only to using it for *ordered* data.

## Trade-offs

Using an ordered shape sequence might be a novel or engaging way to encode data. However, this novelty comes at the direct cost of interpretation speed and efficiency.

## Signs of Trouble

- **Slow Reading Time:** Users report that the chart is "hard to read" or takes a long time to understand.
- **"I have to count":** User feedback includes comments like "I had to stop and count the points on the stars" to understand the values.
- **High Abandonment Rates:** In an analytics context, users may avoid interacting with a chart that requires too much mental effort.

## How to Improve

- **Quick Fix:** If you must use ordered shapes, drastically reduce the number of distinct shapes in the sequence to the absolute minimum required (e.g., three or fewer).
- **Moderate Redesign:** Demote the shape encoding to a secondary role. Use a more efficient channel like `size` or `value` as the primary indicator of order, and use the ordered shapes to redundantly reinforce that message.
- **Comprehensive Redesign:** Replace the ordered shape encoding entirely with a more perceptually efficient channel like `size`, `value` (lightness), or `position`. Reserve `shape` for its primary strength: encoding unordered, categorical data where each shape represents a distinct category.