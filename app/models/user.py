from sqlalchemy import Column, Integer, String, Enum
from app.models.base import Base
from app.enums.user_role import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    role = Column(Enum(UserRole), default=UserRole.USER)
