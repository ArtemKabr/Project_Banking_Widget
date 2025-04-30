# test_masks.py

import pytest
from src.masks import get_mask_card_number, get_mask_account


# Параметризация для тестирования get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),  # Тест с корректным номером карты
    ("9876543210123456", "9876 54** **** 3456"),  # Другой корректный номер карты
    ("1111222233334444", "1111 22** **** 4444"),  # Еще один номер карты
])
def test_get_mask_card_number_valid(card_number, expected):
    """Тестирование корректного маскирования номеров карт"""
    assert get_mask_card_number(card_number) == expected

# Тестирование некорректных номеров карт
def test_get_mask_card_number_invalid_length(invalid_card_number):
    """Тестирование ошибки для некорректного номера карты (не 16 цифр)"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(invalid_card_number)

def test_get_mask_card_number_invalid_chars():
    """Тестирование ошибки для строки, содержащей буквы в номере карты"""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("1234abcd12345678")

# Параметризация для тестирования get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("9876543210", "**3210"),  # Тест с корректным номером счета
    ("1234567890", "**7890"),  # Другой корректный номер счета
    ("5555555555", "**5555"),  # Еще один номер счета
])
def test_get_mask_account_valid(account_number, expected):
    """Тестирование корректного маскирования номеров счетов"""
    assert get_mask_account(account_number) == expected

# Тестирование некорректных номеров счетов
def test_get_mask_account_invalid_chars(invalid_account_number):
    """Тестирование ошибки для некорректного номера счета (буквы в строке)"""
    with pytest.raises(ValueError, match="Номер счета должен содержать только цифры."):
        get_mask_account(invalid_account_number)

def test_get_mask_account_short_account(short_account_number):
    """Тестирование короткого номера счета (меньше 4 символов)"""
    assert get_mask_account(short_account_number) == "**123"

# Граничные случаи для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("1", "**1"),  # Один символ
    ("12345678901234567890", "**7890"),  # Очень длинный номер счета (правильное значение для последней части — 7890)
])
def test_get_mask_account_edge_cases(account_number, expected):
    """Тестирование крайних случаев для номеров счетов"""
    assert get_mask_account(account_number) == expected

