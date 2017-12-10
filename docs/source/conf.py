# -*- coding: utf-8 -*-
DESCRIPTION = (
    'googletrans command line interface to translate your i18n file into 10' +
    '6 languages' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'fy'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'fydoc'
latex_elements = {}
latex_documents = [
    ('index', 'fy.tex',
     'fy Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'fy',
     'fy Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'fy',
     'fy Documentation',
     'Onni Software Ltd.', 'fy',
     DESCRIPTION,
     'Miscellaneous'),
]
