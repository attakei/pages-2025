import re
from copy import deepcopy
from typing import Any
from unicodedata import normalize

from ablog import blog  # type: ignore
from ablog.post import PostDirective  # type: ignore
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.config import Config
from sphinx.writers.html5 import HTML5Translator


def slugify(string: Any) -> str:
    """Slugify *s*.

    This is override of ``ablog.blog.slugify`` to normalize Japanese Kana correctly.

    * Original slugs from "ゲーム" to "ケーム" (Removed VOICED SOUND MARK).
    * Due to normalize by NKKD (form-D) that split kana and mark from marked kana.
    * This func changes these:

      * Use form-C normalize.
      * Does not format lower.
    """
    string = normalize("NFKC", str(string))
    string = re.sub(r"[^\w\s-]", "", string).strip()
    return re.sub(r"[-\s]+", "_", string)


class frontmatter(nodes.Element, nodes.General):
    pass


def visit_frontmatter(self: HTML5Translator, node: frontmatter):
    self.body.append(
        self.builder.templates.render("ablog/frontmatter.html", {"post": node})
    )


def depart_frontmatter(self, node: frontmatter):
    pass


class PagesPostDirective(PostDirective):
    def run(self):
        nodes = super().run()
        tags = nodes[0].get("tags", None)
        if tags and tags[-1] == "":
            nodes[0]["tags"] = tags[:-1]
        nodes[0]["nocomments"] = True
        node = frontmatter()
        node.attributes = deepcopy(nodes[0].attributes)
        return nodes + [node]


def bind_slugify(app: Sphinx, builder: Builder):
    if builder.format == "html":
        builder.templates.environment.filters["slugify"] = slugify


def setup(app: Sphinx):
    app.setup_extension("ablog")
    blog.slugify = slugify
    app.add_node(frontmatter, html=(visit_frontmatter, depart_frontmatter))
    app.add_directive("post", PagesPostDirective, override=True)
    app.connect("write-started", bind_slugify)
