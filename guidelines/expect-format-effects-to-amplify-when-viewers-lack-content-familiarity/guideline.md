---
id: expect-format-effects-to-amplify-when-viewers-lack-content-familiarity
title: Expect stronger reliance on visually salient patterns when content is unfamiliar
  (and choose formats accordingly)
bibliography: references.bib
description: When variable content is unfamiliar, viewers default more to salient
  interaction descriptions shaped by format.
labels:
- chart:bar
- chart:line
- task:interpret
- impact:robustness
- data:multivariate
- audience:novice
- complexity:medium
- custom:top-down-bottom-up
---

## For unfamiliar topics, design for bottom-up reading because viewers will lean on salience <!-- role: advice -->

When your audience is unfamiliar with the variables or lacks expectations about what the data should look like, choose the chart format assuming viewers will describe the most visually salient interaction pattern rather than infer main effects.

## Why unfamiliarity shifts interpretation toward surface-driven chunking <!-- role: reason -->

Without strong expectations from domain knowledge, viewers’ interpretation is more driven by perceptual grouping, making the “default” description align with what is most visually organized by the display.

**Mechanism:** Reduced top-down guidance (expectations/goals tied to familiar content) increases reliance on bottom-up grouping cues, which shifts what viewers select as the “main point.”

**Evidence:** Viewers were somewhat more likely to describe interactions for unfamiliar than familiar graphs, and x–y interaction descriptions were especially likely when unfamiliar data were shown in the line format that makes x–y interactions most salient [@shahBarLineGraph2011]. Viewers generated far fewer main-effect inferences for unfamiliar content than familiar content overall [@shahBarLineGraph2011].

**Notes:** This guideline targets open-ended comprehension; explicit question prompts may change the pattern.

## When this applies: low-expectation, low-context graph reading <!-- role: context -->

- **User Goal:** Get a quick sense of what the data show without deep prior beliefs.
- **Task:** Open-ended “main point” interpretation in short text.
- **Data:** Multivariate (three-variable) data where both interactions and main effects are plausible summaries.
- **Chart Setting:** Situations where readers cannot be trained on the domain before reading (news, broad-audience reports).
- **Audience:** Readers with low content familiarity for the variable names/constructs.
- **Success Criterion:** The chart’s most salient pattern matches your intended takeaway because viewers will default to it.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You can supply strong framing (e.g., explicit analytic questions or instructions) that constrains what viewers should extract. **Why:** The evidence is based on unconstrained “main point” descriptions where viewers select what to mention [@shahBarLineGraph2011].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to prioritize one salient message over showing a “neutral” view of the data. **Risk:** Viewers may miss less salient but important relationships that you did not make visually prominent. **Mitigation:** Use accompanying text to specify which relationship to attend to if multiple are important.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming unfamiliar audiences will compute and report main effects from a multivariate chart without additional support. **Why it fails:** Main-effect inference reporting drops sharply for unfamiliar content in open-ended interpretation [@shahBarLineGraph2011].

## Quick tests <!-- role: check -->

**Failure Sign:** Reader summaries focus on whichever pattern is visually loudest, even when it is not your intended message. **Quick Check:** Ask a few unfamiliar readers to summarize the chart; see whether their summaries converge on the same salient interaction framing. **Stronger Test:** Run a small counterbalanced study with unfamiliar variable labels and code interaction vs main-effect language to verify which message dominates by format [@shahBarLineGraph2011].

## What to do instead <!-- role: fix -->

- Add a short prompt telling readers what relationship to describe (e.g., averaged difference vs interaction).
- Provide a second, simplified view that directly shows the intended main effect instead of requiring mental collapsing.
- Redesign variable placement (what goes on x vs in the legend) so the intended comparison is supported by the strongest grouping cue.
