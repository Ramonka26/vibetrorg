# autotrade/utils/validators.py
def validate_bid(current_price: float, rule: dict, trade: dict) -> bool:
    """Проверяет, нужно ли делать ставку"""
    # Проверка направления
    if trade["route"] != rule["route"]:
        return False
    
    # Проверка типа авто
    if trade["truck_type"] not in rule["truck_types"]:
        return False
    
    # Проверка объема груза
    if trade["cargo_volume"] < rule["min_volume"]:
        return False
    
    # Проверка лимита
    if current_price >= rule["min_price"]:
        return False
    
    return True