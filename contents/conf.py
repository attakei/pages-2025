import os

# -- Project information
project = "attakei pages"
copyright = "2024, attakei"
author = "attakei"
release = "2025"

# -- General configuration
extensions = [
    # Built-in extensions
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # My extensions
    "atsphinx.footnotes",
    # Third-party extensions
    "pages.ext.ablog",
    "sphinx_last_updated_by_git",
    "sphinx_sitemap",
    "sphinxnotes.strike",
    # Private
    "pages",
]
templates_path = ["_templates"]
exclude_patterns = []
language = "ja"

# -- Options for HTML output
html_baseurl = os.environ.get("SITE_BASE_URL", "/")
html_static_path = ["_static"]
html_extra_path = ["_extra/robots.txt"]
html_title = "attakei pages"
html_short_title = html_title
html_favicon = "_static/images/favicon.ico"
html_logo = "_static/images/icon-attakei@2x.png"
html_css_files = [
    "css/custom.css",
]
html_js_files = [
    "https://kit.fontawesome.com/9da28e60fd.js",
]
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"
html_last_updated_use_utc = True
html_theme = "pages-2025"
html_theme_options = {
    "globaltoc_includehidden": False,
    "globaltoc_maxdepth": 2,
    "bulmaswatch": "flatly",
    "color_mode": "light",
    "logo_description": "attakeiのあれこれ置き場。ノート/ブログ/登壇記録など。",
    "navbar_search": True,
}

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
# ablog
blog_path = "blog"
blog_title = "Blog of attakei pages"
blog_baseurl = html_baseurl
post_date_format = "%Y-%m-%d"
fontawesome_included = True
# sphinx-sitemap
sitemap_url_scheme = "{link}"
sitemap_locales = [None]
sitemap_excludes = [
    "404/",
    "blog/drafts/",
    "search/",
    "genindex/",
]
# pages
pages_template_rule = {
    "404": "error.html",
}
