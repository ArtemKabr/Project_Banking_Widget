import re
from collections import Counter
from typing import List, Dict


def search_transactions_by_description(transactions: List[Dict], query: str) -> List[Dict]:
    """
    Ищет операции, в описании которых содержится заданная строка.

    :param transactions: Список словарей с транзакциями.
    :param query: Строка для поиска в описании.
    :return: Список транзакций, содержащих строку в поле 'description'.
    """
    pattern = re.compile(query, re.IGNORECASE)
    return [tx for tx in transactions if "description" in tx and pattern.search(tx["description"])]


def count_transaction_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям из поля 'description'.

    :param transactions: Список словарей с транзакциями.
    :return: Словарь {категория: количество}.
    """
    descriptions = [tx["description"] for tx in transactions if "description" in tx]
    return dict(Counter(descriptions))
