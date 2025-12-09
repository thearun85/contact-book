from __future__ import annotations
from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from app.db import Base

class Contact(Base):

    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    nick_name: Mapped[str] = mapped_column(String(50), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(DateTime, nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    emails: Mapped[list[Email]] = relationship("Email", back_populates="contact", cascade="all, delete-orphan")
    phones: Mapped[list[Phone]] = relationship("Phone", back_populates="contact", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Contact {self.id}: {self.first_name} {self.last_name}>"

