VENV=venv

venv:
	virtualenv $(VENV)

install: venv
	$(VENV)/bin/pip install flask

go: install
	$(VENV)/bin/python queens.py

tests: install
	$(VENV)/bin/python test_queens.py