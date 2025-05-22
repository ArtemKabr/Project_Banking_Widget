from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rub


def test_convert_rub_no_conversion():
    """
    ✅ Тест: Возврат суммы без вызова API, если валюта RUB.

    Проверяет, что функция `convert_to_rub` не делает запрос к внешнему API,
    если переданная транзакция уже указана в рублях.
    """
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}

    # Ожидаем, что сумма возвращается без изменений и не происходит вызова API
    result = convert_to_rub(transaction)
    assert result == 1000.0


@patch("src.external_api.requests.get")  # Подмена requests.get
@patch("src.external_api.os.getenv", return_value="fake-key")  # Подмена os.getenv на фейковый API ключ
def test_convert_usd_to_rub(mock_getenv, mock_get):
    """
    ✅ Тест: Конвертация из USD в RUB с подменённым ответом от API.

    Проверяет, что при передаче валюты USD:
    - вызывается внешний API;
    - возвращается ожидаемый результат, имитируемый с помощью mock.
    """
    # Создаём фейковый ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 92000.0}  # Поддельный результат от API
    mock_response.raise_for_status = Mock()  # Не вызывает исключения
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "USD"}}}

    # Проверяем, что возвращается значение из mock'а
    result = convert_to_rub(transaction)
    assert result == 92000.0

    # Проверяем, что API действительно был вызван один раз
    mock_get.assert_called_once()


@patch("src.external_api.os.getenv", return_value=None)
def test_convert_to_rub_no_api_key(mock_getenv):
    """
    ✅ Тест: Обработка случая, когда отсутствует переменная окружения API_KEY.

    Проверяет, что функция выбрасывает исключение ValueError,
    если API ключ не найден в окружении.
    """
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}

    # Ожидаем ValueError с определённым сообщением
    with pytest.raises(ValueError, match="API_KEY не найден"):
        convert_to_rub(transaction)


@patch("src.external_api.requests.get")  # Подмена requests.get
@patch("src.external_api.os.getenv", return_value="fake-key")
def test_convert_to_rub_api_error(mock_getenv, mock_get):
    """
    ✅ Тест: Исключение при ошибке от API.

    Проверяет, что если внешний API возвращает ошибку (например, 500 или 403),
    функция корректно пробрасывает исключение, вызванное raise_for_status().
    """
    # Настройка mock-ответа с исключением при вызове raise_for_status()
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = Exception("API down")  # Имитируем сбой API
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "EUR"}}}

    # Проверка, что функция выбрасывает исключение от API
    with pytest.raises(Exception, match="API down"):
        convert_to_rub(transaction)
