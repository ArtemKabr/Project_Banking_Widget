"""
main.py — демонстрация и отладка функций проекта Project_Banking_Widget.
"""

import time
import os
import pandas as pd
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


def show_transactions():
    # 📁 Убедимся, что папка data существует
    os.makedirs("data", exist_ok=True)

    # 🔄 Загрузка операций из JSON-файла
    operations = load_operations("data/operations.json")
    print(f"Загружено операций: {len(operations)}")

    for op in operations:
        if op:
            print("Первая непустая операция:")
            print(op)
            break

    # 🛡️ Маскирование
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("700079228960636"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))

    # 📅 Преобразование даты
    print(get_date("2024-03-11T02:26:18.671407"))

    # 🔍 Демонстрационные данные
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("EXECUTED:", filter_by_state(data))
    print("CANCELED:", filter_by_state(data, state="CANCELED"))

    print("Сортировка по убыванию:")
    for item in sort_by_date(data):
        print(item)

    print("\nСортировка по возрастанию:")
    for item in sort_by_date(data, descending=False):
        print(item)

    # 💱 Конвертация валют
    print("\n💱 Конвертация USD/EUR в RUB:")
    for tx in operations:
        if not tx:
            continue
        try:
            currency = tx["operationAmount"]["currency"]["code"]
            if currency in {"USD", "EUR"}:
                rub_amount = convert_to_rub(tx)
                print(f"ID {tx['id']}: {tx['operationAmount']['amount']} {currency} = {rub_amount:.2f} RUB")
                time.sleep(1)
        except Exception as e:
            print(f"Ошибка при конвертации операции ID {tx.get('id')}: {e}")

    # 📥 Загрузка CSV и Excel с рабочего стола
    csv_path = "data/transactions.csv"
    excel_path = "data/transactions_excel.xlsx"

    try:
        df_csv = pd.read_csv(csv_path, delimiter=";")
        print("📄 CSV-файл (локальный):")
        print(df_csv.head())
        df_csv.to_csv("data/transactions_copy.csv", index=False)
        print("✅ CSV сохранён в data/transactions_copy.csv")
    except Exception as e:
        print(f"❌ Ошибка при чтении CSV: {e}")

    try:
        df_excel = pd.read_excel(excel_path)
        print("\n📘 Excel-файл (локальный):")
        print(df_excel.head())
        df_excel.to_excel("data/transactions_copy.xlsx", index=False)
        print("✅ Excel сохранён в data/transactions_copy.xlsx")
    except Exception as e:
        print(f"❌ Ошибка при чтении Excel: {e}")



if __name__ == "__main__":
    show_transactions()
