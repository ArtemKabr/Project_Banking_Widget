import pytest

from src.widget import get_date, get_mask_account, get_mask_card_number, mask_account_card


# Тестирование get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # Корректный номер карты
        ("9876543210123456", "9876 54** **** 3456"),  # Другой номер
        ("1111222233334444", "1111 22** **** 4444"),  # Еще номер
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    """Тестирование корректного маскирования номеров карт"""
    assert get_mask_card_number(card_number) == expected


# Тестирование некорректных номеров карт
@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "123456789012345",  # Слишком короткий номер
        "1234abcd12345678",  # Содержит буквы
        "",  # Пустая строка
    ]
)
def test_get_mask_card_number_invalid(invalid_card_number):
    """Тестирование ошибки для некорректного номера карты (не 16 цифр)"""
    with pytest.raises(ValueError,
                       match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(invalid_card_number)


# Тестирование get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("9876543210", "**3210"),  # Корректный номер счета
        ("1234567890", "**7890"),  # Другой номер
        ("5555555555", "**5555"),  # Еще номер
    ],
)
def test_get_mask_account_valid(account_number, expected):
    """Тестирование корректного маскирования номеров счетов"""
    assert get_mask_account(account_number) == expected


# Тестирование некорректных номеров счетов
@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "1234abcd",  # Содержит буквы
        "",  # Пустая строка
    ]
)
def test_get_mask_account_invalid(invalid_account_number):
    """Тестирование ошибки для некорректного номера счета (буквы в строке)"""
    with pytest.raises(ValueError,
                       match="Номер счета должен содержать только цифры."):
        get_mask_account(invalid_account_number)


# Тестирование mask_account_card
@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("Счет 9876543210", "Счет **3210"),
        # Корректный номер счета
        ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
        # Корректный номер карты
        ("Карта abcdefghijklmnop", "Неверный формат ввода."),
        # Некорректный номер карты
        ("Счет abcdefghij", "Неверный формат ввода."),
        # Некорректный номер счета
        ("", "Неверный формат ввода."),
        # Пустая строка
    ]
)
def test_mask_account_card(account_info, expected):
    """Тестирование обработки информации о банковской карте или счете"""
    assert mask_account_card(account_info) == expected


# Тестирование get_date
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2025-04-30T12:34:56", "30.04.2025"),
        # Корректный формат
        ("2020-01-01T00:00:00", "01.01.2020"),
        # Другой корректный формат
        ("2024-02-29T12:00:00", "29.02.2024"),
        # Високосный год
        ("2025-02-29T12:00:00", "Неверный формат даты"),
        # Некорректный 29 февраля в 2025 году
    ],
)
def test_get_date_valid(date_str, expected):
    """Тестирование корректной обработки даты"""
    assert get_date(date_str) == expected


# Тестирование некорректного формата даты
@pytest.mark.parametrize(
    "invalid_date_str",
    [
        "2025-04-30",  # Неверный формат
        "30.04.2025",  # Неверный формат
        "",  # Пустая строка
    ]
)
def test_get_date_invalid(invalid_date_str):
    """Тестирование обработки некорректной даты"""
    assert get_date(invalid_date_str) == "Неверный формат даты"
    # Ожидаем ошибку для некорректного формата


