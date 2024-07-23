import pandas as pd
import matplotlib.pyplot as plt

class BaseDataReader:
    def __init__(self, data=None):
        """
        Initialize the BaseDataReader with optional data.
        """
        self.data = data

    def get_data(self):
        """
        Return the loaded data as a pandas DataFrame.
        """
        return self.data

    def display_info(self):
        """
        Display basic information about the loaded DataFrame.
        """
        if self.data is not None:
            print(self.data.info())
        else:
            print("No data loaded.")

    def plot_histogram(self, column_name, bins=10):
        """
        Plot a histogram for the specified column.
        """
        if self.data is not None and column_name in self.data.columns:
            self.data[column_name].plot(kind='hist', bins=bins, title=f'Histogram of {column_name}')
            plt.xlabel(column_name)
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f"Column '{column_name}' not found or no data loaded.")

    def plot_line(self, x_column, y_column):
        """
        Plot a line chart using specified columns for x and y axes.
        """
        if self.data is not None and x_column in self.data.columns and y_column in self.data.columns:
            self.data.plot(x=x_column, y=y_column, kind='line', title=f'Line Chart: {x_column} vs {y_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.show()
        else:
            print(f"One or both columns '{x_column}' and '{y_column}' not found or no data loaded.")

