#Panda And Book Conditions By Marshall

import pandas as pd

# import the data from the data.csv file
# set max_columns to None
pd.set_option('display.max_columns', None)
df = pd.read_csv("data.csv")

# Example set (can be removed)
example_page_threshold = 150
example_publisher = "HarperCollins UK"

# print title and page count for books that have less
# than a specified number of pages
value_1 = 100  # Replace with your desired page number
less_than_value_1_pages = df[df['page_count'] < value_1][['title', 'page_count']]
print(f"Books with less than {value_1} pages:")
print(less_than_value_1_pages)
print("\n")

# print only the rows that have a specified publisher
publisher_name = 'IDW Publishing'  # Replace with your desired publisher
publisher_name_books = df[df['publisher'] == publisher_name]
print(f"Books published by {publisher_name}:")
print(publisher_name_books)
print("\n")

# print the title, rating and voters columns for books
# that have a rating of a specified value or higher and
# a specified number of voters
rating_value = 4.0  # Replace with your desired rating
voter_value = 9000  # Replace with your desired voter number
high_rating_high_voters = df[(df['rating'] >= rating_value) & (df['voters'] > voter_value)][['title', 'rating', 'voters']]
print(f"Books with rating >= {rating_value} and voters > {voter_value}:")
print(high_rating_high_voters)
print("\n")

# print only the row(s) with the max price
max_price_books = df[df['price'] == df['price'].max()]
print("Book(s) with the maximum price:")
print(max_price_books)

#Demonstration of using the example set
print(f"\nExample: Books with less than {example_page_threshold} pages:")
example_result = df[df['page_count'] < example_page_threshold][['title', 'page_count']]
print(example_result)

print(f"\nExample: Books published by {example_publisher}:")
example_publisher_result = df[df['publisher'] == example_publisher]
print(example_publisher_result)
