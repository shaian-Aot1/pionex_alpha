# Pionex_alpha
# Data Cleaning Script for Crypto Trading Bots User Database
This script performs data cleaning and validation on a raw dataset of crypto trading bot users. It removes unwanted data, validates fields, and prepares a cleaned dataset for further analysis. Invalid data is saved to a separate file for review.

# Requirements
This script requires the following:

* Python 3.6 or higher
* Pandas library
* Regular Expressions (re) library
#Script Overview
# 1. Loading the Dataset
The script begins by loading the raw dataset using the pandas library.
<!-- Python block -->
```python
import pandas as pd
import re

# File path for the raw dataset
raw_file_path = '/content/241k-Singapore-pionex.com-Crypto-Trading-Bots-UsersDB-csv-2023.csv'

# Load the dataset
df = pd.read_csv(raw_file_path)
```

# 2. Dropping Unwanted Columns
Unnecessary columns (lang and BrandCode) are removed to simplify the dataset.
<!-- Python block -->
```python
# Drop unwanted columns
df = df.drop(columns=['lang', 'BrandCode'], errors='ignore')
```

# 3. Reordering Columns
The dataset columns are reordered for consistency and readability.

<!-- Python block -->
```python
# Reorder columns
columns_order = ['RegistrationDate', 'First Name', 'Last Name', 'Phone', 'Country', 'Email']
df = df[columns_order]
```

# 4. Validating Email Addresses
An email validation function checks if the email addresses in the dataset match a standard email format.

<!-- Python block -->
```python
# Email validation function
def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, str(email)))
```

# 5. Identifying Invalid Rows
The script identifies rows with missing values, duplicate entries, and invalid email addresses.

<!-- Python block -->
```python
# Identify invalid rows
rows_with_missing_values = df[df.isnull().any(axis=1)]
rows_with_duplicates = df[df.duplicated()]
rows_with_invalid_emails = df[~df['Email'].apply(validate_email)]
```
# 6. Removing Invalid Rows
All invalid rows are removed from the original dataset.

<!-- Python block -->
```python
# Combine all invalid rows
invalid_rows = pd.concat([rows_with_missing_values, rows_with_duplicates, rows_with_invalid_emails]).drop_duplicates()

# Remove invalid rows from the original dataset
df = df.drop(invalid_rows.index)
```

# 7. Standardizing Name Fields
First and last names are capitalized, and the column names are renamed for consistency.

<!-- Python block -->
```python
# Capitalize 'First Name' and 'Last Name', rename to 'first_name' and 'last_name'
df['First Name'] = df['First Name'].str.capitalize()
df['Last Name'] = df['Last Name'].str.capitalize()
df = df.rename(columns={'First Name': 'first_name', 'Last Name': 'last_name'})
```

# 8. Saving Invalid Data
Rows identified as invalid are saved to a separate CSV file for review.

<!-- Python block -->
```python
# Save invalid data to a separate file
invalid_data_file_path = '/content/invalid_data.csv'
invalid_rows.to_csv(invalid_data_file_path, index=False)
```

# 9. Saving the Cleaned Dataset
The cleaned dataset is saved to a new CSV file.
<!-- Python block -->
```python
# Save the cleaned dataset
cleaned_file_path = '/content/cleaned_phoniex.csv'
df.to_csv(cleaned_file_path, index=False)
```
# 10. Summary of Operations
The script prints a summary of the total rows removed and the file paths for the saved datasets.

<!-- Python block -->
```python
# Print summary of operations
print(f"Total rows removed: {len(invalid_rows)}")
print(f"Invalid data saved to: {invalid_data_file_path}")
print(f"Cleaned dataset saved to: {cleaned_file_path}")
```
# Output Files
* Cleaned Dataset: /content/cleaned_phoniex.csv
* Invalid Data: /content/invalid_data.csv
