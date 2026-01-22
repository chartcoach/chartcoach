---
id: avoid-stereotypical-skin-tone-colors-for-race-ethnicity-and-regions
title: Avoid stereotypical skin-tone colors for race, ethnicity, and world-region
  categories
bibliography: references.bib
description: Do not encode racial, ethnic, or world-region groups with colors that
  resemble stereotypical skin tones.
labels:
- chart:bar
- task:compare
- visual:color
- impact:fairness
- data:categorical
- audience:general
- domain:demographics
---

## Use non–skin-tone hues for race, ethnicity, and world-region categories <!-- role: advice -->

Use colors that do not resemble stereotypical skin tones when encoding race, ethnicity, or world-region categories. Avoid mapping “Black/White/Asian/etc.” to black/white/yellow (or other skin-associated hues) as a direct stand-in for people.

## Skin-tone encoding invites stereotyping and disrespect <!-- role: reason -->

Using skin-associated colors turns a social category into a visual proxy for bodies and stereotypes, which can cue biased interpretations and make readers (and data subjects) feel reduced to skin color rather than represented as people.

**Mechanism:** Skin-tone palettes trigger immediate cultural associations (“this color equals this kind of person”), which can override the intended analytic message and create harm through stereotype reinforcement and perceived disrespect.

**Evidence:** Stereotypical “skin color” mappings (e.g., black for Black people, white for white people, yellow for Asian people; or historic region maps colored as “yellow Asia/black Africa/white Europe”) are described as insensitive and stereotype-reinforcing, with modern best practice shifting away from these mappings [@muth_race_ethnicity_colors_2024].

**Notes:** This guidance targets category colors for groups; it does not forbid using neutral tones as background or de-emphasis when the story requires it.

## Demographic group categories with social sensitivity <!-- role: context -->

- **User Goal:** Communicate differences among demographic groups without implying hierarchy or stereotypes.
- **Task:** Compare categories (levels, shares, change) across races, ethnicities, or world regions.
- **Data:** Nominal categories that describe people (race/ethnicity) or culturally loaded aggregates (world regions).
- **Chart Setting:** Any chart or map using color as the primary category key (static or interactive).
- **Audience:** Broad audiences, including people represented in the data; readers with different cultural associations.
- **Success Criterion:** Readers feel respected and interpret categories without stereotype cues.

## Exceptions for neutral backdrops or intentional de-emphasis <!-- role: exceptions -->

**Break it when:** A neutral white/gray/black is used only as a backdrop or to deliberately de-emphasize a non-focal category while the story emphasizes other groups. **Why:** The color is not functioning as a “skin tone = group identity” mapping but as a visual hierarchy device in the composition [@muth_race_ethnicity_colors_2024].

## Tradeoffs when avoiding skin-associated hues <!-- role: costs -->

**Sacrifice:** You may lose an “obvious” mnemonic color mapping that some readers expect. **Risk:** A fully arbitrary palette can make categories harder to remember across a series. **Mitigation:** Use clear labeling and a well-designed key so identity does not depend on color memory.

## Common stereotype-triggering color shortcuts <!-- role: mistakes -->

- **Mistake:** Coloring categories as black/white/yellow/red to “match” racial labels. **Why it fails:** It equates social groups with skin color and can reinforce racist stereotypes or feel dehumanizing [@muth_race_ethnicity_colors_2024].
- **Mistake:** Reusing historic “continent colors” (e.g., yellow Asia, black Africa, white Europe). **Why it fails:** It inherits outdated, racialized conventions that embed bias in the visual encoding [@muth_race_ethnicity_colors_2024].

## Quick checks for skin-tone stereotyping <!-- role: check -->

**Failure Sign:** A reader can guess your category names from the palette because the colors resemble stereotyped skin tones. **Quick Check:** Ask “If I were in this category, would I feel reduced to a skin color?” **Stronger Test:** Show the palette (without labels) to a few colleagues and ask what groups they assume the colors represent.

## Replace skin-tone cues with neutral, distinct category palettes <!-- role: fix -->

- Choose distinct hues that do not resemble skin tones and assign them to categories without relying on cultural stereotypes.
- Use a clear, readable legend (or direct labels) so categories don’t need “obvious” color metaphors to be understood.
- If you need a muted baseline category, set it in a light neutral and keep the focal categories in more saturated (but not skin-associated) colors.
- If color meaning feels socially loaded no matter what you pick, reduce reliance on color by adding direct labels or grouping/ordering to carry meaning.
