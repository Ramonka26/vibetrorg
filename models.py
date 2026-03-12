# autotrade/models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserRule(Base):
    __tablename__ = "user_rules"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    route = Column(String, nullable=False)
    truck_types = Column(String)  # JSON-строка: ["фура", "рефрижератор"]
    min_volume = Column(Float, nullable=False)
    min_price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)