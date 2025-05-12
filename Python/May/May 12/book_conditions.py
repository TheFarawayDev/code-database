import pandas as pd

# import the data from the data.csv file
# set max_columns to None
pd.set_option('display.max_columns', None)
df = pd.read_csv("data.csv")

# print title and page count for books that have less
# than 100 pages
less_than_100_pages = df[df['page_count'] < 100][['title', 'page_count']]
print("Books with less than 100 pages:")
print(less_than_100_pages)
print("\n")

# print only the rows that have the publisher "IDW Publishing"
idw_publishing_books = df[df['publisher'] == 'IDW Publishing']
print("Books published by IDW Publishing:")
print(idw_publishing_books)
print("\n")

# print the title, rating and voters columns for books
# that have a rating of 4.0 or higher and over 9000 voters
high_rating_high_voters = df[(df['rating'] >= 4.0) & (df['voters'] > 9000)][['title', 'rating', 'voters']]
print("Books with rating >= 4.0 and voters > 9000:")
print(high_rating_high_voters)
print("\n")

# print only the row(s) with the max price
max_price_books = df[df['price'] == df['price'].max()]
print("Book(s) with the maximum price:")
print(max_price_books)
