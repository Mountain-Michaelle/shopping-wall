
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base 



class Store(Base):
    __tablename__ = "stores"
    id =   Column(Integer, primary_key=True, index=True) 
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))