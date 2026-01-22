---
id: prefer-less-saturated-colors-for-race-ethnicity-categories-to-reduce-associations
title: Prefer less-saturated colors for race and ethnicity categories to reduce value-laden
  associations
bibliography: references.bib
description: Use toned-down hues for racial and ethnic categories to avoid strong
  connotations like danger, positivity, or prestige.
labels:
- chart:bar
- task:compare
- visual:color
- impact:neutrality
- data:categorical
- audience:general
- domain:demographics
---

## Use toned-down hues for racial and ethnic categories instead of crayon-bright colors <!-- role: advice -->

Prefer less-saturated colors when encoding race, ethnicity, or world-region categories. If you need the full palette, tone colors down or shift hues slightly so no category inherits a strong “good/bad/important” connotation.

## Saturated colors carry strong meanings that can attach to groups <!-- role: reason -->

Highly saturated colors often come with learned meanings (e.g., red as danger, green as positive, dark blue as competent/royal). When these meanings are mapped onto racial or regional categories, they can create unintended value judgments unrelated to the data.

**Mechanism:** Viewers interpret saturated, high-chroma hues as more emotionally charged and semantically loaded, which can bias how group differences are perceived.

**Evidence:** Strong saturated hues are described as having strong associations (competent/royal blue, positive/right green, danger/important red), and a recommended strategy is to use less saturated or slightly shifted hues to reduce these effects; accessibility risks are noted for pale/pastel colors [@muth_race_ethnicity_colors_2024].

**Notes:** Less-saturated colors can be harder to distinguish and may fail contrast needs; this is a palette-neutrality goal that must be balanced with legibility.

## Sensitive categorical encodings where neutrality matters <!-- role: context -->

- **User Goal:** Compare demographic groups without implying moral or status judgments.
- **Task:** Identify categories and compare values across them.
- **Data:** Nominal demographic categories with potential social sensitivity.
- **Chart Setting:** Any chart/map where color is the primary identity cue for groups.
- **Audience:** Broad audiences; includes readers sensitive to framing and bias.
- **Success Criterion:** Colors feel neutral and no group seems “good/bad/special” due to hue intensity.

## When maximum distinctness is required under severe constraints <!-- role: exceptions -->

**Break it when:** You need highly distinct category colors under tight conditions (many categories, small marks, limited labeling) and toned-down colors become too confusable. **Why:** Distinguishability can override neutrality if viewers cannot reliably identify categories [@muth_race_ethnicity_colors_2024].

## Tradeoffs of toning down saturation <!-- role: costs -->

**Sacrifice:** Some palettes will look less vivid and may feel less visually “punchy.” **Risk:** Pastel or pale colors can reduce color-difference and can fail contrast expectations in some settings. **Mitigation:** Distinguish categories with additional styling such as darker outlines when needed.

## Overly vivid palettes that accidentally moralize categories <!-- role: mistakes -->

**Mistake:** Assigning bright red/green/royal blue to demographic groups because the palette is vivid and distinct. **Why it fails:** The color meanings can attach to groups, creating unintended positive/negative framing [@muth_race_ethnicity_colors_2024].

## Quick checks for semantic overload <!-- role: check -->

**Failure Sign:** The palette feels like it’s signaling “danger,” “success,” or “prestige” for a specific group. **Quick Check:** Ask what adjectives the colors evoke (e.g., “warning,” “official,” “good”) and check whether any adjective maps to a group. **Stronger Test:** Print or view in grayscale and verify the design still communicates without relying on emotional color punch.

## Practical ways to keep colors neutral and legible <!-- role: fix -->

- Reduce saturation and slightly adjust hues so categories remain distinct but less semantically loaded.
- Add darker or more saturated outlines to keep boundaries clear when fills are pale.
- Increase direct labeling so the palette can be quieter without losing identification.
- If neutrality and distinguishability conflict, reduce the number of simultaneously encoded categories (e.g., group small categories) rather than using crayon-bright hues.
