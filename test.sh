pip freeze
nosetests --with-coverage --cover-package fanyi --cover-package tests  tests docs/source fanyi && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
