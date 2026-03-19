from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Boolean
from app.utils.uuid import generate_uuid, uuid_length
from app.utils.timenow import utcnow

class TimestampMixin:
    id = Column(String(uuid_length), primary_key=True, default=generate_uuid)
    created_at = Column(DateTime(timezone=True), default=utcnow)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)
    is_active = Column(Boolean, default=True)

Base = declarative_base()