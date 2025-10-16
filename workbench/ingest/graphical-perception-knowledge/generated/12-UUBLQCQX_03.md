---
id: avoid-dull-yellow-greens
title: "Avoid dull yellow-green colors in general-purpose palettes"

tags:
  - impact:aesthetic
  - impact:pathos
  - impact:ethos
  - visual:color
  - data:categorical
  - audience:general

evidence:
  strength: medium
  summary: "Based on cross-cultural studies of color preference (e.g., Palmer & Schloss, 2010), the dark, dull yellow-green region (e.g., olive, khaki) is one of the most disliked on average. Gramazio et al. (2017) explicitly identified and excluded this region (CIELAB H in [85°, 114°], L* in [35, 75]) from their palette generation tool to improve the typical aesthetic appeal and user reception."

sources:
  - type: research
    ref: Gramazio, Laidlaw, & Schloss, 2017
    url: https://doi.org/10.1109/TVCG.2016.2598918
    note: "The authors specifically filter this region to prevent their optimization algorithm from selecting these colors, noting 'the goal is to cater to the average observer' and improve 'typical aesthetic palette preference'."
    role: primary
  - type: research
    ref: Palmer & Schloss, 2010
    url: https://www.pnas.org/doi/10.1073/pnas.0906172107
    note: "This foundational paper on the 'ecological valence theory' of color preference identifies a strong, cross-culturally consistent dislike for colors associated with negative concepts, such as decaying matter (e.g., brownish/yellowish greens)."
    role: supporting
  - type: research
    ref: Taylor & Franklin, 2012
    url: https://doi.org/10.3758/s13423-011-0205-z
    note: "Further investigates the link between color-object associations and preference, reinforcing the findings of ecological valence theory."
    role: supporting

tools:
  - type: implement
    name: Colorgorical
    url: http://vrl.cs.brown.edu/color
    description: "This tool automatically filters out the 'dark yellowish-green region' by default to generate more aesthetically preferable palettes."

examples:
  - type: bad
    description: "A bar chart where one of the main categories is represented by a muddy, olive-green color. This may cause a negative emotional reaction in some viewers and make the chart less appealing."
  - type: good
    description: "When a green hue is needed, the palette uses a more vibrant, saturated green or a lighter, minty green, avoiding the disliked dull yellow-green range."
---

## Guidance

When designing color palettes for a general audience, avoid using colors from the dark, dull, yellow-green region (often described as "olive," "khaki," or "swampy" green).

## Why

Aesthetic appeal is not merely decorative; it influences viewer engagement, trust, and the overall emotional tone of a visualization. Research on color preference has shown that, on average and across cultures, people have a strong aversion to dull yellow-green colors. These colors are often associated with negative concepts like decay or sickness. Using them in your visualization can create an unintended negative impression and reduce the credibility and appeal of your work.

### Core Principle

The aesthetic and emotional impact of color choices can affect how an audience receives and trusts the information presented. Cater to the preferences of the average observer to maximize positive reception.

## When it applies

- When designing visualizations for a broad, general, or public audience.
- When the goal is to create a positive, trustworthy, or aesthetically pleasing impression.
- In any chart using categorical colors where you have the flexibility to choose your palette.

## Exceptions

- **Thematic Relevance:** If the data is specifically *about* something associated with this color (e.g., military uniforms, olives, swamp ecosystems), then using it is thematically appropriate and expected. The context removes the negative association.
- **Branding:** If these colors are part of a required brand palette, you may be forced to use them.
- **Expert Audience:** An expert audience may be less influenced by general aesthetic preferences and more focused on data, or they may have domain-specific conventions that use these colors.

## Trade-offs

- **Reduced Palette Options:** By excluding a region of the color space, you are slightly limiting the total number of available colors for your palette. However, this is rarely a practical issue given the vastness of the remaining color space.

## Signs of Trouble

- **"That's an ugly chart":** Viewers comment on the aesthetics of the chart in a negative way, often without being able to pinpoint why.
- **Muddy or Murky Feel:** The visualization feels drab, sickly, or unappealing. The colors may be technically discriminable but are emotionally off-putting.
- **User Feedback:** In testing, users describe a color as "weird," "gross," or "muddy."

## How to Improve

- **Quick Fix: Hue Shift.** If you have a color that falls into this range, keep its lightness and saturation the same but shift its hue. Move it towards a purer green (away from yellow) or a purer yellow/orange (away from green).

- **Moderate Approach: Select a New Palette.** If your palette relies on this color, it's best to select a new one. Use a tool that generates aesthetically pleasing palettes or choose a pre-made palette from a reputable source (like ColorBrewer's qualitative schemes) that avoids these colors.

- **Comprehensive Approach: Use a Preference-Aware Tool.** Use a tool like Colorgorical that is built on models of color preference. It automatically avoids these disliked regions, ensuring the palettes it generates are more likely to be well-received by an average viewer.