import re
from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты,
    отображая только первые 6 цифр и последние 4 цифры.

    Параметры:
    card_number (str): Номер банковской карты (должен быть строкой из 16 цифр).

    Возвращает:
    str: Маскированный номер карты в формате 'XXXX XX** **** XXXX'.

    Исключения:
    ValueError: Если номер карты не состоит из 16 цифр."""
    # Проверяем, что номер карты состоит из 16 цифр
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Формируем маску
    masked_number = f"{card_number[:4]} {card_number[4:6]}**" f" **** {card_number[-4:]}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета, отображая только последние 4 цифры.

    Параметры:
    account_number (str): Номер банковского счета
    (должен быть строкой из цифр).

    Возвращает:
    str: Маскированный номер счета в формате '**XXXX'.

    Исключения:
    ValueError: Если номер счета содержит не только цифры."""
    # Проверяем, что номер счёта состоит только из цифр
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")

    # Маскируем номер счёта, оставляя только последние 4 цифры
    masked_account = f"**{account_number[-4:]}"

    return masked_account


def mask_account_card(account_info: str) -> str:
    """Обрабатывает информацию о банковской карте
    или счете и возвращает маскированный номер.

    Параметры:
    account_info (str): Строка, содержащая тип и номер карты или счета.

    Возвращает:
    str: Строка с замаскированным номером.
    """
    # Разбиваем строку на тип и номер
    match = re.match(r"(\D+)\s(\d+)", account_info.strip())
    if match:
        account_type = match.group(1).strip()
        account_number = match.group(2).strip()

        if "Счет" in account_type:
            # Если тип "Счет", маскируем номер счета
            return f"{account_type} {get_mask_account(account_number)}"
        else:
            # Если это карта, маскируем номер карты
            return f"{account_type} {get_mask_card_number(account_number)}"
    else:
        return "Неверный формат ввода."


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Параметры:
    date_str (str): Строка с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss".

    Возвращает:
    str: Дата в формате "ДД.ММ.ГГГГ".
    """
    try:
        # Преобразуем строку в объект datetime
        date_obj = datetime.fromisoformat(date_str)
        # Форматируем в нужный вид
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"
