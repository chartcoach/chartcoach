---
id: use-visually-symmetric-encodings-to-avoid-within-the-bar-bias
title: Use Visually Symmetric Encodings Around the Mean
bibliography: references.bib
description: "Choose uncertainty displays symmetric about the mean to prevent \u201C\
  within-the-bar\u201D bias."
labels:
- chart:bar
- task:judge-likelihood
- visual:symmetry
- impact:bias-reduction
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

Encode uncertainty symmetrically around the mean; avoid asymmetric marks that visually “contain” values on one side of the mean.

## The Logic <!-- role: reason -->

Asymmetric bar glyphs create a containment metaphor: outcomes visually inside the bar are judged more likely than outcomes outside it, even when they are equally distant from the mean. Symmetric encodings mitigate this bias.

- **The Principle:** Visual containment bias (“within-the-bar” bias).
- **The Evidence:** In one-sample tasks, participants judged dots below the mean (inside the bar area) as more likely than dots above the mean; this bias was not significant for symmetric encodings (gradient/violin/modified box) [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging how likely a specific outcome is relative to an estimated mean with uncertainty.
- **Data Type:** A mean plus an uncertainty interval/distribution; “one-sample” reasoning tasks.
- **Audience:** Broad/public audiences, especially when statistical training is unknown.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want an asymmetric metaphor for a different task (not likelihood around a mean).
- **Reason:** The paper’s bias findings are tied to inferential likelihood judgments around the mean; other tasks may not require symmetry [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some viewers may need time to learn unfamiliar symmetric forms.
- **The Risk:** If symmetry is implemented but the mean is not clearly marked, viewers may lose the point estimate.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping bars but “centering” error bars or adding caps while retaining the filled bar area.
- **Why it fails:** The filled area still implies containment, preserving the bias mechanism [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** The uncertainty display has a large filled region only on one side of the mean (e.g., from baseline up to mean).
- **The Test:** Mirror the graphic around the mean mentally—if it wouldn’t look the same, you’re likely introducing asymmetric judgment cues [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the filled bar area; show a symmetric uncertainty shape centered on the mean.
- **Best Fix:** Use violin plots or gradient plots centered at the mean, with an explicit mean marker [@correllErrorBarsConsidered2014].
