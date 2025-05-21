import json
from typing import Any


def load_operations(path: str) -> list[dict[str, Any]]:
    """
    Загружает список операций из JSON-файла.
    Возвращает список словарей или пустой список при ошибке.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    return []
