---
id: match-saliency-to-certainty
title: Scale Visual Saliency by Data Certainty
bibliography: references.bib
description: Use blur and density estimation to ensure uncertain data is less visually
  prominent than certain data.
labels:
- chart:scatter
- chart:parallel-coordinates
- visual:blur
- visual:texture
- impact:clarity
- data:uncertain
- task:identify
---

## The Rule <!-- role: advice -->
Represent multivariate data points using probability density functions (PDFs) rather than discrete glyphs. Use the data point's statistical uncertainty (e.g., standard deviation) to define the width of the splat or kernel. Ensure that uncertain values appear larger and blurrier, while certain values appear smaller, brighter, and sharper.

## The Logic <!-- role: reason -->
This technique leverages the human visual system's preattentive processing.
*   **The Principle:** Semantic Depth of Field.
*   **The Evidence:** [@feng_matching_2010] explains that the visual system preattentively separates high-contrast (sharp) features from low-contrast (blurred) ones. By mapping uncertainty to the spread of a distribution, highly uncertain data creates low-contrast "smudges" that recede into the background, while certain data creates high-contrast "peaks" that attract the eye. This prevents viewers from perceiving false clusters formed by unreliable data.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying reliable clusters, trends, or correlations while avoiding false positives caused by noisy data.
*   **Data Type:** Multivariate data where each sample has associated statistical uncertainty (e.g., mean and variance).
*   **Audience:** Analysts or domain experts (e.g., radiologists) who need to make decisions based only on trustworthy data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise reading of individual uncertain values is required.
*   **Reason:** Density plots blend individual data points together. If the user needs to read the specific coordinates of a single uncertain outlier, the blur may make the exact center difficult to pinpoint without additional augmentation [@feng_matching_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Individual data point recoverability. In dense regions, distributions merge into a single field, making it impossible to count specific points.
*   **The Risk:** Outliers with very high uncertainty (very large variance) may become so diffuse that they effectively vanish from the plot entirely.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using color (hue) to encode uncertainty magnitude.
*   **Why it fails:** [@feng_matching_2010] notes that color is not quantitative; it requires a legend to interpret, adds cognitive load, and can create perceived clusters based on color categories rather than data density.
*   **The Wrong Fix:** Using simple transparency (alpha) on discrete glyphs without spatial spreading.
*   **Why it fails:** This shows density but fails to visually suppress the spatial footprint of uncertain values.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do large clusters of uncertain data dominate the screen?
*   **The Test:** If you have a cluster of data points with high variance (uncertainty) and a cluster with low variance (certainty), the low-variance cluster should appear significantly brighter and sharper. The uncertain cluster should look like a diffuse fog.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Implement Kernel Density Estimation (KDE) where the kernel for each point is its own probability distribution function (e.g., a normal distribution scaled by its standard deviation). Sum these distributions to create the final image.
