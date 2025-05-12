from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    data: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:

    """
    Фильтрует список словарей по значению ключа 'state'.

    Параметры:
        data (List[Dict[str, Any]]): Список операций.
        state (str): Статус операции, по умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Отфильтрованный список операций.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data: Список операций, содержащих ключ 'date'
    :param descending: Порядок сортировки. По убыванию — True (по умолчанию),
                       по возрастанию — False
    :return: Новый список, отсортированный по дате
    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=descending,
    )
