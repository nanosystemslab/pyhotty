"""Sphinx configuration."""

project = "Pyhotty"
author = "Nanosystems Lab"
copyright = "2024, Nanosystems Lab"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
