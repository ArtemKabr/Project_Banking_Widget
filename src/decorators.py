import datetime
import sys
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызовов функций.

    Логирует имя функции, статус выполнения (успешно или с ошибкой),
    входные параметры (в случае ошибки) и время вызова.

    Если задан параметр `filename`, лог сохраняется в файл.
    Если `filename` не указан, лог выводится в консоль.

    Args:
        filename (Optional[str]): Имя файла для сохранения логов.
            Если None — лог будет выведен в stdout.

    Returns:
        Callable: Обёрнутая функция с логированием.
    """
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                return result
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                raise
            finally:
                timestamp = datetime.datetime.now().isoformat()
                final_log = f"[{timestamp}] {log_message}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(final_log)
                else:
                    print(final_log, file=sys.stdout)

        return cast(F, wrapper)

    return decorator
