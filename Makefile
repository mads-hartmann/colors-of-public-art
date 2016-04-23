 SHELL = /usr/bin/env bash

VENV ?= .venv
PIP := $(VENV)/bin/pip
PYTHON := $(VENV)/bin/python
PYTHONPATH ?= src

COUNT ?= 20000


default: run-web


run-web: .setup.made
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) src/web/server.py


run-analyze: .setup.made
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) src/cli/analyze.py --start 0 --end $(COUNT)


run-download: .setup.made
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) src/cli/download.py --count $(COUNT)


.setup.made: $(VENV)/.installed
	mkdir -p static/images
	touch $@


$(VENV)/.made:
	virtualenv -q --no-site-packages -p python2.7 $(VENV)
	$(PIP) install pip==7.1.2 setuptools==18.2
	touch $@


$(VENV)/.installed: $(VENV)/.made requirements.txt
	$(PIP) install -r requirements.txt
	touch $@
