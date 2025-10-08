import os
from datetime import datetime

# --- Project info ---
project = "FRC Tutorials"
author = "Contributors"
copyright = f"{datetime.now().year} {author}"

# --- Extensions ---
extensions = [
    "myst_parser",        # đọc Markdown (MyST)
    "sphinx_copybutton",  # nút copy cho code block
]

# MyST options
myst_enable_extensions = [
    "deflist", "tasklist", "attrs_block", "attrs_inline", "substitution"
]
myst_heading_anchors = 3

# Vì conf.py nằm ở root, trỏ vào thư mục dưới docs/
templates_path = ["docs/_templates"]
html_static_path = ["docs/_static"]
exclude_patterns = ["_build"]
language = "vi"

# --- Theme ---
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
    # nạp CSS tùy biến trong docs/_static/custom.css
    app.add_css_file("custom.css")
