import os
from datetime import datetime

project = "FRC Tutorials"
author = "Contributors"
copyright = f"{datetime.now().year} {author}"

extensions = ["myst_parser", "sphinx_copybutton"]

myst_enable_extensions = ["deflist", "tasklist", "attrs_block", "attrs_inline", "substitution"]
myst_heading_anchors = 3

templates_path = ["docs/_templates"]
html_static_path = ["docs/_static"]
exclude_patterns = ["_build"]
language = "vi"

html_theme = "furo"
html_title = "FRC Tutorials"
html_baseurl = ""

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3f51b5",
        "color-brand-content": "#3f51b5",
    },
    "dark_css_variables": {
        "color-brand-primary": "#90caf9",
        "color-brand-content": "#90caf9",
    },
    "sidebar_hide_name": False,
}

def setup(app):
    app.add_css_file("custom.css")
