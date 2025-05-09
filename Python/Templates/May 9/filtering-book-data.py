#Pandas loc and iloc Template by Marshall

import pandas as pd

def pandas_loc_iloc_examples(file_path):
    """
    Demonstrates how to use .loc and .iloc for selecting data in a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        None. Prints the results.
    """
    try:
        # 1. Import the data from the CSV file
        data_frame = pd.read_csv(file_path)

        # 2. Optional: Set display options
        pd.set_option('display.max_columns', None)  # Show all columns

        # 3. .loc examples (label-based indexing)
        print("\n--- .loc Examples ---")

        # a. Select rows 3 to 6 (inclusive) and specific columns
        print("\nSelecting rows 3 to 6 and columns 'title' and 'page_count':")
        print(data_frame.loc[3:6, ['title', 'page_count']])

        # b. Select a single row by label (index 400) and a column
        print("\nSelecting the 'title' column from row with index 400:")
        print(data_frame.loc[400, 'title'])

        # c. Select a range of rows and a range of columns by label
        #    Here, we're using df.columns to get column labels, then slicing.
        print("\nSelecting rows 10 to 15 and columns with labels at positions 3 to 5:")
        print(data_frame.loc[10:15, data_frame.columns[3:6]])

        # 4. .iloc examples (integer-based indexing)
        print("\n--- .iloc Examples ---")

        # a. Select rows 3 to 6 (exclusive of 7) and specific columns by integer position
        print("\nSelecting rows 3 to 6 and columns at positions 0 and 6:")
        print(data_frame.iloc[3:7, [0, 6]])

        # b. Select a single row by integer position and a column by integer position
        print("\nSelecting the column at position 0 from row at position 400:")
        print(data_frame.iloc[400, 0])

        # c. Select a range of rows and a range of columns by integer position
        print("\nSelecting rows 10 to 15 and columns 3 to 5:")
        print(data_frame.iloc[10:16, 3:6])

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.  Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'data.csv' with the actual path to your CSV file
    pandas_loc_iloc_examples('data.csv')
