from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import relationship

# using uuid
import uuid
from sqlalchemy.dialects.postgresql import UUID

# Create table and coulumns
class Note(Base):
    __tablename__ = "notes"

    # id = Column(Integer, primary_key=True, nullable=False)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    # server_default="TRUE", default on database
    # default=True, default on application

    # Foreign key to reference the user
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)

    # Relationship to the User model
    user = relationship("User", back_populates="notes")
    votes = relationship("Vote", back_populates="note", cascade="all, delete-orphan")
    # [
    #     {
    #         "title": "hello",
    #         "content": "sadasd",
    #         "published": true,
    #         "user": {
    #         "id": "79d1a15a-e3c5-43f1-a110-957de36aedd9",
    #         "email": "email1@gmail.com"
    #         }
    #     }
    # ]

class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True, nullable=False)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String, nullable=True)

    # Relationship to the Note model
    notes = relationship("Note", back_populates="user", cascade="all, delete-orphan")
    votes = relationship("Vote", back_populates="user", cascade="all, delete-orphan")
    # [
    #     {
    #         "title": "hello",
    #         "content": "sadasd",
    #         "published": true,
    #         "user": {
    #         "id": "79d1a15a-e3c5-43f1-a110-957de36aedd9",
    #         "email": "email1@gmail.com"
    #         }
    #     }
    # ]

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id', ondelete="CASCADE"), primary_key=True)
    note_id = Column(UUID(as_uuid=True), ForeignKey('notes.id', ondelete="CASCADE"), primary_key=True)

    # Relationship to the User model
    user = relationship("User", back_populates="votes")
    # Relationship to the Note model
    note = relationship("Note", back_populates="votes")
    