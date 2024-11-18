import pandas as pd
import re

# File path for the raw dataset
raw_file_path = '/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv'

# Load the dataset
df = pd.read_csv(raw_file_path)

# Drop unwanted columns
df = df.drop(columns=['lang', 'BrandCode'], errors='ignore')

# Reorder columns
columns_order = ['RegistrationDate', 'First Name', 'Last Name', 'Phone', 'Country', 'Email']
df = df[columns_order]

# Email validation function
def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, str(email)))

# Identify invalid rows
rows_with_missing_values = df[df.isnull().any(axis=1)]
rows_with_duplicates = df[df.duplicated()]
rows_with_invalid_emails = df[~df['Email'].apply(validate_email)]

# Combine all invalid rows
invalid_rows = pd.concat([rows_with_missing_values, rows_with_duplicates, rows_with_invalid_emails]).drop_duplicates()

# Remove invalid rows from the original dataset
df = df.drop(invalid_rows.index)

# Capitalize 'First Name' and 'Last Name', rename to 'first_name' and 'last_name'
df['First Name'] = df['First Name'].str.capitalize()
df['Last Name'] = df['Last Name'].str.capitalize()
df = df.rename(columns={'First Name': 'first_name', 'Last Name': 'last_name'})

# Save invalid data to a separate file
invalid_data_file_path = '/content/invalid_data.csv'
invalid_rows.to_csv(invalid_data_file_path, index=False)

# Save the cleaned dataset
cleaned_file_path = '/content/cleaned_phoniex.csv'
df.to_csv(cleaned_file_path, index=False)

# Print summary of operations
print(f"Total rows removed: {len(invalid_rows)}")
print(f"Invalid data saved to: {invalid_data_file_path}")
print(f"Cleaned dataset saved to: {cleaned_file_path}")
