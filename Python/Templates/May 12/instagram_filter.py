#Panda And Instagram Filter By Marshall

import pandas as pd

# import the data from the data.csv file
df = pd.read_csv("data.csv")
pd.set_option("display.max_columns", None)

# print the rows where followers are greater than a specified value
value_placeholder = 230  # Replace with your desired value
filtered_df = df[df['followers'] > value_placeholder]
print(f"Rows where followers are greater than {value_placeholder} million:")
print(filtered_df)
print("\n")

# print only the account columns of those from a specified country
country_placeholder = 'United States'  # Replace with your desired country
accounts_from_country = df.loc[df['country'] == country_placeholder, 'account']
print(f"Accounts from {country_placeholder}:")
print(accounts_from_country)
print("\n")

# print the account and followers columns of the row with the maximum number of followers
row_with_max_followers = df.loc[df['followers'].idxmax(), ['account', 'followers']]
print("Account and followers with the maximum number of followers:")
print(row_with_max_followers)
