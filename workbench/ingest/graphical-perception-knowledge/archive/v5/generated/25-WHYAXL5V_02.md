---
id: use-countable-features-for-ordered-shapes
title: "Encode ordered data with shapes by varying a countable feature"

tags:
  - impact:perceptual
  - impact:cognitive
  - chart:glyphs
  - chart:scatter
  - task:rank
  - task:find-extremum
  - data:quantitative
  - data:ordinal
  - visual:shape
  - access:cognitive-load-risk

evidence:
  strength: low
  summary: "A 2016 study found that, contrary to some theories, shape can encode ordered data if the shape variation is based on a countable feature (e.g., number of spikes on a star). This encoding was surprisingly accurate for finding extrema, but also the slowest to process."

sources:
  - type: research
    ref: "Chung et al., 2016"
    url: "https://doi.org/10.1111/cgf.12889"
    note: "The study tested a star-shaped glyph where the number of spikes represented an ordered value. In Experiment 1, it was perceived as more ordered than hue or orientation. In Experiment 2, it was the second-most accurate channel for finding extrema (after size), but also had the second-longest response time."
    role: primary
  - type: research
    ref: "Bertin, 1983. Semiology of Graphics."
    note: "Classic theory that categorizes 'shape' as a categorical (associative) visual variable, not an ordered one. This study provides a nuance to that rule."
    role: related

---
## Guidance
If you must use `shape` to encode ordered data, vary the shape along a single, easily countable dimension, such as the number of sides of a polygon or points on a star. Be aware that this increases cognitive load and interpretation time.

## Why
While shape is generally considered a categorical (unordered) visual variable, the human brain can perceive order if the variation is systematic and quantifiable. By changing the number of points on a star (e.g., 3, 4, 5, 6 points), you are implicitly encoding the data with a "count" channel, which is ordered. This allows for surprisingly accurate judgments but requires more conscious effort (counting) than pre-attentive channels like size or color value.

### Core Principle
A visual channel can be "forced" to be ordered if its variation is mapped to an ordered and countable geometric property. This combines a categorical channel (`shape`) with a quantitative one (`count`).

## When it applies
- When designing custom glyphs to represent multivariate data.
- In situations where more effective channels like position, size, and color are already used to encode other variables.
- When accuracy is more important than speed, and the number of distinct steps is relatively small.

## Exceptions
- Do not use a set of arbitrary, unrelated shapes (e.g., a circle, a square, a triangle, a cross) to represent ordered data. This provides no perceptual ordering. The shapes themselves must vary systematically.
- This method is not suitable for tasks requiring rapid interpretation, as the cognitive load of counting or differentiating complex shapes is high.

## Trade-offs
- **Accuracy for Speed:** Using countable shapes can be relatively accurate for magnitude comparison tasks, but it is one of the slowest methods, significantly increasing the time and mental effort required from the viewer.
- **Limited Steps:** The number of easily distinguishable shapes is low. It's hard to quickly tell the difference between a 10-sided and an 11-sided polygon, limiting the practical cardinality of the data.
- **Cognitive Load:** This method is cognitively demanding. Other channels like size or value are processed much more automatically.

## Signs of Trouble
- **Arbitrary Shapes:** The legend shows a collection of unrelated shapes (e.g., circle, star, square) mapped to a quantitative scale.
- **Slow Reading Time:** Users take a very long time to interpret the chart because they have to stop and carefully inspect or count features on each shape.
- **High Cognitive Load:** Viewers report that the chart is "tiring" or "hard to read."
- **Indistinguishable Shapes:** The shape variations are too subtle to be easily distinguished (e.g., comparing a 9-pointed star to a 10-pointed star).

## How to Improve
- **Quick Fix:** If using arbitrary shapes, switch to a more effective channel like `size` or `color value`.
- **Moderate Redesign:** If you must use shape, ensure the variation is simple and clear. For example, use regular polygons with a small number of sides (e.g., triangle, square, pentagon, hexagon). Add labels if necessary to aid interpretation.
- **Comprehensive Approach:** Re-evaluate if `shape` is the right channel for this data attribute. Typically, ordered data should be mapped to a more perceptually efficient channel (position, length, size, saturation). Reserve `shape` for purely categorical data where it excels.
