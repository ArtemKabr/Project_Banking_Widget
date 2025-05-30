import os
import time
from typing import Any

import requests
from dotenv import load_dotenv
from src.utils_logger import logger as utils_logger

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
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        utils_logger.debug("Пропуск конвертации — валюта уже RUB: %.2f", amount)
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        utils_logger.error("API_KEY не найден в переменных окружения")
        raise ValueError("API_KEY не найден в переменных окружения")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": api_key}

    retries = 3
    delay = 1

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=(2, 5))
            response.raise_for_status()
            # print(response.text)

            if response.status_code == 200:
                utils_logger.info(
                    "[RATE-LIMIT] Осталось сегодня: %s/%s, в месяц: %s/%s",
                    response.headers.get("x-ratelimit-remaining-day", "?"),
                    response.headers.get("x-ratelimit-limit-day", "?"),
                    response.headers.get("x-ratelimit-remaining-month", "?"),
                    response.headers.get("x-ratelimit-limit-month", "?"),
                )

            data = response.json()
            result = float(data["result"])
            utils_logger.debug("Успешная конвертация: %s %.2f -> RUB %.2f", currency, amount, result)
            return result


        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 429:
                if attempt == retries - 1:
                    utils_logger.warning(
                        "Попытка %d: Лимит API превышен (429). Прерываем повторы — переходим к fallback.",
                        attempt + 1
                    )
                    break  # Прерываем цикл и переходим к заглушке
                utils_logger.warning(
                    "Попытка %d: Превышен лимит API (429). Повтор через %d сек.",
                    attempt + 1, delay
                )
                utils_logger.warning("429: лимит запросов превышен — заголовки лимитов недоступны.")
                time.sleep(delay)
                delay *= 2
            else:
                utils_logger.error(
                    "Ошибка HTTP при конвертации ID %s: %s",
                    transaction.get("id", "неизвестно"), str(e)
                )
                raise

    # 🔁 После 3-х неудачных попыток используем fallback-курс
    # === НАЧАЛО ЗАГЛУШКИ (можно удалить при переходе на платный API) ===
    fallback_rate = 90 if currency == "USD" else 100
    fallback_value = round(amount * fallback_rate, 2)
    utils_logger.warning(
        "Использован fallback-курс для %s: %.2f * %d = %.2f",
        currency, amount, fallback_rate, fallback_value
    )
    return fallback_value
    # === КОНЕЦ ЗАГЛУШКИ ===

