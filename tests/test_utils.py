import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


def test_load_operations_valid_list():
    """
    ✅ Тест: корректная загрузка JSON-файла, содержащего список словарей.

    Проверяет, что функция `load_operations` успешно возвращает список
    транзакций при корректном формате JSON-файла.
    """
    # Мокаем содержимое JSON-файла: список из двух транзакций
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    # Подменяем open и возвращаем mock-данные при чтении файла
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("dummy.json")

        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0]["id"] == 1


def test_load_operations_not_a_list():
    """
    ✅ Тест: обработка случая, когда в JSON содержится не список, а объект.

    Проверяет, что если JSON содержит словарь, а не список — возвращается пустой список.
    """
    mock_data = json.dumps({"id": 1, "amount": 100})  # ❌ Это не список

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("dummy.json")
        assert result == []


def test_load_operations_file_not_found():
    """
    ✅ Тест: поведение при отсутствии файла.

    Проверяет, что если файл не найден (`FileNotFoundError`),
    функция возвращает пустой список.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations("not_exists.json")
        assert result == []


def test_load_operations_invalid_json():
    """
    ✅ Тест: поведение при некорректном формате JSON.

    Проверяет, что при ошибке разбора JSON (`JSONDecodeError`)
    функция возвращает пустой список.
    """
    mock_data = '{"id": 1, "amount": 100'  # ❌ Нарушен формат JSON (нет закрытия)

    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Имитируем исключение при json.load
        with patch("json.load", side_effect=json.JSONDecodeError("msg", doc="", pos=0)):
            result = load_operations("broken.json")
            assert result == []


def test_load_operations_empty_list():
    """
    ✅ Тест: корректная загрузка пустого списка.

    Проверяет, что если JSON-файл содержит пустой список, функция его и возвращает.
    """
    mock_data = json.dumps([])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_operations("empty.json")
        assert result == []
