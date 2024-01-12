import pytest

from tests.conftest import Base, User, USER_DATA

BASE_FIELDS = ('id',)
USER_MODEL_FIELDS = USER_DATA.keys()
USER_MODEL_UNIQUE_FIELDS = ('email',)


@pytest.mark.parametrize('class_, field_names', (
    (Base, BASE_FIELDS),
    (User, USER_MODEL_FIELDS),
))
def test_model_fields(class_, field_names) -> None:
    for field_name in field_names:
        assert hasattr(class_, field_name)


@pytest.mark.parametrize('field_names', (USER_MODEL_UNIQUE_FIELDS,))
def test_unique_fields(field_names):
    for field_name in field_names:
        assert hasattr(getattr(User, field_name), 'unique')


@pytest.mark.parametrize('instance, field_names', (
    (Base(), BASE_FIELDS),
    (User(**USER_DATA), USER_MODEL_FIELDS),
))
def test_model_repr(instance, field_names) -> None:
    for field_name in field_names:
        assert repr(instance).find(field_name) != -1
