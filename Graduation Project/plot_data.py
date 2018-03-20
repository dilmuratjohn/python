#!/usr/bin/env python3.6

"""A simple function for showing the figure of row data """


import numpy as np
import matplotlib.pyplot as plt
import get_data_from_excel


def plot(data, name):
    sum_of_rows = data.shape[0]
    axis_x = np.linspace(0, sum_of_rows, sum_of_rows)
    axis_y = data
    plt.figure()
    plt.plot(axis_x, axis_y)
    plt.grid(True)
    plt.savefig("auto_save#%s.png" % name)
    return 0


def main():
    file = 'train.xls'
    sheet = 0
    row = 2
    columns = 2
    sheet = get_data_from_excel.GetData(file, sheet)
    row_data = sheet.get_data_by_row(row)
    columns_data = sheet.get_data_by_columns(columns)
    print(row_data)
    print(columns_data)
    plot(row_data, 'row_data')
    plot(columns_data, 'columns_data')
if __name__ == "__main__":
    main()
