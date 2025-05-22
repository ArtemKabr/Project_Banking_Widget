import pytest

from src.widget import (
    get_date,
    get_mask_account,
    get_mask_card_number,
    is_leap_year,
    mask_account_card,
)


# ✅ Тестирование функции get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("9876543210123456", "9876 54** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    """
    ✅ Тест: корректное маскирование номеров банковских карт.

    Проверяет, что функция возвращает строку с первыми 6 и последними 4 цифрами,
    а остальные — заменены на символы "*".
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "123456789012345",  # Недостаточная длина
        "1234abcd12345678",  # Содержит недопустимые символы
        "",  # Пустая строка
    ],
)
def test_get_mask_card_number_invalid(invalid_card_number):
    """
    ✅ Тест: обработка ошибок в номерах карт.

    Проверяет, что при передаче невалидного номера карты вызывается исключение ValueError.
    """
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(invalid_card_number)


# ✅ Тестирование функции get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("9876543210", "**3210"),
        ("1234567890", "**7890"),
        ("5555555555", "**5555"),
    ],
)
def test_get_mask_account_valid(account_number, expected):
    """
    ✅ Тест: корректное маскирование номеров банковских счетов.

    Проверяет, что возвращаются только последние 4 цифры с префиксом "**".
    """
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "1234abcd",  # Содержит буквы
        "",  # Пустая строка
    ],
)
def test_get_mask_account_invalid(invalid_account_number):
    """
    ✅ Тест: проверка обработки нецифровых номеров счетов.

    При наличии букв или пустой строки должно быть выброшено исключение.
    """
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры."):
        get_mask_account(invalid_account_number)


# ✅ Тестирование функции mask_account_card
@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("Счет 9876543210", "Счет **3210"),
        ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
        ("Карта abcdefghijklmnop", "Неверный формат ввода."),
        ("Счет abcdefghij", "Неверный формат ввода."),
        ("", "Неверный формат ввода."),
    ],
)
def test_mask_account_card(account_info, expected):
    """
    ✅ Тест: маскирование по типу источника — карта или счёт.

    Проверяет, что функция корректно определяет тип источника
    и вызывает соответствующую маскировку, либо возвращает сообщение об ошибке.
    """
    assert mask_account_card(account_info) == expected


# ✅ Тестирование функции get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2025-04-30T12:34:56", "30.04.2025"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("2024-02-29T12:00:00", "29.02.2024"),  # високосный год
        ("2025-02-29T12:00:00", "Неверный формат даты"),  # не високосный
    ],
)
def test_get_date_valid(date_str, expected):
    """
    ✅ Тест: преобразование ISO-формата в ДД.ММ.ГГГГ.

    Проверяет как обычные даты, так и обработку високосных годов.
    """
    assert get_date(date_str) == expected


@pytest.mark.parametrize(
    "invalid_date_str",
    [
        "2025-04-30",  # без времени
        "30.04.2025",  # неверный формат
        "",  # пустая строка
    ],
)
def test_get_date_invalid(invalid_date_str):
    """
    ✅ Тест: обработка некорректных строк даты.

    Проверяет, что функция возвращает сообщение об ошибке при неправильном формате.
    """
    assert get_date(invalid_date_str) == "Неверный формат даты"


# ✅ Тестирование функции is_leap_year
def test_is_leap_year_explicit():
    """
    ✅ Тест: проверка условий для високосного года.

    - Делится на 4 и не делится на 100 => True
    - Делится на 400 => True
    - Делится на 100, но не на 400 => False
    - Не делится на 4 => False
    """
    assert is_leap_year(2020) is True  # делится на 4, не на 100
    assert is_leap_year(1900) is False  # делится на 100, не на 400
    assert is_leap_year(2000) is True  # делится на 400
    assert is_leap_year(2019) is False  # не делится на 4
