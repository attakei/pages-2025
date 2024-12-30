from copy import deepcopy

from ablog.post import PostDirective  # type: ignore
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


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
        node = frontmatter()
        node.attributes = deepcopy(nodes[0].attributes)
        return nodes + [node]


def setup(app: Sphinx):
    app.setup_extension("ablog")
    app.add_node(frontmatter, html=(visit_frontmatter, depart_frontmatter))
    app.add_directive("post", PagesPostDirective, override=True)
