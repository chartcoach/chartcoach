---
id: show-coalitions-over-time-with-multicolored-lines
title: Track Coalition Totals Over Time With Multicolored Lines
bibliography: references.bib
description: "Use multicolored time-series lines to show how coalition feasibility\
  \ changes as the contributing parties\u2019 totals shift."
labels:
- chart:line
- task:track
- visual:color
- impact:clarity
- data:temporal
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

To show how coalitions change over time, plot coalition totals as time-series lines and color the lines to reflect the coalition’s party composition. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

Coalitions are defined by their components. Multicolored line styling ties each trend to its underlying parties, reducing the need to decode abstract labels while still showing change over time.

- **The Principle:** Encode composition with color while encoding trend with position
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See when a coalition moved above/below majority over the campaign
- **Data Type:** Poll-based coalition totals computed over time (often with rolling averages)
- **Audience:** Readers following election dynamics across weeks/months [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Too many coalitions at once.\
  **Reason:** Many multicolored lines become unreadable and visually overwhelming. [@muth_german_election_2021]
- **Scenario:** Coalition composition is not stable or not the story.\
  **Reason:** Multicolor cues imply stable membership and can confuse if membership varies. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Simplicity; multicolored styling is harder to parse than single-color lines
- **The Risk:** Color complexity can hinder accessibility and quick scanning if overused. [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using many similar colors or relying on a legend only.\
  **Why it fails:** Readers can’t reliably associate lines with coalitions while tracking time. [@muth_german_election_2021]
- **The Wrong Fix:** Plotting coalition totals without indicating which parties are included.\
  **Why it fails:** Viewers can’t interpret what the line “means” politically. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** You need to repeatedly look back and forth between legend and lines to know which coalition is which.
- **The Test:** If you can’t identify each coalition line in under ~2 seconds, reduce the number of lines or strengthen labeling/color distinctions. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to a few key coalitions and label lines clearly.
- **Best Fix:** Combine multicolored lines with a visible 50% reference line so feasibility changes are instantly interpretable. [@muth_german_election_2021]
