import datetime
import sys
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

# Обобщённый тип для типизации входящей функции
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор логирования выполнения функции.

    При успешном выполнении — пишет сообщение
     "<имя_функции> ok".
    При ошибке — пишет сообщение "<имя_функции>
    error: <тип_ошибки>. Inputs: <args>, <kwargs>".

    Лог сохраняется:
    - в консоль (stdout), если `filename` не задан;
    - в указанный файл, если передано имя файла.

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
                log_message = f"{func.__name__} ok\n"  # Сообщение об успешном выполнении
                return result

            except Exception as e:
                # Формируем сообщение об ошибке с параметрами вызова
                log_message = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"
                raise  # Пробрасываем исключение дальше

            finally:
                # Добавляем отметку времени
                timestamp = datetime.datetime.now().isoformat()
                final_log = f"[{timestamp}] {log_message}"

                # Запись в файл, если указан путь
                if filename:
                    with open(filename, "a") as f:
                        f.write(final_log)
                else:
                    # Иначе — вывод в стандартный поток
                    print(final_log, file=sys.stdout)

        return cast(F, wrapper)  # Возвращаем обёрнутую функцию с сохранением типа

    return decorator
