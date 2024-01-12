from typing import AsyncGenerator
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from tests.conftest import get_async_session


@pytest.mark.asyncio
async def test_get_async_session() -> None:
    agen = get_async_session()
    assert isinstance(agen, AsyncGenerator)
    async_session = await anext(agen)
    assert isinstance(async_session, AsyncSession)
