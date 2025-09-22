import pandas as pd
import numpy as np


# Sample raw dataset with nulls, duplicates, inconsistent formats
raw_data = {
    'Name': ['Alice', 'Bob', 'Alice', None, 'Eve', 'Frank', 'Alice'],
    'Age': ['25', '30', '25', '22', None, '35', '25'],
    'Gender': ['F', 'M', 'F', 'F', 'Female', 'M', 'F'],
    'Country': ['US', 'USA', 'US', 'UK', 'UK ', 'usa', 'UK'],
    'JoinDate': ['2020-01-01', '01-02-2020', '2020/01/01', '2020-03-01', '03/15/2020', None, '2020-01-01'],
    'Subscription': ['Basic', 'Premium', 'Basic', 'Basic', 'Premium', 'Basic', 'Basic']
}

# Creating DataFrame
df = pd.DataFrame(raw_data)

# Display raw dataset
print("Raw Dataset:")
print(df)

# Cleaning Steps

# 1. Handle missing values - Fill missing Age with median, missing Name with 'Unknown', missing JoinDate with mode
median_age = pd.to_numeric(df['Age'], errors='coerce').median()
df['Age'] = df['Age'].fillna(median_age)
df['Name'] = df['Name'].fillna('Unknown')
df['JoinDate'] = df['JoinDate'].fillna(df['JoinDate'].mode()[0])

# 2. Remove duplicates
# Check duplicates ignoring index
print("\nDuplicates before removal:")
print(df.duplicated(keep=False))
df = df.drop_duplicates()

# 3. Standardize text values
# Gender: Map 'Female' to 'F', uppercase all
# Country: Strip spaces, uppercase, and replace 'USA' and 'usa' with 'US'
df['Gender'] = df['Gender'].replace({'Female': 'F', 'female': 'F'}).str.upper()
df['Country'] = df['Country'].str.strip().str.upper().replace({'USA': 'US'})

# 4. Convert date to a consistent format yyyy-mm-dd
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce').dt.strftime('%Y-%m-%d')

# 5. Rename columns to lowercase, no spaces
df.columns = [col.lower() for col in df.columns]

# 6. Fix data types
# Convert age to int
df['age'] = df['age'].astype(int)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)