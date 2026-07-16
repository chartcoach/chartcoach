---
name: contribute
description: Use this to draft a local chartcoach catalog improvement issue from a verified retrieval gap.
---

# chartcoach Contribute

Draft a catalog issue when retrieval exposes missing coverage, unclear wording,
weak labels, duplicate records, or a source gap. The target repository is
`https://github.com/chartcoach/catalog`.

Keep the draft local until a human approves issue creation. Load `core` for
catalog selection and exact-read mechanics.

## Confirm The Catalog Problem

Record:

| Field          | Evidence                                                             |
| -------------- | -------------------------------------------------------------------- |
| User task      | The critique, recommendation, discussion, or search question.        |
| Retrieval path | Terms, labels, roles, SQL, and indexed searches tried.               |
| Result         | Missing, partial, surprising, duplicate, or weakly sourced record.   |
| Diagnosis      | Why catalog content caused the problem.                              |
| Related ids    | Records that partially match, conflict, duplicate, or need revision. |

Verify every named record:

```sh
chartcoach catalog read <guideline-id> --source-detail full
chartcoach catalog cite <guideline-id>
```

Route command crashes, install failures, cache failures, and storage failures to
the chartcoach tooling repository. A retrieval false positive belongs in a
catalog issue when wording or labels caused it.

## Choose One Change Type

- Missing topic
- Wording improvement
- Relabeling
- Split or merge
- Cross-linking
- Source trail
- Manifest vocabulary

Use one primary type so the issue names a concrete maintainer action.

## Draft The Issue

```md
## Summary

<Catalog problem and the recurring case where it appeared.>

## Evidence From Use

- Task:
- Retrieval path:
- Result:
- Content diagnosis:

## Related Guideline Records

- `<guideline-id>`: `<title>`
  - Relevant section:
  - Exact-read command:
  - Citation:
  - Scope or gap:

## Suggested Catalog Change

<One concrete content, vocabulary, relationship, or source change.>

## Public Disclosure Check

- [ ] Private user data and local paths are excluded.
- [ ] Referenced guideline ids were checked with exact reads.
- [ ] Source claims were checked with `catalog cite`.

## Uncertainty

<What a catalog maintainer should verify.>
```

Use `None found` for a missing topic and preserve the failed retrieval terms.

## Hand Off

Return the proposed title, Markdown body, and a prefilled issue URL:

```python
from urllib.parse import urlencode

title = "[Missing topic]: <short title>"
body = """## Summary

<reviewed issue body>
"""
url = "https://github.com/chartcoach/catalog/issues/new?" + urlencode(
    {"title": title, "body": body}
)
print(url)
```

Create the issue through `gh` or another GitHub integration after the human
approves the reviewed title and body.
