---
id: treat-occlusion-as-a-data-dependent-risk-and-use-3d-when-the-data-structure-keeps-it-low
title: Treat occlusion as a data-dependent risk and use 3D when the data structure
  keeps it low
bibliography: references.bib
description: Use 3D when typical datasets for the domain produce low occlusion (e.g.,
  long-tail patterns), and avoid 3D when occlusion dominates.
labels:
- chart:3d
- task:see
- visual:occlusion
- impact:clarity
- data:distribution
- audience:expert
- custom:domain-fit
---

## Choose 3D only when domain data keeps occlusion manageable <!-- role: advice -->

Use 3D encodings when the expected data distributions and layouts in the target domain keep occlusion low enough that important items and anomalies remain visible from the intended view.

## Why occlusion is sometimes acceptable and sometimes fatal <!-- role: reason -->

Occlusion is not unique to 3D (2D overplotting exists too), but 3D can amplify hiding; whether it harms depends on the dataset structure and the visualization’s anchoring and arrangement.

**Mechanism:** When a few large values dominate and many values are small (or the layout spaces items regularly), the visible structure can remain readable while occlusion stays limited; in dense, uniformly populated scenes, occlusion hides too much.

**Evidence:** Occlusion occurs in both 2D and 3D, and in specialized domain visualizations the typical data behavior (e.g., long-tail distributions) can reduce occlusion so expected patterns and anomalies remain apparent [@brath3DInfoVisHere2014].

**Notes:** This is a selection criterion for whether 3D is appropriate, not a guarantee of success.

## When this applies <!-- role: context -->

- **User Goal:** See patterns and anomalies without losing items behind others.
- **Task:** Visual scanning and comparison in a 3D scene.
- **Data:** Domain datasets with predictable structure (e.g., long-tail or regular spacing) that reduces overlap in 3D.
- **Chart Setting:** 3D layout with an intended primary viewpoint.
- **Audience:** Users who can tolerate some occlusion but not widespread hidden data.
- **Success Criterion:** Key values and anomalies are visible without constant viewpoint changes.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The dataset is dense and evenly populated such that many items will occlude regardless of viewpoint. **Why:** The display becomes incomplete and biased toward front-most items [@brath3DInfoVisHere2014].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to constrain layouts to preserve visibility. **Risk:** Viewers may infer absence from invisibility (hidden items). **Mitigation:** Treat visibility as a first-class requirement in layout selection.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Dismissing 3D solely because occlusion exists. **Why it fails:** 2D also overplots, and some domains’ data keep 3D occlusion low enough to be workable [@brath3DInfoVisHere2014].
- **Mistake:** Assuming interaction will solve occlusion in all contexts. **Why it fails:** Navigation may be unavailable or impractical, making hidden data effectively lost [@brath3DInfoVisHere2014].

## Quick tests <!-- role: check -->

**Failure Sign:** Many items disappear behind others in the default view. **Quick Check:** Estimate what fraction of marks are fully visible from the primary viewpoint. **Stronger Test:** Sample several real datasets from the domain and verify visibility remains high across them.

## What to do instead <!-- role: fix -->

- Use 2D separation (small multiples) to avoid overlap when occlusion would be pervasive.
- Filter, aggregate, or sample to reduce mark count in the 3D scene.
- Use a linked 2D detail view to ensure hidden items can still be inspected precisely.
- Switch to a representation with regular spacing or surfaces if free-floating marks cause heavy occlusion.
