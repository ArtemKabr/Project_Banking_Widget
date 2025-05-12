# Удалите строку импорта pytest, если не используете его
# import pytest
from datetime import datetime

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_data):
    # Проверяем, что фильтрация работает для состояния 'EXECUTED'
    result = filter_by_state(sample_data)
    assert len(result) == 2
    for item in result:
        assert item["state"] == "EXECUTED"


def test_filter_by_state_custom(sample_data):
    # Проверяем, что фильтрация работает для состояния 'PENDING'
    result = filter_by_state(sample_data, state="PENDING")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_no_match(sample_data):
    # Проверяем, что фильтрация возвращает пустой список, если нет совпадений
    result = filter_by_state(sample_data, state="CANCELED")
    assert result == []


def test_sort_by_date_descending(sample_data):
    # Проверяем, что сортировка по дате работает в порядке убывания
    result = sort_by_date(sample_data)
    dates = [datetime.fromisoformat(item["date"]) for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_data):
    # Проверяем, что сортировка по дате работает в порядке возрастания
    result = sort_by_date(sample_data, descending=False)
    dates = [datetime.fromisoformat(item["date"]) for item in result]
    assert dates == sorted(dates)
