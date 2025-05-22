import json
from typing import Any


def load_operations(path: str) -> list[dict[str, Any]]:
    """
    Загружает список операций из JSON-файла.

    Функция читает содержимое указанного файла и преобразует его в список словарей.
    Если файл не найден или содержит некорректный JSON, возвращается пустой список.

    :param path: Путь к JSON-файлу с операциями
    :return: Список операций в формате list[dict[str, Any]] или пустой список при ошибке
    """
    try:
        # Открываем файл с указанием кодировки
        with open(path, encoding="utf-8") as f:
            # Загружаем содержимое как JSON
            data = json.load(f)
            # Проверяем, что результат — список
            if isinstance(data, list):
                return data
    # Обработка ошибок: файл не найден или некорректный JSON
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    # Если возникла ошибка или данные не являются списком — возвращаем пустой список
    return []
