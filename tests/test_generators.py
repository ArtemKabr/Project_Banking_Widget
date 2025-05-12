import pytest
from src.generators import (filter_by_currency,
                            transaction_descriptions, card_number_generator)


@pytest.fixture
def sample_transactions():
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
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["USD транзакция", "RUB транзакция"]


@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"])
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
