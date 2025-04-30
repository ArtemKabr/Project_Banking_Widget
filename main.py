from src.processing import filter_by_state, sort_by_date
from src.widget import (
    get_date,
    get_mask_account,
    get_mask_card_number,
    mask_account_card,
)

# Тест для get_mask_card_number
print(get_mask_card_number("7000792289606361"))

# Тест для get_mask_account
print(get_mask_account("700079228960636"))

# Тест для mask_account_card с разными примерами
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

# Тест для get_date
print(get_date("2024-03-11T02:26:18.671407"))  # Ожидаемый вывод: 11.03.2024

# Пример данных для filter_by_state
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

# Тест с состоянием по умолчанию (EXECUTED)
executed = filter_by_state(data)
print("EXECUTED:", executed)

# Тест с другим состоянием (CANCELED)
canceled = filter_by_state(data, state="CANCELED")
print("CANCELED:", canceled)

# Пример данных для sort_by_date
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

# Сортировка по убыванию даты
sorted_data = sort_by_date(data)
print("Сортировка по убыванию:")
for item in sorted_data:
    print(item)

# Сортировка по возрастанию даты
sorted_asc = sort_by_date(data, descending=False)
print("\nСортировка по возрастанию:")
for item in sorted_asc:
    print(item)
