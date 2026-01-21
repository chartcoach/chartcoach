from .model import Guideline, GuidelineSection


def parse_guideline(markdown: str) -> Guideline:
    """
    Parse the given markdown content with YAML frontmatter and body into a ``Guideline`` object.

    Args:
        markdown (str): The markdown content to parse including YAML frontmatter.

    Returns:
        Guideline: The parsed guideline entry.
    """
    frontmatter, body = parse_markdown_with_frontmatter(markdown)
    return Guideline.model_validate({**frontmatter, "body": body})


def parse_guideline_sections(body: str) -> list[GuidelineSection]:
    """
    Parse the body content of a guideline into its structured sections based on role annotations.

    Args:
        body: The guideline body content of the guideline in markdown format.

    Returns:
        A list of GuidelineSection objects representing the structured sections of the guideline body.

    Example:
        Given the following guideline body content:

        .. code-block:: markdown
            Some dangling, untagged content.

            ## The Advice <!-- role: advice -->

            This is the main instruction or recommendation.

            ## Why This Matters <!-- role: reason -->

            Explanation of why this advice is important.

        The function will return:

        .. code-block:: python

            [
                GuidelineSection(
                    role=GuidelineSection.DANGLING_ROLE,
                    title="",
                    content="Some dangling, untagged content."
                ),
                GuidelineSection(
                    role="advice",
                    title="The Advice",
                    content="This is the main instruction or recommendation."
                ),
                GuidelineSection(
                    role="reason",
                    title="Why This Matters",
                    content="Explanation of why this advice is important."
                ),
            ]
    """
    import re

    sections: list[GuidelineSection] = []
    lines = body.split("\n")

    # Pattern to match heading with role annotation: ## Title <!-- role: role_name -->
    heading_pattern = re.compile(r"^##\s+(.+?)\s*<!--\s*role:\s*(\S+)\s*-->")

    current_section: dict[str, str] | None = None
    current_content_lines: list[str] = []

    for line in lines:
        match = heading_pattern.match(line)

        if match:
            # Save previous section if exists
            if current_section is not None:
                current_section["content"] = "\n".join(current_content_lines).strip()
                sections.append(GuidelineSection(**current_section))
            elif current_content_lines:
                # Dangling content before first section
                content = "\n".join(current_content_lines).strip()
                if content:
                    sections.append(
                        GuidelineSection(
                            role=GuidelineSection.DANGLING_ROLE,
                            title="",
                            content=content,
                        )
                    )

            # Start new section
            title = match.group(1).strip()
            role = match.group(2).strip()
            current_section = {"role": role, "title": title}
            current_content_lines = []
        else:
            # Accumulate content lines
            current_content_lines.append(line)

    # Handle final section or dangling content
    if current_section is not None:
        current_section["content"] = "\n".join(current_content_lines).strip()
        sections.append(GuidelineSection(**current_section))
    elif current_content_lines:
        content = "\n".join(current_content_lines).strip()
        if content:
            sections.append(
                GuidelineSection(
                    role=GuidelineSection.DANGLING_ROLE,
                    title="",
                    content=content,
                )
            )

    return sections


def parse_markdown_with_frontmatter(markdown: str) -> tuple[dict, str]:
    """
    Parse the given markdown content with YAML frontmatter.

    Args:
        markdown (str): The markdown content to parse including YAML frontmatter.

    Returns:
        A tuple containing the frontmatter as a dictionary and the body content as a string.
    """
    import yaml

    if not markdown.startswith("---"):
        return {}, markdown

    parts = markdown.split("---", 2)
    if len(parts) < 3:
        return {}, markdown

    frontmatter_str = parts[1].strip()
    body = parts[2].strip()

    frontmatter = yaml.safe_load(frontmatter_str) or {}

    return frontmatter, body


def parse_bibtex(bibtex_content: str) -> list[str]:
    """
    Parse the given BibTeX content into a list of individual BibTeX entries.

    Args:
        bibtex_content (str): The BibTeX content as a string.

    Returns:
        A list of strings, each representing a single BibTeX entry.
    """
    import re

    # Split entries by '@' while preserving the '@' at the start of each entry
    comment_free_lines = [
        line for line in bibtex_content.splitlines() if not line.strip().startswith("%")
    ]
    comment_free_content = "\n".join(comment_free_lines)
    entries = re.split(r"(?=@)", comment_free_content)
    entries = [stripped_entry for entry in entries if (stripped_entry := entry.strip())]

    return entries
