---
id: visualize-range-distribution
title: Visualize Attribute Range and Distribution
bibliography: references.bib
description: Show the span and shape of data values to establish context and normalcy.
labels:
- task:determine-range
- task:characterize-distribution
- visual:context
- impact:clarity
---

## The Rule <!-- role: advice -->
Explicitly visualize the span (range) and frequency (distribution) of attribute values to help users establish a baseline of "normalcy."

## The Logic <!-- role: reason -->
Determining the range of values allows users to judge the suitability of a dataset for their analysis. Characterizing the distribution allows users to understand "normalcy" in the data. Without understanding the distribution, users cannot effectively identify meaningful anomalies or outliers, as an outlier is defined by its deviation from the expected distribution [@amar_low-level_2005].

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing data quality, understanding general trends, or spotting outliers.
*   **Data Type:** Quantitative attributes (e.g., age, price, speed).
*   **Audience:** Users performing initial exploratory analysis or data validation.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is looking for a single specific value (Retrieve Value).
*   **Reason:** Range and distribution are context tasks; retrieval is a precision task.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate for histograms, box plots, or range sliders.
*   **The Risk:** Misinterpretation of distribution shapes by novice users (e.g., misreading a bimodal distribution).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Providing only a min/max numeric label without the shape of the distribution.
*   **Why it fails:** It hides the internal dynamics of the data (e.g., is it skewed? Is it uniform?).

## How to Check <!-- role: check -->
*   **Visual Sign:** Can I see the "shape" of the data, or just the data points themselves?
*   **The Test:** Ask "What is the typical value for [Attribute X]?" If you have to scan the whole table to guess, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add summary statistics (Min, Max, Median) to the interface.
*   **Best Fix:** Integrate histograms or density plots alongside filter controls to show range and distribution simultaneously.
