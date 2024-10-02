from flask_login import UserMixin
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)
from app import db


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(
        DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now()
    )

    def __init__(self, email, password, is_admin=False) -> None:
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return f"<User: {self.email}"
