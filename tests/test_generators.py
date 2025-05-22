import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """
    Фикстура: пример списка транзакций с разными валютами и описаниями.

    Содержит:
    - одну транзакцию в USD;
    - одну транзакцию в RUB.
    """
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "USD транзакция"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "RUB транзакция"
        }
    ]


def test_filter_by_currency_usd(sample_transactions):
    """
    ✅ Тест: фильтрация по валюте USD.

    Проверяет, что функция `filter_by_currency` возвращает
    только транзакции с кодом валюты 'USD'.
    """
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_transaction_descriptions(sample_transactions):
    """
    ✅ Тест: генерация описаний транзакций.

    Проверяет, что `transaction_descriptions` корректно
    извлекает описание каждой транзакции.
    """
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["USD транзакция", "RUB транзакция"]


@pytest.mark.parametrize("start, stop, expected", [
    (
        1, 3,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]
    )
])
def test_card_number_generator(start, stop, expected):
    """
    ✅ Тест: генерация номеров карт.

    Проверяет, что `card_number_generator` генерирует правильные
    номера карт в формате XXXX XXXX XXXX XXXX.
    """
    result = list(card_number_generator(start, stop))
    assert result == expected
