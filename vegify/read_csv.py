# File to read in CSV

import csv
import os


def open_read_csv_file(file_to_read_in):
    with open(file_to_read_in, newline='') as csvfile:
        opened_file = csv.reader(csvfile, delimiter=' ' , quotechar='|')
        for row in opened_file:
            print(', '.join(row))
    return opened_file


if __name__ == "__main__":
    vegify_csv_file = 'GoVegifyMenuAnalyzerData-menuItemTitleReps.csv'
    open_read_csv_file(vegify_csv_file)