import pandas as pd

# Import the data from the data.csv file and set max_columns to None
pd.set_option('display.max_columns', None)
df = pd.read_csv('data.csv')

# Check the data types
print("Data types before cleaning:")
print(df.dtypes)

# Drop the publisher and published_date columns permanently
df.drop(['publisher', 'published_date'], axis=1, inplace=True)

# Print the shape of the data and check for duplicate rows
print("\nShape before dropping duplicates:", df.shape)
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)

# Drop duplicate rows permanently
df.drop_duplicates(inplace=True)
print("Shape after dropping duplicates:", df.shape)

# Determine the number of missing values in the dataset
print("\nMissing values per column:")
print(df.isnull().sum())

# Decision for missing values:
# For this dataset, since missing values are likely in rating, voters, and price,
# and these are important for analysis, it's best to drop rows with any missing values.
df.dropna(inplace=True)
print("\nShape after dropping missing values:", df.shape)
print("Missing values after cleaning:")
print(df.isnull().sum())