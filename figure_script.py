import argparse
import ast
import pandas as pd

def parse_data(filename):
    # Define a list to store all parsed data
    parsed_data = []

    # Open the file and read line by line
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into individual elements
            elements = line.split()

            # Convert elements to appropriate data types
            converted_elements = [int(el) if el.isdigit() else float(el) for el in elements]

            # Append the converted elements to the parsed data list
            parsed_data.append(converted_elements)

    return parsed_data


def parse_data_with_pandas(filename):
    # Read the data into a DataFrame, assuming comma-separated values
    df = pd.read_csv(filename, sep=',', header=None)

    # Convert list-like strings to lists
    for col in df.columns:
        if df[col].dtype == object:  # If the column type is 'object' (string)
            # Safely evaluate the string as a Python expression (e.g., converting "[1, 2, 3]" to [1, 2, 3])
            df[col] = df[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x)

    return df

def iterate_dataframe_columns(df):
    for column in df.columns:
        print(f"Column: {column}")
        print(f"Mean: {df[column].mean()}")
        print(f"Standard Deviation: {df[column].std()}")
        print(f"Median: {df[column].median()}")
        print("-" * 30)

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Parse data from files")
    parser.add_argument("file1", help="Path to the first data file")
    parser.add_argument("file2", help="Path to the second data file")

    # Parse arguments
    args = parser.parse_args()

    # Parse data from the provided files
    data1 = parse_data_with_pandas(args.file1)
    data2 = parse_data_with_pandas(args.file2)

    # Print the data (or you can process it as needed)
    print("Data from file 1:")
    iterate_dataframe_columns(data1)
    print("Data from file 2:")
    iterate_dataframe_columns(data2)
    

if __name__ == "__main__":
    main()