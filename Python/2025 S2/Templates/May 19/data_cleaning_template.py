#Made by Marshall

import pandas as pd

def clean_dataset(file_path, columns_to_drop=None):
    """
    A template function for cleaning dataset using pandas
    
    Parameters:
    file_path (str): Path to the CSV file
    columns_to_drop (list): List of column names to drop from the dataset
    
    Returns:
    pd.DataFrame: Cleaned dataset
    """
    # Set display options for better visualization
    pd.set_option('display.max_columns', None)
    
    # Import the data
    df = pd.read_csv(file_path)
    
    # Display initial data information
    print("Initial data information:")
    print("Shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)
    
    # Drop specified columns if any
    if columns_to_drop:
        df.drop(columns_to_drop, axis=1, inplace=True)
        print(f"\nColumns dropped: {columns_to_drop}")
        print("Shape after dropping columns:", df.shape)
    
    # Check and remove duplicates
    print("\nChecking for duplicates:")
    duplicates = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicates}")
    
    if duplicates > 0:
        df.drop_duplicates(inplace=True)
        print("Shape after dropping duplicates:", df.shape)
    
    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # Handle missing values
    df.dropna(inplace=True)  # You can modify this based on your needs
    print("\nShape after handling missing values:", df.shape)
    print("Final missing values count:")
    print(df.isnull().sum())
    
    return df

# Example usage:
if __name__ == "__main__":
    # Replace 'data.csv' with your file path
    # Replace column_list with columns you want to drop
    cleaned_df = clean_dataset('data.csv', columns_to_drop=['column1', 'column2'])
    print("\nFirst few rows of cleaned dataset:")
    print(cleaned_df.head())
