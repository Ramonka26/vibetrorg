# autotrade/services/bid_service.py
import aiohttp
import asyncio
from config import Config
from utils.validators import validate_bid

async def send_bid(trade_id: str, price: float) -> bool:
    """Отправляет ставку через API Atrucks"""
    url = f"https://api.atrucks.su/trades/{trade_id}/bid"
    payload = {"price": price}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, 
            json=payload,
            headers={"Authorization": f"Bearer {Config.ATRUCKS_API_KEY}"}
        ) as resp:
            if resp.status == 200:
                return True
            # Обработка rate-limit
            if resp.status == 429:
                await asyncio.sleep(1)  # Ждем 1 сек
            return False

async def auto_bid(trade: dict, rule: dict):
    """Динамически повышает ставку до min_price"""
    current_price = trade["current_bid"]
    target_price = rule["min_price"]
    
    while current_price < target_price:
        # Проверка на соответствие правилам
        if not validate_bid(current_price, rule, trade):
            break
            
        # Вычисляем новую ставку
        new_price = min(current_price + Config.BID_INCREMENT, target_price)
        success = await send_bid(trade["id"], new_price)
        
        if success:
            current_price = new_price
            print(f"Ставка повышена до {new_price} ₽ для {trade['id']}")
        else:
            await asyncio.sleep(0.2)  # Защита от спама
            
        await asyncio.sleep(0.1)  # Задержка между попытками