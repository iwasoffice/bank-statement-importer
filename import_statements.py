# 📄 import_statements.py
# ------------------------------------------
# A robust utility script to import and clean bank statement data
# from either CSV or Excel formats. Ideal for finance automation,
# data analysis, and dashboard readiness.
# ------------------------------------------

import pandas as pd
import os

def import_bank_statement(file_path):
    """
    Imports a bank statement from a CSV or Excel file and returns
    a cleaned pandas DataFrame.
    
    Supported formats:
    - .csv
    - .xlsx
    - .xls
    
    Required columns (case-insensitive):
    - Date
    - Description
    - Amount
    - Balance (optional for some use cases)
    
    Returns:
        pd.DataFrame: Cleaned DataFrame with parsed dates and numeric amounts.
    
    Raises:
        FileNotFoundError: If the specified file path doesn't exist.
        ValueError: If the file format is unsupported.
    """

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ The file '{file_path}' does not exist.")

    # Determine and read file type
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("❌ Unsupported file format. Please upload a CSV or Excel file.")
    except Exception as read_error:
        raise Exception(f"❌ Failed to read file: {read_error}")

    # Normalise and clean column headers
    df.columns = [col.strip().lower() for col in df.columns]

    # Convert and clean key fields
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    else:
        raise ValueError("❌ 'Date' column not found in uploaded file.")

    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    else:
        raise ValueError("❌ 'Amount' column not found in uploaded file.")

    # Drop rows with invalid dates or amounts
    df = df.dropna(subset=['date', 'amount'])

    # Return cleaned data
    return df

# 🔁 Run directly for testing
if __name__ == "__main__":
    sample_file = "sample_data/zenith_sample.csv"  # Replace with your file path
    try:
        df = import_bank_statement(sample_file)
        print("✅ Bank statement imported and cleaned successfully!")
        print(df.head())
    except Exception as e:
        print(f"❌ An error occurred: {e}")
