from __future__ import annotations

from typing import TYPE_CHECKING

from docutils import nodes

if TYPE_CHECKING:
    from collections.abc import Iterable

    from sphinx.application import Sphinx


def get_description(
    doctree: nodes.document,
    description_length: int,
    known_titles: Iterable[str] | None = None,
    document: nodes.document | None = None,
):
    para = [
        n
        for n in doctree.findall(nodes.paragraph)
        if isinstance(n.parent, nodes.section)
    ]
    if para:
        return para[0].astext()
    return ""


def setup(app: Sphinx):
    import sphinxext.opengraph  # type: ignore

    sphinxext.opengraph.get_description = get_description
    app.setup_extension("sphinxext.opengraph")
    return {
        "version": "0",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
