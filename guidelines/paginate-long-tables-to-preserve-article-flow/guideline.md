---
id: paginate-long-tables-to-preserve-article-flow
title: Paginate long tables so readers notice content continues below
bibliography: references.bib
description: Use pagination when a table would otherwise exceed a screen and hide
  the continuation of an article.
labels:
- chart:table
- task:navigate
- visual:interaction
- impact:usability
- data:tabular
- audience:general
- context:storytelling
---

## Paginate when the table is taller than a desktop screen <!-- role: advice -->

Turn on pagination for long tables that would extend beyond a desktop screen, so the table doesn’t conceal that the article continues below.

## Pagination prevents tables from becoming scroll traps in stories <!-- role: reason -->

In story layouts, a long embedded table can dominate the scroll area and make readers assume they’ve reached the end of the piece.

**Mechanism:** Pagination chunks the table into discrete segments and signals incompleteness, reducing the chance that the table visually “swallows” the rest of the narrative.

**Evidence:** A rule of thumb is to keep a table shorter than a desktop screen to avoid readers missing that the article continues, and pagination helps make readers aware they haven’t reached the end [@muth_tables_2019].

**Notes:** This guidance is specific to storytelling contexts where the table sits inside a longer page.

## When pagination is the right interaction pattern <!-- role: context -->

- **User Goal:** Read an article and optionally consult the table without losing place.
- **Task:** Navigate through content while referencing tabular details.
- **Data:** Many rows that exceed a typical viewport height.
- **Chart Setting:** Embedded in an article page; vertical scrolling is also used for narrative flow.
- **Audience:** General readers who may not expect a large interactive component mid-article.
- **Success Criterion:** Readers continue past the table and understand there is more content.

## When not to paginate <!-- role: exceptions -->

**Break it when:** The main purpose is exploration and continuous scanning across many rows. **Why:** Pagination interrupts scanning and can make it harder to compare entries across pages [@muth_tables_2019].

## Tradeoffs of pagination <!-- role: costs -->

**Sacrifice:** Continuous overview of the full list at once. **Risk:** Users may not discover entries on later pages if they don’t paginate forward. **Mitigation:** Pair pagination with strong ordering or discovery aids like search when appropriate [@muth_tables_2019].

## Common pagination mistakes <!-- role: mistakes -->

**Mistake:** Leaving a very long table unpaginated inside an article. **Why it fails:** Readers may think the story ends at the table and stop scrolling [@muth_tables_2019].

## Quick checks for pagination need <!-- role: check -->

**Failure Sign:** The table visually occupies most of the page and the next paragraph is not visible without substantial scrolling. **Quick Check:** If the table is taller than a desktop viewport, pagination is likely warranted. **Stronger Test:** Observe whether readers continue scrolling past the table without prompting; drop-off at the table indicates it behaves like an endpoint [@muth_tables_2019].

## Alternatives if pagination harms the task <!-- role: fix -->

- Shorten the table by showing only the most relevant rows in the story context [@muth_tables_2019].
- Add a search field so readers can jump to relevant entries without paging through [@muth_tables_2019].
- Sort the table so the most important rows appear first, reducing reliance on later pages [@muth_tables_2019].
