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

project = u'bendihua'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.2'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'bendihuadoc'
latex_elements = {}
latex_documents = [
    ('index', 'bendihua.tex',
     'bendihua Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'bendihua',
     'bendihua Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'bendihua',
     'bendihua Documentation',
     'Onni Software Ltd.', 'bendihua',
     DESCRIPTION,
     'Miscellaneous'),
]
