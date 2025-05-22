import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # Корректный номер карты
        ("9876543210123456", "9876 54** **** 3456"),  # Другой корректный номер
        ("1111222233334444", "1111 22** **** 4444"),  # Ещё один пример
        ("0000000000000000", "0000 00** **** 0000"),  # Все цифры — нули
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    """
    ✅ Тест: маскирование корректных номеров банковских карт.

    Проверяет, что функция `get_mask_card_number` возвращает
    корректно отформатированную и замаскированную строку.
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "12345",               # Недостаточно цифр
        "1234abcd12345678",    # Буквы в строке
        "",                    # Пустая строка
    ],
)
def test_get_mask_card_number_invalid_length(invalid_card_number):
    """
    ✅ Тест: обработка ошибок при неверных номерах карт.

    Проверяет, что функция `get_mask_card_number` выбрасывает ValueError,
    если номер карты не состоит из 16 цифр.
    """
    with pytest.raises(
        ValueError,
        match="Номер карты должен содержать 16 цифр."
    ):
        get_mask_card_number(invalid_card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("9876543210", "**3210"),
        ("1234567890", "**7890"),
        ("5555555555", "**5555"),
        ("1", "**1"),  # Один символ
    ],
)
def test_get_mask_account_valid(account_number, expected):
    """
    ✅ Тест: маскирование корректных номеров банковских счетов.

    Проверяет, что функция `get_mask_account` корректно
    маскирует и возвращает последние 4 цифры счёта.
    """
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "1234abcd",     # Содержит буквы
        "98765432$",    # Символы, кроме цифр
        "",             # Пустая строка
    ],
)
def test_get_mask_account_invalid_chars(invalid_account_number):
    """
    ✅ Тест: обработка невалидных номеров счетов.

    Проверяет, что функция `get_mask_account` выбрасывает ValueError,
    если номер содержит нецифровые символы.
    """
    with pytest.raises(
        ValueError,
        match="Номер счета должен содержать только цифры."
    ):
        get_mask_account(invalid_account_number)


@pytest.mark.parametrize(
    "short_account_number, expected",
    [
        ("123", "**123"),  # Менее 4 цифр
        ("12", "**12"),
    ],
)
def test_get_mask_account_short_account(short_account_number, expected):
    """
    ✅ Тест: маскирование коротких номеров счетов.

    Проверяет, что функция корректно работает с номерами длиной < 4 цифр.
    """
    assert get_mask_account(short_account_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1", "**1"),                           # Один символ
        ("12345678901234567890", "**7890"),    # Очень длинный номер
    ],
)
def test_get_mask_account_edge_cases(account_number, expected):
    """
    ✅ Тест: обработка крайних случаев для номеров счетов.

    Проверяет корректную маскировку как коротких, так и длинных номеров.
    """
    assert get_mask_account(account_number) == expected
