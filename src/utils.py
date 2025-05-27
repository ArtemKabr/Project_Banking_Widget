import json
from typing import Any

from src.utils_logger import logger as utils_logger


def load_operations(path: str) -> list[dict[str, Any]]:
    """
    Загружает список операций из JSON-файла.

    :param path: Путь к JSON-файлу с операциями
    :return: Список операций или пустой список при ошибке
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                utils_logger.debug("Успешно загружены операции из файла: %s", path)
                return data
            else:
                utils_logger.error("Файл %s не содержит список", path)
    except FileNotFoundError:
        utils_logger.error("Файл не найден: %s", path)
    except json.JSONDecodeError:
        utils_logger.error("Ошибка декодирования JSON в файле: %s", path)

    return []
