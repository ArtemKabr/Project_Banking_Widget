import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # Корректный номер карты
        ("9876543210123456", "9876 54** **** 3456"),  # Другой номер
        ("1111222233334444", "1111 22** **** 4444"),  # Еще номер
        ("0000000000000000", "0000 00** **** 0000"),  # Номер с нулями
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    # Тестирование корректного маскирования номеров карт
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "12345",  # Неверная длина
        "1234abcd12345678",  # Строка с буквами
        "",  # Пустая строка
    ],
)
def test_get_mask_card_number_invalid_length(invalid_card_number):
    # Тестирование ошибки для номера карты не из 16 цифр
    with pytest.raises(
        ValueError,
        match="Номер карты должен содержать 16 цифр."
    ):
        get_mask_card_number(invalid_card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("9876543210", "**3210"),  # Корректный номер счета
        ("1234567890", "**7890"),  # Другой номер
        ("5555555555", "**5555"),  # Еще номер
        ("1", "**1"),  # Один символ
    ],
)
def test_get_mask_account_valid(account_number, expected):
    # Тестирование корректного маскирования номеров счетов
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "1234abcd",  # Строка с буквами
        "98765432$",  # Строка с нецифровыми символами
        "",  # Пустая строка
    ],
)
def test_get_mask_account_invalid_chars(invalid_account_number):
    # Тестирование ошибки для номера счета с буквами или нецифровыми символами
    with pytest.raises(
        ValueError,
        match="Номер счета должен содержать только цифры."
    ):
        get_mask_account(invalid_account_number)


@pytest.mark.parametrize(
    "short_account_number, expected",
    [
        ("123", "**123"),  # Короткий номер счета
        ("12", "**12"),  # Еще более короткий номер
    ],
)
def test_get_mask_account_short_account(short_account_number, expected):
    # Тестирование короткого номера счета
    assert get_mask_account(short_account_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1", "**1"),  # Один символ
        ("12345678901234567890", "**7890"),  # Длинный номер
    ],
)
def test_get_mask_account_edge_cases(account_number, expected):
    # Тестирование крайних случаев для номеров счетов
    assert get_mask_account(account_number) == expected
