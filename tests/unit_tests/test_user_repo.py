from typing import Callable

import pytest

from app.repositories.user_repository import UserRepository


class TestUserRepository:
    OBJECT_ALREADY_EXISTS = 'Пользователь с таким email уже существует.'
    NOT_FOUND = 'Пользователь(и) не найден(ы).'
    repo: UserRepository | None = None

    @pytest.fixture
    def init_repo(self, get_test_session) -> None:
        assert self.repo is None
        self.repo = UserRepository(get_test_session)

    def test_init_repo_fixture(self, init_repo) -> None:
        assert isinstance(self.repo, UserRepository)

    def test_messages(self) -> None:
        def get_class_vars(class_):
            return [attr for attr in class_.__dict__ if (
                getattr(class_, attr) is not None and
                not isinstance(getattr(class_, attr), Callable) and
                not attr.startswith('__')
            )]
        self_class_messages = get_class_vars(self.__class__)
        user_class_messages = get_class_vars(UserRepository)
        assert self_class_messages == user_class_messages
        for message in self_class_messages:
            assert getattr(self, message) == getattr(UserRepository, message)

    @pytest.mark.parametrize('method_name', ('has_permission', 'is_delete_allowed', 'is_update_allowed'))
    def test_hooks(self, init_repo, method_name):
        assert self.repo.__getattribute__(method_name)() is None
