from fastapi import APIRouter, status

from app import schemas
from app.core import settings
from app.models.user import User
from app.repositories.user_repository import user_repo

router = APIRouter(prefix='/user', tags=['Users'])

SUM_ALL_USERS = 'Возвращает список всех пользователей.'
SUM_USER = 'Возвращает пользователя по ID.'
SUM_CREATE_USER = 'Создание нового пользователя.'
SUM_DELETE_USER = 'Удаление пользователя.'


@router.get(
    '',
    response_model=list[schemas.UserResponse],
    response_model_exclude_none=True,
    summary=SUM_ALL_USERS,
    description=(f'{settings.ALL_USERS} {SUM_ALL_USERS}'))
async def get_all_users(user_repo: user_repo) -> list[User]:
    result = await user_repo.get_all()
    return [] if result is None else result


@router.post(
    '',
    response_model=schemas.UserResponse,
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
    summary=SUM_CREATE_USER,
    description=(f'{settings.ALL_USERS} {SUM_CREATE_USER}'))
async def create_user(payload: schemas.UserCreate, user_repo: user_repo) -> User:
    return await user_repo.create(payload)


@router.get(
    '/{user_id}',
    response_model=schemas.UserResponse,
    response_model_exclude_none=True,
    summary=SUM_USER,
    description=(f'{settings.ALL_USERS} {SUM_USER}'))
async def get_user(user_id: int, user_repo: user_repo) -> User:
    return await user_repo.get_or_404(user_id)


@router.delete(
    '/{user_id}',
    response_model=schemas.UserResponse,
    response_model_exclude_none=True,
    summary=SUM_DELETE_USER,
    description=(f'{settings.ALL_USERS} {SUM_DELETE_USER}'))
async def delete_user(user_id: int, user_repo: user_repo) -> User:
    return await user_repo.delete(user_id)
