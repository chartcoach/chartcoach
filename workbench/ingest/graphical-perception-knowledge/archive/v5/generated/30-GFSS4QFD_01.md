---
id: account-for-shape-size-bias
title: "Account for perceived size differences when using various shapes"

tags:
  - impact:perceptual
  - impact:ethical
  - chart:scatter
  - chart:map.glyphs
  - task:compare
  - data:categorical
  - data:quantitative
  - visual:size
  - visual:shape

evidence:
  strength: medium
  summary: "A 2019 study found that mark shape systematically biases size perception in scatterplots. Shapes with more visual weight at their top or bottom (e.g., ▲, T) are perceived as significantly larger than shapes of the same geometric size (e.g., +, ★)."

sources:
  - type: research
    ref: Smart & Szafir, 2019
    url: https://doi.org/10.1145/3290605.3300899
    note: "Primary study that modeled the perceptual bias in size comparisons between 120 pairs of shapes, finding consistent and significant asymmetric effects."
    role: primary

tools:
  - type: implement
    name: "Perceptual Model (D3)"
    url: https://bit.ly/2prjuRu
    description: The paper's authors implemented their models as a D3.js extension to help normalize visual encodings based on perceptual biases.

examples:
  - type: bad
    description: "In this chart, shape encodes one category and size encodes a quantitative value. However, the 'T' shapes are perceived as inherently larger than the '+' shapes, which could mislead the viewer into thinking the 'T' category has higher values overall."
  - type: good
    description: "This chart avoids the issue by using only one shape (circles) and encoding the category with color instead. Now, size differences can be compared more accurately across all categories without interference from shape."
---

## Guidance

When using different shapes to encode categories, be aware that some shapes will be perceived as larger than others, even if they have the same pixel dimensions. Shapes with more visual density at their top or bottom edges (e.g., `T`, `▲`, `■`) appear larger than more open or centrally-weighted shapes (e.g., `+`, `★`, `Y`).

## Why

Our perception of an object's size is not a perfect reading of its geometric dimensions. It is influenced by the distribution of pixels, or its "visual mass." This creates an unintentional and potentially misleading visual hierarchy where some categories appear more prominent or to have greater value than others, simply due to the shape chosen to represent them. This effect is asymmetric: shape has a much stronger impact on perceived size than size has on perceived shape.

### Core Principle

Visual channels are not always perceptually separable. The geometric properties of a shape can interfere with the viewer's ability to accurately perceive its other visual properties, like size, leading to systematic biases.

## When it applies

-   In any multiclass visualization where different shapes represent different categories (e.g., scatterplots, maps with glyphs).
-   The bias is especially problematic if you *also* use size to encode a quantitative variable, as the shape-induced bias will directly conflict with the interpretation of the size-encoded data.

## Exceptions

-   When size is not used to encode any data and the potential for a false visual hierarchy is a low-risk or acceptable consequence (e.g., the shapes are purely decorative labels).
-   When you are using only a few shapes (e.g., 2-3) and can select a set that is known to have similar perceived sizes (e.g., a filled circle and a filled square).

## Trade-offs

-   Manually adjusting mark sizes to achieve perceptual balance is difficult and time-consuming without specialized tools.
-   Limiting your shape palette to only perceptually similar shapes restricts design freedom and the number of categories you can encode with shape.

## Signs of Trouble

-   **False Emphasis:** Certain categories in your legend or plot seem to "pop" or look more important than others, even for data points of equal value.
-   **Size Mismatch:** When you visually compare two marks from different shape categories that should be the same size, one consistently looks larger than the other.
-   **Misleading Patterns:** When size encodes a variable, one shape category appears to have systematically higher values than another, a pattern that disappears if you swap the shapes used for the categories.

## How to Improve

-   **Quick Fix: Use a Single Shape.** The simplest way to eliminate shape-induced size bias is to not use shape to encode categories. Use a single shape (e.g., circles) for all marks and use a different channel, like color, to distinguish categories.

-   **Moderate Approach: Choose Shapes Carefully.** If you must use multiple shapes, try to select a set with similar perceptual properties. Avoid mixing shapes from different families (e.g., filled, unfilled, and linear/open). For example, using a set of only filled shapes (`●`, `■`, `▲`) will likely have less perceptual size variance than mixing `▲`, `○`, and `+`.

-   **Comprehensive Approach: Perceptually Balance Sizes.** Actively counteract the bias by making the "perceptually larger" shapes (like `T` and `▲`) physically smaller, and "perceptually smaller" shapes (like `+` and `★`) physically larger, until they appear visually equal in size for a given data value. This requires perceptual models, such as those developed in the source research.
