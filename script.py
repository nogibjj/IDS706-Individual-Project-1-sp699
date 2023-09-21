# Script.py using polars and matplotlib to set data and see some plot

import os
import matplotlib.pyplot as plt
from lib import load_data
import numpy as np
import pandas as pd

my_data = "Auto.csv"


# Describe mean, median, standard deviation of each columns
def describe_stat(dataset):
    data = load_data(dataset)
    data_desc = data.describe()
    print(data_desc)
    return data_desc


# Calculate the mean, median, and standard deviation of each column
def calculate_stat(dataset):
    data = pd.read_csv(dataset)

    num_columns = data.shape[1]
    # Mean
    for column in range(1, num_columns - 3):
        column_name = data.columns[column]
        column_data = data.iloc[:, column]  # Current column data
        column_data = pd.to_numeric(column_data, errors="coerce")
        column_data = column_data.dropna()
        col_mean = np.mean(column_data)  # Calculate the mean
        col_median = np.median(column_data)  # Calculate the median
        col_std = np.std(column_data)  # Calculate the standard deviation

        print(f"Column name: {column_name}")
        print(f"Mean: {col_mean}")
        print(f"Median: {col_median}")
        print(f"Standard deviation: {col_std}")
        print()


# Make a boxplot for each column in the CSV file
def build_boxplot(dataset):
    data = load_data(dataset)
    numeric_columns = data.select_dtypes(include=["number"]).columns

    directory_path = "C:/Users/User/.git/Suim-Park-Individual-Project-1/Outputs"
    folder_name = "Graphs"
    save_folder = os.path.join(directory_path, folder_name)

    # Create the folder if it does not exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for column in numeric_columns[1:7]:
        plt.figure()  # Create a new plot
        plt.boxplot(data[column].to_list())  # Draw a Box Plot
        plt.title(f"{column} Box Plot")  # Set the title of the plot
        plt.xlabel("Value")  # Set the x-axis label
        plt.ylabel("Distribution")  # Set the y-axis label

        save_path = os.path.join(save_folder, f"boxplot {column}.png")
        plt.savefig(save_path)

        plt.show()
    return


if __name__ == "__main__":
    describe_stat(my_data)
    calculate_stat(my_data)
    build_boxplot(my_data)
