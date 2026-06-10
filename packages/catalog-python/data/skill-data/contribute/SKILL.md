---
name: contribute
description: Use this to draft local ChartCoach catalog improvement issues. Teaches agents how to turn individual retrieval friction into community-facing improvement signals for missing topics, wording gaps, labels, source gaps, and curation requests without posting anything.
---

# ChartCoach Contribute

ChartCoach treats source-traced visualization knowledge as an evolving shared resource. Friction in one user's critique, recommendation, or consultation workflow can reveal catalog improvements that help the wider community: missing coverage, unclear wording, weak labels, or sources that need checking.

Use this skill to turn those improvement signals into local Markdown issue drafts. The issue target is `https://github.com/chartcoach/catalog/issues/new`, but do not open, submit, post, or disclose anything by default. Draft the issue for human review. The human decides whether to share it, revise private details, attach artifacts, or open it.

Load `core` first when catalog source, index setup, package extras, or output formats are unclear. This workflow assumes the `chartcoach` command already points at the intended Catalog Instance.

## What Belongs Here

Draft a catalog issue when the problem is about catalog content or curation:

- missing guideline or missing topic area
- existing guideline is hard to retrieve
- existing guideline is too narrow, too broad, ambiguous, or poorly phrased
- labels, label families, or section roles made the right record hard to find
- guideline may need splitting, merging, cross-linking, or duplicate review
- source reference is missing, weak, stale, or needs checking
- recurring coverage skew by chart family, audience, task, literacy level, medium, or data type
- manifest vocabulary does not describe a recurring retrieval or authoring need

Route away from catalog issues when the problem is not content:

| Problem                                                                        | Route                                                                  |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| CLI bug, command crash, install failure, or confusing command syntax           | ChartCoach tooling issue.                                              |
| Infrastructure, package, cache, release, or download failure                   | ChartCoach tooling or infrastructure issue.                            |
| Pure index false positive                                                      | Retrieval tooling or index diagnostics.                                |
| Index false positive caused by weak wording, labels, or missing topic coverage | Catalog issue.                                                         |
| Private project preference or one-off user policy                              | Keep local unless the human wants to propose a general catalog change. |

## Preserve The Retrieval Trace

Start from what happened in the workflow:

| Field             | Record                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| User task         | The chart critique, recommendation, consultation, or search question.                                |
| Retrieval path    | Commands, search terms, labels, roles, and indexed queries tried.                                    |
| Result            | Missing record, partial match, surprising match, duplicate, weak citation, or hard-to-apply wording. |
| Content diagnosis | Why the problem appears to be catalog content rather than tooling.                                   |
| Candidate records | Guideline ids that partially match, conflict, duplicate, or need revision.                           |

Use exact reads before naming records in the issue:

```sh
chartcoach catalog read <guideline-id> --source-detail minimal --format markdown
chartcoach catalog cite <guideline-id> <another-guideline-id> --format markdown
```

Discovery commands produce candidate ids. `catalog read` verifies the record text. `catalog cite` produces the public guideline page and formatted source references for verified ids.

If no guideline id was found, say which searches failed and which broader concepts were tried.

## Classify The Catalog Change

Choose one primary issue type:

| Issue type          | Use when                                                                                     |
| ------------------- | -------------------------------------------------------------------------------------------- |
| Missing topic       | No guideline covers a recurring chart, task, audience, or data situation.                    |
| Wording improvement | A guideline exists but its title, description, or section text is hard to retrieve or apply. |
| Relabeling          | Labels or label families hide the right record or overstate its scope.                       |
| Split or merge      | One record bundles separate ideas, or multiple records duplicate one guidance unit.          |
| Cross-linking       | A record should point readers toward a related boundary, exception, fix, or alternative.     |
| Source trail        | The guideline needs better source evidence, source metadata, or citation checking.           |
| Catalog vocabulary  | The manifest needs a role, label-family, or vocabulary review for a recurring catalog need.  |

Use secondary issue types only when they change what a maintainer should do.

## Draft The Issue

Use this Markdown shape. Keep it concise and remove private context before handing it to the human.

```md
Title: <short issue title>

## Issue Type

Missing guideline, wording improvement, relabeling, split or merge, cross-linking, source trail, or catalog vocabulary.

## Summary

One short paragraph describing the catalog problem and the practical case where it appeared.

## Evidence From Use

- Task or chart context:
- Retrieval path:
- What was missing, hard to find, ambiguous, duplicate, or misleading:
- Why this looks like a catalog content issue rather than a tooling issue:

## Related Guideline Records

- `<guideline-id>`: `<title>`
  - Exact-read command:
  - Relevant section:
  - Why it partially applies or fails to cover the case:
  - Citation output:

Use `None found` when the issue is about a missing topic. Include the failed searches in Evidence From Use.

## Suggested Catalog Change

Describe the requested change. Use the lines that fit:

- Add a new guideline about:
- Rephrase an existing guideline:
- Add or revise labels:
- Split or merge records:
- Add cross-links:
- Add or check source coverage:
- Clarify manifest vocabulary:

## Public Disclosure Check

- No private user data.
- No local filesystem paths.
- No unpublished screenshots or session artifacts unless the human explicitly approves including them.
- Guideline ids were verified with exact reads.
- Source-backed records were checked with `chartcoach catalog cite` when the issue mentions references.

## Uncertainty

What the agent is unsure about and what a catalog maintainer should check.
```

## Hand Off To The Human

End with the local draft and a short note that the human can review it before opening `https://github.com/chartcoach/catalog/issues/new`.

Do not include private logs, local paths, screenshots, browser artifacts, session transcripts, or unpublished examples unless the human explicitly asks to attach them. When the issue came from a private chart or work context, generalize the chart facts to the catalog need.
