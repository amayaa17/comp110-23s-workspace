"""Data Utilities (CSV Files)."""

from csv import DictReader

def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read CSV file and return as a list of dictionaries with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(file_name, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result

def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    result: list[str] = []
    #Step through table
    for row in table:
        #Save every value under the key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #Loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #For each key, make a dictionary entry with all column values.
        result[key] = column_vals(table, key)
    return result