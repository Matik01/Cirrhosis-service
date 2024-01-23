from sqlalchemy import Boolean, Column, Integer, String, Float

from src.core.database import Base


class Predictor(Base):
    __tablename__ = "predictors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    cost = Column(Float)
    is_active = Column(Boolean, default=True)
