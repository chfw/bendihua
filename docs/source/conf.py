# -*- coding: utf-8 -*-
DESCRIPTION = (
    'translate your i18n file into 106 languages' +
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

project = u'fanyi'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'fanyidoc'
latex_elements = {}
latex_documents = [
    ('index', 'fanyi.tex',
     'fanyi Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'fanyi',
     'fanyi Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'fanyi',
     'fanyi Documentation',
     'Onni Software Ltd.', 'fanyi',
     DESCRIPTION,
     'Miscellaneous'),
]
