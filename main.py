"""
main.py — демонстрация и пользовательский интерфейс для Project_Banking_Widget.
"""

import os
import time

import pandas as pd

from src.analytics import count_transaction_categories, search_transactions_by_description
from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.utils import load_operations
from src.widget import (
    get_date,
    get_mask_account,
    get_mask_card_number,
    mask_account_card,
)


def show_transactions() -> None:
    """
    Демонстрация функций проекта: загрузка, маскирование, сортировка, преобразование и т.д.
    """
    os.makedirs("data", exist_ok=True)

    operations = load_operations("data/operations.json")
    print(f"Загружено операций: {len(operations)}")

    for op in operations:
        if op:
            print("Первая непустая операция:")
            print(op)
            break

    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("700079228960636"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))

    print(get_date("2024-03-11T02:26:18.671407"))

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


def load_transactions() -> list[dict]:
    """
    Загружает транзакции из JSON, CSV или XLSX — выбор пользователя.
    """
    while True:
        print("\n📥 Выберите источник данных:")
        print("1. JSON")
        print("2. CSV")
        print("3. XLSX")
        choice = input("Ваш выбор: ")

        try:
            if choice == "1":
                return load_operations("data/operations.json")
            elif choice == "2":
                return pd.read_csv("data/transactions.csv", delimiter=";").to_dict(orient="records")
            elif choice == "3":
                # Не забудьте установить openpyxl: poetry add openpyxl
                return pd.read_excel("data/transactions_excel.xlsx").to_dict(orient="records")
            else:
                print("Неверный выбор. Повторите ввод.")
        except Exception as e:
            print(f"❌ Ошибка при загрузке файла: {e}")


def ask_status() -> str:
    """
    Запрашивает статус транзакции у пользователя с выбором по цифрам.
    """
    options = {
        "1": "EXECUTED",
        "2": "CANCELED",
        "3": "PENDING",
    }
    while True:
        print("📌 Выберите статус операций:")
        print("1. EXECUTED")
        print("2. CANCELED")
        print("3. PENDING")
        choice = input("Ваш выбор: ").strip()
        if choice in options:
            return options[choice]
        print(f"❌ Неверный выбор: {choice}. Повторите.")


def ask_yes_no(prompt: str) -> bool:
    """
    Спрашивает «Да/Нет» до тех пор, пока пользователь не введёт
    корректный ответ. Возвращает True для «да», False для «нет».
    Допустимы ответы: да | y | yes  ― и  нет | n | no
    Регистр и пробелы игнорируются.
    """
    valid_yes = {"да", "y", "yes"}
    valid_no = {"нет", "n", "no"}
    while True:
        answer = input(f"{prompt} (Да/Нет): ").strip().lower()
        if answer in valid_yes:
            return True
        if answer in valid_no:
            return False
        print("❌ Пожалуйста, введите 'Да' или 'Нет'.")


def ask_sort_order() -> bool:
    """
    Спрашивает порядок сортировки.
    ▸ Возвращает False — по возрастанию (старые → новые)
    ▸ Возвращает True  — по убыванию   (новые → старые)
    Принимает:
        1 / возрастание / вверх / asc
        2 / убывание    / вниз  / desc
    """
    asc_variants = {"1", "возрастание", "вверх", "asc", "по возрастанию"}
    desc_variants = {"2", "убывание", "вниз", "desc", "по убыванию"}
    while True:
        answer = input("Сортировать по возрастанию или убыванию? (1/2): ").strip().lower()
        if answer in asc_variants:
            return False            # возрастание
        if answer in desc_variants:
            return True             # убывание
        print("❌ Неверный ввод. Введите 1 (возрастание) или 2 (убывание).")


def print_transaction(tx: dict):
    print(get_date(tx["date"]))
    print(tx["description"])
    if "from" in tx:
        print(mask_account_card(tx["from"]), end=" -> ")
    if "to" in tx:
        print(mask_account_card(tx["to"]))
    amount = tx.get("operationAmount", {}).get("amount") or tx.get("amount")
    currency = (
        tx.get("operationAmount", {}).get("currency", {}).get("code")
        or tx.get("currency")
    )
    print(f"Сумма: {amount} {currency}\n")


def main():
    """
    Основной пользовательский интерфейс для работы с транзакциями.
    """
    print("👋 Добро пожаловать в Project Banking Widget!")
    transactions = load_transactions()

    if not transactions:
        print("❌ Нет доступных операций.")
        return

    status = ask_status()
    filtered = filter_by_state(transactions, status)
    print(f"✅ Отфильтровано по статусу: {status}")

    if ask_yes_no("Отсортировать по дате?"):
        descending = ask_sort_order()
        filtered = sort_by_date(filtered, descending)

    # ───────────── Фильтр: только операции в RUB ─────────────
    if ask_yes_no("Показать только рублевые операции?"):
        # Проверяем, встречается ли вообще валюта RUB среди уже отфильтрованных операций
        has_rub = any(
            (tx.get("operationAmount", {}).get("currency", {}).get("code") == "RUB")
            or (tx.get("currency") == "RUB")
            for tx in filtered
        )

        if has_rub:
            filtered = [
                tx for tx in filtered
                if (
                        tx.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
                        or tx.get("currency") == "RUB"
                )
            ]
            print(f"💸 Операций в RUB осталось: {len(filtered)}")
        else:
            print("⚠️ Среди выбранных транзакций вообще нет валюты RUB — фильтрация пропущена.")
    # ─────────────────────────────────────────────────────────

    if ask_yes_no("Фильтровать по описанию?"):
        query = input("Введите подстроку для поиска: ")
        filtered = search_transactions_by_description(filtered, query)

    # ─────────── Когда после всех фильтров список пуст ───────────
    if not filtered:
        print("⚠️ Ни одной операции не найдено.")

        # Собираем уникальные описания среди операций c тем  
        # же статусом (без валютного фильтра, чтобы дать максимум вариантов)
        fallback_pool = filter_by_state(transactions, status)
        descriptions = sorted({tx.get("description", "<без описания>") for tx in fallback_pool})

        if not descriptions:
            print("❌ В этих операциях даже описаний нет — ничего предложить.")
            return

        # Показываем список с номерами
        print("\n🔍 Доступные описания:")
        for i, desc in enumerate(descriptions, 1):
            print(f"{i}. {desc}")

        try:
            choice = int(input("\nВведите номер описания для повторного поиска: "))
            chosen_desc = descriptions[choice - 1]
        except (ValueError, IndexError):
            print("❌ Неверный номер. Завершаю.")
            return

        # Повторная фильтрация уже по выбранному описанию
        filtered = [
            tx for tx in fallback_pool
            if chosen_desc in tx.get("description", "")
        ]

        if not filtered:
            print("⚠️ По выбранному описанию тоже ничего не найдено.")
            return
    # ──────────────────────────────────────────────────────────────

    print(f"\n📋 Всего операций: {len(filtered)}\n")
    for tx in filtered:
        print_transaction(tx)

    print("📊 Категории:")
    for category, count in count_transaction_categories(filtered).items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    # show_transactions()  # отладочный режим
    main()  # пользовательский интерфейс
