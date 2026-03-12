# autotrade/services/rule_service.py
from models import UserRule
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
import json

engine = create_engine(Config.DB_URL)
Session = sessionmaker(bind=engine)

def get_active_rules():
    """Получает активные правила пользователей"""
    session = Session()
    rules = session.query(UserRule).filter(UserRule.is_active == True).all()
    session.close()
    
    return [
        {
            "id": rule.id,
            "user_id": rule.user_id,
            "route": rule.route,
            "truck_types": json.loads(rule.truck_types),
            "min_volume": rule.min_volume,
            "min_price": rule.min_price
        }
        for rule in rules
    ]