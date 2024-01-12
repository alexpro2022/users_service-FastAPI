import pytest

from app.schemas import UserCreate


@pytest.mark.parametrize('value', (
    '11111', 'asd@', '@asd', 'asd@a.a', 'asd@as,as',
))
def test_email_validator_raises_exception(value):
    with pytest.raises(ValueError) as e:
        UserCreate.validate_email_field(value)


@pytest.mark.parametrize('value', (
    'asd@asd.as', '1asd@asd.as', '_asd@asd.as'
))
def test_email_validator(value):
    assert UserCreate.validate_email_field(value) == value