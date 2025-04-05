"""Private project for website."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata


def setup(app: Sphinx) -> ExtensionMetadata | None:
    app.setup_extension("pages.theme2025")
    app.setup_extension("pages.template_resolver")
    app.setup_extension("pages.custom404")
    return {
        "version": "0",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
