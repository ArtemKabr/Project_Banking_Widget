import re
from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты, отображая только первые 6 и последние 4 цифры."""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета, отображая только последние 4 цифры."""
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")
    return f"**{account_number[-4:]}"


def mask_account_card(account_info: str) -> str:
    """Определяет тип данных (карта или счет) и возвращает маскированную строку."""
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
    """Определяет, является ли указанный год високосным."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формат 'ДД.ММ.ГГГГ'."""
    if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$", date_str):
        try:
            parsed_date = datetime.strptime(
                date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S"
            )
            return parsed_date.strftime("%d.%m.%Y")
        except ValueError:
            return "Неверный формат даты"
    return "Неверный формат даты"
