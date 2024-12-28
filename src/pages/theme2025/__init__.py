"""Theme entrypoint."""

from pathlib import Path

from sphinx.application import Sphinx

here = Path(__file__).parent


def setup(app: Sphinx):  # noqa: D103
    app.add_html_theme("pages-2025", str(here))
    app.setup_extension("atsphinx.bulma")
    app.setup_extension("atsphinx.bulma.themes.bulma_basic")
