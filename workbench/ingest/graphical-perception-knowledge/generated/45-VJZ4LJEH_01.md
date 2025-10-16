---
id: use-multi-hue-for-continuous
title: "Consider perceptually uniform multi-hue colormaps for high-resolution continuous data"

tags:
  - impact:perceptual
  - chart:heatmap
  - chart:map.choropleth
  - data:quantitative
  - task:compare
  - task:lookup
  - visual:color

evidence:
  strength: medium
  summary: "Liu & Heer (2018) found that while single-hue colormaps are effective, they suffer from poor resolution for making fine-grained comparisons (low 'span'). Perceptually uniform multi-hue colormaps (e.g., viridis) provided better discrimination for these small value differences without sacrificing overall performance."

sources:
  - type: research
    ref: Liu & Heer, 2018
    url: https://doi.org/10.1145/3173574.3174172
    note: "Showed single-hue schemes had higher error rates for small data spans (e.g., span=15 on a 100-point scale), while multi-hue schemes like 'viridis' maintained low error across all spans. This suggests 'multi-hue colormaps can provide improved resolution'."
    role: primary

tools:
  - type: implement
    name: viridis
    url: https://bids.github.io/colormap/
    description: "A family of perceptually uniform colormaps that ramp in both hue and luminance, providing good resolution while being colorblind-safe."
  - type: implement
    name: ColorBrewer
    url: https://colorbrewer2.org/#type=sequential&scheme=BuPu&n=3
    description: "Provides pre-made single-hue and multi-hue sequential palettes, though not all are fully perceptually uniform."
---

## Guidance

For visualizing continuous quantitative data where fine-grained discrimination is important, consider using a perceptually uniform multi-hue colormap (e.g., Viridis, Plasma) over a single-hue sequential colormap.

## Why

Single-hue colormaps (e.g., light blue to dark blue) are perceptually ordered but can have insufficient resolution for discerning small differences in data values. This is because all the variation is packed into the luminance channel. By carefully designing a colormap that ramps in both luminance and hue, it's possible to create more perceptual "steps" across the range, making it easier for viewers to distinguish between similar but not identical values.

## When it applies

- When visualizing continuous scalar fields (e.g., heatmaps, geographic maps) where small local variations are meaningful.
- When the data range is large, and you need to ensure discriminability across the entire scale.
- When the number of discrete steps in a binned colormap is high (e.g., > 9 bins), making the differences between adjacent colors small.

## Exceptions

- When the number of distinct values or bins is small (e.g., 3-5), a single-hue colormap is often sufficient and may be more aesthetically subtle.
- When the primary task is to judge overall magnitude and not to resolve fine details. A simple single-hue ramp can be very intuitive for this purpose.

## Trade-offs

- **Simplicity vs. Resolution:** A single-hue colormap is arguably simpler and more immediately intuitive ("darker means more"). A multi-hue colormap offers higher perceptual resolution at the cost of this simplicity.
- **Design Effort:** Creating a *bad* multi-hue colormap is easy (see: rainbow colormaps). Using a *good* one requires relying on pre-vetted, perceptually uniform palettes like Viridis or Cividis.

## Signs of Trouble

- **Banding/Contouring:** A visualization using a single-hue scheme appears to have large patches of uniform color, even though the underlying data contains subtle gradients.
- **Indistinguishable Neighbors:** In a binned single-hue colormap, it's difficult to tell the difference between adjacent color steps, especially if there are many of them.
- **User Feedback:** Viewers report difficulty seeing the difference between two values that are numerically distinct.

## How to Improve

- **Quick Fix: Reduce Bins.** If using a binned single-hue scale, try reducing the number of bins (e.g., from 9 to 5). This will increase the perceptual distance between adjacent colors.
- **Moderate Approach: Switch to a Pre-vetted Multi-Hue Palette.** Replace the single-hue colormap with a perceptually uniform multi-hue sequential palette from a library like Viridis or ColorBrewer (e.g., 'YlGnBu').
- **Comprehensive Approach: Test and Choose.** If possible, test both a single-hue and a multi-hue palette with your specific data and a sample of your audience to see which one better supports the required interpretation tasks. For some data, the improved resolution of a multi-hue map will be critical; for others, the simplicity of a single-hue map will suffice.