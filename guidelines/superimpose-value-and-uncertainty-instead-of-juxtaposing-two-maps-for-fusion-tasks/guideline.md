---
id: superimpose-value-and-uncertainty-instead-of-juxtaposing-two-maps-for-fusion-tasks
title: Superimpose Value and Uncertainty for Information Fusion Tasks
bibliography: references.bib
description: For tasks that require combining value and uncertainty, use a single
  integrated map rather than two juxtaposed maps.
labels:
- chart:heatmap
- chart:choropleth
- task:identify
- task:compare
- task:decide
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- design:superposition
---

## The Rule <!-- role: advice -->

When users must integrate value and uncertainty to answer a question, show them together in one superimposed bivariate display—not as two separate (juxtaposed) univariate maps.

## The Logic <!-- role: reason -->

Juxtaposition adds an additional correspondence/search step: viewers must locate a region in one map and then match the same region in the other, which increases errors in information fusion. In the paper’s identification experiment, superimposed charts achieved higher accuracy than juxtaposed ones (58% vs. 51%) [@correllValueSuppressingUncertaintyPalettes2018].

- **The Principle:** Reduce cross-view search and alignment burden in comparative/fusion tasks.
- **The Evidence:** Significant effect of juxtaposition on accuracy in the identification task [@correllValueSuppressingUncertaintyPalettes2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify or choose locations/regions based on both value and uncertainty.
- **Data Type:** Dense grids/regions where correspondence between two maps is not trivially supported by landmarks.
- **Audience:** General audiences performing quick lookups or decisions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is to analyze value and uncertainty distributions separately (not fuse them into a single judgment).
- **Reason:** Juxtaposed univariate views can support independent pattern inspection; the paper frames superposition as best for fusion tasks [@correllValueSuppressingUncertaintyPalettes2018].
- **Scenario:** You can add interaction that explicitly links regions across views.
- **Reason:** The paper notes interaction (e.g., highlighting) can make comparison easier in dense juxtaposed charts [@correllValueSuppressingUncertaintyPalettes2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Simplicity of univariate legends and fully separable channels.
- **The Risk:** Bivariate color channels may interfere perceptually, requiring careful design and discretization [@correllValueSuppressingUncertaintyPalettes2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping juxtaposed maps and assuming viewers will “mentally merge” them accurately.
- **Why it fails:** The added search/correspondence step is error-prone and measurably reduces accuracy [@correllValueSuppressingUncertaintyPalettes2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must look back and forth between two separate maps to answer a single integrated question.
- **The Test:** Time a simple lookup (“find value X with uncertainty Y”); if users repeatedly switch views and miss targets, juxtaposition is hurting fusion.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the two maps with a single bivariate map and a bivariate legend.
- **Best Fix:** Use a discrete superimposed bivariate encoding such as a VSUP to improve integration and interpretability under uncertainty [@correllValueSuppressingUncertaintyPalettes2018].
