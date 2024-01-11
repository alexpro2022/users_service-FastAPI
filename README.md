# Generic database repository:

[![Test Suite](https://github.com/alexpro2022/users_service-FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/users_service-FastAPI/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/alexpro2022/generic-db-repository/graph/badge.svg?token=Y0F4lINe5B)](https://codecov.io/gh/alexpro2022/generic-db-repository)

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск тестов](#установка-и-запуск-тестов)
- [Автор](#автор)

<br>

## Технологии
<details><summary>Подробнее</summary><br>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest-asyncio)](https://pypi.org/project/pytest-asyncio/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

[⬆️Оглавление](#оглавление)

</details>

<br>

## Описание работы


[⬆️Оглавление](#оглавление)

<br>

## Установка и запуск тестов:
1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/alexpro2022/users_service-FastAPI.git
cd users_service-FastAPI
```
<br>
<details><summary>В docker-контейнере</summary><br>

2. Из корневой директории проекта выполните команду:
```bash
docker build -f ./docker/test.Dockerfile -t component .
docker run --name tests component
docker container rm tests
docker rmi component
```
<h1></h1>
</details>

<details><summary>В виртуальном окружении</summary><br>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:
```bash
python -m pip install --upgrade pip
pip install -r component/requirements.txt
```

4.  Для запуска тестов выполните команду:
```bash
pytest
```
<h1></h1>
</details>

[⬆️Оглавление](#оглавление)

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr generic-db-repository
```

[⬆️Оглавление](#оглавление)

<br>

## Автор:

[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Generic-database-repository:)
