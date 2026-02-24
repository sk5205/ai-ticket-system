from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    category = Column(String)
    priority = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Open")