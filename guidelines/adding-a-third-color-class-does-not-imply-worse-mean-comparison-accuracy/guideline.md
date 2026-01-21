---
id: adding-a-third-color-class-does-not-imply-worse-mean-comparison-accuracy
title: "Don\u2019t Avoid a Third Class When Comparing Means by Color"
bibliography: references.bib
description: For mean-comparison aggregation in scatterplots, adding an extra (third)
  color-coded class did not reduce accuracy versus two classes in the evaluated conditions.
labels:
- chart:scatter
- task:aggregate
- visual:color
- impact:robustness
- data:categorical
- data:quantitative
- audience:general
- custom:multiclass
- source:collated
---

## The Rule <!-- role: advice -->

Do not automatically simplify a color-encoded scatterplot down to only two classes just because the user is doing mean-comparison; a third color-coded class is not inherently harmful to accuracy in the tested setup.

## The Logic <!-- role: reason -->

Adding an additional class (via color hue) did not show a drop in aggregate-task accuracy compared to comparable two-class, color-hue encodings in the recorded ranking group.

- **The Principle:** Additional, task-irrelevant categories do not necessarily degrade aggregate judgement when selection can focus on the relevant subset.
- **The Evidence:** Two-class color-hue designs (e.g., E-1) and three-class color-hue designs (e.g., E-4) appear in the same top-performing rank group for aggregate accuracy [@gleicherPerceptionAverageValue2013]. This is preserved in the collated representation intended for recommendation rule extraction [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare which of two focal classes has a higher mean while the plot may contain additional classes.
- **Data Type:** Scatterplot with two quantitative axes and a nominal class variable shown via color hue.
- **Audience:** Users doing aggregate comparisons in dense scatterplots.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You expect class confusion because colors are too similar or the number of classes becomes large.
- **Reason:** This guideline is only supported for the specific extracted comparison patterns (two vs three classes in this dataset); it does not establish safety for many classes or poorly separated colors [@gleicherPerceptionAverageValue2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** More legend entries and potentially more visual complexity.
- **The Risk:** Even if accuracy doesn’t drop in the tested conditions, users may still perceive the chart as more complex.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Removing “distractor” classes by default even when they provide useful context.
- **Why it fails:** The extracted evidence does not support an inherent accuracy penalty for adding a third class under color-hue encoding for this aggregate task [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Designers remove classes to “help users,” but user accuracy on mean-comparison questions does not improve.
- **The Test:** Keep the third class and ask users the same two-class mean question; if accuracy is stable, the third class is not the problem (consistent with the collated ranking group).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Restore the third class if it provides context; keep class encoding consistent with color hue.
- **Best Fix:** If complexity is still a concern, keep the third class but visually de-emphasize it through non-encoded means (e.g., layout or filtering controls)—while keeping the primary class encoding as color hue for the mean task [@gleicherPerceptionAverageValue2013; @zengReviewCollationGraphical2023].
