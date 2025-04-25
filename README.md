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

## 📌 Примеры использования

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

