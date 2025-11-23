---
id: mix-open-closed-shapes-for-search
title: Mix Open and Closed Shapes for Category Distinction
bibliography: references.bib
description: Combine open and closed shapes to maximize discriminability in multi-class
  scatterplots.
labels:
- chart:scatterplot
- task:find-anomalies
- task:filter
- visual:shape
- impact:discriminability
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
When mapping a categorical variable to shape in a scatterplot, assign shapes from opposing perceptual categories (one open, one closed) to distinct data classes, rather than using shapes from the same category.

## The Logic <!-- role: reason -->
"Open" (unbounded line segments like crosses) and "Closed" (bounded regions like squares) act as distinct perceptual categories. It is significantly easier to filter out distractors from one category while searching for a target in the other.
*   **The Principle:** Perceptual Categorical Interference.
*   **The Evidence:** @zeng_review_2023 highlights that mixed-category designs (e.g., Triangle vs. Cross) ranked highest for "find anomalies" and search tasks. @burlinson_open_2018 found that processing interference is higher when competing shapes come from the same category (e.g., Square vs. Triangle) than when they come from different categories (e.g., Square vs. Cross).

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding specific data points (anomalies) or filtering a specific category out of a multiclass display.
*   **Data Type:** Scatterplots containing categorical data (different groups/series).
*   **Audience:** Users who need to discriminate between groups in a cluttered display.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization requires more than two distinct categories.
*   **Reason:** There are only two "super-categories" here (Open and Closed). Once you have 3+ categories, you will inevitably have to use multiple shapes from the same category, reducing the effectiveness of this binary distinction.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may disrupt the visual consistency of the chart, as open shapes and closed shapes have different visual weights (closed shapes look "heavier").
*   **The Risk:** If not balanced by size or stroke width, the closed shapes may dominate the user's attention, making the open shapes harder to see.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** assigning a square to Category A and a triangle to Category B.
*   **Why it fails:** Both are "closed" shapes. @burlinson_open_2018 indicates that it is harder to ignore a square when searching for a triangle than it is to ignore a cross when searching for a triangle.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do all your markers look like little polygons (square, triangle, diamond)? Or do they all look like sticks (cross, plus, asterisk)?
*   **The Test:** Try to mentally "erase" one category to look only at the other. Is it difficult?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change one of the categories to an open symbol (e.g., `x` or `+`) while keeping the other as a closed symbol (e.g., `o` or `s`).
*   **Best Fix:** Assign the most important category to a closed shape and the background/comparison category to an open shape, ensuring the closed shape has sufficient visual weight to stand out.
