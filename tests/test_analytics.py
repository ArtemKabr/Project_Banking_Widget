import pytest
from src.analytics import search_transactions_by_description, count_transaction_categories


@pytest.fixture
def sample_transactions():
    """
    Пример списка транзакций для тестов.
    """
    return [
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
        {"description": "Покупка кофе"},
        {"description": "перевод в другую страну"},
    ]


def test_search_transactions_by_description_found(sample_transactions):
    """
    Тестирует поиск транзакций, содержащих подстроку 'перевод' (регистр игнорируется).
    Ожидается 3 совпадения.
    """
    result = search_transactions_by_description(sample_transactions, "перевод")
    assert len(result) == 3
    assert all("перевод" in tx["description"].lower() for tx in result)


def test_search_transactions_by_description_not_found(sample_transactions):
    """
    Проверяет, что при отсутствии совпадений возвращается пустой список.
    """
    result = search_transactions_by_description(sample_transactions, "автомобиль")
    assert result == []


def test_count_transaction_categories(sample_transactions):
    """
    Тестирует корректную агрегацию количества операций по полю 'description'.
    """
    result = count_transaction_categories(sample_transactions)
    assert result == {
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
        "Перевод организации": 1,
        "Покупка кофе": 1,
        "перевод в другую страну": 1,
    }
