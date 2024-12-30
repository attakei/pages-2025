# -- Project information
project = "attakei pages"
copyright = "2024, attakei"
author = "attakei"
release = "2025"

# -- General configuration
extensions = [
    # Built-in extensions
    "sphinx.ext.todo",
    # My extensions
    "atsphinx.footnotes",
    # Third-party extensions
    "sphinxnotes.strike",
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
html_js_files = [
    "https://kit.fontawesome.com/9da28e60fd.js",
]
html_theme = "pages-2025"
html_theme_options = {
    "bulmaswatch": "flatly",
    "color_mode": "light",
    "logo_description": "attakeiのあれこれ置き場。ノート/ブログ/登壇記録など。",
    "navbar_search": True,
}

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
# pages
pages_template_rule = {
    "404": "error.html",
}
