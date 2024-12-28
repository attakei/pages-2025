# -- Project information
project = "attakei pages"
copyright = "2024, attakei"
author = "attakei"
release = "2025"

# -- General configuration
extensions = [
    # Private
    "pages",
]
templates_path = ["_templates"]
exclude_patterns = []
language = "ja"

# -- Options for HTML output
html_static_path = ["_static"]
html_title = "attakei pages"
html_short_title = html_title
html_theme = "pages-2025"
html_theme_options = {
    "bulmaswatch": "flatly",
}
