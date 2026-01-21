---
id: test-for-individual-differences-in-perceptual-proxies-before-standardizing-a-design
title: Test for Individual Differences in Perceptual Proxies Before Standardizing
  a Design
bibliography: references.bib
description: Validate comparison charts with users because different people may rely
  on different perceptual proxies.
labels:
- chart:bar
- task:compare
- impact:robustness
- audience:general
- custom:validation
- concept:individual-differences
- concept:perceptual-proxies
---

## The Rule <!-- role: advice -->

Do not assume one bar-chart design supports mean/range comparisons equally for everyone; test with multiple viewers to detect proxy-driven individual differences.

## The Logic <!-- role: reason -->

The paper finds evidence of individual differences: participants were broadly self-consistent but differed in which proxies deceived them, and some participants appeared to “select against” certain proxy manipulations due to proxy conflicts [@ondovRevealingPerceptualProxies2021]. This implies a single design may systematically mislead subsets of users depending on which proxy they favor.

- **The Principle:** Heterogeneous perceptual strategies (different proxy reliance across individuals)
- **The Evidence:** Mixed-effects modeling and participant-level patterns show variability across proxy conditions [@ondovRevealingPerceptualProxies2021].

## Where to Apply <!-- role: context -->

- **User Goal:** Reliable comparisons (mean or range) across a broad population
- **Data Type:** Multi-bar comparisons where multiple proxies (centroid, hull/shape, slope motifs) can disagree with the target statistic
- **Audience:** Diverse audiences (dashboards, public-facing reporting) [@ondovRevealingPerceptualProxies2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are designing for a narrowly trained internal audience and can enforce a specific reading strategy.
- **Reason:** Training and conventions may reduce variability in proxy use (though the paper does not test training effects).

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires time and participants to validate; may slow iteration.
- **The Risk:** Testing may reveal you need multiple views/encodings to serve different users.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Optimizing the design based on an “average user” result only.
- **Why it fails:** The paper shows proxy susceptibility can vary substantially; averages can hide subgroups that are misled [@ondovRevealingPerceptualProxies2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Different viewers confidently give different answers on the same comparison.
- **The Test:** Run a short forced-choice validation with diverse users and look for systematic disagreement patterns tied to chart shape cues (e.g., centroid-leaning vs slope-leaning judgments) [@ondovRevealingPerceptualProxies2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add redundant cues to the target statistic (e.g., explicit mean or range markers) and re-test.
- **Best Fix:** Provide alternate views or interactions that let users directly access the statistic when proxy cues may conflict, and validate across individuals using the paper’s adversarial mindset [@ondovRevealingPerceptualProxies2021].
