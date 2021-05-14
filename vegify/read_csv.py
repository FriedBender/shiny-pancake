# File to read in CSV

import csv
import os


def read_csv_file(file_to_read_in):
    with open(file_to_read_in, newline='') as csvfile:
        opened_file = csv.reader(csvfile, delimiter=' ' , quotechar='|')
        for row in opened_file:
            print(', '.join(row))


if __name__ == "__main__":
    read_csv_file('/home/maksim/Documents/School/CS 469 - Capstone I/playground/Vegify/vegan_options.csv')