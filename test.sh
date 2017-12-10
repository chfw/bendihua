pip freeze
nosetests --with-coverage --cover-package bendihua --cover-package tests  tests docs/source bendihua && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
