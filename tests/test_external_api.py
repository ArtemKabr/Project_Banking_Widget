from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rub


def test_convert_rub_no_conversion():
    """
    ✅ Тест: Возврат суммы без вызова API, если валюта RUB.

    Проверяет, что функция `convert_to_rub` не обращается к API,
    если переданная транзакция уже в рублях (код валюты RUB).
    """
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}  # Валюта — рубли

    # Ожидаем, что сумма возвращается без изменений
    result = convert_to_rub(transaction)
    assert result == 1000.0


@patch("src.external_api.requests.get")  # Подменяем requests.get
@patch("src.external_api.os.getenv", return_value="fake-key")  # Подменяем os.getenv на фейковый ключ
def test_convert_usd_to_rub(mock_getenv, mock_get):
    """
    ✅ Тест: Конвертация из USD в RUB с подменённым ответом от API.
    Проверяет, что при валюте USD вызывается внешний API и
    возвращается ожидаемый результат.
    """
    # Настраиваем фейковый ответ от API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 92000.0}  # Фейковый курс
    mock_response.raise_for_status = Mock()  # Ошибок нет
    mock_get.return_value = mock_response

    # Пример транзакции в USD
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "USD"}}}

    # Ожидаем результат, полученный от mock'а
    result = convert_to_rub(transaction)
    assert result == 92000.0

    # Убедимся, что API действительно был вызван
    mock_get.assert_called_once()


@patch("src.external_api.os.getenv", return_value=None)
def test_convert_to_rub_no_api_key(mock_getenv):
    """
    ✅ Тест: Поведение при отсутствии переменной окружения API_KEY.

    Проверяет, что если API_KEY не задан в окружении,
    функция выбрасывает исключение ValueError.
    """
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    # Ожидаем ValueError с нужным текстом
    with pytest.raises(ValueError, match="API_KEY не найден"):
        convert_to_rub(transaction)


@patch("src.external_api.requests.get")  # Подменяем requests.get
@patch("src.external_api.os.getenv", return_value="fake-key")
def test_convert_to_rub_api_error(mock_getenv, mock_get):
    """
    ✅ Тест: Исключение при ошибке от API.

    Проверяет, что если API возвращает ошибку
    (например, 500 или 403),
    функция пробрасывает это исключение через
    raise_for_status().
    """
    # Подготавливаем фейковый ответ с ошибкой
    mock_response = Mock()
    # Искусственная ошибка
    mock_response.raise_for_status.side_effect = Exception("API down")
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}

    # Ожидаем, что исключение будет проброшено
    with pytest.raises(Exception, match="API down"):
        convert_to_rub(transaction)
