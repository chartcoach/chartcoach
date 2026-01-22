---
id: do-not-assume-low-graphicacy-viewers-will-generate-main-effect-inferences-from-multivariate-graphs
title: Do not rely on low-graphicacy audiences to generate main-effect inferences
  from multivariate graphs
bibliography: references.bib
description: Low graph-literacy viewers rarely report main effects in open-ended interpretations,
  even when format supports them.
labels:
- chart:bar
- chart:line
- task:infer
- impact:accessibility
- data:multivariate
- audience:novice
- complexity:medium
- custom:graphicacy
---

## For low-graphicacy audiences, treat main effects as non-obvious unless explicitly supported <!-- role: advice -->

When your audience has low graphicacy (graphical literacy), assume they will not reliably compute and report main effects from a three-variable graph in open-ended interpretation, even in formats that make comparisons easier.

## Why main effects require skills beyond noticing patterns <!-- role: reason -->

Main effects in multivariate displays often require mentally collapsing across a variable (e.g., averaging or checking consistency across groups), which depends on knowing what that operation means in a graph and how to execute it during interpretation.

**Mechanism:** Low graphicacy reduces the likelihood of performing the mental transformations needed for aggregation-based inferences, so viewers stay closer to surface descriptions.

**Evidence:** Higher graphicacy viewers made more main-effect inferences overall than lower graphicacy viewers, and the strongest inference generation occurred when graphicacy was high, content was familiar, and the format (bar graphs) supported those inferences [@shahBarLineGraph2011]. Graph skills did not meaningfully affect interaction-description rates, consistent with interaction descriptions often requiring little transformation beyond reading salient structure [@shahBarLineGraph2011].

**Notes:** The study operationalized graphicacy with a graph skills test and assessed inference generation through written “main point” descriptions.

## When this applies: communicating computed summaries to general audiences <!-- role: context -->

- **User Goal:** Extract averaged relationships (main effects) from multivariate results.
- **Task:** Unprompted summarization or explanation of “most important” findings.
- **Data:** Three-variable graphs where main effects are not directly plotted as separate aggregates.
- **Chart Setting:** Public-facing reports, education settings, or broad-audience dashboards where graph literacy varies widely.
- **Audience:** Readers likely to have low graph interpretation skills (as measured by limited ability to answer graph reasoning items).
- **Success Criterion:** The intended main effect is understood without requiring the reader to mentally compute it.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your audience is screened or trained to have high graphicacy and the task includes explicit prompts to compute main effects. **Why:** The evidence concerns open-ended description without targeted prompting and includes substantial individual differences by graph skill [@shahBarLineGraph2011].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to add supporting explanation or additional displays, increasing space and production time. **Risk:** Overloading the display with extra elements can distract from the core message. **Mitigation:** Keep the main effect representation separate from the main multivariate view when clarity is the priority.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming that because a main effect is “in the data,” most readers will state it as the main takeaway. **Why it fails:** Main-effect inference reporting depends strongly on graphicacy and content familiarity, and is not guaranteed by the presence of the data alone [@shahBarLineGraph2011].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers restate only visible group differences or interactions and do not mention any averaged relationship. **Quick Check:** Ask readers to write 2–4 sentences of the main point; check whether a main effect is present without prompting. **Stronger Test:** Segment feedback by a short graph-skills screener and verify whether low-scorers omit main effects disproportionately [@shahBarLineGraph2011].

## What to do instead <!-- role: fix -->

- Add a separate display that explicitly shows the main effect (collapsed across the third variable) rather than requiring mental aggregation.
- Provide a short, direct sentence stating the main effect next to the graph.
- Use a format that supports easier comparisons (such as grouped bars) when you cannot add extra explanatory elements.
