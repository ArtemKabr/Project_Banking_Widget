import pytest

from src.decorators import log


# Тестовая функция, к которой применён декоратор log
@log()
def add(x, y):
    """
    Пример успешной функции для тестирования логирования.

    Возвращает сумму двух чисел.
    """
    return x + y


# Тестовая функция, вызывающая ошибку
@log()
def fail_func(x):
    """
    Функция, вызывающая исключение, для проверки логирования ошибок.

    Всегда выбрасывает ValueError.
    """
    raise ValueError("Fail!")


def test_add_success(capsys):
    """
    Проверяет, что функция `add`:
    - возвращает правильный результат;
    - выводит лог об успешном выполнении в консоль.
    """
    result = add(1, 2)
    assert result == 3

    # Захватываем вывод в консоль
    captured = capsys.readouterr()
    assert "add ok" in captured.out  # Проверяем, что лог записался


def test_fail_func_logs_error(capsys):
    """
    Проверяет, что при исключении в `fail_func`:
    - выбрасывается исключение ValueError;
    - лог содержит сообщение об ошибке с именем функции и типом ошибки.
    """
    with pytest.raises(ValueError):
        fail_func(5)

    # Захватываем вывод в консоль
    captured = capsys.readouterr()
    assert "fail_func error" in captured.out
    assert "ValueError" in captured.out


# Тестовая функция, логирующая в файл
@log(filename="test_log_output.txt")
def log_to_file(x, y):
    """
    Пример функции, логирующей выполнение в файл.

    Используется для проверки параметра filename в декораторе log.
    """
    return x + y


def test_log_written_to_file(tmp_path):
    """
    Проверяет, что при передаче параметра filename лог записывается в файл.

    - Создаёт временный файл;
    - Вызывает функцию с логированием в этот файл;
    - Проверяет, что файл содержит ожидаемую запись.
    """
    # Создаём временный путь к лог-файлу
    log_file = tmp_path / "mylog.txt"

    # Функция с логированием в указанный файл
    @log(filename=str(log_file))
    def sample_func(x, y):
        return x + y

    sample_func(10, 5)

    # Читаем содержимое лог-файла
    content = log_file.read_text()
    assert "sample_func ok" in content  # Убедимся, что лог записался
