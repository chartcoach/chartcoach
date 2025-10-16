---
id: use-perceptual-models-for-color-palettes
title: "Use perceptual models to generate custom categorical color palettes"

tags:
  - impact:perceptual
  - impact:aesthetic
  - impact:performance
  - visual:color
  - data:categorical

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "The paper introduces and validates Colorgorical, a tool based on perceptual models. Experiment 2 shows that its generated palettes are as discriminable and often more preferable than industry-standard, expert-made palettes."

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: The tool from the paper, which uses iterative sampling based on perceptual scores to generate custom palettes.
  - type: validate
    name: Viz Palette
    url: https://projects.susielu.com/viz-palette
    description: Test how a color palette looks on different chart types and check for colorblind safety.

examples:
  - type: good
    description: "Using Colorgorical to generate a 5-color palette for a dashboard, specifying a blue hue range to align with branding, while ensuring the tool generates four other colors that are still discriminable."
  - type: bad
    description: Manually picking five colors from a standard RGB color picker without considering their perceptual distance in a perceptually uniform color space like CIELAB.
  - type: bad
    description: "Forcing the use of a pre-made 5-color palette (e.g., from ColorBrewer) that clashes with brand guidelines or is not well-suited for the specific data being presented."
---

## Guidance

Instead of relying solely on pre-made palettes or manual color picking, use tools that leverage perceptual models to generate custom palettes. These tools can balance discriminability, aesthetic preference, and user-defined constraints like specific hue ranges.

## Why

Manually picking colors is difficult and often leads to ineffective results. Pre-made palettes (like ColorBrewer) are reliable but inflexible. The Colorgorical paper introduced and validated a model that operationalizes effective palette design by scoring colors based on Perceptual Distance (CIEDE2000), Name Difference, and Pair Preference. This allows for flexible, custom palettes that are grounded in perceptual principles. The study showed that palettes generated this way are as effective, and often more aesthetically preferable, than standard expert-designed palettes.

## When it applies

- When you need a categorical color palette that is both perceptually effective and tailored to specific needs.
- When you need to align with brand colors but also ensure data clarity.
- When you need a specific number of colors not offered by standard pre-made palettes.
- When you want to build upon an existing set of colors with new, compatible ones.

## Exceptions

- For quick, standard visualizations where an expert-designed palette like those from ColorBrewer or Viridis is sufficient and there are no branding or other constraints, using a pre-made palette is often faster and more straightforward.

## Trade-offs

- Generating a custom palette requires more initial effort and decision-making than simply picking a pre-made one. The user must actively decide on the relative importance of discriminability versus aesthetic preference for their specific project.

## Signs of Trouble

- **Palette Rigidity:** Your design system or team feels locked into using a few pre-made palettes, even when they don't fit the data or brand identity.
- **Manual Guesswork:** Designers spend significant time manually picking and tweaking colors, often with inconsistent or perceptually poor results.
- **Brand vs. Clarity Conflict:** A custom brand palette is applied directly to a chart, but it makes categories impossible to distinguish, forcing a choice between brand consistency and data clarity.

## How to Improve

- **Quick Fix: Test Your Existing Palette.** Before replacing it, run your current brand or custom palette through a colorblindness simulator and a tool like Viz Palette to identify specific pairs of colors that are too similar or problematic.

- **Moderate Approach: Augment an Existing Palette.** Use a tool like Colorgorical to "build on" your existing palette. Provide your core brand colors as a starting point and ask the tool to generate additional, discriminable colors that work well with them.

- **Comprehensive Approach: Integrate a Generative Tool into Your Workflow.** Adopt a tool like Colorgorical for creating all new categorical palettes. Set your desired constraints (e.g., hue filters for brand colors) and generate options based on your project's goals, explicitly balancing clarity and aesthetics.