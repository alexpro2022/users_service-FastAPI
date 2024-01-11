from datetime import datetime as dt

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core import Base, settings


class User(Base):
    username: Mapped[str] = mapped_column(String(settings.username_max_length))
    email: Mapped[str] = mapped_column(unique=True, index=True)
    registration_date: Mapped[dt] = mapped_column(default=dt.now)

    def __repr__(self) -> str:
        return (
            f'\nid: {self.id}'
            f'\nusername: {self.username},'
            f'\nemail: {self.email},'
            f'\nregistration date: {self.registration_date},\n'
        )
