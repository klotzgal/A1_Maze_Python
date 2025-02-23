# Maze

## Описание

Программа Maze предназначена для генерации и отрисовки идеальных лабиринтов, т.е. лабиринтов без зацикливаний и закрытых областей.
Максимальный размер лабиринта 50 на 50 клеток и 500 на 500 пикселей. Также реализован поиск кратчайших путей между двумя точками.

## Установка зависимостей

В качестве пакетного менеджера и средства управления зависимостями в проекте используется [Poetry](https://python-poetry.org/docs/).
Его можно установить с помощью

```bash
python3.11 -m pip install poetry
```

После чего нужно создать виртуальное окружение и установить зависимости из pyproject.toml с помощью

```bash
make venv
```

Poetry создаст виртуальное окружение в папке src. Проверить его можно с помощью `poetry env list`, удалить с помощью `poetry env remove --all`

## Проверка кода

Для форматирования кода используется утилита ruff, для сортировки импортов isort

```bash
make format
```

Также ruff проверяет код на не используемые импорты, не допустимые имена переменных и прочие ошибки.
Утилита mypy нужна для статической проверки типов. Она работает на основе аннотаций типов и помогает отлавливать баги, связанные с использованием методов и функций с не корректными типами. Даже если mypy показывает ошибки, то программа всё равно запустится

```bash
make check
```

## Работа с пакетами в Poetry

- Добавление пакета для сборки проекта

    ```bash
    poetry add <имя пакета>
    ```

- Добавление пакета для разработки (например линтеры и форматеры)

    ```bash
    poetry add <имя пакета> --group dev
    ```

- Удаление пакета

    ```bash
    poetry remove <имя пакета>
    ```

- Удаление пакета из группы

    ```bash
    poetry remove <имя пакета> --group <название группы>
    ```
