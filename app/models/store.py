
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import TimestampMixin, Base



class Store(TimestampMixin, Base):
    __tablename__ = "stores"
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))