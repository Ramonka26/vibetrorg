Установите зависимости:
pip install -r requirements.txt

Запустите сервис:
python main.py

Создайте правило через API:

curl -X POST http://localhost:8000/rules \
-H "Content-Type: application/json" \
-d '{
  "route": "Москва-Санкт-Петербург",
  "truck_types": ["фура", "рефрижератор"],
  "min_volume": 20,
  "min_price": 30000
}'

