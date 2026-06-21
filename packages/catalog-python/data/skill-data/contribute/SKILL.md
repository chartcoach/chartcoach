---
name: contribute
description: Use this to draft local chartcoach catalog improvement issues. Teaches agents how to draft issue text when retrieval exposes missing topics, wording gaps, labels, source gaps, or curation requests without posting anything.
---

# chartcoach Contribute

The Guideline Catalog is maintained as a shared resource. Friction in one user's critique, recommendation, discussion, or search can reveal catalog improvements for future users: missing coverage, unclear wording, weak labels, or sources that need checking.

Use this skill to draft local Markdown issues from those cases. The issue target is `https://github.com/chartcoach/catalog`. Do not open, submit, post, or disclose anything until the human approves it. The default handoff is a reviewed Markdown draft plus a prefilled issue URL using `https://github.com/chartcoach/catalog/issues/new?body=<encoded-body>`. If `gh` or an authenticated GitHub skill is available, offer issue creation only after approval.

Load `core` first when catalog source, index setup, package extras, or output formats are unclear. This skill assumes the `chartcoach` command already points at the intended Catalog Instance.

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
| CLI bug, command crash, install failure, or confusing command syntax           | chartcoach tooling issue.                                              |
| Infrastructure, package, cache, release, or download failure                   | chartcoach tooling or infrastructure issue.                            |
| Pure index false positive                                                      | Retrieval tooling or index diagnostics.                                |
| Index false positive caused by weak wording, labels, or missing topic coverage | Catalog issue.                                                         |
| Private project preference or one-off user policy                              | Keep local unless the human wants to propose a general catalog change. |

## Preserve The Retrieval Trace

Start from what happened in the task:

| Field             | Record                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| User task         | The chart critique, recommendation, discussion, or search question.                                  |
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

## Choose The Issue Template

Match the catalog repository templates:

| Catalog issue template       | Use when                                                                                     | Title prefix          |
| ---------------------------- | -------------------------------------------------------------------------------------------- | --------------------- |
| `missing-guideline.md`        | No guideline covers a recurring chart, task, audience, data setting, or design situation.    | `[Missing topic]:`    |
| `improve-guideline.md`        | An existing record needs clearer wording, labels, sections, sources, cross-links, or splits. | `[Improve guideline]:` |
| `catalog-curation.md`         | Manifest vocabulary, label families, source trails, duplicate handling, or coverage skew.    | `[Catalog curation]:` |

Use the selected template's section headings, checkbox list, and title prefix. Do not include the YAML front matter in the issue body. Keep the GitHub title separate from the body.

## Draft The Issue Body

Use this Markdown shape. It mirrors the shared section order in the catalog issue templates. Replace the issue type line and use note with the selected template language. Keep it concise and remove private context before handing it to the human.

```md
## Issue Type

<issue type line from the selected template>

<one-line use note from the selected template>

## Summary

One short paragraph describing the catalog problem and the practical case where it appeared.

## Evidence From Use

- Task or chart context:
- Retrieval path:
- Searches or labels tried:
- What was missing, hard to find, ambiguous, duplicate, or misleading:
- Why this appears to be a catalog content issue rather than a tooling issue:

## Related Guideline Records

- `<guideline-id>`: `<title>`
  - Exact-read command:
  - Relevant section:
  - Why it partially applies or fails to cover the case:
  - Citation output:

Use `None found` when the issue is about a missing topic. Include the failed searches in Evidence From Use.

## Suggested Catalog Change

Use the lines that fit.

- Add a new guideline about:
- Candidate title or phrasing:
- Rephrase an existing guideline:
- Clarify manifest vocabulary:
- Add or revise label families:
- Add or revise labels:
- Split or merge records:
- Add cross-links:
- Add or check source coverage:

## Public Disclosure Check

- [ ] No private user data.
- [ ] No local filesystem paths.
- [ ] No unpublished screenshots or session artifacts unless intentionally attached.
- [ ] Any referenced guideline ids were verified with exact reads.
- [ ] Source-backed records were checked with `chartcoach catalog cite` when references are discussed.

## Uncertainty

What the agent is unsure about and what a catalog maintainer should check.
```

Remove unused suggested-change lines before handing off the draft. Keep failed searches in Evidence From Use when the issue is about missing coverage.

## Prepare The Manual Link

Always provide a prefilled GitHub issue URL for human review:

```text
https://github.com/chartcoach/catalog/issues/new?body=<encoded-body>&title=<encoded-title>
```

URL-encode the final Markdown body and title. Use a real URL encoder rather than manual escaping.

```sh
python - <<'PY'
from urllib.parse import urlencode

title = "[Missing topic]: <short issue title>"
body = """## Issue Type

Missing guideline or missing topic area.
"""
print("https://github.com/chartcoach/catalog/issues/new?" + urlencode({"body": body, "title": title}))
PY
```

## Hand Off To The Human

End with the local draft, the issue title, and the prefilled URL. The human can review or edit the body before opening the issue.

Check whether the GitHub CLI is available before offering automatic creation:

```sh
command -v gh
gh auth status --hostname github.com
```

If both commands succeed, ask for explicit approval to create the issue in `chartcoach/catalog`. After approval, write the reviewed body to a temporary file and run:

```sh
gh issue create --repo chartcoach/catalog --title "<reviewed title>" --body-file <reviewed-body-file>
```

If a GitHub skill, MCP tool, or plugin is available, use it only after the same approval gate. The target repository is `chartcoach/catalog`, the title is the reviewed title, and the body is the reviewed Markdown body.

Do not include private logs, local paths, screenshots, browser artifacts, session transcripts, or unpublished examples unless the human explicitly asks to attach them. When the issue came from a private chart or work context, generalize the chart facts to the catalog need.
