import sys
sys.path.append("../database")
from database.database import *

from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.sql import func

class TodoDB(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    