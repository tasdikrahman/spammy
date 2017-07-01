# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-04-12
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman

clean:
	-find . -name '*.pyc' -delete
	-find . -name '__pycache__' -delete

tests: clean
	nosetests

register: clean
	python setup.py register -r pypi

dist: tests clean
	python setup.py sdist
	python setup.py bdist_wheel

upload: tests clean
	python setup.py sdist upload -r pypi
	#$(PYTHON) setup.py bdist_wheel upload -r pypi

.PHONY: help
help:
	@echo "\nPlease call with one of these targets:\n"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F:\
        '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}'\
        | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs | tr ' ' '\n' | awk\
        '{print "    - "$$0}'
	@echo "\n"
