from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text

# Create table and coulumns
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
# server_default="TRUE", default on database
# default=True, default on application
