"""Disclosure components for HTML.

:ref: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from docutils import nodes
from sphinx.domains import Domain
from sphinx.util.docutils import SphinxDirective

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata
    from sphinx.writers.html5 import HTML5Translator


class disclosure(nodes.Element, nodes.General):
    pass


class disclosure_summary(nodes.Element, nodes.General):
    pass


class disclosure_details(nodes.Element, nodes.General):
    pass


def visit_disclosure(self: HTML5Translator, node: disclosure):
    self.body.append("<details>")
    pass


def depart_disclosure(self: HTML5Translator, node: disclosure):
    self.body.append("</details>")
    pass


def visit_disclosure_summary(self: HTML5Translator, node: disclosure_summary):
    self.body.append("<summary>")
    pass


def depart_disclosure_summary(self: HTML5Translator, node: disclosure_summary):
    self.body.append("</summary>")
    pass


def visit_disclosure_details(self: HTML5Translator, node: disclosure_details):
    pass


def depart_disclosure_details(self: HTML5Translator, node: disclosure_details):
    pass


class DisclosureSummary(SphinxDirective):
    has_content = True

    def run(self):
        node = disclosure_summary()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class DisclosureDetails(SphinxDirective):
    has_content = True

    def run(self):
        node = disclosure_details()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class Disclosure(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        print(self.arguments)
        if self.arguments:
            return self.run_simple(summary_text=self.arguments[0])

        node = disclosure()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, node)
        print(node)
        return [node]

    def run_simple(self, summary_text: str):
        summary_node = disclosure_summary()
        summary_node.append(nodes.Text(data=summary_text))
        details_node = disclosure_details()
        self.state.nested_parse(self.content, self.content_offset, details_node)
        node = disclosure()
        node.append(summary_node)
        node.append(details_node)
        print(node)
        return [node]


class DisclosureDomain(Domain):
    name = "disclosure"
    label = "The Details disclosure element."

    directives = {
        "summary": DisclosureSummary,
        "details": DisclosureDetails,
    }


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_domain(DisclosureDomain)
    app.add_directive("disclosure", Disclosure)
    app.add_node(disclosure, html=(visit_disclosure, depart_disclosure))
    app.add_node(
        disclosure_summary, html=(visit_disclosure_summary, depart_disclosure_summary)
    )
    app.add_node(
        disclosure_details, html=(visit_disclosure_details, depart_disclosure_details)
    )
    return {}
