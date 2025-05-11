import pandas as pd

def import_bank_statement(file):
    """
    Imports and cleans bank statement from CSV or Excel file-like object.
    """
    # Detect file type
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file type")

    # Normalise column names
    df.columns = [col.strip().lower() for col in df.columns]

    # Clean common fields
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    if 'amount' in df.columns:
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Drop rows with missing critical data
    df = df.dropna(subset=['date', 'amount'])

    return df
