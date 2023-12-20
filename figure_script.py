import argparse
import ast

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from matplotlib import rcParams


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
    df = pd.read_csv(filename, sep='\t')

    # Convert list-like strings to lists
    for col in df.columns:
        if df[col].dtype == object:  # If the column type is 'object' (string)
            # Safely evaluate the string as a Python expression (e.g., converting "[1, 2, 3]" to [1, 2, 3])
            df[col] = df[col].apply(lambda x: np.array(ast.literal_eval(x)) if isinstance(x, str) and x.startswith('[') else x)

    return df

def iterate_dataframe_columns(df):
    for column in df.columns:
        print(f"Column: {column}")
        print(f"Data: {df[column]}")
        print("-" * 30)

def find_largest_differences(df1, df2):
    # Ensure the dataframes have the same shape
    if df1.shape != df2.shape:
        raise ValueError("DataFrames do not have the same shape")

    largest_differences = {}

    # Iterate over the columns
    for col in df1.columns:
        # Calculate the absolute differences
        for row,row2 in zip(df1[col],df2[col]):
            differences = row - row2
    
            print(differences)
            print(col)
        

    return largest_differences


#T-Test function
def compare_sets(set1, set2):
    u_stat, p_value = stats.mannwhitneyu(set1, set2, alternative='two-sided')

    print("U-statistic:", u_stat)
    print("P-value:", p_value)


def make_plot(df1, df2,col="OverallEnergy"):
    plt.figure(figsize=(10, 6))
    
    rcParams['font.family'] = 'serif'
    rcParams['font.serif'] = ['Times New Roman']
    rcParams['font.size'] = 18
    rcParams['text.usetex'] = True

    # Assuming 'Overall Energy' is the column you want to plot
    plt.plot(df1[col], label='2D Simulation')
    plt.plot(df2[col], label='3D Simulation')

    print(col)
    compare_sets(df1[col],df2[col])

    plt.title(f'{col} Comparison')
    plt.xlabel('Number of Nodes')
    plt.ylabel(f'{col}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./figures/{col}_figure.pdf")

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
    # print("Data from file 1:")
    # iterate_dataframe_columns(data1)
    # print("Data from file 2:")
    # iterate_dataframe_columns(data2)
    
    # find_largest_differences(data1,data2)
    for col in data1.columns:
        make_plot(data1,data2,col=col)

if __name__ == "__main__":
    main()