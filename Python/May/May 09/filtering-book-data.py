import pandas as pd

# import the data from the data.csv file
df = pd.read_csv('data.csv')
pd.set_option('display.max_columns', None)

# Using loc - Print the title and page count columns
# for rows 3 to 6
print("Using loc:")
print(df.loc[3:6, ['title', 'page_count']])

# Using iloc - Print the title and page count columns
# for rows 3 to 6
print("\nUsing iloc:")
print(df.iloc[3:7, [0, 6]])

# Using loc - Print the title of the book at index 400
print("\nUsing loc for index 400:")
print(df.loc[400, 'title'])

# Using iloc - Print the title of the book at index 400
print("\nUsing iloc for index 400:")
print(df.iloc[400, 0])

# Using loc - Print rows at index 10-15 and columns at index 3-5
print("\nUsing loc for rows 10-15 and columns 3-5:")
print(df.loc[10:15, df.columns[3:6]])

# Using iloc - Print rows at index 10-15 and columns at index 3-5
print("\nUsing iloc for rows 10-15 and columns 3-5:")
print(df.iloc[10:16, 3:6])