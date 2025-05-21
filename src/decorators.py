import datetime
import sys
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

# Обобщённый тип для типизации входящей функции
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор логирования выполнения функции.

    При успешном выполнении записывает сообщение "<имя_функции> ok".
    При ошибке — "<имя_функции> error: <тип_ошибки>. Inputs: <args>, <kwargs>".

    Лог сохраняется:
    - в консоль (stdout), если `filename` не задан
    - в указанный файл, если передано имя файла

    :param filename: Имя файла для записи логов.
    Если None — лог выводится в консоль.

    :return: Обёрнутая функция с логированием
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = ""  # Сообщение для логирования

            try:
                # Вызов основной функции
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"  # Успешный лог
                return result

            except Exception as e:
                # Лог ошибки + параметры
                log_message = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"
                raise  # Пробрасываем исключение дальше

            finally:
                # Добавляем отметку времени
                timestamp = datetime.datetime.now().isoformat()
                final_log = f"[{timestamp}] {log_message}"

                # Либо пишем в файл
                if filename:
                    with open(filename, "a") as f:
                        f.write(final_log)
                else:
                    # Либо выводим в консоль
                    print(final_log, file=sys.stdout)

        return cast(F, wrapper)  # Приводим тип для сохранения сигнатуры

    return decorator
