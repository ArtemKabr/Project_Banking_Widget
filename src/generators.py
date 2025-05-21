# generators.py
from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict],
                       currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по коду валюты.

    :param transactions: Список транзакций
    :param currency_code: Код валюты (например, 'USD')
    :return: Итератор транзакций, где код валюты совпадает
    """
    return (
        tx for tx in transactions
        if tx.get("operationAmount",
                  {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций по очереди.

    :param transactions: Список транзакций
    :return: Итератор строк с описаниями
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт от start до stop в формате XXXX XXXX XXXX XXXX

    :param start: Начальное значение
    :param stop: Конечное значение
    :return: Итератор строк с номерами карт
    """
    for number in range(start, stop + 1):
        num = f"{number:016d}"
        yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
