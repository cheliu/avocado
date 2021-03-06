# -*- coding: utf-8 -*-

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
root_path = os.path.abspath(os.path.join("..", ".."))
sys.path.insert(0, root_path)

import avocado.version
from avocado.utils import process

# Auto generate API documentation
_sphinx_apidoc = process.find_command('sphinx-apidoc')
_output_dir = os.path.join(root_path, 'docs', 'source', 'api')
_api_dir = os.path.join(root_path, 'avocado')
process.run("%s -o %s %s" % (_sphinx_apidoc, _output_dir, _api_dir))

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage']

master_doc = 'index'
project = u'Avocado'
copyright = u'2014, Red Hat'

version = avocado.version.VERSION
release = avocado.version.VERSION

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from
# docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except ImportError:
        html_theme = 'default'

htmlhelp_basename = 'avocadodoc'

latex_documents = [
    ('index', 'avocado.tex', u'avocado Documentation',
     u'Lucas Meneghel Rodrigues', 'manual'),
]

man_pages = [
    ('index', 'avocado', u'avocado Documentation',
     [u'Lucas Meneghel Rodrigues'], 1)
]

texinfo_documents = [
    ('index', 'avocado', u'avocado Documentation',
     u'Lucas Meneghel Rodrigues', 'avocado', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

autoclass_content = 'both'
