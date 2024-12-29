# -- Project information
project = "attakei pages"
copyright = "2024, attakei"
author = "attakei"
release = "2025"

# -- General configuration
extensions = [
    # My extensions
    "atsphinx.footnotes",
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
html_favicon = "_static/images/favicon.ico"
html_logo = "_static/images/icon-attakei@2x.png"
html_theme = "pages-2025"
html_theme_options = {
    "bulmaswatch": "flatly",
    "logo_description": "attakeiのあれこれ置き場。ノート/ブログ/登壇記録など。",
}
