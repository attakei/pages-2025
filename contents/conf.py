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
    "oembedpy.ext.sphinx",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
    "sphinxnotes.strike",
    # Wrapped third-party extensions
    "pages.ext.opengraph",
    # Private
    "pages",
]
templates_path = ["_templates"]
exclude_patterns = []
language = "ja"

# -- Options for HTML output
html_baseurl = os.environ.get("SITE_BASEURL", "/")
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
    "bulmaswatch": "flatly",
    "color_mode": "light",
    "logo_description": "attakeiのあれこれ置き場。ノート/ブログ/登壇記録など。",
    "navbar_search": True,
    "navbar_icons": [
        {
            "icon": "fa-brands fa-solid fa-bluesky fa-2x",
            "url": "https://bsky.app/profile/attakei.dev",
        },
        {
            "icon": "fa-brands fa-solid fa-x-twitter fa-2x",
            "url": "https://x.com/attakei",
        },
    ],
}

# -- Options for Linkcheck output
linkcheck_ignore = [
    r"https://atnd.org/.*",
    r"http://minorichihara.com/summerchampion2019/",
    r"http://www.foxmovies-jp.com/odyssey/",
    r"http://www.pacificrim.jp/",
    r"https://conference2019.laravel.jp/",  # Certificate expired
    r"https://igordavydenko.com/slides/lvivpy-9/#/",
    r"https://pypi.attakei.net.+",
    r"https://speakerdeck.com/skyjoker/ansiblefalsexue-xi-huan-jing-wovspheredezuo-tuteruohua",
    r"https://sphinx-revealjs.readthedocs.io/en/v0.11.0/",
    r"https://sphinx-rtd-revealjs.readthedocs.io/en/latest/",
    r"https://docs.google.com/presentation/d/1yVjHN_35xPih3X3tlXgwpmxftLlCP8raC-i-1k5KJLc/edit#slide=id.p",
    r"https://github.com/.+",
]
linkcheck_anchors_ignore_for_url = [
    r"https://pypi.org/.+",
    r"https://github.com/.+",
    r"https://slides.com/.+",
]

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
# ablog
blog_path = "blog"
blog_title = "Blog of attakei pages"
blog_baseurl = html_baseurl
post_date_format = "%Y-%m-%d"
fontawesome_included = True
# oembedpy.ext.sphinx
oembed_fallback_type = True
# sphinx-sitemap
sitemap_url_scheme = "{link}"
sitemap_locales = [None]
sitemap_excludes = [
    "404/",
    "blog/drafts/",
    "search/",
    "genindex/",
]
# sphinxext.opengraph
ogp_site_url = html_baseurl
ogp_social_cards = {
    "enable": False,
}
ogp_image = "_static/images/og-image.png"
# pages
pages_template_rule = {
    "index": "index.html",
    "404": "error.html",
}

# -- Options for environments
# For production/staging build
if os.environ.get("SITE_ENV") in ["production", "staging"]:
    extensions += [
        "sphinx_last_updated_by_git",
        "sphinxcontrib.gtagjs",
    ]

    # sphinxcontrib-gtagjs
    gtagjs_ids = [
        id_ for id_ in os.environ.get("SITE_GTAGJS_IDS", "").split(",") if id_ != ""
    ]
