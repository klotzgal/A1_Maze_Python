.PHONY: all install uninstall clean fclean dvi dist tests format check
PYTHON=python3.11
VENV=.venv
PYEXEC=poetry run

all: tests

install:
# TODO: Заменить на установку проекта в каталог ../build
	$(PYEXEC) python main.py

uninstall:
# TODO: Заменить на удаление проекта
	echo "Uninstalling..."

clean:
	rm -rf build *cache* .*cache dist .coverage htmlcov

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
	$(PYEXEC) isort .
	$(PYEXEC) ruff format .

check:
	$(PYEXEC) ruff check
	$(PYEXEC) mypy main.py --strict

tests:
	$(PYEXEC) pytest #-W ignore::DeprecationWarning

cov:
	$(PYEXEC) pytest --cov --cov-report=html #-W ignore::DeprecationWarning
	open htmlcov/index.html

venv:
	poetry env use $(PYTHON)
	poetry config --local virtualenvs.in-project true
	poetry install
