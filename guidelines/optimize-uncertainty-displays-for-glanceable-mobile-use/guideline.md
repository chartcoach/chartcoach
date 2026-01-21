---
id: optimize-uncertainty-displays-for-glanceable-mobile-use
title: Design Uncertainty Displays for Glanceable Mobile Decision-Making
bibliography: references.bib
description: Ensure uncertainty encodings remain usable under mobile glance constraints
  by keeping them compact and quickly interpretable.
labels:
- chart:uncertainty
- task:decide
- visual:layout
- impact:usability
- data:temporal
- audience:novice
- domain:mobile
- domain:transit
---

## The Rule <!-- role: advice -->

Design transit uncertainty displays to be glanceable: compact, legible on a phone, and interpretable quickly without requiring detailed area judgments.

## The Logic <!-- role: reason -->

The paper targets “quick, in-the-moment” transit decisions on mobile, where too much information can confuse users. Displays that supported fast probability reasoning (dotplots and CCDF/CDF-style plots) led to higher-quality and more consistent decisions than several alternatives in this constrained context [@fernandesUncertaintyDisplaysUsing2018].

- **The Principle:** Match visual encoding to time/attention constraints.
- **The Evidence:** In a mobile-like bus-catching task, dotplots and CDFs outperformed PDFs/intervals/text in decision outcomes [@fernandesUncertaintyDisplaysUsing2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Make a leave-now vs. wait decision while multitasking (walking, at home, at an event).
- **Data Type:** Short-horizon arrival-time distributions (minutes from now).
- **Audience:** Non-expert commuters using a mobile app.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users have ample time and screen space for deep analysis (desktop planning tools).
- **Reason:** The paper’s findings are grounded in mobile, time-constrained decision-making; other contexts may tolerate more complex encodings [@fernandesUncertaintyDisplaysUsing2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may omit some detailed statistical information to maintain glanceability.
- **The Risk:** Over-simplification can reduce flexibility; the paper shows single-threshold text can be brittle across scenarios [@fernandesUncertaintyDisplaysUsing2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more uncertainty detail (multiple bands, dense marks) until it no longer reads at a glance.
- **Why it fails:** Overloading the display conflicts with the quick-decision constraint emphasized in the study context [@fernandesUncertaintyDisplaysUsing2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users need to zoom, squint, or spend time interpreting before making a choice.
- **The Test:** Time users on first exposure; if they consistently hesitate or misread the uncertainty, it’s not glanceable.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce mark density and prioritize encodings that can be read via counting or monotone position (dotplot/CCDF).
- **Best Fix:** Use the best-performing glance-friendly encodings from the study (low-density quantile dotplots or CCDF/CDF) [@fernandesUncertaintyDisplaysUsing2018].
