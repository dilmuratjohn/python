#!/usr/bin/env python3.6


import xlrd
import numpy


class GetData(object):
    """A simple class for getting data from Excel """

    def __init__(self, file, sheet):
        """A simple function for getting data by columns"""

        try:
            read = xlrd.open_workbook(file)
            self.data = read.sheets()[sheet]
        except Exception as exception:
            print(str(exception))

    def get_data_by_row(self, row):
        sum_of_columns = self.data.ncols
        list_of_columns = []
        for n in range(1, sum_of_columns):
            list_of_columns.append(self.data.col_values(n))
        matrix_of_data = numpy.array(list_of_columns)
        matrix_of_row = matrix_of_data[:, row-1]
        return matrix_of_row.astype(numpy.float64)

    def get_data_by_columns(self, columns):
        sum_of_row = self.data.nrows
        list_of_row = []
        for n in range(1, sum_of_row):
            list_of_row.append(self.data.row_values(n))
        matrix_of_data = numpy.array(list_of_row)
        matrix_of_columns = matrix_of_data[:, columns-1]
        return matrix_of_columns.astype(numpy.float64)


def main():
    file = 'train.xls'
    sheet = 0
    row = 2
    columns = 2
    sheet = GetData(file, sheet)
    row_data = sheet.get_data_by_row(row)
    columns_data = sheet.get_data_by_columns(columns)
    print(row_data)
    print(columns_data)
if __name__ == "__main__":
    main()
