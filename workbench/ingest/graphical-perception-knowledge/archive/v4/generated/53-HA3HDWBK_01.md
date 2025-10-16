---
id: standard-scatter-for-class-separation
title: "Use standard scatterplot designs for simple class separation tasks"
tags:
  - impact:perceptual
  - impact:performance
  - chart:scatter
  - task:cluster
  - data:quantitative
  - data:categorical
  - visual:color
  - visual:position
  - audience:general
sources:
  - type: research
    ref: "Micallef et al., 2017"
    url: "https://doi.org/10.1109/TVCG.2017.2674978"
    note: "Found no significant difference in accuracy for class separation tasks between default software (R, MATLAB) and a perceptually optimized design. This suggests standard designs are robust for this task."
---

## Guidance

For tasks involving the separation of pre-defined, colored classes in a scatterplot, standard designs from common software are often sufficient and perform comparably to more complex, optimized designs.

## Why

Experimental studies have found no significant difference in user accuracy when identifying classes between default scatterplots (like those in R or MATLAB) and perceptually optimized ones. While some minor speed differences may exist, the accuracy is robust across standard designs, suggesting that the additional effort of optimization provides diminishing returns for simple class separation tasks.

## When it applies

- When visualizing 2D data where points are colored by a known categorical label.
- When the primary task is to identify, locate, or get a general sense of the different groups.
- When the classes are reasonably well-separated and not heavily overlapping.

## Exceptions

- When classes are heavily overlapping or have complex, non-linear boundaries. In these cases, perceptual optimization techniques that specifically model and enhance class perceivability can be beneficial. Standard designs with full opacity may create a "color soup" that obscures the boundaries in dense, overplotted regions.

## Trade-offs

- Sticking with a standard design is faster to generate and requires no special tooling. However, it might not be optimal for datasets with significant overplotting and class overlap.
- Investing in an optimized design takes more effort but can improve the clarity and perceivability of class distributions in complex, dense cases.

## Signs of Trouble

- **Color Soup:** Colors from different classes mix together in dense regions, making it impossible to discern the composition of the cluster.
- **Lost Boundaries:** It is unclear where one class ends and another begins due to overplotting.
- **Dominant Class:** A large or dense class plotted last completely obscures a smaller class plotted underneath it.
- **Ambiguous Membership:** A viewer cannot tell which class a point in a dense region belongs to.

## How to Improve

- **Quick Fix: Adjust Marker Opacity.** Lowering the opacity of all markers is the single most effective way to address overplotting. It helps reveal the underlying structure and shows the relative densities and mixing of different colored classes.

- **Moderate Approach: Change Drawing Order.** If one class is more important or smaller than others, try drawing it on top (last). This is a manual tweak that can improve the visibility of a specific group, though it may obscure others.

- **Comprehensive Approach: Use Faceting or Small Multiples.** Instead of plotting all classes on one chart, create a separate, juxtaposed scatterplot for each class. This completely eliminates overlap issues and makes the distribution of each class perfectly clear, though it makes direct comparison of point positions across classes more difficult.