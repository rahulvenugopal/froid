# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import time
import sys

import sphinx_bootstrap_theme


# Source code dir relative to this file
sys.path.insert(0, os.path.abspath(".."))

import froid


# General information about the project.
project = froid.__name__
release = froid.__version__
version = froid.__version__
author = froid.__author__.split("<")[0].strip()
curr = time.strftime("%Y")
copyright = f"2023-{curr}, {author}, Dream Mining Lab"



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "sphinx.ext.doctest",
    # "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories to ignore when
# looking for source files. This patterns also effect to html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# configure sphinx-copybutton
# https://github.com/executablebooks/sphinx-copybutton
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# Generate the API documentation when building
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "member-order": "groupwise",
    "undoc-members": False,
    # 'special-members': '__init__',
    # 'exclude-members': '__weakref__'
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "bootstrap"
html_static_path = ["_static"]
html_show_sourcelink = False

html_theme_options = {
    # "source_link_position": "footer",
    # # 'navbar_title': ' ',  # we replace this with an image
    "navbar_class": "navbar",
    "navbar_sidebarrel": False,  # Render the next and previous page links in navbar.
    "navbar_pagenav": False,  # Render the current pages TOC in the navbar.
    # "navbar_site_name": "Site",
    # "globaltoc_depth": -1,  # Global TOC depth for "site" navbar tab. (Default: 1) (-1 shows all)
    # # 'nosidebar': True,
    "bootswatch_theme": "cerulean",
    # "bootstrap_version": "3",
    # "globaltoc_includehidden": "false",
    "navbar_links": [
        ("Functions", "api"),
        # ("Quickstart", "quickstart"),
        # ("FAQ", "faq"),
        # ("What's new", "changelog"),
        ("Contribute", "contribute"),
    ],
}
