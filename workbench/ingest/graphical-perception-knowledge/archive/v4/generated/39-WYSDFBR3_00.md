---
id: avoid-rainbow-colormaps-for-ordered-data
title: "Avoid rainbow colormaps for encoding quantitative or sequential data"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:accessibility
  - impact:ethical
  - visual:color
  - data:quantitative
  - data:ordinal
  - task:rank
  - task:compare
  - task:distribution
  - task:trend
  - chart:map
  - chart:map.choropleth
  - chart:heatmap
  - access:color-vision-risk
  - access:cognitive-load-risk

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2022
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "Found that rainbow colors have no intuitive order, unlike sequential schemes which leverage a strong 'dark is more' bias. Sequential schemes outperformed rainbow schemes in tasks requiring ordering or pattern interpretation."
  - type: research
    ref: Borland & Taylor, 2007
    url: https://doi.org/10.1109/MCG.2007.323435
    note: "Classic paper arguing that rainbow colormaps are 'harmful' because they have an unordered perceptual sequence and non-uniform luminance, which can introduce artifacts and obscure data features."
  - type: research
    ref: Zeng & Battle, 2023
    url: https://arxiv.org/abs/2109.01271v3
    note: "Proposes a methodology for collating graphical perception knowledge, highlighting the need to synthesize findings from papers like Gołębiowska & Çöltekin into actionable guidelines for recommendation systems."

tools:
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/
    description: Provides a set of well-vetted sequential, diverging, and qualitative color schemes for cartography and data visualization.
  - type: implement
    name: Viridis color palettes
    url: https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html
    description: A family of perceptually-uniform, colorblind-safe color palettes (viridis, magma, plasma, cividis) designed to replace rainbow schemes.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Lets you create a color palette and immediately see how it would look on different chart types, including simulations for various forms of color vision deficiency.

examples:
  - type: bad
    caption: Elevation map with rainbow colormap
    description: This map uses a rainbow colormap, making it difficult to determine if yellow is higher or lower than green without constantly referring to the legend. The non-uniform changes in lightness create false boundaries and obscure the true shape of the terrain.
    url: https://www.datavis.ca/io/images/rainbow-elevation.png
  - type: good
    caption: Elevation map with sequential colormap
    description: The same elevation data is shown with a perceptually-uniform sequential colormap (light-to-dark). It is immediately clear that lighter colors are higher and darker colors are lower, allowing for intuitive interpretation of the terrain's features.
    url: https://www.datavis.ca/io/images/sequential-elevation.png
---

## Guidance

Use a sequential color scheme (e.g., from light to dark in a single hue) or a perceptually-uniform multi-hue scheme (e.g., Viridis) to represent ordered quantitative or sequential data. Avoid using a spectral rainbow colormap for this purpose.

## Why

Rainbow colormaps lack an intuitive perceptual order. Viewers cannot reliably determine whether one color represents a higher or lower value than its neighbor (e.g., is green more or less than yellow?). This forces constant, effortful back-and-forth lookups between the chart and the legend, increasing cognitive load and the risk of misinterpretation.

In contrast, sequential color schemes leverage a natural and widely understood perceptual convention: "darker is more" or "lighter is more." This allows for immediate, intuitive ranking and comparison of values. Research shows that for tasks involving ordering or interpreting general patterns, sequential schemes lead to higher accuracy and faster performance than rainbow schemes. Furthermore, rainbow colormaps are not colorblind-safe and can create misleading visual artifacts due to non-uniform changes in lightness.

## When it applies

- When encoding any **ordered data**, including quantitative (e.g., temperature, population) or ordinal (e.g., low, medium, high) values.
- When the viewer needs to perform tasks like **comparing** values, **ranking** regions, or identifying **trends** and **patterns** in the data.
- When creating visualizations for a general audience, as sequential schemes are more intuitive.
- When accessibility for users with color vision deficiency is a concern.

## Exceptions

- In the niche scenario where the *only* task is for a user to **recall the specific hue** of a location from memory, the distinct, nameable colors of a rainbow map can be more effective.
- For tasks that require **rapidly locating a specific value range** (a `filter` task), the high contrast between adjacent hues in a rainbow map can sometimes lead to faster performance, though it comes at a great cost to all other tasks. This is a risky trade-off that should be made with extreme caution.

## Trade-offs

- **Clarity vs. "Pop"**: You sacrifice the vibrant, high-contrast "pop" of a rainbow colormap for the much greater perceptual clarity, intuitive ordering, and accessibility of a sequential scheme.
- **Interpretability vs. Lookup Speed**: While a rainbow map may slightly speed up the specific task of *locating* a known color, it severely harms the ability to *interpret* the relationships between all colors. A sequential scheme prioritizes overall interpretability.

## Signs of Trouble

- **The "Green is More than Yellow?" Problem:** You cannot tell the order of two adjacent colors without checking the legend.
- **Forced Legend Checks:** Viewers must constantly refer to the legend to understand the data, indicating a lack of intuitive ordering.
- **False Boundaries:** The visualization appears to have sharp edges or bands that are not present in the underlying data. This is an artifact of the non-uniform perceptual steps in a rainbow scheme.
- **Colorblind Simulation Failure:** When viewed through a color vision deficiency simulator, multiple distinct colors collapse into one, making the chart unreadable.
- **Inconsistent Interpretation:** Different viewers draw different conclusions about the patterns and rankings in the data.

## How to Improve

- **Quick Fix: Switch to Grayscale.** The simplest sequential scheme is a grayscale ramp from white to black. This immediately provides a clear perceptual order, though it may be less visually engaging.

- **Moderate Redesign: Use a Single-Hue Sequential Scheme.** Use a tool like ColorBrewer to select a sequential palette that transitions from a light to a dark shade of a single hue (e.g., light blue to dark blue). This is a robust, intuitive, and often print-friendly solution.

- **Comprehensive Redesign: Adopt a Perceptually-Uniform Palette.** For complex data, switch to a multi-hue but perceptually-uniform and colorblind-safe palette like Viridis, Cividis, or Plasma. These palettes offer more visual distinctiveness than single-hue schemes while ensuring that perceptual distance corresponds to data distance, preventing the misleading artifacts common to rainbow schemes.