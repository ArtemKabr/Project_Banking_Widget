from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict],
                       currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданному коду валюты.

    Перебирает список транзакций и возвращает только те,
    у которых код валюты соответствует переданному значению.

    :param transactions: Список транзакций (каждая — словарь)
    :param currency_code: Код валюты, по которому нужно фильтровать (например, 'USD', 'RUB')
    :return: Итератор транзакций с заданной валютой
    """
    return (
        tx for tx in transactions
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор описаний транзакций.

    Последовательно извлекает поле "description" из каждой транзакции
    и возвращает строку с описанием. Если поле отсутствует, возвращает пустую строку.

    :param transactions: Список транзакций
    :return: Итератор строк с описаниями транзакций
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт.

    Генерирует числа от start до stop включительно, преобразует их в формат
    банковской карты вида XXXX XXXX XXXX XXXX.

    :param start: Начальное значение (включительно)
    :param stop: Конечное значение (включительно)
    :return: Итератор строк, каждая из которых представляет номер карты
    """
    for number in range(start, stop + 1):
        # Преобразуем число в строку из 16 цифр, дополняя нулями слева
        num = f"{number:016d}"
        # Форматируем номер с пробелами между блоками по 4 цифры
        yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
