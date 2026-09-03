import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "packages" / "data-structures" / "src"))

project = "LazyPye"
author = "MechtrixPrime"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "LazyPye"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#3157a4",
        "color-brand-content": "#3157a4",
        "color-admonition-background": "#f5f7fb",
        "color-background-secondary": "#f7f8fa",
        "color-sidebar-background": "#f7f8fa",
        "color-sidebar-background-border": "#e2e5ea",
    },
    "dark_css_variables": {
        "color-brand-primary": "#9cbcff",
        "color-brand-content": "#9cbcff",
        "color-admonition-background": "#202633",
        "color-background-primary": "#151922",
        "color-background-secondary": "#1c222d",
        "color-sidebar-background": "#11151d",
        "color-sidebar-background-border": "#303745",
    },
}
add_module_names = False
autodoc_class_signature = "mixed"
autodoc_member_order = "bysource"
