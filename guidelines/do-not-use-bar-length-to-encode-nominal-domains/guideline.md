---
id: do-not-use-bar-length-to-encode-nominal-domains
title: Do Not Use Bar Length to Encode Nominal Categories
bibliography: references.bib
description: Bar-length encodings imply ordered magnitude; avoid them when the encoded
  domain is nominal.
labels:
- chart:bar
- task:categorize
- visual:length
- impact:correctness
- data:categorical
- audience:any
- scale:nominal
- source:mackinlay-1986
---

## The Rule <!-- role: advice -->

Do not use bar charts (bar length) to encode a nominal (unordered) domain.

## The Logic <!-- role: reason -->

Bar charts introduce an ordering (and implied magnitude comparison) through bar length; this encodes additional facts (e.g., “A > B”) that are not present for nominal domains, violating expressiveness (“only the facts”).

- **The Principle:** Some graphical languages add facts via geometric relationships
- **The Evidence:** The paper’s Nation example shows bar length implies ordering and thus misrepresents nominal data [@mackinlayAutomatingDesignGraphical1986b].

## Where to Apply <!-- role: context -->

- **User Goal:** Show membership/association with a category (e.g., country, type, label) without implying rank
- **Data Type:** Nominal categories (unordered sets)
- **Audience:** Any

## When to Break It <!-- role: exceptions -->

- **Scenario:** The categories are truly ordered or quantitative (or you explicitly intend to encode an ordering).
- **Reason:** Then bar length’s implied ordering matches the data semantics rather than adding incorrect facts [@mackinlayAutomatingDesignGraphical1986b].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a familiar “big vs small” visual metaphor.
- **The Risk:** If you mistakenly use bars, viewers may infer a ranking among categories that is not meaningful [@mackinlayAutomatingDesignGraphical1986b].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping bars but making them “all the same length,” while still visually suggesting an ordered axis meaning.
- **Why it fails:** The bar form itself invites magnitude reading; it still risks implied ordering [@mackinlayAutomatingDesignGraphical1986b].

## How to Check <!-- role: check -->

- **Visual Sign:** The viewer can plausibly answer “which category is bigger/better?” from bar length, even though that question is meaningless.
- **The Test:** Ask: “Does length encode an order or magnitude here?” If yes and the domain is nominal, the design is wrong [@mackinlayAutomatingDesignGraphical1986b].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace bars with equal-sized marks (a plot/dot chart) positioned to indicate category membership.
- **Best Fix:** Use a graphical language whose conventions do not encode ordering for nominal domains (e.g., plot chart for nominal categories) [@mackinlayAutomatingDesignGraphical1986b].
