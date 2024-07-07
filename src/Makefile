.PHONY: all install uninstall clean dvi dist tests format check
PYTHON=python3.11
VENV=.venv
PYEXEC=poetry run

all: test

install:
# TODO: Заменить на установку проекта в каталог ../build
	$(PYEXEC) python main.py

uninstall:
# TODO: Заменить на удаление проекта
	echo "Uninstalling..."

clean:
	rm -rf build *cache* .*cache dist

fclean: clean
	rm -rf $(VENV)

dvi:
# TODO: Добавить документацию
	open README.md

dist:
# TODO: Проверить после добавления install
	mkdir -p dist
	cp -r build/* dist
	tar -czf dist.tar.gz dist

format:
	$(PYEXEC) ruff format . --config "format.quote-style = 'single'"
	$(PYEXEC) isort .

check:
	$(PYEXEC) ruff check
	$(PYEXEC) mypy main.py --strict

tests:
	export $(grep -v '^#' test.env | xargs)
	$(VENV)/bin/pytest -W ignore::DeprecationWarning

venv:
	poetry env use $(PYTHON)
	poetry config --local virtualenvs.in-project true
	poetry install
