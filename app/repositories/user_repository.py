from typing import Annotated

from fastapi import Depends

from app.core import async_session
from app.models.user import User
from app.repositories.generic_db_repo.generic_db_repository import \
    CRUDBaseRepository


class UserRepository(CRUDBaseRepository):
    OBJECT_ALREADY_EXISTS = 'Пользователь с таким email уже существует.'
    NOT_FOUND = 'Пользователь(и) не найден(ы).'

    def __init__(self, session: async_session):
        super().__init__(User, session)

    def has_permission(self, *args, **kwargs) -> None:
        """Always allowed in the project."""
        pass

    def is_delete_allowed(self, *args, **kwargs) -> None:
        """Always allowed in the project."""
        pass

    def is_update_allowed(self, *args, **kwargs) -> None:
        """Always allowed in the project."""
        pass


user_repo = Annotated[UserRepository, Depends()]
