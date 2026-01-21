---
id: include-deviating-polls
title: Show Multiple Pollsters to Reveal Differences
bibliography: references.bib
description: Prevent over-reliance on a single poll by showing results from multiple
  pollsters and making deviations visible.
labels:
- chart:bar
- task:compare
- visual:layout
- impact:trust
- data:categorical
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Do not present a single poll as the whole story; include results from multiple pollsters and make their differences visible (e.g., with split bars or a pollster-by-pollster view).

## The Logic <!-- role: reason -->

Different pollsters can produce meaningfully different results due to methodology, potential bias, or error; showing multiple sources reduces the chance that readers mistake one house’s result for the electorate’s true state [@jockers_election_polls_2021].

- **The Principle:** Cross-source context to reduce single-source distortion
- **The Evidence:** [@jockers_election_polls_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand the plausible spread of current support across pollsters
- **Data Type:** Election poll shares reported by several organizations for the same race/time window
- **Audience:** News audiences encountering polls through headlines and quick charts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Only one credible poll exists for the relevant period or you cannot access additional pollster data.
- **Reason:** You can’t display what you don’t have; in that case, be explicit that the view is single-source and avoid implying consensus [@jockers_election_polls_2021].

## The Price <!-- role: costs -->

- **The Sacrifice:** More ink and attention required; the chart becomes denser.
- **The Risk:** Readers may struggle to find “the takeaway” if you don’t provide a clear structure (e.g., ordering and an average row) [@jockers_election_polls_2021].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking one pollster and treating its numbers as definitive.
- **Why it fails:** It hides variability and can amplify outliers or systematic leanings, misleading audiences about the state of the race [@jockers_election_polls_2021].

## How to Check <!-- role: check -->

- **Visual Sign:** Only one set of party shares is shown with no indication other polls exist or differ.
- **The Test:** Ask: “If another pollster reported a different number today, would the reader learn that from this graphic?” If not, you’re missing deviations [@jockers_election_polls_2021].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a second poll (or a range across pollsters) to show that results vary.
- **Best Fix:** Build a pollster-by-pollster comparison (optionally including an “Average” row) or use split bars that let readers compare pollsters side-by-side [@jockers_election_polls_2021].
