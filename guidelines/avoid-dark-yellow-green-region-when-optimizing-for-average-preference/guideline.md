---
id: avoid-dark-yellow-green-region-when-optimizing-for-average-preference
title: Avoid the Dark Yellow-Green Region When Optimizing for Average Preference
bibliography: references.bib
description: Exclude commonly disliked dark yellowish-green colors when building generally
  appealing categorical palettes.
labels:
- chart:categorical
- task:choose
- visual:color
- impact:preference
- data:categorical
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When targeting broad, average aesthetic preference, exclude dark yellowish-green colors from your categorical palette candidates.

## The Logic <!-- role: reason -->

Colorgorical filters out a defined dark yellowish-green region because these colors are generally disliked on average, and because the interaction between preference (bias toward cool hues and lightness contrast) and discriminability can otherwise push selection toward disliked dark yellows as “opposites” of blues [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Preference-aware constraints on candidate color space
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Produce palettes that most people find pleasant while staying usable
- **Data Type:** Categorical palettes intended for broad audiences
- **Audience:** General public / mixed user populations

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your brand/style explicitly requires those hues, or you are designing for a specific audience known to like them.
- **Reason:** The filter targets the average observer; individual and contextual preferences can differ [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less hue coverage (fewer options for balancing hue oppositions).
- **The Risk:** Over-filtering can reduce achievable discriminability for some palette sizes or hue-restricted designs [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Letting “opposite-of-blue” selection drift into dark yellows to maximize contrast.
- **Why it fails:** Those dark yellowish-green choices can degrade perceived quality even if they help separation [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** The palette includes murky, dark yellow-green swatches that users describe as “unpleasant” or “dirty.”
- **The Test:** Inspect hue/lightness coordinates; if colors fall in the dark yellow-green band Colorgorical excludes, treat them as high-risk for preference [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the dark yellow-green for a different hue that still preserves separation from nearby colors.
- **Best Fix:** Apply an explicit candidate-space filter (and optionally a soft penalty near that region) during palette generation [@gramazioColorgoricalCreatingDiscriminable2017a].
