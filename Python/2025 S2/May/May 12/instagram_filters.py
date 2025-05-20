import pandas as pd

# import the data from the data.csv file
df = pd.read_csv("data.csv")
pd.set_option("display.max_columns", None)

# print the rows where followers are greater than 230 (million)
followers_greater_than_230 = df[df['followers'] > 230]
print("Rows where followers are greater than 230 million:")
print(followers_greater_than_230)
print("\n")

# print only the account columns of those from the United States
accounts_from_usa = df.loc[df['country'] == 'United States', 'account']
print("Accounts from the United States:")
print(accounts_from_usa)
print("\n")

# print the account and followers columns of the row with the maximum number of followers
row_with_max_followers = df.loc[df['followers'].idxmax(), ['account', 'followers']]
print("Account and followers with the maximum number of followers:")
print(row_with_max_followers)
