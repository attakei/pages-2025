"""Theme entrypoint."""

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config

here = Path(__file__).parent


def setup_resources(app: Sphinx, config: Config):
    config.templates_path.insert(1, str(here / "templates"))
    config.html_static_path.insert(1, str(here / "static"))


def setup(app: Sphinx):  # noqa: D103
    app.add_html_theme("pages-2025", str(here))
    app.setup_extension("atsphinx.bulma")
    app.setup_extension("atsphinx.bulma.themes.bulma_basic")
    app.connect("config-inited", setup_resources)
    return {
        "version": "0",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
