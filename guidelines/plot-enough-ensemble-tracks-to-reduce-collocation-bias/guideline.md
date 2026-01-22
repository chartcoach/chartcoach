---
id: plot-enough-ensemble-tracks-to-reduce-collocation-bias
title: Plot enough ensemble tracks to reduce collocation bias in location-specific
  judgments
bibliography: references.bib
description: Increase the number of ensemble tracks shown so a single path intersecting
  a location does not disproportionately raise perceived risk.
labels:
- chart:ensemble-track
- task:assess-risk
- visual:mark-density
- impact:accuracy
- data:uncertainty
- audience:novice
- domain:hurricane
---

## Plot enough ensemble tracks to reduce collocation bias in location-specific judgments <!-- role: advice -->

When an ensemble track display is used to judge risk at a specific location, show enough ensemble members that any one line crossing the location does not dominate the judgment.

## Collocation bias shrinks as individual tracks become less visually meaningful <!-- role: reason -->

Sparse ensembles encourage viewers to treat each line as a meaningful, deterministic path, so a location touched by a line is judged as much more at risk than an equally plausible nearby location that is not touched. Increasing the number of plotted paths reduces the relative weight of any single mark, which reduces this overreaction to a line-location intersection.

**Mechanism:** Increasing mark count reduces the perceptual salience and implied meaning of a single line, weakening the tendency to substitute “a line hits here” for “this area is more likely.”

**Evidence:** Damage judgments were higher when a location was intersected by an ensemble track than when it was not (a collocation effect), and this effect was significantly smaller when 17, 33, or 65 tracks were shown compared to 9 tracks [@padillaPowerfulInfluenceMarks2020]. The reduction was substantial but incomplete, with the 33-track condition showing the largest reduction relative to the 9-track baseline in this study [@padillaPowerfulInfluenceMarks2020].

**Notes:** The collocation effect persisted even with many tracks, so increasing track count is a mitigation rather than a complete fix.

## Contexts where a viewer judges risk for a particular point location <!-- role: context -->

- **User Goal:** Decide how much damage/risk a specific site (town, facility, asset) may incur.
- **Task:** Compare risk between two candidate locations on the map.
- **Data:** Ensemble forecast tracks representing uncertainty in path.
- **Chart Setting:** Static, overlaid track lines on a geographic basemap.
- **Audience:** Non-expert or mixed-expertise audiences.
- **Success Criterion:** Risk judgments reflect the distribution of paths rather than a single line intersection.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The display is already so dense that additional tracks are not visually separable. **Why:** Overplotting can make the distribution unreadable and introduce new misconceptions about what the set of lines represents [@padillaPowerfulInfluenceMarks2020].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional tracks increase visual clutter and may reduce legibility of the distribution’s shape. **Risk:** Very dense displays can prompt viewers to infer that all possible paths are shown, which can increase misinterpretation in other ways. **Mitigation:** Monitor for overplotting and viewer misconceptions about completeness when increasing track counts [@padillaPowerfulInfluenceMarks2020].

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using very few ensemble tracks for a point-specific risk decision. **Why it fails:** Viewers overweight a single line crossing the point and inflate perceived damage relative to nearby points not crossed [@padillaPowerfulInfluenceMarks2020].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers consistently rate substantially higher damage when a line exactly intersects the target than when it narrowly misses at comparable distance from the distribution center. **Quick Check:** Run a simple internal review using paired “on-line vs off-line” variants and see if judgments diverge strongly. **Stronger Test:** Conduct a small user study measuring the on-minus-off “damage change” score and verify it decreases when more tracks are shown [@padillaPowerfulInfluenceMarks2020].

## Fix: What to do instead <!-- role: fix -->

- Increase the number of plotted ensemble tracks until the impact of any one intersecting line is reduced.
- Validate that the distribution remains perceivable after increasing tracks by checking whether viewers still differentiate nearer-to-center vs farther-from-center locations.
- If adding tracks makes the distribution hard to perceive, switch to an approach that does not rely on single crisp line intersections for meaning.
- Add evaluation questions that detect whether viewers think the plotted lines represent all possible paths.
