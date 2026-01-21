---
id: avoid-shuffling-animated-scattered-icon-arrays-for-risk-comparisons
title: Avoid Shuffling Scattered Icon Arrays in Two-Risk Comparisons
bibliography: references.bib
description: Randomly shuffling scattered event icons (automatic or user-triggered)
  reduces comprehension and is strongly disliked in side-by-side risk comparisons.
labels:
- chart:icon-array
- task:compare
- visual:motion
- impact:comprehension
- data:probabilistic
- audience:general-public
- animation:shuffle
- domain:health-risk
- source:zikmund-fisher-2012
---

## The Rule <!-- role: advice -->

Do not use shuffling animations (automatic or user-controlled) on scattered icon arrays when users must compare two risks.

## The Logic <!-- role: reason -->

Shuffling adds continuous motion and changing spatial patterns, which competes for attention and undermines extracting and comparing magnitudes across two displays.

- **The Principle:** Motion-induced distraction and unstable grouping impair magnitude comparison
- **The Evidence:** Shuffling conditions (auto or user-controlled) had significantly lower graph evaluation ratings than static grouped arrays and often reduced gist knowledge and/or choice accuracy, with particularly poor performance and ratings in shuffle-heavy versions [@zikmund-fisherAnimatedGraphicsComparing2012].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which option is safer; judge which side effect risk is higher across two treatments
- **Data Type:** Two side-by-side icon arrays with small differences in probabilities
- **Audience:** Mixed numeracy; especially relevant when you expect users to compare by counting or estimating counts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your primary intended outcome is to increase subjective uncertainty or emphasize randomness rather than support accurate comparison
- **Reason:** The paper notes prior work where dynamic scattered displays increased subjective uncertainty; that goal differs from maximizing choice/knowledge accuracy tested here [@zikmund-fisherAnimatedGraphicsComparing2012].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a strong visual cue for “randomness” (events could happen to anyone)
- **The Risk:** Users may take away a more deterministic-feeling representation, even if they compare magnitudes more accurately [@zikmund-fisherAnimatedGraphicsComparing2012].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a “shuffle” button to give users control and assuming interactivity will improve understanding
- **Why it fails:** User-controlled shuffling still performed poorly and was rated very negatively relative to the static grouped baseline [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Check <!-- role: check -->

- **Visual Sign:** Event icons keep relocating to new random positions while users are supposed to decide which risk is larger.
- **The Test:** Time-box a user to 10–20 seconds and ask which option has higher risk; if responses are inconsistent or confidence/ratings drop, remove shuffling [@zikmund-fisherAnimatedGraphicsComparing2012].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Disable shuffling and show a stable final arrangement.
- **Best Fix:** Replace the scattered/shuffling design with static grouped icon arrays for the comparison task [@zikmund-fisherAnimatedGraphicsComparing2012].
