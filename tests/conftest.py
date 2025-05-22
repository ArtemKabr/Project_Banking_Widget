"""
Фикстуры для модульного тестирования функций банковского виджета.

Содержит фикстуры для:
- валидных и невалидных номеров карт и счетов;
- коротких номеров;
- тестовых данных транзакций;
- корректных и некорректных дат;
- тест-кейсов для функции mask_account_card.

Фикстуры используются в тестах Pytest.
"""

import os
import sys

import pytest  # Подключение pytest

# Добавляем папку src в sys.path, чтобы модули можно было импортировать
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


# Фикстура: некорректный номер карты (слишком короткий)
@pytest.fixture
def invalid_card_number():
    return "12345"


# Фикстура: некорректный номер карты (содержит буквы)
@pytest.fixture
def invalid_card_number_with_letters():
    return "1234abcd12345678"


# Фикстура: некорректный номер счета (содержит буквы)
@pytest.fixture
def invalid_account_number():
    return "123A56789"


# Фикстура: слишком короткий номер счета
@pytest.fixture
def short_account_number():
    return "123"


# Фикстура: пример списка операций для фильтрации и сортировки
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-05-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-04-01T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-06-01T11:30:00"},
    ]


# Фикстура: валидные номера карт
@pytest.fixture
def valid_card_numbers():
    return ["1234567812345678", "9876543210123456", "1111222233334444"]


# Фикстура: невалидные номера карт
@pytest.fixture
def invalid_card_numbers():
    return [
        "123456789012345",  # Меньше 16 цифр
        "1234abcd12345678",  # Содержит буквы
        "9876543210",  # Слишком короткий
        "",  # Пустая строка
    ]


# Фикстура: валидные номера счетов
@pytest.fixture
def valid_account_numbers():
    return ["9876543210", "1234567890", "5555555555"]


# Фикстура: невалидные номера счетов
@pytest.fixture
def invalid_account_numbers():
    return [
        "1234abcd",  # Содержит буквы
        "98765432$",  # Символы кроме цифр
        "",  # Пустая строка
    ]


# Фикстура: слишком короткие номера счетов
@pytest.fixture
def short_account_numbers():
    return ["12", "1"]


# Фикстура: корректные ISO-даты
@pytest.fixture
def valid_dates():
    return ["2025-04-30T12:34:56", "2020-01-01T00:00:00"]


# Фикстура: некорректные даты
@pytest.fixture
def invalid_dates():
    return ["2025-04-30", "30.04.2025"]  # Отсутствует время / неверный формат


# Фикстура: пары (вход, ожидаемый результат) для mask_account_card
@pytest.fixture
def account_card_test_cases():
    return [
        ("Счет 9876543210", "Счет **3210"),
        ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
        ("Карта abcdefghijklmnop", "Неверный формат ввода."),
        ("Счет abcdefghij", "Неверный формат ввода."),
    ]
