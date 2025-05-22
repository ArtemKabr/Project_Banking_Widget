import re
from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, отображая только первые 6 и последние 4 цифры.

    Формат маскирования: 'XXXX XX** **** XXXX'

    :param card_number: Строка из 16 цифр
    :return: Маскированная строка
    :raises ValueError: Если строка не является валидным номером карты
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта, оставляя только последние 4 цифры.

    Формат маскирования: '**XXXX'

    :param account_number: Строка, содержащая только цифры
    :return: Маскированная строка
    :raises ValueError: Если строка содержит нецифровые символы
    """
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")
    return f"**{account_number[-4:]}"


def mask_account_card(account_info: str) -> str:
    """
    Определяет, является ли переданная строка номером карты или счёта,
    и возвращает соответствующую маскированную строку.

    Поддерживаемый формат: "<Тип> <Номер>", например:
        - "Visa 1234567890123456"
        - "Счет 40817810099910004312"

    :param account_info: Строка с типом и номером
    :return: Маскированная строка или сообщение об ошибке
    """
    # Используем регулярное выражение для разделения типа и номера
    match = re.match(r"(\D+)\s(\d+)", account_info.strip())
    if match:
        account_type = match.group(1).strip()
        account_number = match.group(2).strip()
        if "Счет" in account_type:
            return f"{account_type} {get_mask_account(account_number)}"
        else:
            return f"{account_type} {get_mask_card_number(account_number)}"
    return "Неверный формат ввода."


def is_leap_year(year: int) -> bool:
    """
    Проверяет, является ли указанный год високосным.

    Високосный год:
        - делится на 4,
        - но не делится на 100, за исключением тех, что делятся на 400.

    :param year: Год в формате int
    :return: True, если год високосный, иначе False
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_date(date_str: str) -> str:
    """
    Преобразует строку в формате ISO (с временем) в формат 'ДД.ММ.ГГГГ'.

    Ожидаемый входной формат: 'YYYY-MM-DDTHH:MM:SS[.microsec]'

    :param date_str: Строка с датой и временем
    :return: Строка с датой в формате 'ДД.ММ.ГГГГ' или сообщение об ошибке
    """
    # Проверяем соответствие формату ISO с помощью регулярного выражения
    if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$", date_str):
        try:
            # Отбрасываем микросекунды (если есть) и преобразуем в datetime
            parsed_date = datetime.strptime(
                date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S"
            )
            return parsed_date.strftime("%d.%m.%Y")
        except ValueError:
            return "Неверный формат даты"
    return "Неверный формат даты"
