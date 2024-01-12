from tests.conftest import CREATE_USER_DATA, NOW, User


def check_user(user: User) -> None:
    assert isinstance(user, User)
    assert user.id == 1
    assert user.username == CREATE_USER_DATA.get('username')
    assert user.email == CREATE_USER_DATA.get('email')
    assert user.registration_date == NOW