#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config


import os
import sys
from datetime import datetime
from subprocess import check_call

import django
import git

from path import Path

root = Path('..').abspath()

# Hack the PYTHONPATH to match what LMS and Studio use so all the code
# can be successfully imported
sys.path.insert(0, root)
sys.path.append(root / "docs")

from repository_docs import RepositoryDocs

# Use a settings module that allows all LMS and Studio code to be imported
# without errors.  If running sphinx-apidoc, we already set a different
# settings module to use in the on_init() hook of the parent process
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'docs.docs_settings'

django.setup()

# -- Project information -----------------------------------------------------

project = 'edx-platform'
copyright = f'{datetime.now().year}, Axim Collaborative, Inc'  # pylint: disable=redefined-builtin
author = 'Axim Collaborative, Inc'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinxcontrib.openapi',
    'sphinxext.rediraffe',
    'sphinx_design',
    'code_annotations.contrib.sphinx.extensions.featuretoggles',
    'code_annotations.contrib.sphinx.extensions.settings',
    # 'autoapi.extension',  # Temporarily disabled
    'sphinx_reredirects',
]

# Temporarily disabling autoapi_dirs and the AutoAPI extension due to performance issues.
# This will unblock ReadTheDocs builds and will be revisited for optimization.
# autoapi_type = 'python'
# autoapi_dirs = ['../lms/djangoapps', '../openedx/core/djangoapps', "../openedx/features"]
#
# autoapi_ignore = [
#     '*/migrations/*',
#     '*/tests/*',
#     '*.pyc',
#     '__init__.py',
#     '**/xblock_serializer/data.py',
# ]

# Rediraffe related settings.
rediraffe_redirects = "redirects.txt"
rediraffe_branch = 'origin/master'

# code_annotations.(featuretoggles|settings) related settings.
edxplatform_repo_url = "https://github.com/openedx/edx-platform"
edxplatform_source_path = root

try:
    edx_platform_version = git.Repo(search_parent_directories=True).head.object.hexsha
except git.InvalidGitRepositoryError:
    edx_platform_version = "master"

featuretoggles_source_path = str(edxplatform_source_path)
featuretoggles_repo_url = edxplatform_repo_url
featuretoggles_repo_version = edx_platform_version

settings_source_path = str(edxplatform_source_path)
settings_repo_url = edxplatform_repo_url
settings_repo_version = edx_platform_version

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# html_theme_path = []

html_logo = "https://logos.openedx.org/open-edx-logo-color.png"
html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "repository_url": "https://github.com/openedx/edx-platform",
    "repository_branch": "master",
    "path_to_docs": "docs",
    "home_page_in_toc": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "navigation_depth": 3,
    # Please don't change unless you know what you're doing.
    "extra_footer": """
        <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
            <img
                alt="Creative Commons License"
                style="border-width:0"
                src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
        </a>
        <br>
        These works by
            <a
                xmlns:cc="https://creativecommons.org/ns#"
                href="https://axim.org/"
                property="cc:attributionName"
                rel="cc:attributionURL"
            >Axim Collaborative, Inc</a>
        are licensed under a
            <a
                rel="license"
                href="https://creativecommons.org/licenses/by-sa/4.0/"
            >Creative Commons Attribution-ShareAlike 4.0 International License</a>.
    """
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'edx-platformdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'edx-platform.tex', 'edx-platform Documentation',
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'edx-platform', 'edx-platform Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'edx-platform', 'edx-platform Documentation',
     author, 'edx-platform', 'The Open edX platform, the software that powers edX!',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Read the Docs Specific Configuration
# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'django': ('https://docs.djangoproject.com/en/4.2/', 'https://docs.djangoproject.com/en/4.2/_objects/'),
}

# Start building a map of the directories relative to the repository root to
# run sphinx-apidoc against and the directories under "docs" in which to store
# the generated *.rst files
modules = {
    'lms': 'references/docstrings/lms',
    'openedx': 'references/docstrings/openedx',
    # Commenting this out for now because they blow up the build
    # time and memory limits for RTD.  We can come back to these
    # later once we get parallel builds working hopefully.
    # 'cms': 'references/docstrings/cms',
    # 'common': 'references/docstrings/common',
    # 'xmodule': 'references/docstrings/xmodule',
}

# Mapping permanently moved pages to appropriate new location outside of edx-platform
# with by sphinx-reredirects extension redirects.
# More information: https://documatt.com/sphinx-reredirects/usage.html

redirects = {
    'hooks/events': 'https://docs.openedx.org/projects/openedx-events/en/latest/',
    'hooks/filters': 'https://docs.openedx.org/projects/openedx-filters/en/latest/',
    'hooks/index': 'https://docs.openedx.org/en/latest/developers/concepts/hooks_extension_framework.html',
}


def update_settings_module(service='lms'):
    """
    Set the "DJANGO_SETTINGS_MODULE" environment variable appropriately
    for the module sphinx-apidoc is about to be run on.
    """
    settings_module = f'{service}.envs.devstack'
    os.environ['DJANGO_SETTINGS_MODULE'] = settings_module


def on_init(app):  # lint-amnesty, pylint: disable=redefined-outer-name, unused-argument
    """
    Run sphinx-apidoc after Sphinx initialization.

    Read the Docs won't run tox or custom shell commands, so we need this to
    avoid checking in the generated reStructuredText files.
    """
    repo_docs_build_path = f'{root}/docs/references/docs'
    RepositoryDocs(root, repo_docs_build_path).build_rst_docs()

    docs_path = root / 'docs'
    apidoc_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        bin_path = os.path.abspath(os.path.join(sys.prefix, 'bin'))
        apidoc_path = os.path.join(bin_path, apidoc_path)
    exclude_dirs = ['envs', 'migrations', 'test', 'tests']

    exclude_files = ['admin.py', 'test.py', 'testing.py', 'tests.py', 'testutils.py', 'wsgi.py']
    for module in modules:
        module_path = str(root / module)
        output_path = str(docs_path / modules[module])
        args = [apidoc_path, '--ext-intersphinx', '-o',
                output_path, module_path]
        exclude = []
        if module == 'cms':
            update_settings_module('cms')
        else:
            update_settings_module('lms')
        for dirpath, dirnames, filenames in os.walk(module_path):
            to_remove = []
            for name in dirnames:
                if name in exclude_dirs:
                    to_remove.append(name)
                    exclude.append(os.path.join(dirpath, name))
            if 'features' in dirnames and 'openedx' not in dirpath:
                to_remove.append('features')
                exclude.append(os.path.join(dirpath, 'features'))
            for name in to_remove:
                dirnames.remove(name)
            for name in filenames:
                if name in exclude_files:
                    exclude.append(os.path.join(dirpath, name))
        if exclude:
            args.extend(exclude)
        check_call(args)


def setup(app):  # lint-amnesty, pylint: disable=redefined-outer-name
    """Sphinx extension: run sphinx-apidoc."""
    event = 'builder-inited'
    app.connect(event, on_init)
