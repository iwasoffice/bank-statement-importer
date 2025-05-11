import os
import pandas as pd

# Define the directory where the CSV will be saved
sample_data_folder = 'sample_data'

# Create the directory if it does not exist
os.makedirs(sample_data_folder, exist_ok=True)

# Data for the CSV file
data = {
    'Date': ['2024-12-01', '2024-12-02', '2024-12-03'],
    'Description': ['Transfer from GTB', 'POS Purchase', 'ATM Withdrawal'],
    'Amount': [5000, -2000, -5000],
    'Balance': [15000, 13000, 8000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
csv_file_path = os.path.join(sample_data_folder, 'zenith_sample.csv')
df.to_csv(csv_file_path, index=False)

print(f"✅ {csv_file_path} has been created successfully.")
