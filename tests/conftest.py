import os
import sys

import pytest  # Добавляем импорт pytest

# Добавляем папку src в путь для поиска модулей
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')
))


# Фикстура для недопустимого номера карты (короткий)
@pytest.fixture
def invalid_card_number():
    return "12345"  # Пример неверного номера карты


# Фикстура для недопустимого номера карты (с буквами)
@pytest.fixture
def invalid_card_number_with_letters():
    return "1234abcd12345678"  # Строка с буквами в номере карты


# Фикстура для недопустимого номера счета (содержит буквы)
@pytest.fixture
def invalid_account_number():
    return "123A56789"  # Пример некорректного номера счета с буквами


# Фикстура для короткого номера счета
@pytest.fixture
def short_account_number():
    return "123"  # Пример короткого номера счета


# Фикстура для тестов обработки операций
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-05-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-04-01T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-06-01T11:30:00"},
    ]


# Фикстуры для тестов карт
@pytest.fixture
def valid_card_numbers():
    return ["1234567812345678", "9876543210123456", "1111222233334444"]


# Фикстуры для тестов неправильных номеров карт
@pytest.fixture
def invalid_card_numbers():
    return [
        "123456789012345",  # Неверная длина
        "1234abcd12345678",  # Строка с буквами
        "9876543210",  # Слишком короткий номер
        "",  # Пустая строка
    ]


# Фикстуры для тестов счетов
@pytest.fixture
def valid_account_numbers():
    return ["9876543210", "1234567890", "5555555555"]


# Фикстуры для тестов неправильных номеров счетов
@pytest.fixture
def invalid_account_numbers():
    return [
        "1234abcd",  # Строка с буквами
        "98765432$",  # Строка с нецифровыми символами
        "",  # Пустая строка
    ]


# Фикстуры для тестов коротких номеров счетов
@pytest.fixture
def short_account_numbers():
    return ["12", "1"]  # Примеры слишком коротких номеров


# Фикстуры для тестов дат
@pytest.fixture
def valid_dates():
    return ["2025-04-30T12:34:56", "2020-01-01T00:00:00"]


@pytest.fixture
def invalid_dates():
    return ["2025-04-30", "30.04.2025"]


# Фикстура для тестов mask_account_card
@pytest.fixture
def account_card_test_cases():
    return [
        ("Счет 9876543210", "Счет **3210"),
        ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
        ("Карта abcdefghijklmnop", "Неверный формат ввода."),
        ("Счет abcdefghij", "Неверный формат ввода."),
    ]
