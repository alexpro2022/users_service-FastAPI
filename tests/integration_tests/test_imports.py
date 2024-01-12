from fastapi import FastAPI

IMPORT_FAILURE_MSG = 'Import failure - {objs} is(are) not found in the {module}'

try:
    from app.core.base import Base, User
except ImportError:
    assert 0, IMPORT_FAILURE_MSG.format(objs='Base and User', module='app.core.base')


try:
    from app.main import app
except ImportError:
    assert 0, IMPORT_FAILURE_MSG.format(objs='app', module='app.main')
else:
    assert isinstance(app, FastAPI)