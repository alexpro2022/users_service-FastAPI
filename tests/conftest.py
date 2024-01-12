from typing import Any, AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient

from app.core import Base, get_async_session
from app.main import app
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.repositories.generic_db_repo.tests.conftest import get_test_session, engine, TestingSessionLocal
from app.schemas.user import UserCreate

from .data import *


@pytest_asyncio.fixture
async def new_user(get_test_session) -> User:
    return await UserRepository(get_test_session).create(UserCreate(**CREATE_USER_DATA))


async def override_get_async_session():
    async with TestingSessionLocal() as async_session:
        yield async_session


app.dependency_overrides[get_async_session] = override_get_async_session


@pytest_asyncio.fixture(autouse=True)
async def init_db() -> AsyncGenerator[None, Any]:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=app, base_url='http://testserver') as ac:
        yield ac