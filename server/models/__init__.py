from sqlalchemy import Integer, String, TIMESTAMP, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from models.music.Note import Note
from models.music.Interval import Interval
from models.user.User import User

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, default=func.now())
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, default=func.now(), onupdate=func.now())
    disabled_at: Mapped[str|None] = mapped_column(String, nullable=True)
    deleted_at: Mapped[str|None] = mapped_column(String, nullable=True)

class Models:
    User = User
    Note = Note
    Interval = Interval
