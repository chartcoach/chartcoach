---
id: add-brief-explanations-that-ensemble-tracks-are-a-subset-not-deterministic
title: Add brief explanations that ensemble tracks are a subset of many model runs
  (not deterministic paths)
bibliography: references.bib
description: Use short, plain-language instruction to shift interpretation from deterministic
  lines to sampled uncertainty.
labels:
- chart:ensemble-track
- task:interpret-uncertainty
- visual:annotation
- impact:comprehension
- data:uncertainty
- audience:novice
- domain:hurricane
---

## Add brief explanations that ensemble tracks are a subset of many model runs (not deterministic paths) <!-- role: advice -->

When presenting ensemble hurricane tracks, explicitly state that each line is one model output and that the displayed lines are only a subset of many possible paths.

## Instructions can activate knowledge-driven processing but cannot fully override marks <!-- role: reason -->

Without explanation, viewers may interpret each line as a meaningful deterministic forecast, which amplifies the effect of a line crossing a location. Minimal explanatory instruction can shift interpretation toward uncertainty and reduce, but not eliminate, the collocation-driven inflation of risk judgments.

**Mechanism:** Text/video instruction provides a top-down mental model (“sample from many runs”) that competes with bottom-up salience of crisp intersecting marks.

**Evidence:** Compared to no instructions, providing visualization-focused instructions about how ensemble paths are generated significantly reduced the collocation effect in damage judgments [@padillaPowerfulInfluenceMarks2020]. Even with instructions, a residual collocation effect remained, indicating the visual mark intersection continued to influence judgments [@padillaPowerfulInfluenceMarks2020].

**Notes:** In this study, general visualization instructions also improved comprehension that the display does not show all possible paths [@padillaPowerfulInfluenceMarks2020].

## Context: Static ensemble track displays used by general audiences <!-- role: context -->

- **User Goal:** Understand uncertainty in storm track and assess local risk.
- **Task:** Interpret what a set of lines implies about future locations.
- **Data:** Multiple possible storm tracks from an ensemble model.
- **Chart Setting:** Static images in print, web, or brief broadcast segments.
- **Audience:** Viewers with limited prior training in ensemble forecasts.
- **Success Criterion:** Viewers interpret tracks as sampled uncertainty, not a small set of deterministic alternatives.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The display is used only with trained experts who already share the ensemble-sampling mental model. **Why:** The explanatory text may be redundant and consume scarce display space or attention [@padillaPowerfulInfluenceMarks2020].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Adding explanatory text or instruction consumes time/space and may not be read in fast-paced settings. **Risk:** Even read instructions may not eliminate intersection-driven bias, leading to overconfidence in “fixed” interpretations. **Mitigation:** Treat instruction as partial mitigation and validate behavior, not only self-report, after adding it [@padillaPowerfulInfluenceMarks2020].

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming viewers will infer “subset of many model runs” from the presence of multiple lines alone. **Why it fails:** Viewers can default to deterministic interpretations and overweight single line intersections [@padillaPowerfulInfluenceMarks2020].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers say the display shows all possible paths or interpret any single line as highly meaningful. **Quick Check:** Include a comprehension question asking whether the plotted tracks are all paths or a subset. **Stronger Test:** Measure whether the on-line vs off-line damage gap shrinks after adding the explanation [@padillaPowerfulInfluenceMarks2020].

## Fix: What to do instead <!-- role: fix -->

- Add a concise note near the visualization stating that the displayed tracks are only a subset of many model runs.
- Include a short description that the center of the cluster reflects the most likely path direction.
- Add a comprehension check in the surrounding content (caption, sidebar, onboarding) to verify viewers understand “subset” versus “all.”
- If misunderstanding persists, use stronger task-targeted instruction that directly addresses the intersection-overweighting tendency.
