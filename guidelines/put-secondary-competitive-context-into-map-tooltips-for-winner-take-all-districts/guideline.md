---
id: put-secondary-competitive-context-into-map-tooltips-for-winner-take-all-districts
title: Add second-place and margin details in tooltips when mapping winner-take-all
  district results
bibliography: references.bib
description: Winner maps hide competitiveness; tooltips can reveal how close the race
  was by showing runner-up and margin.
labels:
- chart:map
- task:contextualize
- visual:annotation
- impact:trust
- data:geospatial
- audience:general
- domain:elections
- tool:datawrapper
---

## Use tooltips to show runner-up and margin on winner maps <!-- role: advice -->

When mapping winner-take-all district outcomes, include the winner’s and second-place party shares (and the margin) in the tooltip so the map communicates competitiveness, not just who came first.

## Why winner maps can mislead without competitiveness context <!-- role: reason -->

A categorical winner map compresses each district into a single label, which hides whether the district was a landslide or a near tie. Tooltips allow you to preserve the clean “who won” surface while adding on-demand detail that supports accurate interpretation.

**Mechanism:** Layering detail on interaction separates overview (winner) from diagnosis (how close), helping readers avoid equating “won” with “dominant.”

**Evidence:** The post describes mapping first-vote winners and highlights adding the margin for the second-place candidate in the tooltip to show that some areas were decided by small differences [@muth_german_election_2021].

**Notes:** This approach is especially useful when the story includes surprising wins or narrow victories.

## When this applies to district winner maps <!-- role: context -->

- **User Goal:** See who won each district and how competitive each district was.
- **Task:** Identify close races, interpret strength of victories, spot swing districts.
- **Data:** District-level winner, runner-up, and their vote shares (or vote counts to compute margin).
- **Chart Setting:** Interactive map with hover or tap; tooltips available.
- **Audience:** Readers who may over-interpret categorical dominance.
- **Success Criterion:** Readers can distinguish narrow wins from strongholds without leaving the map.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The map will be printed or otherwise used without hover/tap interaction. **Why:** Tooltips won’t be accessible, so the competitiveness information will be lost [@muth_german_election_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Requires additional fields and careful tooltip writing. **Risk:** Tooltips can become cluttered and hard to parse if they include too many metrics. **Mitigation:** Limit tooltip content to winner, runner-up, and margin as the core competitiveness story [@muth_german_election_2021].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Publishing a winner-only map with no indication of how close races were. **Why it fails:** It can imply uniform dominance across a region even where outcomes were decided by small margins [@muth_german_election_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers interpret a solid block of one color as “overwhelming support” everywhere it appears. **Quick Check:** Hover a few districts and confirm the tooltip reveals both first and second place plus margin [@muth_german_election_2021]. **Stronger Test:** Ask someone to find a “close district” using only the map; they should succeed by exploring tooltips.

## What to do instead <!-- role: fix -->

- Add runner-up party and margin fields to the tooltip content so competitiveness is accessible on demand [@muth_german_election_2021].
- If interactivity is not available, annotate a few notable close districts directly on the map with labels or callouts [@muth_german_election_2021].
- Provide a companion table or bar view listing the closest districts when readers need systematic comparison [@muth_german_election_2021].
- Keep the map’s main encoding categorical (winner) and move all competitive nuance into tooltip or supplemental views to avoid clutter [@muth_german_election_2021].
