from datetime import datetime as dt

from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ..generic_db_repository import CRUDBaseRepository

MIN_LEN = 3
MAX_LEN = 50


class Base(DeclarativeBase):
    pass


class Model(Base):
    __tablename__ = 'test_model'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    optional_field: Mapped[dt | None]


class BaseModelConfig(BaseModel):
    model_config = ConfigDict(str_min_length=MIN_LEN)


class SchemaCreate(BaseModelConfig):
    title: str = Field(max_length=MAX_LEN)
    description: str = Field(max_length=MAX_LEN)


class SchemaUpdate(BaseModelConfig):
    title: str | None = Field(None, max_length=MAX_LEN)
    description: str | None = Field(None, max_length=MAX_LEN)


class Data:
    model = Model
    create_schema = SchemaCreate
    update_schema = SchemaUpdate
    field_names = ('id', 'title', 'description', 'optional_field')
    create_payload = {'title': 'My created object', 'description': 'My created object description'}
    update_payload = {'title': 'My updated object', 'description': 'My updated object description'}


class CRUD(CRUDBaseRepository):

    def is_update_allowed(self, obj, payload) -> None:
        pass

    def is_delete_allowed(self, obj) -> None:
        pass
