from typing import Callable

from tests.conftest import CREATE_USER_DATA, User, DONE


def get_fields(item):
    return [key for key in item.__dict__ if (
        getattr(item, key) is not None and
        not isinstance(getattr(item, key), Callable) and
        not key.startswith('__')
    )]


def to_dict(obj):
    d = {}
    for field_name in get_fields(obj):
        d[field_name] = getattr(obj, field_name)
    return d


def check_user(user: list[dict] | dict | User) -> str:
    username = CREATE_USER_DATA.get('username')
    email = CREATE_USER_DATA.get('email')
    if isinstance(user, list):
        user = user[0]
    if isinstance(user, User):
        user = to_dict(user)   
    if isinstance(user, dict):
        assert user['id'] == 1
        assert user['username'] == username
        assert user['email'] == email
        assert user['registration_date']
        return DONE
    else:
        assert 0, f'Неверный формат переменной USER - {type(user)}'      


def empty_list(response_json: list) -> str:
    assert response_json == []
    return DONE