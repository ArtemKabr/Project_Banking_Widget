import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_valid_list():
    """
    ✅ Тест: корректная загрузка JSON-файла, содержащего список словарей.

    Проверяет, что функция возвращает список
    транзакций при корректном содержимом.
    """
    # Мокаем содержимое JSON-файла: список с двумя транзакциями
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    # Подменяем открытие файла
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("dummy.json")

        assert isinstance(result, list)  # Убедимся, что это список
        assert len(result) == 2
        assert result[0]["id"] == 1


def test_load_operations_not_a_list():
    """
    ✅ Тест: обработка JSON-файла, содержащего не список, а объект.

    Проверяет, что при передаче не-списка возвращается пустой список.
    """
    mock_data = json.dumps({"id": 1, "amount": 100})  # ❌ Это не список

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("dummy.json")
        assert result == []


def test_load_operations_file_not_found():
    """
    ✅ Тест: обработка случая, когда файл не существует.

    Проверяет, что при FileNotFoundError возвращается пустой список.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations("not_exists.json")
        assert result == []


def test_load_operations_invalid_json():
    """
    ✅ Тест: обработка некорректного JSON-формата.

    Проверяет, что при ошибке парсинга JSON возвращается пустой список.
    """
    mock_data = '{"id": 1, "amount": 100'  # ❌ Нарушен формат JSON

    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Подменяем json.load, чтобы он выбрасывал JSONDecodeError
        with patch("json.load", side_effect=json.JSONDecodeError("msg", doc="", pos=0)):
            result = load_operations("broken.json")
            assert result == []


def test_load_operations_empty_list():
    """
    ✅ Тест: корректная обработка пустого списка в JSON.

    Проверяет, что если содержимое файла — пустой список, он и возвращается.
    """
    mock_data = json.dumps([])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("empty.json")
        assert result == []
