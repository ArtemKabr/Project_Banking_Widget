import os
from typing import Any
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Преобразует сумму транзакции в рубли (RUB).

    Функция принимает словарь транзакции, извлекает сумму и валюту.
    Если валюта уже указана как RUB, возвращает сумму без изменений.
    Если валюта — USD или EUR, выполняет запрос к API для получения актуального курса
    и возвращает сумму в рублях.

    :param transaction: Словарь с данными о транзакции, содержащий структуру:
                        {
                            "operationAmount": {
                                "amount": <число>,
                                "currency": {
                                    "code": <валюта, например "USD">
                                }
                            }
                        }
    :return: Сумма в рублях (float)
    :raises ValueError: если API_KEY отсутствует в переменных окружения
    :raises requests.HTTPError: если запрос к API завершился ошибкой
    """
    # Извлекаем сумму транзакции
    amount = float(transaction["operationAmount"]["amount"])
    # Извлекаем код валюты
    currency = transaction["operationAmount"]["currency"]["code"]

    # Если валюта уже рубли, возвращаем сумму без изменений
    if currency == "RUB":
        return amount

    # Получаем API ключ из переменных окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения")

    # Адрес API для конвертации валют
    url = "https://api.apilayer.com/exchangerates_data/convert"
    # Параметры запроса: из какой валюты, в какую и сколько
    params = {"to": "RUB", "from": currency, "amount": amount}
    # Заголовок с API ключом
    headers = {"apikey": api_key}

    # Отправляем GET-запрос к API
    response = requests.get(url, params=params, headers=headers, timeout=10)
    # Проверяем наличие HTTP ошибок
    response.raise_for_status()
    # Преобразуем ответ в JSON
    data = response.json()

    # Извлекаем и возвращаем сконвертированную сумму
    return float(data["result"])
