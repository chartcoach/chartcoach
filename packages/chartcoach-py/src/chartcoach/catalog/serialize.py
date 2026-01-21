import pathlib
from os import PathLike

from .catalog import Catalog
from .model import Guideline


def catalog_to_disk(catalog: Catalog, folder_path: PathLike[str]) -> None:
    """
    Dump the catalog entries to the specified folder path.

    Args:
        catalog (Catalog): The catalog to dump.
        folder_path (PathLike[str]): The path to the folder where the catalog entries will be dumped.
    """

    folder_path = pathlib.Path(folder_path)
    folder_path.mkdir(parents=True, exist_ok=True)

    for entry in catalog:
        entry_folder = folder_path / entry.guideline.id
        entry_folder.mkdir(parents=True, exist_ok=True)

        # Write guideline markdown
        guideline_md_path = entry_folder / "guideline.md"
        guideline_md_path.write_text(entry.guideline.to_markdown())

        # Write bibliography if present
        if entry.guideline.bibliography is not None:
            bib_path = entry_folder / "references.bib"
            bib_content = "\n".join(ref for ref in entry.references)
            bib_path.write_text(bib_content)


def guideline_to_markdown(guideline: Guideline) -> str:
    """
    Convert a Guideline object back to its markdown representation.

    Args:
        guideline (Guideline): The guideline to convert.

    Returns:
        str: The markdown string representation of the guideline.
    """
    import mdformat
    import yaml

    frontmatter = {
        "id": guideline.id,
        "title": guideline.title,
        "bibliography": guideline.bibliography,
        "description": guideline.description,
        "labels": guideline.labels,
    }
    frontmatter = {k: v for k, v in frontmatter.items() if v is not None}
    frontmatter_yaml_str = yaml.dump(frontmatter, sort_keys=False).strip()
    return "\n".join(
        [
            "---",
            frontmatter_yaml_str,
            "---",
            "",
            mdformat.text(guideline.body),
        ]
    )
