from src.db.db import Base
from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    UUID
)
from uuid import uuid4


class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(length=255), nullable=False)
    phone = Column(String(length=15), nullable=False, unique=True)
    is_admin = Column(Boolean, default=False, nullable=False)
    password = Column(String, nullable=False)
    
    def __repr__(self) -> str:
        return self.name