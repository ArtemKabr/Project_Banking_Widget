from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    data: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению поля 'state'.

    Возвращает только те операции, у которых состояние (статус)
    совпадает с указанным.

    :param data: Список операций (каждая операция — словарь)
    :param state: Статус операции, по которому фильтруем (по умолчанию — 'EXECUTED')
    :return: Новый список операций, соответствующих заданному статусу
    """
    # Отбираем только те словари, у которых значение ключа 'state' совпадает с заданным
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате (ключ 'date').

    Даты должны быть в формате ISO 8601 (например, "2023-11-20T08:45:00").

    :param data: Список операций, содержащих ключ 'date'
    :param descending: Порядок сортировки:
                       - True — по убыванию (от новых к старым)
                       - False — по возрастанию (от старых к новым)
    :return: Новый отсортированный список операций
    """
    # Используем функцию sorted с преобразованием строки даты в datetime-объект
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=descending,  # Указание направления сортировки
    )
