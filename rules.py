# autotrade/routes/rules.py
from fastapi import APIRouter, Depends, HTTPException
from models import UserRule
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from config import Config

router = APIRouter()
engine = create_engine(Config.DB_URL)
Base = declarative_base()

class RuleCreate(BaseModel):
    route: str
    truck_types: list[str]
    min_volume: float
    min_price: float

@router.post("/rules")
async def create_rule(rule: RuleCreate, user_id: str = "test_user"):
    """Создает новое правило для пользователя"""
    new_rule = UserRule(
        user_id=user_id,
        route=rule.route,
        truck_types=json.dumps(rule.truck_types),
        min_volume=rule.min_volume,
        min_price=rule.min_price
    )
    
    session = Session()
    session.add(new_rule)
    session.commit()
    session.close()
    
    return {"status": "success", "rule_id": new_rule.id}