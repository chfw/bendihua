pip freeze
nosetests --with-coverage --cover-package fy --cover-package tests  tests docs/source fy && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
