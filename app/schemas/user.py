from datetime import datetime as dt

from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core import settings


class UserCreate(BaseModel):
    username: str = Field(max_length=settings.username_max_length,
                          min_length=settings.username_min_length,
                          json_schema_extra={'example': 'New username'})
    email: str = Field(json_schema_extra={'example': 'username@email.ru'})

    @field_validator('email')
    def validate_email_field(cls, field_value: str):
        try:
            emailinfo = validate_email(field_value)  # , check_deliverability=False)
            email = emailinfo.normalized
        except EmailNotValidError as e:
            print(str(e))
            raise ValueError from e
        return email


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    registration_date: dt
    model_config = ConfigDict(from_attributes=True)
