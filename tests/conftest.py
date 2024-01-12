import pytest

from app.core import Base, get_async_session
from app.models.user import User
from app.repositories.generic_db_repo.tests.conftest import get_test_session

NOW = 'now'
CREATE_USER_DATA = {'username': 'test_user', 'email': 'test_user@email.ru',}
USER_DATA = CREATE_USER_DATA.copy()
USER_DATA.update({'id': 1, 'registration_date': NOW})


@pytest.fixture
def user():
    return User(**USER_DATA)
