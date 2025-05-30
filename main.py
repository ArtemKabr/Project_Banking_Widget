"""
main.py — демонстрация и отладка функций проекта Project_Banking_Widget.

Включает:
- загрузку операций из JSON-файла;
- маскирование номеров карт и счетов;
- определение типа и маскирование (карта/счёт);
- преобразование даты;
- фильтрацию и сортировку по состоянию и дате;
- конвертацию валют (USD, EUR → RUB) через внешний API.
"""
import time
from src.Input_Output.parsers import read_csv_transactions, read_excel_transactions
from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.utils import load_operations
from src.widget import (
    get_date,
    get_mask_account,
    get_mask_card_number,
    mask_account_card,
)

# 🔄 Загрузка операций из JSON-файла
operations = load_operations("data/operations.json")
print(f"Загружено операций: {len(operations)}")

# ✅ Отображаем первую непустую операцию для проверки структуры
for op in operations:
    if op:
        print("Первая непустая операция:")
        print(op)
        break

# 🛡️ Маскирование номера карты
print(get_mask_card_number("7000792289606361"))  # → '7000 79** **** 6361'

# 🛡️ Маскирование номера счёта
print(get_mask_account("700079228960636"))  # → '**0636'

# 🛡️ Определение и маскирование карты/счета
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

# 📅 Преобразование даты
print(get_date("2024-03-11T02:26:18.671407"))  # → '11.03.2024'

# 🔍 Демонстрационные данные для фильтрации и сортировки
data = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
    },
]

# 🔎 Фильтрация по состоянию (по умолчанию — EXECUTED)
executed = filter_by_state(data)
print("EXECUTED:", executed)

# 🔎 Фильтрация по состоянию — CANCELED
canceled = filter_by_state(data, state="CANCELED")
print("CANCELED:", canceled)

# 📊 Сортировка операций по дате (по убыванию)
sorted_data = sort_by_date(data)
print("Сортировка по убыванию:")
for item in sorted_data:
    print(item)

# 📊 Сортировка операций по дате (по возрастанию)
sorted_asc = sort_by_date(data, descending=False)
print("\nСортировка по возрастанию:")
for item in sorted_asc:
    print(item)

# 💱 Конвертация валют в рубли через внешний API
print("\n💱 Конвертация USD/EUR в RUB:")


for tx in operations:
    if not tx:
        continue
    try:
        currency = tx["operationAmount"]["currency"]["code"]
        if currency in {"USD", "EUR"}:
            rub_amount = convert_to_rub(tx)
            print(f"ID {tx['id']}: {tx['operationAmount']['amount']} {currency} = {rub_amount:.2f} RUB")
            time.sleep(1)  # Добавляем паузу между запросами
    except Exception as e:
        print(f"Ошибка при конвертации операции ID {tx.get('id')}: {e}")


# 📥 Загрузка операций из CSV и Excel-файлов (демонстрация)

csv_path = "data/transactions.csv"
excel_path = "data/transactions_excel.xlsx"

csv_transactions = read_csv_transactions(csv_path)
excel_transactions = read_excel_transactions(excel_path)

print("\n📄 CSV транзакции:")
for tx in csv_transactions:
    print(tx)

print("\n📊 Excel транзакции:")
for tx in excel_transactions:
    print(tx)