"""
main.py — демонстрация и отладка функций проекта Project_Banking_Widget:
- загрузка операций из JSON
- маскирование карт и счетов
- фильтрация и сортировка операций
- конвертация валют (USD, EUR → RUB)
"""

from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.utils import load_operations
from src.widget import (
    get_date,
    get_mask_account,
    get_mask_card_number,
    mask_account_card,
)

# Загрузка операций из JSON
operations = load_operations("data/operations.json")
print(f"Загружено операций: {len(operations)}")

# Вывод первой непустой операции для проверки структуры данных
for op in operations:
    if op:
        print("Первая непустая операция:")
        print(op)
        break

# Тесты маскировки номера карты и счета
print(get_mask_card_number("7000792289606361"))  # → '7000 79** **** 6361'
print(get_mask_account("700079228960636"))  # → '**0636'

# Тесты mask_account_card с разными форматами входа
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

# Тест преобразования даты
print(get_date("2024-03-11T02:26:18.671407"))  # → '11.03.2024'

# Пример данных для тестов filter_by_state и sort_by_date
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтрация по статусу EXECUTED (по умолчанию)
executed = filter_by_state(data)
print("EXECUTED:", executed)

# Фильтрация по статусу CANCELED
canceled = filter_by_state(data, state="CANCELED")
print("CANCELED:", canceled)

# Сортировка по дате (убывание)
sorted_data = sort_by_date(data)
print("Сортировка по убыванию:")
for item in sorted_data:
    print(item)

# Сортировка по дате (возрастание)
sorted_asc = sort_by_date(data, descending=False)
print("\nСортировка по возрастанию:")
for item in sorted_asc:
    print(item)

# 💱 Конвертация USD/EUR в RUB через внешний API
print("\n💱 Конвертация USD/EUR в RUB:")

for tx in operations:
    if not tx:
        continue
    try:
        currency = tx["operationAmount"]["currency"]["code"]
        if currency in {"USD", "EUR"}:
            rub_amount = convert_to_rub(tx)
            print(f"ID {tx['id']}: {tx['operationAmount']['amount']} " f"{currency} = {rub_amount:.2f} RUB")

    except Exception as e:
        print(f"Ошибка при конвертации операции ID {tx.get('id')}: {e}")
