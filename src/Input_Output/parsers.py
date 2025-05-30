from typing import List, Dict, Any, cast
import pandas as pd


def read_csv_transactions(path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список транзакций (словарей).
    :param path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(path)
    return cast(List[Dict[str, Any]], df.to_dict(orient="records"))


def read_excel_transactions(path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список транзакций (словарей).
    :param path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(path)
    return cast(List[Dict[str, Any]], df.to_dict(orient="records"))
