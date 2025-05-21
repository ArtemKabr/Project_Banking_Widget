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
    Проверяет корректное маскирование номеров карт.
    Ожидается, что отображаются первые 6 и последние 4 цифры.
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "123456789012345",  # Недостаточно цифр
        "1234abcd12345678",  # Содержит буквы
        "",  # Пустая строка
    ],
)
def test_get_mask_card_number_invalid(invalid_card_number):
    """
    Проверяет, что при передаче некорректных номеров карт (не 16 цифр)
    вызывается исключение ValueError.
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
    Проверяет корректную маскировку номеров банковских счетов.
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
    Проверяет, что при передаче некорректного номера счета
    (буквы или пустая строка) вызывается ValueError.
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
    Проверяет определение типа (карта или счет)
    и соответствующую маскировку.
    При некорректных данных — возвращает сообщение об ошибке.
    """
    assert mask_account_card(account_info) == expected


# ✅ Тестирование функции get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2025-04-30T12:34:56", "30.04.2025"),  # обычная дата
        ("2020-01-01T00:00:00", "01.01.2020"),  # начало года
        ("2024-02-29T12:00:00", "29.02.2024"),  # високосный год
        ("2025-02-29T12:00:00", "Неверный формат даты"),  # не високосный год
    ],
)
def test_get_date_valid(date_str, expected):
    """
    Проверяет корректное преобразование даты в формат ДД.ММ.ГГГГ.
    Включает тесты для високосных и не-високосных годов.
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
    Проверяет обработку некорректных строк даты.
    Функция должна возвращать "Неверный формат даты".
    """
    assert get_date(invalid_date_str) == "Неверный формат даты"


# ✅ Тестирование вспомогательной функции is_leap_year
def test_is_leap_year_explicit():
    """
    Проверяет логику функции is_leap_year:
    - делится на 4 и не делится на 100 (високосный)
    - делится на 400 (високосный)
    - не делится на 4 (не високосный)
    """
    assert is_leap_year(2020) is True  # делится на 4 и не на 100
    assert is_leap_year(1900) is False  # делится на 100, но не на 400
    assert is_leap_year(2000) is True  # делится на 400
    assert is_leap_year(2019) is False  # не делится на 4
