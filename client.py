# autotrade/atbucks_client.py
import asyncio
import websockets
import json
from config import Config
from workers.bid_worker import process_trade

async def listen_to_atrucks():
    """Слушает обновления торгов через WebSocket"""
    async with websockets.connect(
        Config.ATRUCKS_WS_URL,
        extra_headers={"Authorization": f"Bearer {Config.ATRUCKS_API_KEY}"}
    ) as ws:
        print("Подключено к Atrucks.su")
        while True:
            try:
                trade_data = await ws.recv()
                trade = json.loads(trade_data)
                # Обработка в фоновом режиме
                asyncio.create_task(process_trade(trade))
            except websockets.ConnectionClosed:
                print("Переподключение...")
                await asyncio.sleep(5)