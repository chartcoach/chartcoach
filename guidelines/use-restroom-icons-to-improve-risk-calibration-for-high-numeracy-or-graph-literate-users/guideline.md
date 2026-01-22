---
id: use-restroom-icons-to-improve-risk-calibration-for-high-numeracy-or-graph-literate-users
title: Use restroom icons to improve perceived-to-actual risk calibration for high
  numeracy or graph literacy users
bibliography: references.bib
description: Among more numerate or more graphically literate users, restroom-style
  icon arrays show stronger alignment between perceived risk and stated risk.
labels:
- chart:icon-array
- task:calibrate
- visual:shape
- impact:accuracy
- data:risk
- audience:expert
- domain:health-risk
---

## Use restroom icons when your audience is higher in numeracy or graph literacy <!-- role: advice -->

Use restroom-style person icons in icon arrays when the goal is to make perceived risk track the displayed risk more closely for audiences with higher numeracy or higher graphical literacy.

## Icon type can change calibration differently across skill levels <!-- role: reason -->

Users with stronger quantitative or graph skills may process icon arrays by counting discrete units, so icon designs that make individual units more distinct can increase how tightly perceptions follow the stated risk.

**Mechanism:** Distinct, countable units can strengthen the mapping from “number of highlighted icons” to perceived likelihood, improving calibration between perceived and actual risk.

**Evidence:** In subgroup analyses, icon type affected the correlation between perceived risk and displayed risk among higher numeracy and higher graphical literacy participants; restroom icons showed higher perceived-to-actual risk correlations than the lowest-performing icon condition in those higher-skill groups. [@zikmund-fisherBlocksOvalsPeople2014]

**Notes:** The same advantage was not observed among lower numeracy or lower graphical literacy participants.

## Use when you care about calibration rather than just average perceived risk <!-- role: context -->

- **User Goal:** Form a subjective risk judgment that matches the communicated probability.
- **Task:** Translate a displayed percent risk into a felt likelihood.
- **Data:** Individual 10-year risk percentage displayed in a 100-icon array.
- **Chart Setting:** Static display in an online calculator or decision aid.
- **Audience:** More numerate and/or more graphically literate users.
- **Success Criterion:** Higher correlation between perceived risk ratings and the displayed risk values.

## Exceptions for calibration-focused restroom icons <!-- role: exceptions -->

- **Break it when:** Your primary audience has lower numeracy or lower graph literacy. **Why:** In lower-skill subgroups, restroom icons did not improve perceived-to-actual risk correlations compared to other icon types.
- **Break it when:** You cannot assess audience skill and the experience must be uniform. **Why:** The benefit is conditional on user skill, so average gains may be inconsistent.

## Tradeoffs of targeting higher-skill calibration <!-- role: costs -->

**Sacrifice:** A single icon choice may not optimize calibration for all users simultaneously. **Risk:** Choosing icons to support counting may not help users who rely on gist/area impressions. **Mitigation:** Treat icon selection as audience- and outcome-dependent rather than one-size-fits-all.

## Common mistakes when aiming for calibrated risk perception <!-- role: mistakes -->

- **Mistake:** Optimizing only for mean perceived risk levels across conditions. **Why it fails:** Mean perceived risk did not differ significantly by icon type even when calibration patterns differed by subgroup.
- **Mistake:** Assuming an icon that improves recall will automatically improve calibration for everyone. **Why it fails:** Recall benefits and perceived-to-actual correlation benefits did not align uniformly across skill levels.

## Quick checks for calibration <!-- role: check -->

**Failure Sign:** Perceived likelihood ratings barely change as the displayed risk increases across users. **Quick Check:** Compute perceived-to-actual risk correlations by icon condition in a pilot. **Stronger Test:** Test for an interaction between displayed risk and icon type within higher-skill segments.

## What to do instead when calibration does not improve <!-- role: fix -->

- Segment your evaluation by numeracy or graphical literacy and pick icon types per segment if your product supports personalization.
- Measure both recall and calibration in pilots so you can choose icon types aligned to the primary outcome.
- If personalization is not possible, select an icon type based on which outcome is most important (recall vs calibration vs preference) for your setting.
- Provide a numeric percent alongside the array so users have a precise anchor even if their subjective calibration varies.
