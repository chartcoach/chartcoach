---
id: avoid-brown-and-olive-for-race-ethnicity-and-regions
title: Avoid brown and olive hues for race, ethnicity, and world-region categories
bibliography: references.bib
description: Skip brown and olive category colors for demographic groups because they
  can resemble skin tones and are often disliked.
labels:
- chart:bar
- task:compare
- visual:color
- impact:trust
- data:categorical
- audience:general
- domain:demographics
---

## Avoid brown and olive category colors for demographic groups <!-- role: advice -->

Avoid brown and olive hues when assigning colors to race, ethnicity, or world-region categories. Prefer other hues that are less likely to resemble skin tones.

## Brown/olive can read as skin-adjacent and feel unappealing <!-- role: reason -->

Brown and olive shades can be interpreted as skin-tone-adjacent, which risks unwanted associations when the categories describe people. These hues are also described as generally less liked, increasing the chance that readers feel negatively about how their group is portrayed.

**Mechanism:** If a color is both socially suggestive (skin-adjacent) and aesthetically disliked, it can create a subtle “this group is unpleasant” framing even when the data does not support any value judgment.

**Evidence:** Brown and olive are highlighted as potentially remindful of skin tones and as colors people tend to like less, making them risky for encoding any racial group [@muth_race_ethnicity_colors_2024].

**Notes:** This is about categorical encodings for groups; it does not forbid brown in other contexts (e.g., terrain maps) where it does not stand for a group of people.

## Categorical colors for race/ethnicity/region comparisons <!-- role: context -->

- **User Goal:** Present demographic differences without negative affect or skin-tone implication.
- **Task:** Identify and compare categories in legends, stacks, small multiples, or maps.
- **Data:** Nominal groups describing people or regional aggregates.
- **Chart Setting:** Any visualization where the palette is seen as “the identity” of groups.
- **Audience:** General audiences, including people represented by the data.
- **Success Criterion:** Categories read as equally respected and visually balanced.

## When brown is semantically required by non-demographic meaning <!-- role: exceptions -->

**Break it when:** Brown/olive encodes something non-demographic with an established semantic meaning (e.g., land/soil) and not a racial/ethnic/region category of people. **Why:** The harmful association depends on the color standing in for a demographic group [@muth_race_ethnicity_colors_2024].

## Tradeoffs of excluding brown/olive from the palette <!-- role: costs -->

**Sacrifice:** You reduce the number of readily distinct hues available for large category sets. **Risk:** Remaining colors may become harder to differentiate if the palette is already crowded. **Mitigation:** Use labeling and grouping so color carries less of the identification burden.

## Easy-to-make palette choices that backfire <!-- role: mistakes -->

**Mistake:** Assigning brown or olive to a demographic group because it “fits” or fills a leftover slot in the palette. **Why it fails:** It can read as skin-tone-adjacent and may be perceived as an unflattering choice for people [@muth_race_ethnicity_colors_2024].

## Quick checks for brown/olive harm potential <!-- role: check -->

**Failure Sign:** Viewers comment that a group’s color feels like a skin color or “muddy/unpleasant.” **Quick Check:** Convert the palette to swatches with labels removed and ask what the colors suggest. **Stronger Test:** Ask someone from a represented group whether any assigned color feels disrespectful or loaded.

## Safer alternatives to brown/olive for group categories <!-- role: fix -->

- Swap brown/olive for a hue family less likely to resemble skin tones, keeping lightness differences similar.
- Increase differentiation using lightness and outlines rather than resorting to brown/olive as a “spare” color.
- Reduce the number of simultaneously colored categories by grouping small categories or using interaction to reveal details.
- Use direct labels so the palette can be simpler and less socially suggestive.
