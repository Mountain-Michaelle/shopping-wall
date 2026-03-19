import uuid
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import TimestampMixin, Base
from app.utils.uuid import generate_uuid, uuid_length


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"))