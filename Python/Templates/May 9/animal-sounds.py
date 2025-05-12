By Marshall
import pandas as pd

def pandas_loc_iloc_examples(csv_file):
    """
    Demonstrates how to use .loc and .iloc for selecting data in a pandas DataFrame.

    Args:
        csv_file (str): Path to the CSV file containing the data.

    Returns:
        None. Prints the results of the examples to the console.
    """
    try:
        # 1. Import the data from the CSV file
        df = pd.read_csv(csv_file)
        pd.set_option('display.max_columns', None)

        # 2. .loc examples (label-based indexing)
        print("\n--- .loc Examples ---")

        # a. Select a range of rows and specific columns
        print("\nUsing loc - Print rows 'start_row' to 'end_row' and columns 'column_name_1', 'column_name_2':")
        print(df.loc['start_row':'end_row', ['column_name_1', 'column_name_2']])  # .loc is inclusive

        # b. Select a single row and a column
        print("\nUsing loc - Print the column 'column_name' of row 'row_label':")
        print(df.loc['row_label', 'column_name'])

        # c. Select a range of rows
        print("\nUsing loc - Print rows 'start_row' to 'end_row':")
        print(df.loc['start_row':'end_row'])

        # 3. .iloc examples (integer-based indexing)
        print("\n--- .iloc Examples ---")

        # a. Select a range of rows and specific columns
        print("\nUsing iloc - Print rows at positions 'start_row_index' to 'end_row_index' and columns at positions 'column_index_1', 'column_index_2':")
        print(df.iloc[start_row_index:end_row_index, [column_index_1, column_index_2]])  # .iloc is exclusive

        # b. Select a single row and a column
        print("\nUsing iloc - Print the column at position 'column_index' of row at position 'row_index':")
        print(df.iloc[row_index, column_index])

        # c. Select a range of rows
        print("\nUsing iloc - Print rows at positions 'start_row_index' to 'end_row_index':")
        print(df.iloc[start_row_index:end_row_index])

    except FileNotFoundError:
        print(f"Error: File not found at {csv_file}. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'data.csv' with the actual path to your CSV file
    pandas_loc_iloc_examples('data.csv')
