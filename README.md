# 📦 Project Banking Widget

## 🔐 Описание

**Project Banking Widget** — модуль Python для маскировки конфиденциальной банковской информации и преобразования даты в читаемый формат. Позволяет безопасно отображать номера карт, счетов и даты транзакций.

---

## ⚙️ Функциональность

- `get_mask_card_number(card_number: str) -> str`  
  Маскирует номер карты: отображает первые 6 и последние 4 цифры.

- `get_mask_account(account_number: str) -> str`  
  Маскирует номер счета: отображает только последние 4 цифры.

- `mask_account_card(account_info: str) -> str`  
  Определяет тип данных (карта или счет) и возвращает маскированную строку.

- `get_date(date_str: str) -> str`  
  Преобразует дату из формата ISO в формат `ДД.ММ.ГГГГ`.

- `filter_by_state(transactions: list, state: str = 'EXECUTED') -> list`  
  Фильтрует список словарей (транзакций) по состоянию (`state`). По умолчанию фильтрует по состоянию **'EXECUTED'**.

- `sort_by_date(transactions: list, descending: bool = True) -> list`  
  Сортирует список транзакций по дате. Параметр `descending` позволяет задать порядок сортировки (по умолчанию убывание).

---

# 📌 Примеры использования

```python
>>> get_mask_card_number("1234567890123456")
'1234 56** **** 3456'

>>> get_mask_account("40817810099910004312")
'**4312'

>>> mask_account_card("Счет 40817810099910004312")
'Счет **4312'

>>> get_date("2023-11-20T08:45:00")
'20.11.2023'

# Пример использования функции фильтрации транзакций по состоянию
transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 2, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
]
filtered_transactions = filter_by_state(transactions, 'EXECUTED')
print(filtered_transactions)

# Пример использования функции сортировки транзакций по дате
sorted_transactions = sort_by_date(transactions, descending=False)
print(sorted_transactions)

```
---
# Тестирование

# Модуль Masks:
### Тесты для функции get_mask_card_number:

-  test_get_mask_card_number_valid:  Тестирует корректное маскирование номера карты с различными примерами карт.

-   test_get_mask_card_number_invalid_length: Проверяет обработку некорректных номеров карт (не 16 цифр).

### Тесты для функции get_mask_account:

- test_get_mask_account_valid: Тестирует корректное маскирование номера счета.

- test_get_mask_account_invalid_chars: Проверяет обработку номеров счета с буквами или другими нецифровыми символами.

- test_get_mask_account_short_account: Тестирует короткие номера счетов.

- test_get_mask_account_edge_cases: Проверяет крайние случаи для номеров счетов.

# Модуль Processing:
### Тесты для функции filter_by_state:


- test_filter_by_state_default: Тестирует фильтрацию по состоянию "EXECUTED".
- test_filter_by_state_custom: Проверяет фильтрацию по состоянию "PENDING".
- test_filter_by_state_no_match: Проверяет, что фильтрация возвращает пустой список, если нет совпадений.

### Тесты для функции sort_by_date:

- test_sort_by_date_descending: Проверяет сортировку по дате в порядке убывания.
- test_sort_by_date_ascending: Проверяет сортировку по дате в порядке возрастания.

# Модуль Widget:
### Тесты для функции get_mask_card_number:

- test_get_mask_card_number_valid: Тестирует корректное маскирование номеров карт.
- test_get_mask_card_number_invalid: Проверяет обработку некорректных номеров карт.

### Тесты для функции get_mask_account:

- test_get_mask_account_valid: Тестирует корректное маскирование номеров счетов.

- test_get_mask_account_invalid: Проверяет обработку некорректных номеров счетов.

### Тесты для функции mask_account_card:

- test_mask_account_card: Тестирует обработку информации о банковской карте или счете, проверяя различные возможные форматы.

### Тесты для функции get_date:

- test_get_date_valid: Проверяет корректную обработку дат в различных форматах.

- test_get_date_invalid: Проверяет обработку некорректных дат.

# Модуль conftest (Фикстуры):
### Фикстуры для тестов карт:

- invalid_card_number: Для тестирования короткого номера карты.
- invalid_card_number_with_letters: Для тестирования номера карты, содержащего буквы.
- valid_card_numbers: Для тестирования валидных номеров карт.
- invalid_card_numbers: Для тестирования некорректных номеров карт.

### Фикстуры для тестов счетов:

- invalid_account_number: Для тестирования некорректного номера счета с буквами.
- valid_account_numbers: Для тестирования валидных номеров счетов.
- invalid_account_numbers: Для тестирования некорректных номеров счетов.
- short_account_number: Для тестирования короткого номера счета.
- short_account_numbers: Для тестирования слишком коротких номеров счетов.

### Фикстуры для тестов дат:

- valid_dates: Для тестирования корректных дат.

- invalid_dates: Для тестирования некорректных дат.

### Фикстура для тестов mask_account_card:

- account_card_test_cases: Для тестирования различных случаев ввода информации о банковской карте или счете.



## 🌀 Модуль generators

Модуль содержит генераторы для обработки больших массивов транзакций.

### 📘 Функции:

- `filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]`  
  Генератор транзакций с заданной валютой (например, `"USD"`).

- `transaction_descriptions(transactions: List[Dict]) -> Iterator[str]`  
  Итератор описаний транзакций.

- `card_number_generator(start: int, stop: int) -> Iterator[str]`  
  Генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

### 📌 Примеры использования:

```python
# filter_by_currency
for tx in filter_by_currency(transactions, "USD"):
    print(tx)

# transaction_descriptions
for desc in transaction_descriptions(transactions):
    print(desc)

# card_number_generator
for card in card_number_generator(1, 3):
    print(card)



🧾 Модуль decorators
Модуль decorators.py содержит универсальный декоратор log, который автоматически регистрирует вызовы функций.

📌 Возможности:
Логирует имя функции, успешное завершение или возникшую ошибку.

Отображает входные параметры при ошибке.

Поддерживает логирование в файл или в консоль (stdout).

Позволяет анализировать поведение кода в режиме отладки или в продакшене.

🛠️ Сигнатура:
python
Копировать
Редактировать
@log(filename: Optional[str] = None)
filename — путь к лог-файлу (если не указан, лог выводится в консоль).

🧪 Пример использования:
python
Копировать
Редактировать
from src.decorators import log

@log(filename="mylog.txt")
def divide(x, y):
    return x / y

divide(10, 2)
✅ Пример лога при успешном вызове:
csharp
Копировать
Редактировать
[2025-05-17T18:00:00] divide ok
❌ Пример лога при ошибке:
css
Копировать
Редактировать
[2025-05-17T18:01:00] divide error: ZeroDivisionError. Inputs: (10, 0), {}
🧪 Покрытие тестами:
Декоратор покрыт тестами:

успешное выполнение;

логирование ошибок;

логирование в консоль (через capsys);

типизация проверена с mypy, ошибок нет;

HTML-отчёт о покрытии (htmlcov/).


✅ Функции

convert_to_rub(transaction: dict) -> float — конвертация валюты через внешний API (USD/EUR → RUB).

is_leap_year(year: int) -> bool — определение високосного года.

✅ Модуль decorators

Универсальный декоратор @log с поддержкой логирования в файл и консоль.

Логирует:

успешные вызовы;

ошибки с указанием типа и входных данных.

✅ Модуль generators

filter_by_currency — генератор по валютам.

transaction_descriptions — итератор по описаниям.

card_number_generator — генератор номеров карт с форматированием.

✅ main.py

Демонстрация всех функций: загрузка, маскирование, фильтрация, сортировка, дата, API-конвертация.

Вывод первой операции, тестирование через print, работа с JSON.

✅ Покрытие тестами (pytest)

Все функции протестированы (в т.ч. edge cases и ошибки).

Покрытие:

widget, processing, utils, external_api, generators, decorators.

Использование capsys, tmp_path, mock_open, patch, parametrize.

✅ Фикстуры

Разделены по типам: карты, счета, даты, операции.

Фикстура account_card_test_cases — проверка различных форматов ввода (карта/счёт).



---

## 📂 Модуль Input_Output.parsers

Добавлена поддержка новых источников данных:

- `read_csv_transactions(path: str) -> list[dict]`  
  Считывает транзакции из CSV-файла, возвращает список словарей.

- `read_excel_transactions(path: str) -> list[dict]`  
  Считывает транзакции из Excel-файла, возвращает список словарей.

Файлы размещаются в папке `data/`, поддержка форматов `.csv` и `.xlsx`.

