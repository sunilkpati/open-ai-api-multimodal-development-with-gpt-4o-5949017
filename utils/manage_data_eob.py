import pandas as pd
from datetime import date


def import_eob(input_path):
    """
    Import eob data from a CSV file.

    Parameters:
    - input_path: Path to the input CSV file

    Returns:
    - DataFrame: DataFrame containing the eob data
    """
    try:
        eob_df = pd.read_csv(input_path)
    except FileNotFoundError:
        eob_df = pd.DataFrame()

    return eob_df


def add_rows(eob_df, receipt_data):
    """
    Add rows to the eob DataFrame from the receipt_data in the function call.

    Parameters:
    - eob_df: DataFrame containing the eob data
    - receipt_data: Dictionary containing the expense items to be added to the DataFrame

    Returns:
    - DataFrame: Updated eob DataFrame with the new rows added
    """

    print(f"Adding rows to eob DataFrame")

    # Process each item and append to the DataFrame
    new_rows = []
    for item in receipt_data['items']:

        print(f"Adding item: {item['name']}")
        new_row = {
            "Date": receipt_data.get("date", date.today().isoformat()),
            "Vendor": receipt_data.get("vendor", ""),
            "Name": item.get("name", ""),
            "Quantity": item.get("quantity", 1),
            "Price": item.get("price", 0),
            "Category": item.get("category", "Uncategorized"),
            "Payment method": receipt_data.get("payment_method", "Unknown"),
        }
        new_rows.append(new_row)

    # Convert the list of new rows to a DataFrame
    new_rows_df = pd.DataFrame(new_rows)

    print(f"New rows added: {new_rows_df.shape[0]}")
    # Concatenate the new rows DataFrame to the existing eob DataFrame
    if eob_df.empty:
        eob_df = new_rows_df
    else:
        eob_df = pd.concat([eob_df, new_rows_df], ignore_index=True)

    return eob_df


def write_eob(eob_df, output_path):
    """
    Write the eob DataFrame to a CSV file.

    Parameters:
    - eob_df: DataFrame containing the eob data
    - output_path: Path to the output CSV file
    """
    eob_df.to_csv(output_path, index=False)
