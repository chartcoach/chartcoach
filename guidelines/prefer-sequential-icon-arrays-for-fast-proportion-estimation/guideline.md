---
id: prefer-sequential-icon-arrays-for-fast-proportion-estimation
title: Prefer sequential (blocked) icon arrays over random ones for fast proportion
  estimation
bibliography: references.bib
description: Sequentially grouped icon arrays support more accurate and less variable
  first-glance proportion estimates than randomly scattered arrays.
labels:
- chart:icon-array
- task:estimate
- visual:position
- impact:clarity
- data:proportion
- audience:novice
- domain:risk-communication
---

## Use sequential (blocked) icon arrays for first-glance proportion reading <!-- role: advice -->

Use a sequential (blocked) arrangement of colored icons when you need viewers to quickly estimate a proportion at a glance. Prefer this format over randomly scattered icons when the viewer will not have time to count or scrutinize.

## Grouping reduces perceptual summation load and estimation variability <!-- role: reason -->

Randomly scattered affected icons force viewers to mentally sum many noncontiguous patches, increasing cognitive load and noise in estimation under time pressure, whereas blocked icons create a clearer part-to-whole area that can be judged more directly.

**Mechanism:** Contiguous blocks support faster gestalt judgments of area/proportion; dispersed marks require effortful visual aggregation, producing larger bias and higher between-person variability.

**Evidence:** Under a 10-second deadline, randomly arranged stick-figure arrays produced higher mean overestimation and wider variability than sequential (blocked) arrays for most tested proportions [@anckerEffectArrangementStick2011]. Relative inaccuracy was about 10% higher for random than sequential arrangements in a mixed model controlling for numeracy and education [@anckerEffectArrangementStick2011].

**Notes:** The accuracy advantage for sequential arrangements was most pronounced away from ~40–50%, where random and sequential were more similar.

## When fast, unlabeled proportion judgments are expected <!-- role: context -->

- **User Goal:** Rapidly gauge “how many” are affected from an icon array.
- **Task:** Estimate a percentage/proportion without counting.
- **Data:** Part-to-whole proportions shown by colored icons.
- **Chart Setting:** Brief exposure, glanceable dashboard/handout, or any time-limited viewing.
- **Audience:** General public, including low-numeracy viewers.
- **Success Criterion:** Low bias and low between-viewer variance in estimated proportion.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The goal is to visually emphasize randomness/unpredictability rather than enable accurate first-glance proportion estimation. **Why:** Random scattering can be perceived as more “random” but is less reliable for reading exact proportions quickly [@anckerEffectArrangementStick2011].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Sequential blocks can look less “random” or less representative of chance processes. **Risk:** Viewers may infer clustering or a localized outbreak if the block implies spatial grouping rather than a mere count. **Mitigation:** Treat sequential grouping as a display convention (not a spatial claim) in surrounding explanation when needed.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Using random scatter icon arrays as the default for risk graphics that must be compared or read quickly. **Why it fails:** Random arrangements inflate and destabilize first impressions of the proportion, especially at low and high values [@anckerEffectArrangementStick2011].
- **Mistake:** Assuming average accuracy implies individual viewers will reliably distinguish nearby risks. **Why it fails:** Even with modest mean error, variance can be high enough to confuse moderately different proportions [@anckerEffectArrangementStick2011].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Different people give widely different percentage guesses for the same icon array, or the same person’s guess shifts noticeably when only the arrangement changes. **Quick Check:** Show a random and a sequential version of the same proportion for 10 seconds each and compare how often estimates differ. **Stronger Test:** In a small pilot, test whether users correctly rank two nearby proportions (for example, ~29% vs ~40%) when shown in the chosen format [@anckerEffectArrangementStick2011].

## Fix: What to do instead <!-- role: fix -->

- Convert scattered colored icons into a contiguous block (sequential arrangement) while keeping the same total icon count.
- If you must show randomness, keep a sequential “reading version” for estimation tasks and reserve the random version for illustrating unpredictability.
- Reduce reliance on glance-based estimation by adding explicit numeric labels near the graphic.
- If side-by-side risk comparison is required, ensure both icon arrays use the same sequential grouping so differences remain visually discriminable.
