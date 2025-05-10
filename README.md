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


