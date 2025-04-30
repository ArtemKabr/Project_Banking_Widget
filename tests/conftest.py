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

# Фикстура для тестов обработки операций
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-05-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-04-01T09:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-06-01T11:30:00"},
    ]
