NOW = 'now'
CREATE_USER_DATA = {'username': 'test_user', 'email': 'test_user@yandex.ru',}
USER_DATA = CREATE_USER_DATA.copy()
USER_DATA.update({'id': 1, 'registration_date': NOW})

ID = 1
ENDPOINT = 'user'

DELETE, GET, POST, PUT, PATCH, DONE = 'DELETE', 'GET', 'POST', 'PUT', 'PATCH', 'DONE'