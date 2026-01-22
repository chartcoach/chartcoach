---
id: use-line-graphs-to-evoke-x-y-interaction-descriptions-in-three-variable-data
title: "Use line graphs to elicit x\u2013y interaction descriptions in three-variable\
  \ data (when z is the legend variable)"
bibliography: references.bib
description: "Line graphs bias viewers toward describing how the x\u2013y relationship\
  \ changes across the legend variable (z)."
labels:
- chart:line
- task:describe
- task:interpret
- visual:continuity
- impact:salience
- data:multivariate
- audience:novice
- audience:expert
- complexity:medium
---

## Line graphs bias interpretations toward x–y interactions <!-- role: advice -->

Use a line graph when you want readers to spontaneously describe how the x–y relationship differs across the legend variable (z). Prefer this when highlighting interactions is more important than highlighting main effects.

## Why line continuity makes x–y interactions the default reading <!-- role: reason -->

Line graphs visually connect points into continuous traces, which encourages viewers to treat each trace as a unit and compare slopes or trends across traces, making an x–y-by-z interaction feel like the “main point.”

**Mechanism:** Good continuity groups points into lines, so viewers encode and compare line patterns (slopes/separations) rather than compute averages across categories.

**Evidence:** Viewers produced more x–y interaction descriptions with line graphs than with bar graphs in open-ended “main point” descriptions of three-variable graphs [@shahBarLineGraph2011]. Line graphs also produced a larger imbalance favoring x–y interaction descriptions over z–y interaction descriptions than bar graphs did [@shahBarLineGraph2011].

**Notes:** This effect reflects salience in open-ended interpretation and does not guarantee deep conceptual understanding of statistical interaction.

## When this applies: interaction-first communication in multivariate displays <!-- role: context -->

- **User Goal:** Identify “what’s going on” in the relationships, especially moderation across groups.
- **Task:** Open-ended summarization of the main takeaway from a three-variable display.
- **Data:** One dependent variable (y) and two independent variables (x and z), each with multiple levels (e.g., 3×3).
- **Chart Setting:** Static report, paper, slide, or non-interactive display where readers choose what to mention.
- **Audience:** Mixed graph literacy; readers may default to visually salient patterns.
- **Success Criterion:** Readers primarily report the intended x–y-by-z interaction without heavy prompting.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You need readers to focus on main effects (averaged trends across the third variable) as the key message. **Why:** Line graphs make the interaction visually dominant and can reduce the likelihood that readers compute or report main effects in open-ended tasks [@shahBarLineGraph2011].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose emphasis on main effects because interaction patterns consume attention and description space. **Risk:** Readers may over-prioritize interaction-like interpretations even when your message depends on averaged comparisons. **Mitigation:** Plan for explicit support if main effects must be communicated alongside the interaction.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a line graph for multivariate data when the intended takeaway is an averaged difference across x levels (an x–y main effect). **Why it fails:** Viewers tend to describe interaction patterns from line graphs rather than compute and report main effects in open-ended descriptions [@shahBarLineGraph2011].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers’ summaries talk about “lines diverging/converging” but omit averaged differences you care about. **Quick Check:** Ask two readers to write 2–4 sentences of the “main point”; see whether they mention the intended main effect unprompted. **Stronger Test:** Run a small pilot comparing line vs bar versions and code whether x–y interaction vs main effect language dominates [@shahBarLineGraph2011].

## What to do instead <!-- role: fix -->

- Use a bar graph if the priority is encouraging main-effect-oriented summaries rather than interaction-oriented summaries.
- Provide an explicit statement of the key main effect in accompanying text when a line graph must be used.
- Reframe the display goal so the interaction is the intended takeaway, and ensure labels/legend align with that interpretation.
