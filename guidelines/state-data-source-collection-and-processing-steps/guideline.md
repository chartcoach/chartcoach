---
id: state-data-source-collection-and-processing-steps
title: State the data source, collection method, and processing steps for each visualization
bibliography: references.bib
description: Disclose where the data came from, how it was collected, and what you
  changed or omitted so viewers can judge credibility.
labels:
- chart:any
- task:interpret
- visual:annotation
- impact:trust
- data:any
- audience:general
- quality:credibility
- documentation:provenance
---

## Add source, collection, and processing details <!-- role: advice -->

State where the data comes from, how it was collected, and how it was processed, including any exclusions or missing areas. Make the attribution specific enough that readers can identify the dataset and understand what was changed between raw data and the visualization.

## Why provenance details increase trust <!-- role: reason -->

When viewers can see the provenance of the data and the key transformation steps, they can evaluate reliability, spot potential bias, and interpret gaps as methodological choices rather than negligence or manipulation.

**Mechanism:** Clear sourcing and processing notes reduce ambiguity about how the numbers were produced and what is unknown, which lowers suspicion and supports more accurate interpretation.

**Evidence:** Viewers tend to trust a visualization more when they recognize the data source as reputable [@knoll_gulf_2025]. Methodological details in captions (including data collection) are appreciated because they help people form more complete and accurate takeaways [@koesten_what_2023]. Unexplained blank or missing areas can be interpreted as a credibility problem rather than missing data [@koesten_encountering_2025]. In journalistic practice, explicitly distinguishing sources (including mapping which parts come from which dataset) and crediting contributors is a common credibility-building norm [@gregory_data_2024].

**Notes:** “Processed” can include cleaning, filtering, imputation, aggregation, joining sources, model-based estimates, and any rule that removes records.

## When provenance disclosure matters most <!-- role: context -->

- **User Goal:** Decide whether to trust, share, or act on the chart’s message.
- **Task:** Interpret a claim, compare values, or assess risk/uncertainty in a real-world context.
- **Data:** Any dataset with potential missingness, filtering, joins across sources, estimates, or non-obvious definitions.
- **Chart Setting:** Public-facing dashboards, reports, journalism, policy briefings, crisis maps, or any visualization likely to be scrutinized.
- **Audience:** Mixed-literacy audiences, skeptical stakeholders, or viewers who cannot directly inspect the underlying data.
- **Success Criterion:** Readers can identify the source, understand key transformations and omissions, and do not misinterpret missingness as deception.

## When not to fully disclose details <!-- role: exceptions -->

**Break it when:** Releasing collection details or raw sources would violate privacy, security, contractual restrictions, or safety constraints. **Why:** Provenance transparency can expose sensitive information or create harm even if it increases credibility.

## Tradeoffs of adding provenance text <!-- role: costs -->

**Sacrifice:** You spend space and reader attention on metadata instead of the main message. **Risk:** Overly technical processing notes can confuse non-experts or invite unproductive nitpicking. **Mitigation:** Keep the on-chart note brief and link to a longer methodology appendix when needed.

## Common ways provenance goes wrong <!-- role: mistakes -->

**Mistake:** Listing only a vague source label (e.g., “internal data” or “various sources”) without a date, version, or link. **Why it fails:** Readers cannot verify the origin or judge timeliness and authority.
**Mistake:** Omitting how missing data, blanks, or exclusions were handled. **Why it fails:** Viewers may interpret gaps as concealment or poor quality rather than a known limitation.
**Mistake:** Combining multiple datasets without saying which elements come from which source. **Why it fails:** Readers cannot attribute uncertainty or bias to the correct component.

## Fast checks for sufficient context <!-- role: check -->

**Failure Sign:** A reader can’t answer “Where did this come from?” or “What changed from the raw data?” from the chart and its caption.\
**Quick Check:** Verify the visualization includes (or links to) a source, collection description, date range, and at least one sentence on major processing steps (including exclusions/missingness).\
**Stronger Test:** Ask a domain peer to restate the data provenance and key processing decisions after a 30-second scan; if they miss major steps, the context is insufficient.

## Practical ways to add provenance without clutter <!-- role: fix -->

- Add a compact source line with dataset name, publisher/owner, date range, and a stable link or identifier.
- Include a brief “Data notes” sentence covering major processing steps (filters, joins, aggregations, imputations, and exclusions).
- If multiple sources are used, annotate which series/layers/regions come from which dataset.
- When details are too long, link to a methods page or appendix and summarize only the highest-impact transformations on the visualization.
