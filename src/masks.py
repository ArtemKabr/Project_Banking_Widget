def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, отображая только первые 6 и последние 4 цифры.

    Формат маскированного номера: 'XXXX XX** **** XXXX'.

    Пример:
        >>> get_mask_card_number("1234567890123456")
        '1234 56** **** 3456'

    :param card_number: Строка из 16 цифр — номер карты
    :return: Маскированная строка
    :raises ValueError: Если номер карты не состоит из 16 цифр
    """
    # Проверка: длина должна быть ровно 16 символов и все — цифры
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Маскируем средние 6 цифр карты, оставляя первые 6 и последние 4
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя только последние 4 цифры.

    Формат маскированного номера: '**XXXX'.

    Пример:
        >>> get_mask_account("40817810099910004312")
        '**4312'

    :param account_number: Строка, содержащая только цифры
    :return: Маскированная строка
    :raises ValueError: Если номер содержит не только цифры
    """
    # Проверка: строка должна состоять только из цифр
    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")

    # Маскируем все, кроме последних 4 цифр
    masked_account = f"**{account_number[-4:]}"
    return masked_account
