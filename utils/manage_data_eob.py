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


def add_rows(eob_df, eob_data):
    """
    Add rows to the eob DataFrame from the receipt_data in the function call.

    Parameters:
    - eob_df: DataFrame containing the eob data
    - eob_data: Dictionary containing the eob items to be added to the DataFrame

    Returns:
    - DataFrame: Updated eob DataFrame with the new rows added
    """

    print(f"Adding rows to eob DataFrame")

    # Process each item and append to the DataFrame
    new_rows = []

    for item in eob_data['items']:
        for subitem in item['items']:

            print(
                f"Adding item: {item['claim_number']} , {subitem['service_description']}")
            new_row = {
                "Patient Name": eob_data.get("patient", ""),
                "Provider Name": eob_data.get("provider", ""),
                "Document ID": eob_data.get("DocumentID", ""),
                "Claim Number": item.get("claim_number", ""),
                "Claim Date": item.get("claimdate", date.today().isoformat()),
                "Paid On": item.get("paid_on", 0),
                "Service Date": subitem.get("servicedate", date.today().isoformat()),
                "Service Description": subitem.get("service_description", ""),
                "Billed": subitem.get("provider_billed", 0),
                "Discount": subitem.get("member_discount", 0),
                "charged": subitem.get("net_charged", 0),
                "Copay": subitem.get("copay", 0),
                "Plan Paid": subitem.get("your_plan_paid", 0),
                "Total": subitem.get("total", 0),
                "category": subitem.get("category", "Uncategorized"),
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
