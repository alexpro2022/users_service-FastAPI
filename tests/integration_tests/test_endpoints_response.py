from http import HTTPStatus
import pytest
from httpx import AsyncClient

from app.core.config import settings
from tests.unit_tests.test_user_repo import TestUserRepository as UserRepo
from .endpoints_test_lib.endpoints_testlib import assert_response, assert_msg, not_allowed_methods_test, standard_tests
from ..data import *
from ..utils import *

USER_NOT_FOUND_MSG = UserRepo.NOT_FOUND


@pytest.mark.asyncio
@pytest.mark.parametrize('not_allowed_methods, endpoint, path_param ', (
    ((DELETE, PATCH, PUT), ENDPOINT, None),
    ((PATCH, POST, PUT), ENDPOINT, ID),
))
async def test_not_allowed_methods(async_client, not_allowed_methods, endpoint, path_param) -> None:
    await not_allowed_methods_test(async_client, not_allowed_methods, endpoint, path_param)


@pytest.mark.asyncio
@pytest.mark.parametrize('method, endpoint, path_param, payload, func, msg', (
    (GET, ENDPOINT, None, None, empty_list, None),
    (POST, ENDPOINT, None, CREATE_USER_DATA, check_user, UserRepo.OBJECT_ALREADY_EXISTS),
))
async def test_getall_post(async_client, method, endpoint, path_param, payload, func, msg) -> None:
    await standard_tests(async_client, method, endpoint, path_param=path_param, json=payload, func_check_valid_response=func, msg_already_exists=msg)


@pytest.mark.asyncio
@pytest.mark.parametrize('method, endpoint, path_param, payload, func, msg', (
    (GET, ENDPOINT, None, None, check_user, None),
    (GET, ENDPOINT, ID, None, check_user, USER_NOT_FOUND_MSG),
    (DELETE, ENDPOINT, ID, None, check_user, USER_NOT_FOUND_MSG),
))
async def test_get_getall_delete(async_client, new_user, method, endpoint, path_param, payload, func, msg) -> None:
    await standard_tests(async_client, method, endpoint, path_param=path_param, json=payload, func_check_valid_response=func, msg_not_found=msg)


@pytest.mark.asyncio
@pytest.mark.parametrize('username, expected_error_msg', (
    ('a', f'String should have at least {settings.username_min_length} characters'),
    ('a'*51, f'String should have at most {settings.username_max_length} characters'),
))
async def test_invalid_username_length(async_client, username, expected_error_msg) -> None:
    data = CREATE_USER_DATA.copy()
    data['username'] = username
    r = await assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, async_client, POST, ENDPOINT, json=data)
    assert r.json()['detail'][0]['msg'] == expected_error_msg


@pytest.mark.asyncio
@pytest.mark.parametrize('email, expected_error_msg', (
    ('a', f'Value error, The email address is not valid. It must have exactly one @-sign.'),
    ('a@a.a', f'Value error, The domain name a.a does not exist.'),
))
async def test_invalid_email(async_client, email, expected_error_msg) -> None:
    data = CREATE_USER_DATA.copy()
    data['email'] = email
    r = await assert_response(HTTPStatus.UNPROCESSABLE_ENTITY, async_client, POST, ENDPOINT, json=data)
    assert r.json()['detail'][0]['msg'] == expected_error_msg
