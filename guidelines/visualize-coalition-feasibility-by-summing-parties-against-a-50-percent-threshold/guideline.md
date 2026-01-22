---
id: visualize-coalition-feasibility-by-summing-parties-against-a-50-percent-threshold
title: Visualize coalition feasibility by summing party shares against a majority
  threshold
bibliography: references.bib
description: Make governing possibilities legible by comparing coalition totals to
  a clear majority line.
labels:
- chart:bar
- task:threshold
- visual:annotation
- impact:clarity
- data:compositional
- audience:general
- domain:elections
- tool:datawrapper
---

## Show coalition totals relative to the majority threshold <!-- role: advice -->

Visualize coalitions as combined vote-share totals and compare each total to a clearly marked majority threshold so readers can immediately see which coalitions are mathematically possible.

## Why threshold framing turns “party shares” into “governing feasibility” <!-- role: reason -->

Readers often need a derived conclusion—whether a government majority is reachable—rather than just individual party percentages. A threshold comparison translates shares into feasibility by making the decisive condition (majority) visible and by turning coalition arithmetic into a directly readable visual judgment.

**Mechanism:** Summed coalition totals and a single majority reference line reduce mental math and prevent readers from misjudging feasibility based on prominent parties alone.

**Evidence:** The post explains that governing requires a majority, shows a coalition-feasibility visualization based on the latest polling numbers, and explicitly uses the “50% needed to govern” threshold to separate possible from impossible coalitions [@muth_german_election_2021].

**Notes:** The same approach can be extended over time to show how feasibility changes as polls move.

## When this applies to coalition stories <!-- role: context -->

- **User Goal:** Understand which governing coalitions are possible right now.
- **Task:** Compare coalition totals to a fixed threshold (majority).
- **Data:** Party shares from a poll or average; coalition definitions as combinations of parties.
- **Chart Setting:** Pre-election explainers, coalition scenario pieces, election-night analysis (when based on results).
- **Audience:** Readers unfamiliar with coalition arithmetic.
- **Success Criterion:** A reader can identify feasible coalitions without calculating sums.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The governing rule is not a simple fixed threshold (for example, when seats, electoral thresholds, or overhang/leveling effects dominate the outcome). **Why:** Vote-share sums can misrepresent feasibility if the system logic is seat-based or constrained by additional rules [@muth_german_election_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires defining which coalitions to include and can increase chart length. **Risk:** Readers may treat “mathematically possible” as “politically likely.” **Mitigation:** Label the view as mathematical feasibility and keep political commentary separate in text [@muth_german_election_2021].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Listing coalition options in text without showing totals against the majority threshold. **Why it fails:** Readers must do mental arithmetic and can misread which scenarios clear the decisive majority condition [@muth_german_election_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** People ask “Does that coalition reach a majority?” after seeing the chart. **Quick Check:** Ensure every coalition has a visible total and the majority threshold is unmistakable [@muth_german_election_2021]. **Stronger Test:** Hide the data table and ask a colleague to mark feasible coalitions; they should be able to do it quickly from the visualization alone.

## What to do instead <!-- role: fix -->

- Add a clear majority reference line and label it with the governing requirement [@muth_german_election_2021].
- Display coalition totals directly (as numbers or bar endpoints) so feasibility is readable without calculation [@muth_german_election_2021].
- If feasibility changes over time is the story, show coalition totals as time series and retain the majority line as a constant reference [@muth_german_election_2021].
- If political plausibility is the story, keep the math chart and add a separate qualitative explainer rather than encoding “likelihood” into the totals [@muth_german_election_2021].
