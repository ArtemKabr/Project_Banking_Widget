# Удалите строку импорта pytest, если не используете его напрямую
# import pytest
from datetime import datetime

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_data):
    """
    ✅ Тест: фильтрация по умолчанию (EXECUTED).

    Проверяет, что функция возвращает только транзакции со статусом "EXECUTED".
    """
    result = filter_by_state(sample_data)
    assert len(result) == 2
    for item in result:
        assert item["state"] == "EXECUTED"


def test_filter_by_state_custom(sample_data):
    """
    ✅ Тест: фильтрация по пользовательскому статусу.

    Проверяет, что при передаче параметра state="PENDING"
    функция возвращает корректные транзакции.
    """
    result = filter_by_state(sample_data, state="PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_no_match(sample_data):
    """
    ✅ Тест: фильтрация без совпадений.

    Проверяет, что если ни одна транзакция не соответствует заданному статусу,
    функция возвращает пустой список.
    """
    result = filter_by_state(sample_data, state="CANCELED")
    assert result == []


def test_sort_by_date_descending(sample_data):
    """
    ✅ Тест: сортировка транзакций по дате по убыванию.

    Проверяет, что `sort_by_date` правильно сортирует список
    от самой новой даты к самой старой.
    """
    result = sort_by_date(sample_data)
    dates = [datetime.fromisoformat(item["date"]) for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_data):
    """
    ✅ Тест: сортировка транзакций по дате по возрастанию.

    Проверяет, что `sort_by_date` правильно сортирует список
    от самой старой даты к самой новой.
    """
    result = sort_by_date(sample_data, descending=False)
    dates = [datetime.fromisoformat(item["date"]) for item in result]
    assert dates == sorted(dates)
