from typing import Iterable

from docutils import nodes
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
