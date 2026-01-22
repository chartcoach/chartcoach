---
id: downweight-large-and-highly-significant-effects-in-low-ppv-fields
title: "Downweight visually dramatic effects when the field\u2019s PPV is low and\
  \ bias may dominate"
bibliography: references.bib
description: In low-PPV fields, very large or highly significant reported effects
  can reflect bias rather than true relationships.
labels:
- chart:scatter
- task:interpret
- visual:emphasis
- impact:trust
- data:inferential
- audience:expert
- domain:bias-detection
---

## Do not equate extreme effects with stronger truth in low-PPV settings <!-- role: advice -->

When a research area has low pre-study odds and substantial bias risk, avoid visual emphasis that treats the largest or most significant effects as the most credible. Instead, present extreme effects as potential bias signals requiring extra skepticism.

## Why extremes can be bias measures in null or low-signal fields <!-- role: reason -->

If a field has very low PPV, the published literature’s observed effect sizes can be driven largely by net bias and selective reporting rather than true underlying effects; in a fully null field, deviations from null reflect bias magnitude.

**Mechanism:** Reducing “winner” emphasis prevents readers from mistaking selection- and bias-amplified extremes for strong evidence, improving calibration in noisy literatures.

**Evidence:** In settings with very low PPV, claimed research findings may act as accurate measures of prevailing bias, and in a null field the distribution of claimed effect sizes reflects bias rather than true relationships [@ioannidisWhyMostPublished2005]. Large and highly significant effects can therefore be more consistent with large bias in many modern research fields than with important discoveries [@ioannidisWhyMostPublished2005].

**Notes:** This does not say true large effects never exist; it applies when the field-level conditions imply low PPV.

## When this applies in evidence displays <!-- role: context -->

- **User Goal:** Decide how much weight to give to extreme reported effects.
- **Task:** Interpret effect size patterns under publication/selection pressures.
- **Data:** Published significant findings in exploratory domains; small effects expected; many tested relationships.
- **Chart Setting:** “Top effects” plots, ranked effect size charts, literature-wide effect summaries.
- **Audience:** Experts who may translate findings into decisions or follow-up studies.
- **Success Criterion:** Less overconfidence in extremes; better skepticism in low-signal environments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The domain has high pre-study odds and low bias risk and extreme effects are supported by high-powered confirmatory evidence. **Why:** In that context, extreme effects may genuinely indicate strong relationships.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reduced immediacy and excitement in storytelling visuals. **Risk:** Readers may underreact to genuinely important large effects. **Mitigation:** Keep confirmatory status and study quality visible so true strong evidence can still stand out for the right reasons.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Sorting by p-value and using the most saturated color for the smallest p-values as “best.” **Why it fails:** It amplifies selection artifacts and can spotlight bias-driven extremes.
- **Mistake:** Using “largest effect” as synonymous with “most important discovery” without field context. **Why it fails:** In low-PPV fields, extremes can be dominated by bias rather than truth.

## Quick tests <!-- role: check -->

**Failure Sign:** The most emphasized marks are always the most extreme effects, regardless of study design quality or field context. **Quick Check:** Ask whether the visualization would still look compelling if the field were null; if yes, it may be rewarding bias patterns. **Stronger Test:** Compare emphasis patterns against a labeling of confirmatory vs exploratory studies; if exploratory extremes dominate attention, the design is miscalibrated.

## What to do instead <!-- role: fix -->

- Encode confirmatory status, study power, and bias risk alongside effect magnitude so emphasis is not driven by magnitude alone.
- Add a reference annotation stating the field’s likely low PPV context (low R, many tests, flexibility) near the visual takeaway.
- Present effect sizes with uncertainty and avoid “top-N” framing when it implies a ranking of truth.
- Include a companion view that shows the full distribution of reported effects to reveal patterns consistent with selection or bias.
