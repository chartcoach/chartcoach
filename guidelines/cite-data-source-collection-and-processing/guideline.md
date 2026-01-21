---
id: cite-data-source-collection-and-processing
title: Disclose Data Sources, Collection Methods, and Processing Steps
bibliography: references.bib
description: Build credibility by clearly stating where data comes from, how it was
  collected, and what transformations or omissions were applied.
labels:
- chart:any
- task:inform
- visual:annotation
- impact:credibility
- data:provenance
- audience:general
- context:methods
---

## The Rule <!-- role: advice -->

State the data source, how it was collected, and how it was processed (including cleaning, aggregation, merging, and omissions) directly in the visualization or its caption.

## The Logic <!-- role: reason -->

Method details reduce ambiguity about what the viewer is seeing and why it should be trusted: reputable sources increase perceived trustworthiness, and transparent methods prevent viewers from interpreting gaps or missing areas as incompetence or manipulation. Captions with collection and methodology details also help readers form more accurate interpretations of what the visualization means.

- **The Principle:** Provenance transparency increases perceived credibility and reduces suspicious inferences.
- **The Evidence:** Viewers’ trust rose with reputable sources [@knoll_gulf_2025]; methodological details in captions were appreciated and improved interpretation quality [@koesten_what_2023]; unexplained blanks on crisis maps triggered distrust [@koesten_encountering_2025]; professional practice includes explicit source references, distinguishing dataset types and attributing sources to specific chart components [@gregory_data_2024].

## Where to Apply <!-- role: context -->

Use this whenever trust, accountability, or interpretation depends on understanding where the data came from and what was done to it.

- **User Goal:** Assess credibility, interpret correctly, and understand what is included/excluded.
- **Data Type:** Any dataset with non-obvious provenance, multiple sources, cleaning steps, missingness, or derived metrics.
- **Audience:** General public, newsroom readers, policy stakeholders, crisis-map users, and any skeptical or high-stakes audience.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Confidential or sensitive collection methods (e.g., protected sources, security-sensitive monitoring).

- **Reason:** Disclosing methods could endanger people, violate privacy/legal constraints, or enable gaming; provide a safe high-level description and governance notes instead.

- **Scenario:** Ultra-space-constrained graphics (e.g., tiny social thumbnails, dashboard tiles).

- **Reason:** Full provenance text may overwhelm the display; use a short source line plus a link/hover/tap for full methodology.

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and attention that could be used for the main message.
- **The Risk:** Too much methodological detail can distract, increase reading time, or invite misinterpretation if described unclearly.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Writing “Source: Internet,” “Source: internal data,” or “Source: analysis” with no specifics.

- **Why it fails:** It does not let viewers judge reputability or reproduce the logic, undermining the credibility benefits tied to reputable sources [@knoll_gulf_2025].

- **The Wrong Fix:** Hiding processing decisions (filters, dropped rows, imputation, smoothing) or leaving blanks without explanation.

- **Why it fails:** Viewers may interpret missing areas or gaps as untrustworthy or deceptive rather than as known missingness [@koesten_encountering_2025].

- **The Wrong Fix:** Combining multiple sources without mapping which visual elements come from which dataset.

- **Why it fails:** Users cannot tell what evidence supports which claim; best practice is to specify which parts draw from which sources [@gregory_data_2024].

## How to Check <!-- role: check -->

- **Visual Sign:** A viewer could not answer “Where is this data from, when/how was it collected, and what was done to it?” from the chart, caption, or a single click/hover.
- **The Test:** Do a “provenance audit”: ask a colleague to list (1) source(s), (2) collection period and method, (3) key processing steps and omissions. If they guess or miss items, the visualization lacks sufficient context [@koesten_what_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a compact footer/caption line: source name + collection window + link (e.g., “Source: Agency X survey (May–Jun 2024), n=…, weighted; cleaning/aggregation notes: …”).
- **Best Fix:** Provide a structured methods block (or expandable panel) that lists: dataset(s) with identifiers/links, collection method and timeframe, preprocessing pipeline (filters, joins, outlier handling, smoothing), treatment of missing data (and why blanks appear), and per-component attribution when multiple sources are used [@gregory_data_2024].
