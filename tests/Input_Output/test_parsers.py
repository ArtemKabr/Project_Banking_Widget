from unittest.mock import MagicMock, patch

from src.Input_Output.parsers import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    # Подготовка фейкового DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("dummy_path.csv")
    assert isinstance(result, list)
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 200
    mock_read_csv.assert_called_once_with("dummy_path.csv", delimiter=";")


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    # Подготовка фейкового DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 3, "amount": 300}, {"id": 4, "amount": 400}]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("dummy_path.xlsx")
    assert isinstance(result, list)
    assert result[0]["id"] == 3
    assert result[1]["amount"] == 400
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")
