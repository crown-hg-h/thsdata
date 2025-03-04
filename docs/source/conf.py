# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'thsdata'
copyright = '2025, x'
author = 'x'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import thsdata

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_theme_options = {
    "show_powered_by": False,
    "github_user": "thsdata",
    "github_repo": "thsdata",
    "github_banner": True,
    "show_related": False,
    "note_bg": "#FFF59C",
}

html_static_path = ['_static']
