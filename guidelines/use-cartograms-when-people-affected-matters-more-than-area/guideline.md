---
id: use-cartograms-when-people-affected-matters-more-than-area
title: Use a population cartogram when the number of people affected matters more
  than land area
bibliography: references.bib
description: Cartograms shift attention from large sparsely populated regions to where
  more people live, which can be more honest for people-based outcomes.
labels:
- chart:choropleth
- task:interpret
- visual:geometry
- impact:honesty
- data:geospatial
- audience:general
- map:cartogram
---

## Switch to a population cartogram when land area would distort perceived impact <!-- role: advice -->

Use a population cartogram instead of a standard choropleth when the key message is how many people are affected and population density varies greatly across regions. Prefer standard geography when recognizability of shapes and locations is the priority.

## Area-based maps overweight sparsely populated regions <!-- role: reason -->

Standard choropleths allocate visual space by land area, which can make large, lightly populated regions dominate attention even when few people are impacted. Population cartograms reallocate area by population, aligning visual weight with the number of people and producing a view that better matches people-centered interpretations.

**Mechanism:** Resizing regions by population changes salience: the viewer’s attention follows the larger shapes, which now correspond more closely to where most people are.

**Evidence:** Choropleths are described as showing how much geographic area is affected, which can overemphasize large regions with low population; population cartograms are recommended to drive attention to populated areas and can provide a more honest view when population density differs greatly [@muth_choroplethmaps_2018]. Cartograms are noted to reduce region recognizability, working best when readers are familiar with the geography [@muth_choroplethmaps_2018].

**Notes:** This choice is about aligning the visual weighting (area) with the real-world weighting (people).

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Understand impact on people (not on square kilometers).
- **Task:** Judge where most affected people are concentrated.
- **Data:** A people-centered metric by region (rates or outcomes) in a place with strong population density variation.
- **Chart Setting:** News/briefing contexts where viewers may otherwise misread “big land” as “big impact.”
- **Audience:** Readers who can recognize regions even when shapes are distorted, or who have supporting labels/tooltips.
- **Success Criterion:** Visual prominence corresponds to population importance rather than land area.

## When not to follow it <!-- role: exceptions -->

- **Break it when:** Readers are unlikely to recognize regions in distorted shapes. **Why:** Reduced recognizability can prevent viewers from locating places and understanding the map [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You lose geographic fidelity and some immediate place recognition. **Risk:** Viewers may distrust or misread distorted shapes without guidance. **Mitigation:** Rely on clear labeling and tooltips to support orientation.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a standard choropleth for a people-impact story in a country with extreme population density differences. **Why it fails:** It emphasizes land area and can visually downplay where most people live [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The map is dominated by large rural regions even though the topic concerns people affected. **Quick Check:** Compare the largest shapes on the map to known population centers; if they mismatch, consider a cartogram. **Stronger Test:** Ask readers which areas seem most important; if they consistently point to large sparsely populated regions, area is biasing interpretation.

## What to do instead <!-- role: fix -->

- Use a population cartogram to align visual weight with where people live.
- Add labels or tooltips to help readers recognize regions in the distorted geography.
- Keep a small reference map or strong textual cues when geographic familiarity is uncertain.
- Use a different non-map view if region recognition is central and distortion would block understanding.
