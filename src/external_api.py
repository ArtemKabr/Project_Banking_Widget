import os
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()

def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Преобразует сумму транзакции в рубли (RUB).

    Если валюта уже RUB, возвращает её без изменений.
    Если валюта USD или EUR — делает запрос к API для получения курса.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": api_key}

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    return float(data["result"])
