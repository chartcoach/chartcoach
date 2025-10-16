---
id: monotonicity-is-not-sufficient-for-order
title: "Verify perceptual order even with colormaps monotonic in a single channel"
tags:
  - impact:perceptual
  - impact:cognitive
  - task:rank
  - data:quantitative
  - data:ordinal
  - visual:color
  - visual:color.hue
  - visual:color.saturation
  - visual:color.luminance
evidence:
  strength: high
  summary: "Theoretical proof with counter-examples demonstrates that a colormap can be strictly monotonic in a single attribute (e.g., luminance) yet still lack intrinsic perceptual order due to non-monotonic changes in other channels."
sources:
  - type: research
    ref: "Bujack et al., 2018"
    url: "https://doi.org/10.1109/SciVis.2018.8823772"
    note: "Theorem 6 and Figure 1 explicitly provide counter-examples of colormaps that are monotonic in luminance, saturation, or hue, but which fail to be intrinsically ordered because of non-monotonicity in other channels."
    role: primary
tools:
  - type: validate
    name: "viscm"
    url: "https://github.com/matplotlib/viscm"
    description: "A tool for analyzing and creating colormaps. It lets you see the plots for luminance, hue, and chroma simultaneously, making it easy to spot non-monotonicity in any channel."
  - type: validate
    name: "Chroma.js Color Scale Corrector"
    url: "https://gka.github.io/chroma.js/#correct-lightness"
    description: "Can be used to analyze and correct the lightness profile of a color scale, but you should also visually inspect other properties."
examples:
  - type: bad
    description: "The 'purple' colormap in Figure 1 of Bujack et al. (2018) is monotonic in luminance but its saturation dips to zero in the middle. This creates a 'bow-tie' shape in the color space that breaks perceptual order at the center."
  - type: good
    description: "The Viridis colormap has a path through color space that is monotonic in luminance and nearly monotonic in its other perceptual dimensions, resulting in a robust sense of order."
---
## Guidance
Do not rely on monotonicity in a single color channel (e.g., luminance) as sufficient proof that a colormap is perceptually ordered. Always evaluate the colormap's behavior across all perceptual dimensions.

## Why
A colormap that is perfectly monotonic in luminance can simultaneously have a non-monotonic path in saturation (e.g., saturation starts high, dips to zero in the middle, and rises again). This "V" shape in another perceptual dimension can disrupt the overall sense of order, making values in the middle of the colormap hard to place correctly relative to the ends without a legend. Color perception is multi-dimensional, and a smooth progression in one dimension can be undermined by an abrupt change in another.

### Core Principle
A visual encoding is perceived holistically. To achieve robust perceptual order, the path through the multi-dimensional color space must be smooth and generally unidirectional, not just monotonic along a single projected axis.

## When it applies
- When designing or selecting custom colormaps for quantitative or ordinal data. This is a crucial check before deploying a newly created colormap.
- When evaluating a colormap that claims to be "perceptually ordered" based on only one property, like increasing brightness.

## Exceptions
- None. This is a fundamental limitation of relying on a single-channel check for a multi-dimensional perception.

## Trade-offs
- **Ease of Creation vs. Robustness:** It is much easier to design a colormap that is monotonic in only one channel than one that is well-behaved across all channels. This guideline requires more rigorous evaluation but prevents subtle and misleading visualizations.

## Signs of Trouble
- **Mid-point "Dip":** The colormap becomes gray or desaturated in the middle before becoming colorful again at the other end (violates monotonic saturation).
- **Hue "Bend":** A colormap that is monotonic in saturation (e.g., gray-to-blue) might have a hue that shifts towards purple and back, breaking order.
- **Luminance "Dip":** A colormap that is monotonic in hue might have a dip in lightness in the middle (like the standard rainbow colormap).

## How to Improve
- **Quick Fix: Use a Trusted Colormap.** Instead of creating or using an unverified colormap, switch to one known to be perceptually uniform, such as Viridis, Cividis, or a sequential scheme from ColorBrewer.
- **Comprehensive Approach: Analyze in Perceptual Space.** When designing a custom colormap, use tools like `viscm` to visualize its path through a 3D perceptual color space (like CIELAB). The path should be smooth and as straight as possible, without sharp turns or reversals in direction. Simultaneously inspect the plots for luminance, chroma (saturation), and hue to ensure all are reasonably monotonic.