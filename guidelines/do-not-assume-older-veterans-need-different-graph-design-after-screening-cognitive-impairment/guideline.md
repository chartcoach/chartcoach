---
id: do-not-assume-older-veterans-need-different-graph-design-after-screening-cognitive-impairment
title: Do not assume older veterans need different graph designs after screening for
  cognitive impairment
bibliography: references.bib
description: If older veterans are cognitively intact, do not treat age alone as a
  reason to change health literacy, numeracy, or graph-based materials.
labels:
- chart:any
- task:communicate-risk
- visual:any
- impact:accessibility
- data:any
- audience:patient
- population:veterans
- complexity:planning
---

## Avoid age-only tailoring when users are cognitively intact <!-- role: advice -->

If your older veteran audience has been screened as cognitively intact, do not tailor graphs or quantitative materials based on age alone; tailor based on measured or observed comprehension needs instead.

## Why age-only tailoring can misallocate effort <!-- role: reason -->

When age differences in comprehension-related skills are explained by other factors, designing around age alone can miss the true drivers of misunderstanding and may ignore younger users who also struggle.

**Mechanism:** Targeting the actual constraint (health literacy/numeracy/graph literacy) rather than age reduces false assumptions and aligns support with need.

**Evidence:** In this veteran sample, older and younger participants did not differ in health literacy, objective numeracy, or graph literacy after adjustment for covariates, and multivariate tests showed no significant effect of age [@rodriguezHealthLiteracyNumeracy2013]. Older participants differed from younger participants mainly in trust in physicians, not in the literacy measures after adjustment [@rodriguezHealthLiteracyNumeracy2013].

**Notes:** This does not imply older adults never need adaptations; it implies age alone was not a reliable discriminator in this setting.

## When this applies in design decisions <!-- role: context -->

- **User Goal:** Understand patient education materials that may include numbers and graphs.
- **Task:** Extract values, compare quantities, interpret a chart in a clinic workflow.
- **Data:** Any, especially quantitative information intended to support decisions.
- **Chart Setting:** Veteran outpatient settings where cognitive impairment and depression are screened/excluded for the target workflow.
- **Audience:** Mixed-age veterans, with cognitive intactness verified.
- **Success Criterion:** Tailoring resources are spent on observed comprehension barriers, not demographic proxies.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You have not screened for cognitive impairment or sensory limitations in the older audience. **Why:** The study’s lack of adjusted age effects occurred in a cognitively intact sample, and unmeasured impairments can change requirements.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Less ability to use age as a simple segmentation variable. **Risk:** Teams may under-prepare for age-associated impairments if they conflate “cognitively intact” with “no additional needs.” **Mitigation:** Treat cognition and sensory capability as separate design constraints from age.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Create “senior-only” simplified charts by default. **Why it fails:** Age was not a significant adjusted predictor of the literacy/numeracy/graph literacy outcomes in this sample [@rodriguezHealthLiteracyNumeracy2013].
- **Mistake:** Ignore younger users when simplifying. **Why it fails:** The largest adjusted gaps were race-by-age (younger African American vs younger White), not older vs younger overall [@rodriguezHealthLiteracyNumeracy2013].

## Quick tests <!-- role: check -->

**Failure Sign:** Age-targeted versions show no measurable comprehension improvement in older users but add maintenance overhead. **Quick Check:** Compare comprehension outcomes between older and younger users on the same artifact before segmenting by age. **Stronger Test:** Segment based on a brief skill/comprehension screen rather than age and compare error rates.

## What to do instead <!-- role: fix -->

- Use brief comprehension checks (or observed misunderstandings) to trigger adaptations rather than age thresholds.
- Maintain one clear baseline design and add optional clarifying explanations as needed.
- Allocate testing to the subgroups with demonstrated lower performance (e.g., race-by-age groups) rather than age alone.
- Document which parts of a chart require inference so you can simplify only the high-burden steps when issues appear.
