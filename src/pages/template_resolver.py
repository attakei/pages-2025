"""Custom template management."""

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

RuleDict = dict[str, str]


def resolve_template_name(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: nodes.document | None,
) -> str | None:
    rule: RuleDict = app.config.pages_template_rule
    if pagename in rule:
        return rule[pagename]
    return None


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value("pages_template_rule", {}, "env", RuleDict)
    app.connect("html-page-context", resolve_template_name)
    return {
        "version": "0",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
