# autotrade/config.py
import os

class Config:
    # Настройки Atrucks.su
    ATRUCKS_WS_URL = "wss://api.atrucks.su/trades"
    ATRUCKS_API_KEY = os.getenv("ATRUCKS_API_KEY", "your-api-key")
    
    # Настройки Redis
    REDIS_URL = "redis://localhost:6379/0"
    
    # Настройки БД
    DB_URL = "postgresql://user:pass@localhost:5432/autotrade"
    
    # Лимиты
    MAX_BID_PER_SECOND = 3  # Макс. ставок в секунду на пользователя
    BID_INCREMENT = 500     # Шаг повышения ставки