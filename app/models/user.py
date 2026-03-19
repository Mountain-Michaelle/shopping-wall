
from sqlalchemy import Column, String 
from app.db.base import TimestampMixin, Base

class User(TimestampMixin, Base):
    __tablename__ = "users"
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
