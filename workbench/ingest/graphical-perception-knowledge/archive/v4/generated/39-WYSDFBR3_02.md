---
id: use-nameable-colors-for-hue-recall
title: "Use colormaps with distinct, nameable colors for hue recall tasks"

tags:
  - impact:cognitive
  - visual:color
  - task:recall
  - chart:map
  - audience:general

sources:
  - type: research
    ref: Gołębiowska & Çöltekin, 2022
    url: https://doi.org/10.1109/TVCG.2020.3035823
    note: "In a hue recall task (T9), participants were significantly more accurate at remembering the color of a region when a rainbow colormap (RC) was used compared to a sequential colormap (SC). For one map type, accuracy was 67.7% with RC vs. 23.5% with SC."
  - type: research
    ref: Lenneberg, 1961
    url: https://doi.org/10.2466/pms.1961.12.3.375
    note: "Early research establishing the link between color naming and color recognition/memory, suggesting that colors that are easier to name are easier to remember."

examples:
  - type: bad
    description: A sequential colormap with subtle shades of orange is used. If a user is asked to remember the color of a specific state, it is difficult to distinguish 'light orange' from 'slightly lighter orange' in memory.
  - type: good
    description: A qualitative colormap with a few distinct, nameable colors (e.g., blue, green, orange, purple) is used. A user can more easily remember 'California was green' because 'green' is a simple, distinct verbal label. A rainbow map works similarly for this specific task.
---

## Guidance

If the primary goal is for a user to remember the specific *color category* of a location (a hue recall task), use a colormap with a small number of distinct, easily nameable hues (e.g., red, blue, green, yellow).

## Why

Human memory for color is strongly linked to language. We remember colors that we can easily name (e.g., "blue") much better than colors that require complex descriptions (e.g., "a slightly desaturated greenish-cyan"). A rainbow colormap, despite its many flaws, provides a set of simple, nameable color categories. Research shows this leads to significantly higher accuracy in tasks where a user views a map and is later asked to recall the color of a specific region. A sequential scheme with many subtle steps is poor for this task because the differences are not verbally encoded.

## When it applies

- The visualization is being used in a **learning or testing context** where memorization of color-location pairs is the explicit goal.
- The user's task is specifically to **recall the hue** (e.g., "What color was France?") rather than the value or rank ("Was France in the high or low range?").
- The underlying data is either categorical, or you are making a conscious decision to prioritize hue memory over the perception of quantitative order.

## Exceptions

- **Do not** use this for any task that requires understanding the order or magnitude of the data. For recalling the *value* of a location, a sequential colormap is more effective because its perceptual order provides a logical structure for memory.
- This is a highly specific optimization. For most analytical and communication purposes, conveying the data's structure accurately is more important than memorability of its specific colors.

## Trade-offs

- **Memory vs. Meaning:** You are optimizing for the user's ability to remember a color, but you are sacrificing their ability to understand what that color *means* in relation to other colors.
- **Recall vs. Accessibility:** The most distinct and nameable colors (primary hues) are often problematic for users with color vision deficiency. Optimizing for recall among one group may render the chart unusable for another.

## Signs of Trouble

- **Perfect Recall, No Comprehension:** A user can correctly state "That region was green" but has no idea if green represents a high, medium, or low value, or how it compares to a yellow region.
- **Value Recall Failure:** When asked to remember the *value range* of a location (not just its color), users perform poorly because the unordered colors provide no mnemonic anchor for magnitude.

## How to Improve

- **Quick Fix: Add Redundant Labels.** If using a rainbow-like scheme for recall, also add text labels or numbers to the regions. This allows users to memorize a verbal/numeric label instead of just a color, which is more robust.

- **Moderate Redesign: Use a Qualitative Palette.** If the data is truly categorical (not ordered), use a well-designed qualitative palette (e.g., from ColorBrewer) that provides distinct, nameable, and more accessible colors.

- **Comprehensive Redesign: Re-evaluate the Task.** If the goal is for users to learn and remember information about different regions, consider if color is the right channel. Perhaps it is better to use a simple map and present the key information in a supplementary table or text that the user can study. This separates the task of spatial location from the task of memorizing attributes.
