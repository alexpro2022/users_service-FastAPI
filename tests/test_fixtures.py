from .conftest import AsyncClient, User
from .utils import check_user


def test_new_user_fixture(new_user):
    assert isinstance(new_user, User)
    check_user(new_user)


def test_async_client_fixture(async_client) -> None:
    assert isinstance(async_client, AsyncClient)
