import uuid

from app import db
from sqlalchemy import (
    Column,
    Integer,
    Float,
    DECIMAL,
    String,
    Text,
    Boolean,
    ForeignKey,
    text,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID


# class Invoice(db.Model): ...
