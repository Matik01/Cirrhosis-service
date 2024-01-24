from sqlalchemy import Boolean, Column, Integer, String

from src.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String, default="")
    money = Column(Integer, default=1000)
    is_active = Column(Boolean, default=False)
    token = Column(String, default="")
