import pytest

from src.decorators import log


@log()
def add(x, y):
    """
    Пример успешной функции для тестирования логирования.

    Возвращает сумму двух чисел.
    """
    return x + y


@log()
def fail_func(x):
    """
    Функция, вызывающая исключение, для проверки логирования ошибок.

    Всегда выбрасывает ValueError.
    """
    raise ValueError("Fail!")


def test_add_success(capsys):
    """
    Проверяет, что функция `add` возвращает правильный результат
    и логирует успешное выполнение в консоль.
    """
    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_fail_func_logs_error(capsys):
    """
    Проверяет, что при исключении в `fail_func` логируется
    сообщение об ошибке с типом ошибки и входными параметрами.
    """
    with pytest.raises(ValueError):
        fail_func(5)
    captured = capsys.readouterr()
    assert "fail_func error" in captured.out
    assert "ValueError" in captured.out


@log(filename="test_log_output.txt")
def log_to_file(x, y):
    """
    Функция, логирующая в файл для проверки логирования с параметром filename.
    """
    return x + y


def test_log_written_to_file(tmp_path):
    """
    Проверяет, что лог успешно записывается в файл, если задан параметр filename.
    """
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def sample_func(x, y):
        return x + y

    sample_func(10, 5)

    content = log_file.read_text()
    assert "sample_func ok" in content
