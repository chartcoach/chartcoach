---
id: distinguish-perceived-order-from-actual-order
title: "Recognize that some visual channels can exaggerate or understate the perception of order"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:ethical
  - task:correlation
  - task:trend
  - task:rank
  - visual:size
  - visual:color
  - visual:texture
  - data:quantitative
  - data:ordinal

evidence:
  strength: medium
  summary: "A 2016 study found a significant divergence between the actual, measured order in a data sequence and the 'perceived orderedness' reported by viewers. Grayscale value and texture made sequences seem more ordered than they were, while size was a more faithful representation."

sources:
  - type: research
    ref: "Chung et al., 2016"
    url: "https://doi.org/10.1111/cgf.12889"
    note: "Experiment 1 asked 110 participants to rate the 'orderedness' of sequences. Results in Figure 5 show that for the same level of statistical disorder, sequences encoded with 'value' (grayscale) and 'texture' were consistently rated as more ordered, while 'hue' and 'orientation' were rated as less ordered. 'Size' tracked the actual disorder most closely."
    role: primary

---
## Guidance
Be aware that your choice of visual channel can influence how ordered or chaotic a dataset appears to the viewer. To give a more faithful impression of the data's underlying order, use **size**. To create a stronger perception of order and trends, use **value** (grayscale intensity) or **texture**.

## Why
Some visual channels are more "sensitive" to disorder than others. Channels like grayscale `value` and `texture` are so strongly perceived as ordered that viewers may see a pattern or trend even when significant disorder is present. Conversely, channels like `hue` are so perceptually chaotic that they can mask an underlying pattern. `Size` provides a more neutral, accurate visual representation of the statistical level of order or correlation in the data.

### Core Principle
The perceived properties of a visualization do not always map 1:1 to the statistical properties of the data. An effective and ethical designer must understand which visual channels might exaggerate or mask patterns and choose the channel that best aligns with the intended task and message.

## When it applies
- When visualizing data to assess its correlation, trend, or level of order.
- When choosing an encoding for a scatterplot or glyph map where you want to show the relationship between variables.
- When you are deciding whether to emphasize a trend (use `value`) or provide a more neutral view (use `size`).

## Exceptions
- If the primary goal is not to judge order but simply to look up individual values, this effect is less critical.
- When using `value` or `texture`, if the data is truly highly ordered, then the channel choice simply reinforces the existing pattern, which is not misleading. The risk comes from making noisy data look clean.

## Trade-offs
- **Emphasizing vs. Representing:** Using `value` or `texture` can make a weak trend more salient and easier to spot, but at the risk of misleading the viewer about the strength of the pattern.
- **Faithfulness vs. Salience:** Using `size` provides a more honest depiction of the data's messiness, but a subtle trend might be harder for a viewer to detect compared to when it's encoded with `value`.

## Signs of Trouble
- **False Confidence:** A chart using grayscale `value` shows what appears to be a very strong, clean trend, but the underlying data has a low correlation coefficient or high variance. The channel may be creating an illusion of order.
- **Missed Patterns:** A chart using color `hue` or `orientation` to encode a quantitative variable looks like a random mess, causing a viewer to conclude there is no pattern, even if a moderate trend exists in the data.
- **Inaccurate Takeaways:** Viewers consistently overestimate the strength of a correlation when it is encoded with `value` or `texture`.

## How to Improve
- **For Neutral Assessment:** If the goal is to let the viewer make an unbiased assessment of the data's order or correlation, encode the variable using `size`. This channel was found to most closely match the statistical reality.
- **To Emphasize a Trend:** If you have identified a meaningful trend and want to make it as clear as possible for the viewer, encoding it with `value` (grayscale) or `texture` can help make the pattern more perceptually salient. Be prepared to justify this choice and supplement with statistical information (e.g., an R² value).
- **Provide Both:** In an interactive context, you could allow the user to switch the encoding between `size` and `value` to get both a "faithful" and a "salient" view of the data, helping them understand the pattern from multiple perspectives.