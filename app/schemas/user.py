from datetime import datetime as dt

from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core import settings


class UserCreate(BaseModel):
    username: str = Field(max_length=settings.username_max_length,
                          min_length=settings.username_min_length,
                          json_schema_extra={'example': 'Username'})
    email: str = Field(json_schema_extra={'example': 'username@yandex.ru'})

    @field_validator('email')
    def validate_email_field(cls, field_value: str):
        try:
            emailinfo = validate_email(field_value)
            email = emailinfo.normalized
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return email


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    registration_date: dt
    model_config = ConfigDict(from_attributes=True)
