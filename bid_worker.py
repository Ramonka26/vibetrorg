# autotrade/workers/bid_worker.py
import asyncio
from services.rule_service import get_active_rules
from services.bid_service import auto_bid

async def process_trade(trade: dict):
    """Обрабатывает новое торговое предложение"""
    rules = get_active_rules()
    
    for rule in rules:
        if validate_bid(trade["current_bid"], rule, trade):
            # Запуск ставки в фоновом режиме
            asyncio.create_task(auto_bid(trade, rule))
            print(f"Запущена ставка для правила {rule['id']}")