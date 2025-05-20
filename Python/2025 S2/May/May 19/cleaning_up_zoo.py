# Click on the Assignment tab to see more info. -->
# <-- Click on the data.csv file to see the dataset.

import pandas as pd

# import the data from the data.csv file
# set max_columns to None
df = pd.read_csv(r"data.csv")
pd.set_option("display.max_columns", None)

# Check the data types. Do they look okay?
print("Data Types:")
print(df.dtypes)
print("\n")

# The data types look appropriate:
# - row_number is an int64
# - animal is object (string)
# - sound is object (string)
# No changes needed for data types in this case

# Drop the column labeled row_number
df = df.drop(columns=['row_number'])
print("Dataframe after dropping row_number column:")
print(df.head())
print("\n")

# Print the shape of the data and check for duplicate rows
# How many are there?
print("Shape of the data:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Check for duplicate rows
duplicates = df.duplicated()
print("Number of duplicate rows:", duplicates.sum())
print("\n")

# Drop duplicate rows
df_no_duplicates = df.drop_duplicates()
print("Shape after removing duplicates:", df_no_duplicates.shape)
print("Rows removed:", df.shape[0] - df_no_duplicates.shape[0])
print("\n")

# Permanently update the dataframe
df = df_no_duplicates

# Determine the number of missing values
print("Missing values by column:")
print(df.isna().sum())
print("Total missing values:", df.isna().sum().sum())
print("\n")

# What would be the best decision for dealing with the missing values?
# For this dataset, we have a missing value in the 'sound' column for the 'fox'
# Since this is categorical data and there's a known sound for foxes ("Ring-ding-ding-ding-dingeringeding!" 
# or more commonly "What does the fox say?"), 
# we could fill it with the appropriate value or mark it as "unknown"

# For this example, we'll add "what does the fox say?" as the sound
df.loc[df['animal'] == 'fox', 'sound'] = "what does the fox say?"

# Alternative approach: If you prefer to drop rows with missing values
# df = df.dropna()

print("Dataframe after handling missing values:")
print(df)
print("\n")

# Final check for missing values
print("Missing values after cleaning:")
print(df.isna().sum())
print("\n")

print("Final cleaned dataframe shape:", df.shape)