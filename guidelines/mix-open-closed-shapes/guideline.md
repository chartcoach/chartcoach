---
id: mix-open-closed-shapes
title: Pair open and closed shapes for categorical distinction
bibliography: references.bib
description: To maximize discriminability between two data categories in a scatterplot,
  select one shape that encloses space (closed) and one that consists of line segments
  (open).
labels:
- chart:scatterplot
- visual:shape
- task:compare
- task:cluster
- impact:discriminability
- data:categorical
---

## The Rule <!-- role: advice -->
When encoding two different categories using shape in a scatterplot, pair an "open" shape (unbounded line segments like a plus sign, asterisk, or 'x') with a "closed" shape (bounded regions like a circle, square, or triangle). Avoid using two shapes from the same category (e.g., do not pair a square with a triangle).

## The Logic <!-- role: reason -->
The visual system processes "open" and "closed" characteristics as distinct perceptual categories. Research indicates that these topological features influence attentional allocation and processing speed.
*   **The Principle:** Perceptual Interference and Response Competition.
*   **The Evidence:** In flanker and visual search tasks, interference is significantly higher when target and distractor symbols share the same open or closed feature category. Conversely, discriminability improves and reaction times decrease when symbols are drawn from different categories [@burlinson_open_2018]. This effect is particularly strong for extracting ensemble statistics like numerosity and linear trends.

## Where to Apply <!-- role: context -->
This strategy is most effective in scenarios where the user needs to distinguish classes within a single shared space.
*   **User Goal:** Making judgments about numerosity (which class has more points) or linear trends (correlation) within mixed groups.
*   **Data Type:** Multi-class scatterplots, specifically those with heterogeneous distributions (mixed clusters).
*   **Display Condition:** High-load or "cluttered" displays where data points are dense, as the distinctiveness of the categories helps mitigate the effects of visual clutter [@burlinson_open_2018].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Side-by-side (small multiple) plots where each plot contains only a single category.
*   **Reason:** The paper found that the performance advantage of mixing open/closed shapes disappears in homogeneous displays (separate plots) because there is no local perceptual interference to overcome [@burlinson_open_2018].
*   **Scenario:** Tasks strictly requiring judgment of Average Value (y-axis position).
*   **Reason:** Experiment 3 showed that average value judgments were less sensitive to feature category differences than numerosity or trend judgments [@burlinson_open_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetic consistency. Mixing geometric primitives (squares) with line-based symbols (asterisks) may look less uniform than using a consistent "theme" of shapes.
*   **The Risk:** If the open shape is too thin or the lines are too fine, it may suffer from poor visibility compared to the visual weight of the closed shape.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Increasing the distance between shapes to improve clarity without changing the shape types.
*   **Why it fails:** While distance helps, the paper notes that "open/closed feature categories for shapes are found to be particularly important with cluttered rather than sparse displays." Relying solely on spacing fails when data density is high [@burlinson_open_2018].
*   **The Wrong Fix:** Using a Square and a Triangle.
*   **Why it fails:** Both are "closed" shapes. The experiments show that interference is higher between two closed shapes than between one closed and one open shape [@burlinson_open_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the legend. Do all symbols enclose a finite region (circle, square, diamond)? Or do all symbols consist only of intersecting lines (cross, plus, asterisk)?
*   **The Test:** If you describe the shapes, can you apply the word "inside" to all of them? If yes, you lack an open shape.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change one of your symbols. If you have a Square and a Triangle, change the Triangle to an 'X' or Asterisk.
*   **Best Fix:** Assign the "Closed" shape to the most salient or dense category and the "Open" shape to the secondary or sparser category to leverage the processing speed advantage of closed shapes.
