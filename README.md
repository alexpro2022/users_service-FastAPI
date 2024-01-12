# Users management service:

[![Test Suite](https://github.com/alexpro2022/users_service-FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/users_service-FastAPI/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/alexpro2022/users_service-FastAPI/graph/badge.svg?token=s7OXPe3tw9)](https://codecov.io/gh/alexpro2022/users_service-FastAPI)

### Simple RESTful API using FastAPI for a users management:
Сервис предоставляет API для создания, просмотра и удаления пользователей.

<br>

## Оглавление
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск приложения и тестов](#Установка-и-запуск-приложения-и-тестов)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии
<details><summary>Подробнее</summary><br>

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?logo=Pydantic)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?logo=Uvicorn)](https://www.uvicorn.org/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?logo=Pytest)](https://docs.pytest.org/en/latest/)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest-asyncio)](https://pypi.org/project/pytest-asyncio/)
[![pytest-cov](https://img.shields.io/badge/-pytest--cov-464646?logo=codecov)](https://pytest-cov.readthedocs.io/en/latest/)
[![coverage](https://img.shields.io/badge/-coverage-464646?logo=coverage)](https://coverage.readthedocs.io/en/)
[![pre-commit](https://img.shields.io/badge/-pre--commit-464646?logo=pre-commit)](https://pre-commit.com/)

[⬆️Оглавление](#оглавление)

</details>

<br>

## Описание работы

Swagger позволяет осуществлять http-запросы к работающему сервису, тем самым можно управлять пользователями в рамках политики сервиса (указано в Swagger для каждого запроса - в данном проекте нет пользовательских ролей и авторизации, поэтому все операции доступны любому пользователю).

Операции:
   - Создание нового пользователя:
      - необходимо указать username(3-50 символов) и email(уникальное поле). Входные данные валидируются.
      - при создании автоматически устанавливается текущая дата регистрации;
   - Получение списка всех пользователей;
   - Получение информации о конкретном пользователе по его идентификатору;
   - Удаление пользователя.

[⬆️Оглавление](#оглавление)

<br>

## Установка и запуск приложения и тестов:

<details><summary>Предварительные условия</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```
<h1></h1></details>

<details><summary>Локальный запуск</summary><br>

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):

```bash
git clone https://github.com/alexpro2022/users_service-FastAPI.git
cd users_service-FastAPI
cp env_example .env
nano .env
```
<br>

<details><summary>В виртуальном окружении (БД - SQLite)</summary><br>

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
pip install -r requirements/test.requirements.txt
```

4. В проекте уже инициализирована система миграций Alembic с настроенной автогенерацией имен внешних ключей моделей и создан файл первой миграции. Чтобы ее применить, необходимо выполнить команду:
```bash
alembic upgrade head
```
Будут созданы все таблицы из файла миграций.

5. Запуск приложения - выполните команду:
```bash
uvicorn app.main:app
```
Сервер Uvicorn запустит приложение по адресу http://127.0.0.1:8000.
Администрирование приложения может быть осуществлено через Swagger доступный по адресу http://127.0.0.1:8000/docs .

6. Остановить Uvicorn можно комбинацией клавиш Ctl-C.

7.  Для запуска тестов выполните команду:
```bash
pytest --cov --cov-config=.coveragerc
```

<h1></h1>
</details>

<details><summary>В docker-контейнере (БД - PostgreSQL)</summary><br>

2. Из корневой директории проекта выполните команду:
```bash
docker compose -f docker/docker-compose.yml up -d --build
```
Проект будет развернут в docker-контейнерах (db, web) по адресу http://localhost:8000.
Администрирование приложения может быть осуществлено через Swagger доступный по адресу http://localhost:8000/docs .

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f docker/docker-compose.yml down
```
Если также необходимо удалить том базы данных:
```bash
docker compose -f docker/docker-compose.yml down -v
```

4. Для запуска тестов выполните команду:
```bash
docker build -f ./docker/test.Dockerfile -t app .
docker run --name tests app
docker container rm tests
docker rmi app
```
<h1></h1>
</details>

<br>

Для создания тестовых постов можно воспользоваться следующими данными:

```json
{
  "username": "Test user 1",
  "email": "test_user1@yandex.ru"
}
```

```json
{
  "username": "Test user 2",
  "email": "test_user2@yandex.ru"
}
```

[⬆️Оглавление](#оглавление)

</details>

<br>

## Удаление приложения:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr users_service-FastAPI
```

[⬆️Оглавление](#оглавление)

<br>

## Автор:

[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#users-management-service)
