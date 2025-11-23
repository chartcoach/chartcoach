---
id: use-hue-nominal
title: Use Color Hue to Distinguish Categories
bibliography: references.bib
description: After spatial position, use color hue as the most effective channel for
  nominal data.
labels:
- chart:common
- task:categorize
- visual:color
- visual:shape
- impact:clarity
- data:categorical
- data:nominal
---

## The Rule <!-- role: advice -->
When position is already utilized, use **Color Hue** to encode Nominal (categorical) data. Prioritize Hue over Texture, Density, Shape, or Length for categorical distinction.

## The Logic <!-- role: reason -->
For Nominal data (unordered categories), the goal is distinctness rather than magnitude comparison. Based on the theoretical rankings collated in [@zeng_review_2023] and proposed by [@mackinlay_automating_1986], the effectiveness hierarchy for Nominal data is:
1.  **Position** (Spatial grouping)
2.  **Color Hue** (Different colors)
3.  **Texture**
4.  **Density/Saturation**
5.  **Shape**

Color Hue is significantly more effective than Shape or Angle for distinguishing one category from another because perceptual processing separates hues efficiently without implying an order.

## Where to Apply <!-- role: context -->
*   **User Goal:** Differentiating between groups (e.g., "Which points are 'East' vs 'West'?").
*   **Data Type:** Nominal (Unordered categories like Country, Department, or Species).
*   **Audience:** General and expert users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Colorblind-accessible design for specific impairments.
*   **Reason:** Certain hue combinations (Red/Green) are indistinguishable for some users. In these cases, combining Hue with Shape (redundant encoding) is safer.
*   **Scenario:** High cardinality (many categories).
*   **Reason:** Humans can only distinguish a limited number of hues (roughly 6-10) before they become confusing. If you have 50 categories, Hue fails.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Semantic association. Arbitrary colors may not carry meaning (e.g., blue for "banana" is confusing).
*   **The Risk:** False ordering. If the colors vary significantly in brightness (luminance), users might perceive an unintended ranking.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using bar length to represent categories (e.g., a long bar means "Apples" and a short bar means "Oranges" in a non-quantitative context).
*   **Why it fails:** Length implies quantity/order, which confuses the user if the data is purely nominal.
*   **The Wrong Fix:** Using subtle shape differences (e.g., circle vs. square) on small points.
*   **Why it fails:** Shape is ranked lower than Hue [@mackinlay_automating_1986] and requires more cognitive effort to scan and process.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have a legend relying on shapes (triangles vs squares) that are hard to spot in the chart?
*   **The Test:** Convert the image to grayscale. If the categories become indistinguishable, you are relying entirely on Hue (which is good for standard vision, but check accessibility). If you are relying on Shape and it looks messy, switch to Hue.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change shapes to distinct colors (e.g., Orange vs. Blue).
*   **Best Fix:** If position allows, spatially group the categories (e.g., small multiples). If not, use a categorical color palette.
