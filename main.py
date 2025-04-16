from src.widget import get_mask_card_number, get_mask_account, mask_account_card
# from src.widget import get_mask_card_number

print(get_mask_card_number("7000792289606361"))


# from src.widget import get_mask_account

print(get_mask_account("700079228960636"))


# from src.widget import mask_account_card

print(mask_account_card("Maestro 1596837868705199"),'\n',
      mask_account_card('Счет 64686473678894779589'),'\n',
      mask_account_card('MasterCard 7158300734726758'),'\n',
      mask_account_card('Счет 35383033474447895560'),'\n',
      mask_account_card('Visa Classic 6831982476737658'),'\n',
      mask_account_card('Visa Platinum 8990922113665229'),'\n',
      mask_account_card('Visa Gold 5999414228426353'),'\n',
      mask_account_card('Счет 73654108430135874305'),
)

