"""Convert 404 document for not basic html build."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from bs4 import BeautifulSoup
from sphinx.util.logging import getLogger

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.builders.html import StandaloneHTMLBuilder
    from sphinx.util.typing import ExtensionMetadata

logger = getLogger(__name__)


def convert_404(app: Sphinx, exc: Exception | None):  # noqa: D103
    if exc:
        raise exc
    if app.builder.format != "html":
        logger.info("This extension works only for html builder.")
        return
    logger.debug("Find 404 page target.")
    dest = Path(app.outdir / app.config.custom404_output)
    if dest.exists():
        logger.info("Target file is alaready exists.")
        return
    builder: StandaloneHTMLBuilder = app.builder  # type: ignore[assignment]
    source = Path(builder.get_outfilename(app.config.custom404_docname))
    logger.info(f"Target source is {source}")
    logger.info(f"Target output is {dest}")
    diff = str(dest.parent.relative_to(source.parent, walk_up=True))
    soup = BeautifulSoup(source.read_text(encoding="utf8"), "lxml")
    # Convert path attributes
    for tag, attr in [
        ("link", "href"),
        ("script", "src"),
        ("a", "href"),
        ("form", "action"),
    ]:
        for elm in soup.find_all(tag):
            if attr not in elm.attrs:
                continue
            if not elm[attr].startswith(diff):
                continue
            elm[attr] = elm[attr][len(diff) :]
    Path(dest).write_text(str(soup), encoding="utf8")


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value("custom404_docname", "404", "env", str)
    app.add_config_value("custom404_output", "404.html", "env", str)
    app.connect("build-finished", convert_404)
    return {
        "version": "0",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
