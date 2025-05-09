import pandas as pd

# import the data from the data.csv file
df = pd.read_csv("data.csv")
pd.set_option("display.max_columns", None)


# Using loc - Print the row and animal columns for rows 3 to 6
print("\nUsing loc - Print the row and animal columns for rows 3 to 6:")
print(df.loc[2:5, ["row", "animal"]])  # Note: .loc is inclusive of the end index

# Using iloc - Print the row and animal columns for rows 3 to 6
print("\nUsing iloc - Print the row and animal columns for rows 3 to 6:")
print(df.iloc[2:6, [0, 1]])  # Note: .iloc is exclusive of the end index



# Using loc - Print the sound of the animal at index 7
print("\nUsing loc - Print the sound of the animal at index 7:")
print(df.loc[6, "sound"])

# Using iloc - Print the sound of the animal at index 7
print("\nUsing iloc - Print the sound of the animal at index 7:")
print(df.iloc[6, 2])


# Using loc - Print rows at index 8-10
print("\nUsing loc - Print rows at index 8-10:")
print(df.loc[7:9])

# Using iloc - Print rows at index 8-10
print("\nUsing iloc - Print rows at index 8-10:")
print(df.iloc[7:10])
