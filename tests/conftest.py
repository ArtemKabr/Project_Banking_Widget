import pytest

# Фикстура для недопустимого номера карты
@pytest.fixture
def invalid_card_number():
    return '12345'  # Пример неверного номера карты

# Фикстура для недопустимого номера счета (содержит буквы)
@pytest.fixture
def invalid_account_number():
    return '123A56789'  # Пример некорректного номера счета с буквами

# Фикстура для короткого номера счета
@pytest.fixture
def short_account_number():
    return '123'  # Пример короткого номера счета
