from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.sql import func

from .database import Base

class JsonData(Base):
    __tablename__ = 'db_jsondata'
    id = Column(Integer, primary_key = True, index = True)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    json_data = Column(String)